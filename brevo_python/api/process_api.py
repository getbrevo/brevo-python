# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from brevo_python.api_client import ApiClient


class ProcessApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_process(self, process_id, **kwargs):  # noqa: E501
        """Return the informations for a process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_process(process_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int process_id: Id of the process (required)
        :return: GetProcess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_process_with_http_info(process_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_process_with_http_info(process_id, **kwargs)  # noqa: E501
            return data

    def get_process_with_http_info(self, process_id, **kwargs):  # noqa: E501
        """Return the informations for a process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_process_with_http_info(process_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int process_id: Id of the process (required)
        :return: GetProcess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['process_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_process" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'process_id' is set
        if ('process_id' not in params or
                params['process_id'] is None):
            raise ValueError("Missing the required parameter `process_id` when calling `get_process`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'process_id' in params:
            path_params['processId'] = params['process_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/processes/{processId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetProcess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_processes(self, **kwargs):  # noqa: E501
        """Return all the processes for your account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_processes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number limitation for the result returned
        :param int offset: Beginning point in the list to retrieve from.
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetProcesses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_processes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_processes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_processes_with_http_info(self, **kwargs):  # noqa: E501
        """Return all the processes for your account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_processes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number limitation for the result returned
        :param int offset: Beginning point in the list to retrieve from.
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetProcesses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_processes" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_processes`, must be a value less than or equal to `50`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_processes`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/processes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetProcesses',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
