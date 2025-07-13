# brevo_python.ProgramApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_lp**](ProgramApi.md#create_new_lp) | **POST** /loyalty/config/programs | Create loyalty program
[**delete_contact_members**](ProgramApi.md#delete_contact_members) | **DELETE** /loyalty/config/programs/{pid}/subscription-members | Delete subscription member
[**delete_loyalty_program**](ProgramApi.md#delete_loyalty_program) | **DELETE** /loyalty/config/programs/{pid} | Delete Loyalty Program
[**get_loyalty_program_info**](ProgramApi.md#get_loyalty_program_info) | **GET** /loyalty/config/programs/{pid} | Get loyalty program Info
[**get_lp_list**](ProgramApi.md#get_lp_list) | **GET** /loyalty/config/programs | Get loyalty program list
[**get_parameter_subscription_info**](ProgramApi.md#get_parameter_subscription_info) | **GET** /loyalty/config/programs/{pid}/account-info | Get Subscription Data
[**partially_update_loyalty_program**](ProgramApi.md#partially_update_loyalty_program) | **PATCH** /loyalty/config/programs/{pid} | Partially update loyalty program
[**publish_loyalty_program**](ProgramApi.md#publish_loyalty_program) | **POST** /loyalty/config/programs/{pid}/publish | Publish loyalty program
[**subscribe_member_to_a_subscription**](ProgramApi.md#subscribe_member_to_a_subscription) | **POST** /loyalty/config/programs/{pid}/subscription-members | Create subscription member
[**subscribe_to_loyalty_program**](ProgramApi.md#subscribe_to_loyalty_program) | **POST** /loyalty/config/programs/{pid}/subscriptions | Create subscription
[**update_loyalty_program**](ProgramApi.md#update_loyalty_program) | **PUT** /loyalty/config/programs/{pid} | Update loyalty program


# **create_new_lp**
> LoyaltyProgram create_new_lp(body)

Create loyalty program

Creates loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
body = brevo_python.CreateLoyaltyProgramPayload() # CreateLoyaltyProgramPayload | Create Loyalty Program Payload

try:
    # Create loyalty program
    api_response = api_instance.create_new_lp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->create_new_lp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLoyaltyProgramPayload**](CreateLoyaltyProgramPayload.md)| Create Loyalty Program Payload | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_members**
> delete_contact_members(pid, member_contact_ids)

Delete subscription member

Deletes member from a subscription

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
member_contact_ids = 'member_contact_ids_example' # str | Member Contact Ids

try:
    # Delete subscription member
    api_instance.delete_contact_members(pid, member_contact_ids)
except ApiException as e:
    print("Exception when calling ProgramApi->delete_contact_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **member_contact_ids** | **str**| Member Contact Ids | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loyalty_program**
> delete_loyalty_program(pid)

Delete Loyalty Program

Deletes Loyalty Program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id

try:
    # Delete Loyalty Program
    api_instance.delete_loyalty_program(pid)
except ApiException as e:
    print("Exception when calling ProgramApi->delete_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_program_info**
> LoyaltyProgram get_loyalty_program_info(pid)

Get loyalty program Info

Returns loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id

try:
    # Get loyalty program Info
    api_response = api_instance.get_loyalty_program_info(pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->get_loyalty_program_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lp_list**
> LoyaltyProgramPage get_lp_list(limit=limit, offset=offset, sort_field=sort_field, sort=sort)

Get loyalty program list

Returns list of loyalty programs

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
limit = 56 # int | Number of documents per page (optional)
offset = 56 # int | Index of the first document in the page (optional)
sort_field = 'sort_field_example' # str | Sort documents by field (optional)
sort = 'sort_example' # str | Sort the documents in the ascending or descending order (optional)

try:
    # Get loyalty program list
    api_response = api_instance.get_lp_list(limit=limit, offset=offset, sort_field=sort_field, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->get_lp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] 
 **offset** | **int**| Index of the first document in the page | [optional] 
 **sort_field** | **str**| Sort documents by field | [optional] 
 **sort** | **str**| Sort the documents in the ascending or descending order | [optional] 

### Return type

[**LoyaltyProgramPage**](LoyaltyProgramPage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_subscription_info**
> SubscriptionHandlerInfo get_parameter_subscription_info(pid, contact_id=contact_id, params=params, loyalty_subscription_id=loyalty_subscription_id)

Get Subscription Data

Get Information of balances, tiers, rewards and subscription members for a subscription

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
contact_id = 'contact_id_example' # str | Contact Id (optional)
params = 'params_example' # str | Filter List (optional)
loyalty_subscription_id = 'loyalty_subscription_id_example' # str | Loyalty Subscription Id (optional)

try:
    # Get Subscription Data
    api_response = api_instance.get_parameter_subscription_info(pid, contact_id=contact_id, params=params, loyalty_subscription_id=loyalty_subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->get_parameter_subscription_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **contact_id** | **str**| Contact Id | [optional] 
 **params** | **str**| Filter List | [optional] 
 **loyalty_subscription_id** | **str**| Loyalty Subscription Id | [optional] 

### Return type

[**SubscriptionHandlerInfo**](SubscriptionHandlerInfo.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_loyalty_program**
> LoyaltyProgram partially_update_loyalty_program(pid, body)

Partially update loyalty program

Partially updates loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.PatchLoyaltyProgramPayload() # PatchLoyaltyProgramPayload | Loyalty Program Payload

try:
    # Partially update loyalty program
    api_response = api_instance.partially_update_loyalty_program(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->partially_update_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**PatchLoyaltyProgramPayload**](PatchLoyaltyProgramPayload.md)| Loyalty Program Payload | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_loyalty_program**
> publish_loyalty_program(pid)

Publish loyalty program

Publishes loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id

try:
    # Publish loyalty program
    api_instance.publish_loyalty_program(pid)
except ApiException as e:
    print("Exception when calling ProgramApi->publish_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_member_to_a_subscription**
> SubscriptionMember subscribe_member_to_a_subscription(pid, body)

Create subscription member

Add member to a subscription

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.AddSubscriptionMemberPayload() # AddSubscriptionMemberPayload | Add Subscription Member Payload

try:
    # Create subscription member
    api_response = api_instance.subscribe_member_to_a_subscription(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->subscribe_member_to_a_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**AddSubscriptionMemberPayload**](AddSubscriptionMemberPayload.md)| Add Subscription Member Payload | 

### Return type

[**SubscriptionMember**](SubscriptionMember.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_loyalty_program**
> Subscription subscribe_to_loyalty_program(pid, body)

Create subscription

Subscribes to a loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.CreateSubscriptionPayload() # CreateSubscriptionPayload | Create Subscription Payload

try:
    # Create subscription
    api_response = api_instance.subscribe_to_loyalty_program(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->subscribe_to_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**CreateSubscriptionPayload**](CreateSubscriptionPayload.md)| Create Subscription Payload | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_program**
> LoyaltyProgram update_loyalty_program(pid, body)

Update loyalty program

Updates loyalty program

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
api_instance = brevo_python.ProgramApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.UpdateLoyaltyProgramPayload() # UpdateLoyaltyProgramPayload | Update Loyalty Program Payload

try:
    # Update loyalty program
    api_response = api_instance.update_loyalty_program(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgramApi->update_loyalty_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**UpdateLoyaltyProgramPayload**](UpdateLoyaltyProgramPayload.md)| Update Loyalty Program Payload | 

### Return type

[**LoyaltyProgram**](LoyaltyProgram.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

