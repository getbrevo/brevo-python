# brevo_python.TransactionalEmailsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_new_domain**](TransactionalEmailsApi.md#block_new_domain) | **POST** /smtp/blockedDomains | Add a new domain to the list of blocked domains
[**create_smtp_template**](TransactionalEmailsApi.md#create_smtp_template) | **POST** /smtp/templates | Create an email template
[**delete_blocked_domain**](TransactionalEmailsApi.md#delete_blocked_domain) | **DELETE** /smtp/blockedDomains/{domain} | Unblock an existing domain from the list of blocked domains
[**delete_hardbounces**](TransactionalEmailsApi.md#delete_hardbounces) | **POST** /smtp/deleteHardbounces | Delete hardbounces
[**delete_scheduled_email_by_id**](TransactionalEmailsApi.md#delete_scheduled_email_by_id) | **DELETE** /smtp/email/{identifier} | Delete scheduled emails by batchId or messageId
[**delete_smtp_template**](TransactionalEmailsApi.md#delete_smtp_template) | **DELETE** /smtp/templates/{templateId} | Delete an inactive email template
[**get_aggregated_smtp_report**](TransactionalEmailsApi.md#get_aggregated_smtp_report) | **GET** /smtp/statistics/aggregatedReport | Get your transactional email activity aggregated over a period of time
[**get_blocked_domains**](TransactionalEmailsApi.md#get_blocked_domains) | **GET** /smtp/blockedDomains | Get the list of blocked domains
[**get_email_event_report**](TransactionalEmailsApi.md#get_email_event_report) | **GET** /smtp/statistics/events | Get all your transactional email activity (unaggregated events)
[**get_scheduled_email_by_batch_id**](TransactionalEmailsApi.md#get_scheduled_email_by_batch_id) | **GET** /smtp/emailStatus/{batchId} | Fetch scheduled emails by batchId
[**get_scheduled_email_by_message_id**](TransactionalEmailsApi.md#get_scheduled_email_by_message_id) | **GET** /smtp/emailStatus/{messageId} | Fetch scheduled email by messageId
[**get_smtp_report**](TransactionalEmailsApi.md#get_smtp_report) | **GET** /smtp/statistics/reports | Get your transactional email activity aggregated per day
[**get_smtp_template**](TransactionalEmailsApi.md#get_smtp_template) | **GET** /smtp/templates/{templateId} | Returns the template information
[**get_smtp_templates**](TransactionalEmailsApi.md#get_smtp_templates) | **GET** /smtp/templates | Get the list of email templates
[**get_transac_blocked_contacts**](TransactionalEmailsApi.md#get_transac_blocked_contacts) | **GET** /smtp/blockedContacts | Get the list of blocked or unsubscribed transactional contacts
[**get_transac_email_content**](TransactionalEmailsApi.md#get_transac_email_content) | **GET** /smtp/emails/{uuid} | Get the personalized content of a sent transactional email
[**get_transac_emails_list**](TransactionalEmailsApi.md#get_transac_emails_list) | **GET** /smtp/emails | Get the list of transactional emails on the basis of allowed filters
[**post_preview_smtp_email_templates**](TransactionalEmailsApi.md#post_preview_smtp_email_templates) | **POST** /smtp/template/preview | Generate the rendered preview of transactional template
[**send_test_template**](TransactionalEmailsApi.md#send_test_template) | **POST** /smtp/templates/{templateId}/sendTest | Send a template to your test list
[**send_transac_email**](TransactionalEmailsApi.md#send_transac_email) | **POST** /smtp/email | Send a transactional email
[**smtp_blocked_contacts_email_delete**](TransactionalEmailsApi.md#smtp_blocked_contacts_email_delete) | **DELETE** /smtp/blockedContacts/{email} | Unblock or resubscribe a transactional contact
[**smtp_log_identifier_delete**](TransactionalEmailsApi.md#smtp_log_identifier_delete) | **DELETE** /smtp/log/{identifier} | Delete an SMTP transactional log
[**update_smtp_template**](TransactionalEmailsApi.md#update_smtp_template) | **PUT** /smtp/templates/{templateId} | Update an email template


# **block_new_domain**
> block_new_domain(block_domain)

Add a new domain to the list of blocked domains

Blocks a new domain in order to avoid messages being sent to the same

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
block_domain = brevo_python.BlockDomain() # BlockDomain | 

try:
    # Add a new domain to the list of blocked domains
    api_instance.block_new_domain(block_domain)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->block_new_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_domain** | [**BlockDomain**](BlockDomain.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_smtp_template**
> CreateModel create_smtp_template(smtp_template)

Create an email template

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
smtp_template = brevo_python.CreateSmtpTemplate() # CreateSmtpTemplate | values to update in transactional email template

try:
    # Create an email template
    api_response = api_instance.create_smtp_template(smtp_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->create_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_template** | [**CreateSmtpTemplate**](CreateSmtpTemplate.md)| values to update in transactional email template | 

### Return type

[**CreateModel**](CreateModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blocked_domain**
> delete_blocked_domain(domain)

Unblock an existing domain from the list of blocked domains

Unblocks an existing domain from the list of blocked domains

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
domain = 'domain_example' # str | The name of the domain to be deleted

try:
    # Unblock an existing domain from the list of blocked domains
    api_instance.delete_blocked_domain(domain)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->delete_blocked_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of the domain to be deleted | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hardbounces**
> delete_hardbounces(delete_hardbounces=delete_hardbounces)

Delete hardbounces

Delete hardbounces. To use carefully (e.g. in case of temporary ISP failures)

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
delete_hardbounces = brevo_python.DeleteHardbounces() # DeleteHardbounces | values to delete hardbounces (optional)

try:
    # Delete hardbounces
    api_instance.delete_hardbounces(delete_hardbounces=delete_hardbounces)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->delete_hardbounces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_hardbounces** | [**DeleteHardbounces**](DeleteHardbounces.md)| values to delete hardbounces | [optional] 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_email_by_id**
> delete_scheduled_email_by_id(identifier)

Delete scheduled emails by batchId or messageId

Delete scheduled batch of emails by batchId or single scheduled email by messageId

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
identifier = 'identifier_example' # str | The `batchId` of scheduled emails batch (Should be a valid UUIDv4) or the `messageId` of scheduled email.

try:
    # Delete scheduled emails by batchId or messageId
    api_instance.delete_scheduled_email_by_id(identifier)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->delete_scheduled_email_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The &#x60;batchId&#x60; of scheduled emails batch (Should be a valid UUIDv4) or the &#x60;messageId&#x60; of scheduled email. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smtp_template**
> delete_smtp_template(template_id)

Delete an inactive email template

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
template_id = 789 # int | id of the template

try:
    # Delete an inactive email template
    api_instance.delete_smtp_template(template_id)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->delete_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the template | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_smtp_report**
> GetAggregatedReport get_aggregated_smtp_report(start_date=start_date, end_date=end_date, days=days, tag=tag)

Get your transactional email activity aggregated over a period of time

This endpoint will show the aggregated stats for past 90 days by default if `startDate` and `endDate` OR `days` is not passed. The date range can not exceed 90 days

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate (optional)
days = 789 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
tag = 'tag_example' # str | Tag of the emails (optional)

try:
    # Get your transactional email activity aggregated over a period of time
    api_response = api_instance.get_aggregated_smtp_report(start_date=start_date, end_date=end_date, days=days, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_aggregated_smtp_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **tag** | **str**| Tag of the emails | [optional] 

### Return type

[**GetAggregatedReport**](GetAggregatedReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocked_domains**
> GetBlockedDomains get_blocked_domains()

Get the list of blocked domains

Get the list of blocked domains

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))

try:
    # Get the list of blocked domains
    api_response = api_instance.get_blocked_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_blocked_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBlockedDomains**](GetBlockedDomains.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_event_report**
> GetEmailEventReport get_email_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, email=email, event=event, tags=tags, message_id=message_id, template_id=template_id, sort=sort)

Get all your transactional email activity (unaggregated events)

This endpoint will show the aggregated stats for past 30 days by default if `startDate` and `endDate` OR `days` is not passed. The date range can not exceed 90 days

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
limit = 2500 # int | Number limitation for the result returned (optional) (default to 2500)
offset = 0 # int | Beginning point in the list to retrieve from. (optional) (default to 0)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate (optional)
days = 789 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
email = 'email_example' # str | Filter the report for a specific email addresses (optional)
event = 'event_example' # str | Filter the report for a specific event type (optional)
tags = 'tags_example' # str | Filter the report for tags (serialized and urlencoded array) (optional)
message_id = 'message_id_example' # str | Filter on a specific message id (optional)
template_id = 789 # int | Filter on a specific template id (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Get all your transactional email activity (unaggregated events)
    api_response = api_instance.get_email_event_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, email=email, event=event, tags=tags, message_id=message_id, template_id=template_id, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_email_event_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number limitation for the result returned | [optional] [default to 2500]
 **offset** | **int**| Beginning point in the list to retrieve from. | [optional] [default to 0]
 **start_date** | **str**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD). Must be lower than equal to endDate | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **email** | **str**| Filter the report for a specific email addresses | [optional] 
 **event** | **str**| Filter the report for a specific event type | [optional] 
 **tags** | **str**| Filter the report for tags (serialized and urlencoded array) | [optional] 
 **message_id** | **str**| Filter on a specific message id | [optional] 
 **template_id** | **int**| Filter on a specific template id | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetEmailEventReport**](GetEmailEventReport.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_email_by_batch_id**
> GetScheduledEmailByBatchId get_scheduled_email_by_batch_id(batch_id, start_date=start_date, end_date=end_date, sort=sort, status=status, limit=limit, offset=offset)

Fetch scheduled emails by batchId

Fetch scheduled batch of emails by batchId (Can retrieve data upto 30 days old)

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
batch_id = 'batch_id_example' # str | The batchId of scheduled emails batch (Should be a valid UUIDv4)
start_date = '2013-10-20' # date | Mandatory if `endDate` is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older tha current date. (optional)
end_date = '2013-10-20' # date | Mandatory if `startDate` is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
status = 'status_example' # str | Filter the records by `status` of the scheduled email batch or message. (optional)
limit = 100 # int | Number of documents returned per page (optional) (default to 100)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)

try:
    # Fetch scheduled emails by batchId
    api_response = api_instance.get_scheduled_email_by_batch_id(batch_id, start_date=start_date, end_date=end_date, sort=sort, status=status, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_scheduled_email_by_batch_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| The batchId of scheduled emails batch (Should be a valid UUIDv4) | 
 **start_date** | **date**| Mandatory if &#x60;endDate&#x60; is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older tha current date. | [optional] 
 **end_date** | **date**| Mandatory if &#x60;startDate&#x60; is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **status** | **str**| Filter the records by &#x60;status&#x60; of the scheduled email batch or message. | [optional] 
 **limit** | **int**| Number of documents returned per page | [optional] [default to 100]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]

### Return type

[**GetScheduledEmailByBatchId**](GetScheduledEmailByBatchId.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_email_by_message_id**
> GetScheduledEmailByMessageId get_scheduled_email_by_message_id(message_id, start_date=start_date, end_date=end_date)

Fetch scheduled email by messageId

Fetch scheduled email by messageId (Can retrieve data upto 30 days old)

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
message_id = 'message_id_example' # str | The messageId of scheduled email
start_date = '2013-10-20' # date | Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older tha current date. (optional)
end_date = '2013-10-20' # date | Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. (optional)

try:
    # Fetch scheduled email by messageId
    api_response = api_instance.get_scheduled_email_by_message_id(message_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_scheduled_email_by_message_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The messageId of scheduled email | 
 **start_date** | **date**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Can be maximum 30 days older tha current date. | [optional] 
 **end_date** | **date**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 

### Return type

[**GetScheduledEmailByMessageId**](GetScheduledEmailByMessageId.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_report**
> GetReports get_smtp_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, tag=tag, sort=sort)

Get your transactional email activity aggregated per day

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
limit = 10 # int | Number of documents returned per page (optional) (default to 10)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD) (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD) (optional)
days = 789 # int | Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate' (optional)
tag = 'tag_example' # str | Tag of the emails (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Get your transactional email activity aggregated per day
    api_response = api_instance.get_smtp_report(limit=limit, offset=offset, start_date=start_date, end_date=end_date, days=days, tag=tag, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_smtp_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents returned per page | [optional] [default to 10]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]
 **start_date** | **str**| Mandatory if endDate is used. Starting date of the report (YYYY-MM-DD) | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD) | [optional] 
 **days** | **int**| Number of days in the past including today (positive integer). Not compatible with &#39;startDate&#39; and &#39;endDate&#39; | [optional] 
 **tag** | **str**| Tag of the emails | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetReports**](GetReports.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_template**
> GetSmtpTemplateOverview get_smtp_template(template_id)

Returns the template information

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
template_id = 789 # int | id of the template

try:
    # Returns the template information
    api_response = api_instance.get_smtp_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the template | 

### Return type

[**GetSmtpTemplateOverview**](GetSmtpTemplateOverview.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smtp_templates**
> GetSmtpTemplates get_smtp_templates(template_status=template_status, limit=limit, offset=offset, sort=sort)

Get the list of email templates

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
template_status = true # bool | Filter on the status of the template. Active = true, inactive = false (optional)
limit = 50 # int | Number of documents returned per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Get the list of email templates
    api_response = api_instance.get_smtp_templates(template_status=template_status, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_smtp_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_status** | **bool**| Filter on the status of the template. Active &#x3D; true, inactive &#x3D; false | [optional] 
 **limit** | **int**| Number of documents returned per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetSmtpTemplates**](GetSmtpTemplates.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transac_blocked_contacts**
> GetTransacBlockedContacts get_transac_blocked_contacts(start_date=start_date, end_date=end_date, limit=limit, offset=offset, senders=senders, sort=sort)

Get the list of blocked or unsubscribed transactional contacts

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the blocked or unsubscribed contacts (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the blocked or unsubscribed contacts (optional)
limit = 50 # int | Number of documents returned per page (optional) (default to 50)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)
senders = ['senders_example'] # list[str] | Comma separated list of emails of the senders from which contacts are blocked or unsubscribed (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

try:
    # Get the list of blocked or unsubscribed transactional contacts
    api_response = api_instance.get_transac_blocked_contacts(start_date=start_date, end_date=end_date, limit=limit, offset=offset, senders=senders, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_transac_blocked_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the blocked or unsubscribed contacts | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the blocked or unsubscribed contacts | [optional] 
 **limit** | **int**| Number of documents returned per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]
 **senders** | [**list[str]**](str.md)| Comma separated list of emails of the senders from which contacts are blocked or unsubscribed | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]

### Return type

[**GetTransacBlockedContacts**](GetTransacBlockedContacts.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transac_email_content**
> GetTransacEmailContent get_transac_email_content(uuid)

Get the personalized content of a sent transactional email

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique id of the transactional email that has been sent to a particular contact

try:
    # Get the personalized content of a sent transactional email
    api_response = api_instance.get_transac_email_content(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_transac_email_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Unique id of the transactional email that has been sent to a particular contact | 

### Return type

[**GetTransacEmailContent**](GetTransacEmailContent.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transac_emails_list**
> GetTransacEmailsList get_transac_emails_list(email=email, template_id=template_id, message_id=message_id, start_date=start_date, end_date=end_date, sort=sort, limit=limit, offset=offset)

Get the list of transactional emails on the basis of allowed filters

This endpoint will show the list of emails for past 30 days by default. To retrieve emails before that time, please pass startDate and endDate in query filters.

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
email = 'email_example' # str | Mandatory if templateId and messageId are not passed in query filters. Email address to which transactional email has been sent. (optional)
template_id = 789 # int | Mandatory if email and messageId are not passed in query filters. Id of the template that was used to compose transactional email. (optional)
message_id = 'message_id_example' # str | Mandatory if templateId and email are not passed in query filters. Message ID of the transactional email sent. (optional)
start_date = 'start_date_example' # str | Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. (optional)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
limit = 500 # int | Number of documents returned per page (optional) (default to 500)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)

try:
    # Get the list of transactional emails on the basis of allowed filters
    api_response = api_instance.get_transac_emails_list(email=email, template_id=template_id, message_id=message_id, start_date=start_date, end_date=end_date, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->get_transac_emails_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Mandatory if templateId and messageId are not passed in query filters. Email address to which transactional email has been sent. | [optional] 
 **template_id** | **int**| Mandatory if email and messageId are not passed in query filters. Id of the template that was used to compose transactional email. | [optional] 
 **message_id** | **str**| Mandatory if templateId and email are not passed in query filters. Message ID of the transactional email sent. | [optional] 
 **start_date** | **str**| Mandatory if endDate is used. Starting date (YYYY-MM-DD) from which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Ending date (YYYY-MM-DD) till which you want to fetch the list. Maximum time period that can be selected is one month. | [optional] 
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **limit** | **int**| Number of documents returned per page | [optional] [default to 500]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]

### Return type

[**GetTransacEmailsList**](GetTransacEmailsList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_preview_smtp_email_templates**
> TemplatePreview post_preview_smtp_email_templates(fetch_template_preview)

Generate the rendered preview of transactional template

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
fetch_template_preview = brevo_python.FetchTemplatePreview() # FetchTemplatePreview | Values to fetch Template preview

try:
    # Generate the rendered preview of transactional template
    api_response = api_instance.post_preview_smtp_email_templates(fetch_template_preview)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->post_preview_smtp_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_template_preview** | [**FetchTemplatePreview**](FetchTemplatePreview.md)| Values to fetch Template preview | 

### Return type

[**TemplatePreview**](TemplatePreview.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_template**
> send_test_template(template_id, send_test_email)

Send a template to your test list

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
template_id = 789 # int | Id of the template
send_test_email = brevo_python.SendTestEmail() # SendTestEmail | 

try:
    # Send a template to your test list
    api_instance.send_test_template(template_id, send_test_email)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->send_test_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Id of the template | 
 **send_test_email** | [**SendTestEmail**](SendTestEmail.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_transac_email**
> CreateSmtpEmail send_transac_email(send_smtp_email)

Send a transactional email

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
send_smtp_email = brevo_python.SendSmtpEmail() # SendSmtpEmail | Values to send a transactional email

try:
    # Send a transactional email
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_smtp_email** | [**SendSmtpEmail**](SendSmtpEmail.md)| Values to send a transactional email | 

### Return type

[**CreateSmtpEmail**](CreateSmtpEmail.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smtp_blocked_contacts_email_delete**
> smtp_blocked_contacts_email_delete(email)

Unblock or resubscribe a transactional contact

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
email = 'email_example' # str | contact email (urlencoded) to unblock.

try:
    # Unblock or resubscribe a transactional contact
    api_instance.smtp_blocked_contacts_email_delete(email)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->smtp_blocked_contacts_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| contact email (urlencoded) to unblock. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smtp_log_identifier_delete**
> smtp_log_identifier_delete(identifier)

Delete an SMTP transactional log

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
identifier = 'identifier_example' # str | MessageId of the transactional log(s) to delete

try:
    # Delete an SMTP transactional log
    api_instance.smtp_log_identifier_delete(identifier)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->smtp_log_identifier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| MessageId of the transactional log(s) to delete | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smtp_template**
> update_smtp_template(template_id, smtp_template)

Update an email template

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
api_instance = brevo_python.TransactionalEmailsApi(brevo_python.ApiClient(configuration))
template_id = 789 # int | id of the template
smtp_template = brevo_python.UpdateSmtpTemplate() # UpdateSmtpTemplate | values to update in transactional email template

try:
    # Update an email template
    api_instance.update_smtp_template(template_id, smtp_template)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->update_smtp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| id of the template | 
 **smtp_template** | [**UpdateSmtpTemplate**](UpdateSmtpTemplate.md)| values to update in transactional email template | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

