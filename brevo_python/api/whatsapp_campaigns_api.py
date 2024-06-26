# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/getbrevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from brevo_python.api_client import ApiClient


class WhatsappCampaignsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_whatsapp_campaign(self, campaign_id, **kwargs):  # noqa: E501
        """Delete a Whatsapp campaign  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_whatsapp_campaign(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: id of the campaign (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_whatsapp_campaign_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_whatsapp_campaign_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def delete_whatsapp_campaign_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Delete a Whatsapp campaign  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_whatsapp_campaign_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int campaign_id: id of the campaign (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_whatsapp_campaign" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `delete_whatsapp_campaign`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'campaign_id' in params:
            path_params['campaignId'] = params['campaign_id']  # noqa: E501

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
            '/whatsappCampaigns/{campaignId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_campaign(self, campaign_id, **kwargs):  # noqa: E501
        """Get a Whatsapp campaign  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_whatsapp_campaign(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str campaign_id: Id of the campaign (required)
        :return: GetWhatsappCampaignOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_campaign_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_campaign_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def get_whatsapp_campaign_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Get a Whatsapp campaign  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_whatsapp_campaign_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str campaign_id: Id of the campaign (required)
        :return: GetWhatsappCampaignOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_campaign" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `get_whatsapp_campaign`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'campaign_id' in params:
            path_params['campaignId'] = params['campaign_id']  # noqa: E501

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
            '/whatsappCampaigns/{campaignId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetWhatsappCampaignOverview',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_whatsapp_templates(self, **kwargs):  # noqa: E501
        """Return all your created whatsapp templates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_whatsapp_templates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' ) 
        :param str end_date: **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' ) 
        :param int limit: Number of documents per page
        :param int offset: Index of the first document in the page
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetWATemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_whatsapp_templates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_whatsapp_templates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_whatsapp_templates_with_http_info(self, **kwargs):  # noqa: E501
        """Return all your created whatsapp templates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_whatsapp_templates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' ) 
        :param str end_date: **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result** ( only available if either 'status' not passed and if passed is set to 'sent' ) 
        :param int limit: Number of documents per page
        :param int offset: Index of the first document in the page
        :param str sort: Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed
        :return: GetWATemplates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'limit', 'offset', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_whatsapp_templates" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_whatsapp_templates`, must be a value less than or equal to `100`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_whatsapp_templates`, must be a value greater than or equal to `0`")  # noqa: E501
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
            '/whatsappCampaigns/template-list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetWATemplates',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
