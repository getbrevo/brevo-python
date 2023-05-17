# brevo_python.WebhooksApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create a webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete a webhook
[**export_webhooks_history**](WebhooksApi.md#export_webhooks_history) | **POST** /webhooks/export | Export all transactional events
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Get a webhook details
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get all webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhookId} | Update a webhook


# **create_webhook**
> CreateModel create_webhook(create_webhook)

Create a webhook

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
create_webhook = brevo_python.CreateWebhook() # CreateWebhook | Values to create a webhook

try:
    # Create a webhook
    api_response = api_instance.create_webhook(create_webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook** | [**CreateWebhook**](CreateWebhook.md)| Values to create a webhook | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(webhook_id)

Delete a webhook

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
webhook_id = 789 # int | Id of the webhook

try:
    # Delete a webhook
    api_instance.delete_webhook(webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**| Id of the webhook | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_webhooks_history**
> CreatedProcessId export_webhooks_history(export_webhook_history)

Export all transactional events

This endpoint will submit a request to get the history of webhooks in the CSV file. The link to download that CSV file will send to the webhook link provided in notifyURL of the body payload.

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
export_webhook_history = brevo_python.ExportWebhooksHistory() # ExportWebhooksHistory | Values to submit for webhooks history

try:
    # Export all transactional events
    api_response = api_instance.export_webhooks_history(export_webhook_history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->export_webhooks_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_webhook_history** | [**ExportWebhooksHistory**](ExportWebhooksHistory.md)| Values to submit for webhooks history | 

### Return type

[**CreatedProcessId**](CreatedProcessId.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> GetWebhook get_webhook(webhook_id)

Get a webhook details

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
webhook_id = 789 # int | Id of the webhook

try:
    # Get a webhook details
    api_response = api_instance.get_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**| Id of the webhook | 

### Return type

[**GetWebhook**](GetWebhook.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> GetWebhooks get_webhooks(type=type, sort=sort)

Get all webhooks

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
type = 'transactional' # str | Filter on webhook type (optional) (default to transactional)
sort = 'desc' # str | Sort the results in the ascending/descending order of webhook creation (optional) (default to desc)

try:
    # Get all webhooks
    api_response = api_instance.get_webhooks(type=type, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on webhook type | [optional] [default to transactional]
 **sort** | **str**| Sort the results in the ascending/descending order of webhook creation | [optional] [default to desc]

### Return type

[**GetWebhooks**](GetWebhooks.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> update_webhook(webhook_id, update_webhook)

Update a webhook

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
api_instance = brevo_python.WebhooksApi(brevo_python.ApiClient(configuration))
webhook_id = 789 # int | Id of the webhook
update_webhook = brevo_python.UpdateWebhook() # UpdateWebhook | Values to update a webhook

try:
    # Update a webhook
    api_instance.update_webhook(webhook_id, update_webhook)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **int**| Id of the webhook | 
 **update_webhook** | [**UpdateWebhook**](UpdateWebhook.md)| Values to update a webhook | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

