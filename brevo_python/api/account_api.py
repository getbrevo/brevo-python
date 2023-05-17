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


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_account(self, **kwargs):  # noqa: E501
        """Get your account information, plan and credits details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_account_with_http_info(self, **kwargs):  # noqa: E501
        """Get your account information, plan and credits details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAccount
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
                    " to method get_account" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_activity(self, **kwargs):  # noqa: E501
        """Get user activity logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_activity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Enter start date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. Additionally, you can retrieve activity logs from the past 12 months from the date of your search.
        :param str end_date: Mandatory if startDate is used. Enter end date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month.
        :param int limit: Number of documents per page
        :param int offset: Index of the first document in the page.
        :return: GetAccountActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_activity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_account_activity_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_account_activity_with_http_info(self, **kwargs):  # noqa: E501
        """Get user activity logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_activity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Enter start date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. Additionally, you can retrieve activity logs from the past 12 months from the date of your search.
        :param str end_date: Mandatory if startDate is used. Enter end date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month.
        :param int limit: Number of documents per page
        :param int offset: Index of the first document in the page.
        :return: GetAccountActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_activity" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_account_activity`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_account_activity`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/organization/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAccountActivity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
