# brevo_python.MasterAccountApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corporate_group_id_delete**](MasterAccountApi.md#corporate_group_id_delete) | **DELETE** /corporate/group/{id} | Delete a group
[**corporate_group_id_get**](MasterAccountApi.md#corporate_group_id_get) | **GET** /corporate/group/{id} | GET a group details
[**corporate_group_id_put**](MasterAccountApi.md#corporate_group_id_put) | **PUT** /corporate/group/{id} | Update a group of sub-accounts
[**corporate_group_post**](MasterAccountApi.md#corporate_group_post) | **POST** /corporate/group | Create a new group of sub-accounts
[**corporate_group_unlink_group_id_sub_accounts_put**](MasterAccountApi.md#corporate_group_unlink_group_id_sub_accounts_put) | **PUT** /corporate/group/unlink/{groupId}/subAccounts | Delete sub-account from group
[**corporate_master_account_get**](MasterAccountApi.md#corporate_master_account_get) | **GET** /corporate/masterAccount | Get the details of requested master account
[**corporate_sso_token_post**](MasterAccountApi.md#corporate_sso_token_post) | **POST** /corporate/ssoToken | Generate SSO token to access admin account
[**corporate_sub_account_get**](MasterAccountApi.md#corporate_sub_account_get) | **GET** /corporate/subAccount | Get the list of all the sub-accounts of the master account.
[**corporate_sub_account_id_applications_toggle_put**](MasterAccountApi.md#corporate_sub_account_id_applications_toggle_put) | **PUT** /corporate/subAccount/{id}/applications/toggle | Enable/disable sub-account application(s)
[**corporate_sub_account_id_delete**](MasterAccountApi.md#corporate_sub_account_id_delete) | **DELETE** /corporate/subAccount/{id} | Delete a sub-account
[**corporate_sub_account_id_get**](MasterAccountApi.md#corporate_sub_account_id_get) | **GET** /corporate/subAccount/{id} | Get sub-account details
[**corporate_sub_account_id_plan_put**](MasterAccountApi.md#corporate_sub_account_id_plan_put) | **PUT** /corporate/subAccount/{id}/plan | Update sub-account plan
[**corporate_sub_account_ip_associate_post**](MasterAccountApi.md#corporate_sub_account_ip_associate_post) | **POST** /corporate/subAccount/ip/associate | Associate an IP to sub-accounts
[**corporate_sub_account_ip_dissociate_put**](MasterAccountApi.md#corporate_sub_account_ip_dissociate_put) | **PUT** /corporate/subAccount/ip/dissociate | Dissociate an IP from sub-accounts
[**corporate_sub_account_key_post**](MasterAccountApi.md#corporate_sub_account_key_post) | **POST** /corporate/subAccount/key | Create an API key for a sub-account
[**corporate_sub_account_post**](MasterAccountApi.md#corporate_sub_account_post) | **POST** /corporate/subAccount | Create a new sub-account under a master account.
[**corporate_sub_account_sso_token_post**](MasterAccountApi.md#corporate_sub_account_sso_token_post) | **POST** /corporate/subAccount/ssoToken | Generate SSO token to access sub-account
[**corporate_user_invitation_action_email_put**](MasterAccountApi.md#corporate_user_invitation_action_email_put) | **PUT** /corporate/user/invitation/{action}/{email} | Resend / cancel admin user invitation
[**corporate_user_revoke_email_delete**](MasterAccountApi.md#corporate_user_revoke_email_delete) | **DELETE** /corporate/user/revoke/{email} | Revoke an admin user
[**get_account_activity**](MasterAccountApi.md#get_account_activity) | **GET** /organization/activities | Get user activity logs
[**get_corporate_invited_users_list**](MasterAccountApi.md#get_corporate_invited_users_list) | **GET** /corporate/invited/users | Get the list of all admin users
[**get_corporate_user_permission**](MasterAccountApi.md#get_corporate_user_permission) | **GET** /corporate/user/{email}/permissions | Check admin user permissions
[**get_sub_account_groups**](MasterAccountApi.md#get_sub_account_groups) | **GET** /corporate/groups | Get the list of groups
[**invite_admin_user**](MasterAccountApi.md#invite_admin_user) | **POST** /corporate/user/invitation/send | Send invitation to an admin user


# **corporate_group_id_delete**
> corporate_group_id_delete(id)

Delete a group

This endpoint allows you to delete a group of sub-organizations. When a group is deleted, the sub-organizations are no longer part of this group. The users associated with the group are no longer associated with the group once deleted.

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
id = 'id_example' # str | Id of the group

try:
    # Delete a group
    api_instance.corporate_group_id_delete(id)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_group_id_get**
> CorporateGroupDetailsResponse corporate_group_id_get(id)

GET a group details

This endpoint allows you to retrieve a specific group’s information such as the list of sub-organizations and the user associated with the group.

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
id = 'id_example' # str | Id of the group of sub-organization

try:
    # GET a group details
    api_response = api_instance.corporate_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group of sub-organization | 

### Return type

[**CorporateGroupDetailsResponse**](CorporateGroupDetailsResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_group_id_put**
> corporate_group_id_put(id, body)

Update a group of sub-accounts

This endpoint allows you to update a group of sub-accounts

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
id = 'id_example' # str | Id of the group
body = brevo_python.Body3() # Body3 | Group details to be updated.

try:
    # Update a group of sub-accounts
    api_instance.corporate_group_id_put(id, body)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the group | 
 **body** | [**Body3**](Body3.md)| Group details to be updated. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_group_post**
> InlineResponse201 corporate_group_post(body)

Create a new group of sub-accounts

This endpoint allows to create a group of sub-accounts

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
body = brevo_python.Body() # Body | Group details to be created.

try:
    # Create a new group of sub-accounts
    api_response = api_instance.corporate_group_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Group details to be created. | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_group_unlink_group_id_sub_accounts_put**
> corporate_group_unlink_group_id_sub_accounts_put(group_id, body)

Delete sub-account from group

This endpoint allows you to remove a sub-organization from a group.

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
group_id = 'group_id_example' # str | Id of the group
body = brevo_python.Body4() # Body4 | List of sub-account ids

try:
    # Delete sub-account from group
    api_instance.corporate_group_unlink_group_id_sub_accounts_put(group_id, body)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_group_unlink_group_id_sub_accounts_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Id of the group | 
 **body** | [**Body4**](Body4.md)| List of sub-account ids | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **corporate_sso_token_post**
> GetSsoToken corporate_sso_token_post(sso_token_request_corporate)

Generate SSO token to access admin account

This endpoint generates an SSO token to authenticate and access the admin account using the endpoint https://account-app.brevo.com/account/login/corporate/sso/[token], where [token] will be replaced by the actual token.

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
sso_token_request_corporate = brevo_python.SsoTokenRequestCorporate() # SsoTokenRequestCorporate | User email of admin account

try:
    # Generate SSO token to access admin account
    api_response = api_instance.corporate_sso_token_post(sso_token_request_corporate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sso_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_token_request_corporate** | [**SsoTokenRequestCorporate**](SsoTokenRequestCorporate.md)| User email of admin account | 

### Return type

[**GetSsoToken**](GetSsoToken.md)

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

# **corporate_sub_account_id_applications_toggle_put**
> corporate_sub_account_id_applications_toggle_put(id, toggle_applications)

Enable/disable sub-account application(s)

API endpoint for the Corporate owner to enable/disable applications on the sub-account

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
id = 789 # int | Id of the sub-account organization (mandatory)
toggle_applications = brevo_python.SubAccountAppsToggleRequest() # SubAccountAppsToggleRequest | List of applications to activate or deactivate on a sub-account

try:
    # Enable/disable sub-account application(s)
    api_instance.corporate_sub_account_id_applications_toggle_put(id, toggle_applications)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_id_applications_toggle_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the sub-account organization (mandatory) | 
 **toggle_applications** | [**SubAccountAppsToggleRequest**](SubAccountAppsToggleRequest.md)| List of applications to activate or deactivate on a sub-account | 

### Return type

void (empty response body)

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

This endpoint will update the sub-account plan. On the Corporate solution new version v2, you can set an unlimited number of credits in your sub-organization. Please pass the value “-1\" to set the consumable in unlimited mode.

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

# **corporate_sub_account_ip_associate_post**
> object corporate_sub_account_ip_associate_post(body)

Associate an IP to sub-accounts

This endpoint allows to associate an IP to sub-accounts

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
body = brevo_python.Body1() # Body1 | Ip address association details

try:
    # Associate an IP to sub-accounts
    api_response = api_instance.corporate_sub_account_ip_associate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_ip_associate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| Ip address association details | 

### Return type

**object**

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_sub_account_ip_dissociate_put**
> corporate_sub_account_ip_dissociate_put(body)

Dissociate an IP from sub-accounts

This endpoint allows to dissociate an IP from sub-accounts

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
body = brevo_python.Body2() # Body2 | Ip address dissociation details

try:
    # Dissociate an IP from sub-accounts
    api_instance.corporate_sub_account_ip_dissociate_put(body)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_sub_account_ip_dissociate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| Ip address dissociation details | 

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

Generate SSO token to access sub-account

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
    # Generate SSO token to access sub-account
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

# **corporate_user_invitation_action_email_put**
> InlineResponse200 corporate_user_invitation_action_email_put(action, email)

Resend / cancel admin user invitation

This endpoint will allow the user to: - Resend an admin user invitation - Cancel an admin user invitation 

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
action = 'action_example' # str | Action to be performed (cancel / resend)
email = 'email_example' # str | Email address of the recipient

try:
    # Resend / cancel admin user invitation
    api_response = api_instance.corporate_user_invitation_action_email_put(action, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_user_invitation_action_email_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Action to be performed (cancel / resend) | 
 **email** | **str**| Email address of the recipient | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_user_revoke_email_delete**
> corporate_user_revoke_email_delete(email)

Revoke an admin user

This endpoint allows to revoke/remove an invited member of your Admin account

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
email = 'email_example' # str | Email of the invited user

try:
    # Revoke an admin user
    api_instance.corporate_user_revoke_email_delete(email)
except ApiException as e:
    print("Exception when calling MasterAccountApi->corporate_user_revoke_email_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the invited user | 

### Return type

void (empty response body)

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

# **get_corporate_invited_users_list**
> GetCorporateInvitedUsersList get_corporate_invited_users_list()

Get the list of all admin users

This endpoint allows you to list all Admin users of your Admin account

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
    # Get the list of all admin users
    api_response = api_instance.get_corporate_invited_users_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->get_corporate_invited_users_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCorporateInvitedUsersList**](GetCorporateInvitedUsersList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporate_user_permission**
> GetCorporateUserPermission get_corporate_user_permission(email)

Check admin user permissions

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
email = 'email_example' # str | Email of the invited user

try:
    # Check admin user permissions
    api_response = api_instance.get_corporate_user_permission(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->get_corporate_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the invited user | 

### Return type

[**GetCorporateUserPermission**](GetCorporateUserPermission.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_account_groups**
> list[InlineResponse2001] get_sub_account_groups()

Get the list of groups

This endpoint allows you to list all groups created on your Admin account.

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
    # Get the list of groups
    api_response = api_instance.get_sub_account_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->get_sub_account_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_admin_user**
> InviteAdminUser invite_admin_user(send_invitation)

Send invitation to an admin user

`This endpoint allows you to invite a member to manage the Admin account  Features and their respective permissions are as below:  - `my_plan`:   - \"all\" - `api`:   - \"none\" - `user_management`:   - \"all\" - `app_management` | Not available in ENTv2:   - \"all\"  **Note**: - If `all_features_access: false` then only privileges are required otherwise if `true` then it's assumed that all permissions will be there for the invited admin user. 

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
send_invitation = brevo_python.InviteAdminUser() # InviteAdminUser | Payload to send an invitation

try:
    # Send invitation to an admin user
    api_response = api_instance.invite_admin_user(send_invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasterAccountApi->invite_admin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_invitation** | [**InviteAdminUser**](InviteAdminUser.md)| Payload to send an invitation | 

### Return type

[**InviteAdminUser**](InviteAdminUser.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

