# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   | 422  | Error. Unprocessable Entity |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from brevo_python.api_client import ApiClient


class TransactionalSMSApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_sms_events(self, **kwargs):  # noqa: E501
        """Get all your SMS activity (unaggregated events)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of documents per page
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int offset: Index of the first document of the page
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str phone_number: Filter the report for a specific phone number
        :param str event: Filter the report for specific events
        :param str tags: Filter the report for specific tags passed as a serialized urlencoded array
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetSmsEventReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sms_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sms_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sms_events_with_http_info(self, **kwargs):  # noqa: E501
        """Get all your SMS activity (unaggregated events)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of documents per page
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int offset: Index of the first document of the page
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str phone_number: Filter the report for a specific phone number
        :param str event: Filter the report for specific events
        :param str tags: Filter the report for specific tags passed as a serialized urlencoded array
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetSmsEventReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'start_date', 'end_date', 'offset', 'days', 'phone_number', 'event', 'tags', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_events" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_sms_events`, must be a value less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501
        if 'phone_number' in params:
            query_params.append(('phoneNumber', params['phone_number']))  # noqa: E501
        if 'event' in params:
            query_params.append(('event', params['event']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
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
            '/transactionalSMS/statistics/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSmsEventReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transac_aggregated_sms_report(self, **kwargs):  # noqa: E501
        """Get your SMS activity aggregated over a period of time  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transac_aggregated_sms_report(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with startDate and endDate
        :param str tag: Filter on a tag
        :return: GetTransacAggregatedSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transac_aggregated_sms_report_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_transac_aggregated_sms_report_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_transac_aggregated_sms_report_with_http_info(self, **kwargs):  # noqa: E501
        """Get your SMS activity aggregated over a period of time  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transac_aggregated_sms_report_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with startDate and endDate
        :param str tag: Filter on a tag
        :return: GetTransacAggregatedSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'days', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transac_aggregated_sms_report" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

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
            '/transactionalSMS/statistics/aggregatedReport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTransacAggregatedSmsReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transac_sms_report(self, **kwargs):  # noqa: E501
        """Get your SMS activity aggregated per day  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transac_sms_report(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str tag: Filter on a tag
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetTransacSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transac_sms_report_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_transac_sms_report_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_transac_sms_report_with_http_info(self, **kwargs):  # noqa: E501
        """Get your SMS activity aggregated per day  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transac_sms_report_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param str end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str tag: Filter on a tag
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetTransacSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'days', 'tag', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transac_sms_report" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
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
            '/transactionalSMS/statistics/reports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTransacSmsReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_transac_sms(self, send_transac_sms, **kwargs):  # noqa: E501
        """Send SMS message to a mobile number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_transac_sms(send_transac_sms, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendTransacSms send_transac_sms: Values to send a transactional SMS (required)
        :return: SendSms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_transac_sms_with_http_info(send_transac_sms, **kwargs)  # noqa: E501
        else:
            (data) = self.send_transac_sms_with_http_info(send_transac_sms, **kwargs)  # noqa: E501
            return data

    def send_transac_sms_with_http_info(self, send_transac_sms, **kwargs):  # noqa: E501
        """Send SMS message to a mobile number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_transac_sms_with_http_info(send_transac_sms, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendTransacSms send_transac_sms: Values to send a transactional SMS (required)
        :return: SendSms
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['send_transac_sms']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_transac_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'send_transac_sms' is set
        if ('send_transac_sms' not in params or
                params['send_transac_sms'] is None):
            raise ValueError("Missing the required parameter `send_transac_sms` when calling `send_transac_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'send_transac_sms' in params:
            body_params = params['send_transac_sms']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/transactionalSMS/sms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendSms',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
