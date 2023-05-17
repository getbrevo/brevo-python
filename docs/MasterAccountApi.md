# brevo_python.MasterAccountApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corporate_master_account_get**](MasterAccountApi.md#corporate_master_account_get) | **GET** /corporate/masterAccount | Get the details of requested master account
[**corporate_sub_account_get**](MasterAccountApi.md#corporate_sub_account_get) | **GET** /corporate/subAccount | Get the list of all the sub-accounts of the master account.
[**corporate_sub_account_id_delete**](MasterAccountApi.md#corporate_sub_account_id_delete) | **DELETE** /corporate/subAccount/{id} | Delete a sub-account
[**corporate_sub_account_id_get**](MasterAccountApi.md#corporate_sub_account_id_get) | **GET** /corporate/subAccount/{id} | Get sub-account details
[**corporate_sub_account_id_plan_put**](MasterAccountApi.md#corporate_sub_account_id_plan_put) | **PUT** /corporate/subAccount/{id}/plan | Update sub-account plan
[**corporate_sub_account_key_post**](MasterAccountApi.md#corporate_sub_account_key_post) | **POST** /corporate/subAccount/key | Create an API key for a sub-account
[**corporate_sub_account_post**](MasterAccountApi.md#corporate_sub_account_post) | **POST** /corporate/subAccount | Create a new sub-account under a master account.
[**corporate_sub_account_sso_token_post**](MasterAccountApi.md#corporate_sub_account_sso_token_post) | **POST** /corporate/subAccount/ssoToken | Generate SSO token to access Brevo
[**get_account_activity**](MasterAccountApi.md#get_account_activity) | **GET** /organization/activities | Get user activity logs


# **corporate_master_account_get**
> MasterDetailsResponse corporate_master_account_get()

Get the details of requested master account

This endpoint will provide the details of the master account.

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))

try:
    # Get the details of requested master account
    api_response = api_instance.corporate_master_account_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_master_account_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MasterDetailsResponse**](MasterDetailsResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_get**
> SubAccountsResponse corporate_sub_account_get(offset, limit)

Get the list of all the sub-accounts of the master account.

This endpoint will provide the list all the sub-accounts of the master account.

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
offset = 56 # int | Index of the first sub-account in the page
limit = 56 # int | Number of sub-accounts to be displayed on each page

try:
    # Get the list of all the sub-accounts of the master account.
    api_response = api_instance.corporate_sub_account_get(offset, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of the first sub-account in the page | 
 **limit** | **int**| Number of sub-accounts to be displayed on each page | 

### Return type

[**SubAccountsResponse**](SubAccountsResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_id_delete**
> corporate_sub_account_id_delete(id)

Delete a sub-account

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
id = 789 # int | Id of the sub-account organization to be deleted

try:
    # Delete a sub-account
    api_instance.corporate_sub_account_id_delete(id)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the sub-account organization to be deleted | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_id_get**
> SubAccountDetailsResponse corporate_sub_account_id_get(id)

Get sub-account details

This endpoint will provide the details for the specified sub-account company

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
id = 789 # int | Id of the sub-account organization

try:
    # Get sub-account details
    api_response = api_instance.corporate_sub_account_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the sub-account organization | 

### Return type

[**SubAccountDetailsResponse**](SubAccountDetailsResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_id_plan_put**
> corporate_sub_account_id_plan_put(id, update_plan_details)

Update sub-account plan

This endpoint will update the sub-account plan

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
id = 789 # int | Id of the sub-account organization
update_plan_details = brevo_python.SubAccountUpdatePlanRequest() # SubAccountUpdatePlanRequest | Values to update a sub-account plan

try:
    # Update sub-account plan
    api_instance.corporate_sub_account_id_plan_put(id, update_plan_details)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_id_plan_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the sub-account organization | 
 **update_plan_details** | [**SubAccountUpdatePlanRequest**](SubAccountUpdatePlanRequest.md)| Values to update a sub-account plan | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_key_post**
> CreateApiKeyResponse corporate_sub_account_key_post(create_api_key_request)

Create an API key for a sub-account

This endpoint will generate an API v3 key for a sub account

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
create_api_key_request = brevo_python.CreateApiKeyRequest() # CreateApiKeyRequest | Values to generate API key for sub-account

try:
    # Create an API key for a sub-account
    api_response = api_instance.corporate_sub_account_key_post(create_api_key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_key_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)| Values to generate API key for sub-account | 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_post**
> CreateSubAccountResponse corporate_sub_account_post(sub_account_create)

Create a new sub-account under a master account.

This endpoint will create a new sub-account under a master account

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
sub_account_create = brevo_python.CreateSubAccount() # CreateSubAccount | values to create new sub-account

try:
    # Create a new sub-account under a master account.
    api_response = api_instance.corporate_sub_account_post(sub_account_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_create** | [**CreateSubAccount**](CreateSubAccount.md)| values to create new sub-account | 

### Return type

[**CreateSubAccountResponse**](CreateSubAccountResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_sso_token_post**
> GetSsoToken corporate_sub_account_sso_token_post(sso_token_request)

Generate SSO token to access Brevo

This endpoint generates an sso token to authenticate and access a sub-account of the master using the account endpoint https://account-app.brevo.com/account/login/sub-account/sso/[token], where [token] will be replaced by the actual token.

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
sso_token_request = brevo_python.SsoTokenRequest() # SsoTokenRequest | Values to generate SSO token for sub-account

try:
    # Generate SSO token to access Brevo
    api_response = api_instance.corporate_sub_account_sso_token_post(sso_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_sso_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_token_request** | [**SsoTokenRequest**](SsoTokenRequest.md)| Values to generate SSO token for sub-account | 

### Return type

[**GetSsoToken**](GetSsoToken.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_activity**
> GetAccountActivity get_account_activity(start_date=start_date, end_date=end_date, limit=limit, offset=offset)

Get user activity logs

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
api_instance = brevo_python.MasterAccountApi(brevo_python.ApiClient(configuration))
start_date = 'start_date_example' # str | Mandatory if endDate is used. Enter start date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. Additionally, you can retrieve activity logs from the past 12 months from the date of your search. (optional)
end_date = 'end_date_example' # str | Mandatory if startDate is used. Enter end date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. (optional)
limit = 10 # int | Number of documents per page (optional) (default to 10)
offset = 0 # int | Index of the first document in the page. (optional) (default to 0)

try:
    # Get user activity logs
    api_response = api_instance.get_account_activity(start_date=start_date, end_date=end_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->get_account_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Mandatory if endDate is used. Enter start date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. Additionally, you can retrieve activity logs from the past 12 months from the date of your search. | [optional] 
 **end_date** | **str**| Mandatory if startDate is used. Enter end date in UTC date (YYYY-MM-DD) format to filter the activity in your account. Maximum time period that can be selected is one month. | [optional] 
 **limit** | **int**| Number of documents per page | [optional] [default to 10]
 **offset** | **int**| Index of the first document in the page. | [optional] [default to 0]

### Return type

[**GetAccountActivity**](GetAccountActivity.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

