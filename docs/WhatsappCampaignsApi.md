# brevo_python.WhatsAppCampaignsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_whats_app_campaign**](WhatsAppCampaignsApi.md#create_whats_app_campaign) | **POST** /whatsappCampaigns | Create and Send a WhatsApp campaign
[**create_whats_app_template**](WhatsAppCampaignsApi.md#create_whats_app_template) | **POST** /whatsppCampaigns/template | Create a WhatsApp template
[**delete_whats_app_campaign**](WhatsAppCampaignsApi.md#delete_whats_app_campaign) | **DELETE** /whatsappCampaigns/{campaignId} | Delete a WhatsApp campaign
[**get_whats_app_campaign**](WhatsAppCampaignsApi.md#get_whats_app_campaign) | **GET** /whatsappCampaigns/{campaignId} | Get a WhatsApp campaign
[**get_whats_app_campaigns**](WhatsAppCampaignsApi.md#get_whats_app_campaigns) | **GET** /whatsappCampaigns | Return all your created WhatsApp campaigns
[**get_whats_app_config**](WhatsAppCampaignsApi.md#get_whats_app_config) | **GET** /whatsappCampaigns/config | Get your WhatsApp API account information
[**get_whats_app_templates**](WhatsAppCampaignsApi.md#get_whats_app_templates) | **GET** /whatsappCampaigns/template-list | Return all your created WhatsApp templates
[**send_whats_app_template_approval**](WhatsAppCampaignsApi.md#send_whats_app_template_approval) | **POST** /whatsappCampaigns/template/approval/{templateId} | Send your WhatsApp template for approval
[**update_whats_app_campaign**](WhatsAppCampaignsApi.md#update_whats_app_campaign) | **PUT** /whatsappCampaigns/{campaignId} | Update a WhatsApp campaign


# **create_whats_app_campaign**
> CreateModel create_whats_app_campaign(whats_app_campaigns)

Create and Send a WhatsApp campaign

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
whats_app_campaigns = brevo_python.CreateWhatsAppCampaign() # CreateWhatsAppCampaign | Values to create a campaign

try:
    # Create and Send a WhatsApp campaign
    api_response = api_instance.create_whats_app_campaign(whats_app_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->create_whats_app_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whats_app_campaigns** | [**CreateWhatsAppCampaign**](CreateWhatsAppCampaign.md)| Values to create a campaign | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_whats_app_template**
> CreateModel create_whats_app_template(whats_app_templates)

Create a WhatsApp template

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
whats_app_templates = brevo_python.CreateWhatsAppTemplate() # CreateWhatsAppTemplate | Values to create a template

try:
    # Create a WhatsApp template
    api_response = api_instance.create_whats_app_template(whats_app_templates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->create_whats_app_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whats_app_templates** | [**CreateWhatsAppTemplate**](CreateWhatsAppTemplate.md)| Values to create a template | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_whats_app_campaign**
> delete_whats_app_campaign(campaign_id)

Delete a WhatsApp campaign

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
campaign_id = 789 # int | id of the campaign

try:
    # Delete a WhatsApp campaign
    api_instance.delete_whats_app_campaign(campaign_id)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->delete_whats_app_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whats_app_campaign**
> GetWhatsappCampaignOverview get_whats_app_campaign(campaign_id)

Get a WhatsApp campaign

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign

try:
    # Get a WhatsApp campaign
    api_response = api_instance.get_whats_app_campaign(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->get_whats_app_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 

### Return type

[**GetWhatsappCampaignOverview**](GetWhatsappCampaignOverview.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whats_app_campaigns**
> GetWhatsappCampaigns get_whats_app_campaigns(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)

Return all your created WhatsApp campaigns

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
start_date = 'start_date_example' # str | **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the campaigns created. **Prefer to pass your timezone in date-time format for accurate result**  (optional)
end_date = 'end_date_example' # str | **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the campaigns created. **Prefer to pass your timezone in date-time format for accurate result**  (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record modification. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Return all your created WhatsApp campaigns
    api_response = api_instance.get_whats_app_campaigns(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->get_whats_app_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the campaigns created. **Prefer to pass your timezone in date-time format for accurate result**  | [optional] 
 **end_date** | **str**| **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the campaigns created. **Prefer to pass your timezone in date-time format for accurate result**  | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record modification. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetWhatsappCampaigns**](GetWhatsappCampaigns.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whats_app_config**
> GetWhatsAppConfig get_whats_app_config()

Get your WhatsApp API account information

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))

try:
    # Get your WhatsApp API account information
    api_response = api_instance.get_whats_app_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->get_whats_app_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetWhatsAppConfig**](GetWhatsAppConfig.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whats_app_templates**
> GetWATemplates get_whats_app_templates(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort, source=source)

Return all your created WhatsApp templates

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
start_date = 'start_date_example' # str | **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**  (optional)
end_date = 'end_date_example' # str | **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**  (optional)
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record modification. Default order is **descending** if `sort` is not passed (optional) (default to desc)
source = 'source_example' # str | source of the template (optional)

try:
    # Return all your created WhatsApp templates
    api_response = api_instance.get_whats_app_templates(start_date=start_date, end_date=end_date, limit=limit, offset=offset, sort=sort, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->get_whats_app_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| **Mandatory if endDate is used**. Starting (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**  | [optional] 
 **end_date** | **str**| **Mandatory if startDate is used**. Ending (urlencoded) UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) to filter the templates created. **Prefer to pass your timezone in date-time format for accurate result**  | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record modification. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **source** | **str**| source of the template | [optional] 

### Return type

[**GetWATemplates**](GetWATemplates.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_whats_app_template_approval**
> send_whats_app_template_approval(template_id)

Send your WhatsApp template for approval

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
template_id = 789 # int | id of the campaign

try:
    # Send your WhatsApp template for approval
    api_instance.send_whats_app_template_approval(template_id)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->send_whats_app_template_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the campaign | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_whats_app_campaign**
> update_whats_app_campaign(campaign_id, whats_app_campaign=whats_app_campaign)

Update a WhatsApp campaign

### Example
```python
from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = brevo_python.Configuration()
configuration.api_key['partner-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = brevo_python.WhatsAppCampaignsApi(brevo_python.ApiClient(configuration))
campaign_id = 789 # int | Id of the campaign
whats_app_campaign = brevo_python.UpdateWhatsAppCampaign() # UpdateWhatsAppCampaign | values to update WhatsApp Campaign (optional)

try:
    # Update a WhatsApp campaign
    api_instance.update_whats_app_campaign(campaign_id, whats_app_campaign=whats_app_campaign)
except ApiException as e:
    print("Exception when calling WhatsAppCampaignsApi->update_whats_app_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| Id of the campaign | 
 **whats_app_campaign** | [**UpdateWhatsAppCampaign**](UpdateWhatsAppCampaign.md)| values to update WhatsApp Campaign | [optional] 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

