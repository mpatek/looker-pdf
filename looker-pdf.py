import io
import json
import logging
import time
from typing import List, Optional

import click
import looker
from PyPDF2 import PdfFileMerger

logger = logging.getLogger(__name__)


def get_looker_api_client(
    *,
    base_url: str,
    client_id: str,
    client_secret: str
) -> looker.ApiClient:
    """Create a Looker API client."""
    config = looker.Configuration()
    config.host = base_url
    unauthenticated_client = looker.ApiClient(config)
    unauthenticated_auth_api = looker.ApiAuthApi(unauthenticated_client)

    token = unauthenticated_auth_api.login(
        client_id=client_id,
        client_secret=client_secret,
    )
    client = looker.ApiClient(
        config,
        'Authorization',
        f'token {token.access_token}'
    )
    return client


def download_dashboard_to_pdf(
    *,
    client: looker.ApiClient,
    dashboard_id: int,
    width: int,
    height: int,
    dashboard_style: Optional[str]=None,
    dashboard_filters: Optional[str]=None
) -> bytes:
    """Download a Looker dashboard as a PDF."""
    render_api = looker.RenderTaskApi(client)
    body = {}
    if dashboard_style:
        body['dashboard_style'] = dashboard_style
    if dashboard_filters:
        body['dashboard_filters'] = dashboard_filters
    create_response = render_api.create_dashboard_render_task(
        dashboard_id=dashboard_id,
        result_format='pdf',
        body=body,
        width=width,
        height=height,
    )
    task_id = create_response.id
    task = render_api.render_task(task_id)
    while task.status != 'success':
        logger.debug(
            'Render task status: {}. sleeping...'.format(task.status)
        )
        time.sleep(10)
        task = render_api.render_task(task_id)
    response = render_api.render_task_results(task_id, _preload_content=False)
    return response.read()


def merge_pdfs(output_file: io.IOBase, pdf_contents: List[bytes]) -> None:
    """Combine multiple PDFs into a single PDF."""
    merger = PdfFileMerger()
    for pdf_content in pdf_contents:
        merger.append(io.BytesIO(pdf_content))
    merger.write(output_file)


@click.command()
@click.argument('config-file', type=click.File('rt'))
@click.argument('output-file', type=click.File('wb'))
@click.option('--base-url', required=True)
@click.option('--client-id', required=True)
@click.option('--client-secret', required=True)
def cli(config_file, output_file, base_url, client_id, client_secret):
    config = json.load(config_file)
    shared_args = config.get('shared_args', {})
    client = get_looker_api_client(
        base_url=base_url,
        client_id=client_id,
        client_secret=client_secret,
    )
    pdf_contents = [
        download_dashboard_to_pdf(
            client=client,
            **dict(shared_args, **args)
        )
        for args in config['dashboard_args']
    ]
    merge_pdfs(output_file, pdf_contents)


if __name__ == '__main__':
    cli(auto_envvar_prefix='LOOKER')
