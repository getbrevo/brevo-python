# brevo_python.UserApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invited_users_list**](UserApi.md#get_invited_users_list) | **GET** /organization/invited/users | Get the list of all your users
[**get_user_permission**](UserApi.md#get_user_permission) | **GET** /organization/user/{email}/permissions | Check user permission


# **get_invited_users_list**
> GetInvitedUsersList get_invited_users_list()

Get the list of all your users

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
api_instance = brevo_python.UserApi(brevo_python.ApiClient(configuration))

try:
    # Get the list of all your users
    api_response = api_instance.get_invited_users_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_invited_users_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInvitedUsersList**](GetInvitedUsersList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permission**
> GetUserPermission get_user_permission(email)

Check user permission

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
api_instance = brevo_python.UserApi(brevo_python.ApiClient(configuration))
email = 'email_example' # str | Email of the invited user.

try:
    # Check user permission
    api_response = api_instance.get_user_permission(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the invited user. | 

### Return type

[**GetUserPermission**](GetUserPermission.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

