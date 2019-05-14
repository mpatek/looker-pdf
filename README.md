# looker-pdf

This is a tool that can be used to download and combine multiple [Looker](https://looker.com/) dashboards into a single PDF.

## Installation

We use [Conda](https://docs.conda.io/en/latest/) to manage our Python versions. In this project, we are using Python version 3.7.3. To create the Conda environment, change to the root of this repo and type:

```bash
$ conda env create
```

That will install the Python executable and required Python libraries, and create a new Conda environment named `looker-pdf`. In order to switch to the new environment:

```bash
$ source activate looker-pdf
```

## Using The CLI

Once you've switched to the new environment, you should be able to run the included [looker-pdf.py](looker-pdf.py) script:

```bash
Usage: looker-pdf.py [OPTIONS] CONFIG_FILE OUTPUT_FILE

Options:
  --base-url TEXT       [required]
  --client-id TEXT      [required]
  --client-secret TEXT  [required]
  --help                Show this message and exit.
```

`CONFIG_FILE` refers to a JSON file with the arguments to use to generate the dashboard PDFs.
`OUTPUT_FILE` is the name of the output PDF.
`--base-url`, `--client-id`, and `--client-secret` are required to communicate with the Looker API. Details for obtaining API credentials can be found [here](https://docs.looker.com/reference/api-and-integration/api-auth).

### Config File Format

The config file should represent an object with two keys: `dashboard_args` and `shared_args`. `dashboard_args` should be a list of objects, each of which has a required `dashboard_id` number, and optional arguments used to render the dashboard as a PDF:

```JSON
{
    "dashboard_args": [
        {
            "dashboard_id": 1,
            "dashboard_style": "single_column",
            "dashboard_filters": "foo=bar&baz=qux",
            "width": 2048,
            "height": 1536
        },
        {
            "dashboard_id": 2,
            "width": 2048,
            "height": 1536
        },
        ...
    ]
}
```

`shared_args` is a single object which can be used to specify options that should be used by all dashboards:

```JSON
{
    "dashboard_args": [
        {
            "dashboard_id": 1,
            "dashboard_style": "single_column",
            "dashboard_filters": "foo=bar&baz=qux"
        },
        {
            "dashboard_id": 2
        },
        ...
    ],
    "shared_args": {
	"width": 2048,
        "height": 1536
    }
}
```

We've included a [sample config file](config.json.sample) which can be used as a template.

### Authenticating with Environment Variables

In order to communicate with the Looker API you must specify a Base URL, a Client ID, and a Client Secret. You can use the `--base-url`, `--client-id`, and `--client-secret` CLI options to do this, but you can also use environment variables `LOOKER_BASE_URL`, `LOOKER_CLIENT_ID`, and `LOOKER_CLIENT_SECRET`. You can set those from the command line, in a shell setup script, or you can use Honcho to read them from a `.env` file. We've included a [sample .env file](.env.sample). If you fill in the authentication details in the sample file and rename it to `.env`, then you can run the CLI without needing to specify options like this:

```bash
honcho run python looker-pdf.py config.json output.pdf
```

## A Note On the Looker API Client SDK

The Looker API Client SDK in Python is included in the [looker/](looker/) directory of this repo.  I followed the directions for building a Looker API Client SDK in Python [in the Looker Community Forum](https://discourse.looker.com/t/generating-client-sdks-for-the-looker-api/3185). I used the latest release of [swagger-codegen](https://github.com/swagger-api/swagger-codegen) (v. 3.0.8). I also ran `swagger-codegen-cli.jar` with a config.json file which specified the Python module name to use (the module name defaults to swagger_client by default):

```JSON
{
	"packageName": "looker"
}
```

So my command for running `swagger-codegen-cli.jar` looked like this:

```bash
$ java -jar ./swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i looker_api.json -l python -o python_sdk -c config.json
```

I moved the `looker` subdirectory from `python_sdk` to this repo.

On line 49 of [looker/configuration.py](looker/configuration.py#L49], in the `Configuration` class, our company base URL was set as the default base URL. I replaced that with `None`.

```Python
        # Default Base url                                                                                         
        self.host = None
```
