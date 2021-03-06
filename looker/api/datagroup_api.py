# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from looker.api_client import ApiClient


class DatagroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_datagroups(self, **kwargs):  # noqa: E501
        """Get All Datagroups  # noqa: E501

        ### Get information about all datagroups.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_datagroups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Datagroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.all_datagroups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_datagroups_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_datagroups_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Datagroups  # noqa: E501

        ### Get information about all datagroups.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_datagroups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Datagroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_datagroups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datagroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Datagroup]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def datagroup(self, datagroup_id, **kwargs):  # noqa: E501
        """Get Datagroup  # noqa: E501

        ### Get information about a datagroup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.datagroup(datagroup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datagroup_id: ID of datagroup. (required)
        :return: Datagroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.datagroup_with_http_info(datagroup_id, **kwargs)  # noqa: E501
        else:
            (data) = self.datagroup_with_http_info(datagroup_id, **kwargs)  # noqa: E501
            return data

    def datagroup_with_http_info(self, datagroup_id, **kwargs):  # noqa: E501
        """Get Datagroup  # noqa: E501

        ### Get information about a datagroup.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.datagroup_with_http_info(datagroup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datagroup_id: ID of datagroup. (required)
        :return: Datagroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datagroup_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datagroup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datagroup_id' is set
        if ('datagroup_id' not in params or
                params['datagroup_id'] is None):
            raise ValueError("Missing the required parameter `datagroup_id` when calling `datagroup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datagroup_id' in params:
            path_params['datagroup_id'] = params['datagroup_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datagroups/{datagroup_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datagroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_datagroup(self, body, datagroup_id, **kwargs):  # noqa: E501
        """Update Datagroup  # noqa: E501

        ### Update a datagroup using the specified params.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_datagroup(body, datagroup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datagroup body: Datagroup (required)
        :param str datagroup_id: ID of datagroup. (required)
        :return: Datagroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_datagroup_with_http_info(body, datagroup_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_datagroup_with_http_info(body, datagroup_id, **kwargs)  # noqa: E501
            return data

    def update_datagroup_with_http_info(self, body, datagroup_id, **kwargs):  # noqa: E501
        """Update Datagroup  # noqa: E501

        ### Update a datagroup using the specified params.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_datagroup_with_http_info(body, datagroup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datagroup body: Datagroup (required)
        :param str datagroup_id: ID of datagroup. (required)
        :return: Datagroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'datagroup_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_datagroup" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_datagroup`")  # noqa: E501
        # verify the required parameter 'datagroup_id' is set
        if ('datagroup_id' not in params or
                params['datagroup_id'] is None):
            raise ValueError("Missing the required parameter `datagroup_id` when calling `update_datagroup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datagroup_id' in params:
            path_params['datagroup_id'] = params['datagroup_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datagroups/{datagroup_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datagroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
