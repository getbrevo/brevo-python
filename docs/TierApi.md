# brevo_python.TierApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription_to_tier**](TierApi.md#add_subscription_to_tier) | **POST** /loyalty/tier/programs/{pid}/contacts/{cid}/tiers/{tid} | Assign a tier
[**create_tier_for_tier_group**](TierApi.md#create_tier_for_tier_group) | **POST** /loyalty/tier/programs/{pid}/tier-groups/{gid}/tiers | Create a tier
[**create_tier_group**](TierApi.md#create_tier_group) | **POST** /loyalty/tier/programs/{pid}/tier-groups | Create a tier group
[**delete_tier**](TierApi.md#delete_tier) | **DELETE** /loyalty/tier/programs/{pid}/tiers/{tid} | Delete tier
[**delete_tier_group**](TierApi.md#delete_tier_group) | **DELETE** /loyalty/tier/programs/{pid}/tier-groups/{gid} | Delete tier group
[**get_list_of_tier_groups**](TierApi.md#get_list_of_tier_groups) | **GET** /loyalty/tier/programs/{pid}/tier-groups | List tier groups
[**get_loyalty_program_tier**](TierApi.md#get_loyalty_program_tier) | **GET** /loyalty/tier/programs/{pid}/tiers | List tiers
[**get_tier_group**](TierApi.md#get_tier_group) | **GET** /loyalty/tier/programs/{pid}/tier-groups/{gid} | Get tier group
[**update_tier**](TierApi.md#update_tier) | **PUT** /loyalty/tier/programs/{pid}/tiers/{tid} | Update tier
[**update_tier_group**](TierApi.md#update_tier_group) | **PUT** /loyalty/tier/programs/{pid}/tier-groups/{gid} | Update tier group


# **add_subscription_to_tier**
> TierForContact add_subscription_to_tier(pid, cid, tid)

Assign a tier

Manually assigns a tier to a specific membership.

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
cid = 'cid_example' # str | Contact ID
tid = 'tid_example' # str | Tier ID

try:
    # Assign a tier
    api_response = api_instance.add_subscription_to_tier(pid, cid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->add_subscription_to_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **cid** | [**str**](.md)| Contact ID | 
 **tid** | [**str**](.md)| Tier ID | 

### Return type

[**TierForContact**](TierForContact.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tier_for_tier_group**
> Tier create_tier_for_tier_group(pid, gid, payload)

Create a tier

Creates a new tier in a loyalty program tier group. *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
gid = 'gid_example' # str | Tier group ID
payload = brevo_python.TierRequest() # TierRequest | 

try:
    # Create a tier
    api_response = api_instance.create_tier_for_tier_group(pid, gid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->create_tier_for_tier_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **gid** | [**str**](.md)| Tier group ID | 
 **payload** | [**TierRequest**](TierRequest.md)|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tier_group**
> TierGroup create_tier_group(pid, payload)

Create a tier group

Creates a new tier group in a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
payload = brevo_python.CreateTierGroupRequest() # CreateTierGroupRequest | Tier group creation payload

try:
    # Create a tier group
    api_response = api_instance.create_tier_group(pid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->create_tier_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **payload** | [**CreateTierGroupRequest**](CreateTierGroupRequest.md)| Tier group creation payload | 

### Return type

[**TierGroup**](TierGroup.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tier**
> str delete_tier(pid, tid)

Delete tier

Deletes a tier from a loyalty program tier group. *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
tid = 'tid_example' # str | Tier ID

try:
    # Delete tier
    api_response = api_instance.delete_tier(pid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->delete_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **tid** | [**str**](.md)| Tier ID | 

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tier_group**
> str delete_tier_group(pid, gid)

Delete tier group

Deletes a tier group from a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
gid = 'gid_example' # str | Tier group ID

try:
    # Delete tier group
    api_response = api_instance.delete_tier_group(pid, gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->delete_tier_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **gid** | [**str**](.md)| Tier group ID | 

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_tier_groups**
> TierGroupPage get_list_of_tier_groups(pid, version=version)

List tier groups

Returns the list of tier groups defined within the loyalty program.

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
version = 'draft' # str | Select 'active' to retrieve list of all tier groups which are live for clients. Select draft to retrieve list of all non deleted tier groups. (optional) (default to draft)

try:
    # List tier groups
    api_response = api_instance.get_list_of_tier_groups(pid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->get_list_of_tier_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **version** | **str**| Select &#39;active&#39; to retrieve list of all tier groups which are live for clients. Select draft to retrieve list of all non deleted tier groups. | [optional] [default to draft]

### Return type

[**TierGroupPage**](TierGroupPage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_program_tier**
> LoyaltyTierPage get_loyalty_program_tier(pid, version=version)

List tiers

Returns the list of tiers defined within the loyalty program.

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
version = 'draft' # str | Select 'active' to retrieve list of all tiers which are live for clients. Select draft to retrieve list of all non deleted tiers. (optional) (default to draft)

try:
    # List tiers
    api_response = api_instance.get_loyalty_program_tier(pid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->get_loyalty_program_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **version** | **str**| Select &#39;active&#39; to retrieve list of all tiers which are live for clients. Select draft to retrieve list of all non deleted tiers. | [optional] [default to draft]

### Return type

[**LoyaltyTierPage**](LoyaltyTierPage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tier_group**
> TierGroup get_tier_group(pid, gid, version=version)

Get tier group

Returns tier group information.

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
gid = 'gid_example' # str | Tier group ID
version = 'draft' # str | Select active to retrieve active version of tier group. Select draft to retrieve latest changes in tier group. (optional) (default to draft)

try:
    # Get tier group
    api_response = api_instance.get_tier_group(pid, gid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->get_tier_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **gid** | [**str**](.md)| Tier group ID | 
 **version** | **str**| Select active to retrieve active version of tier group. Select draft to retrieve latest changes in tier group. | [optional] [default to draft]

### Return type

[**TierGroup**](TierGroup.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tier**
> Tier update_tier(pid, tid, payload)

Update tier

Modifies an existing tier for the specified tier group *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
tid = 'tid_example' # str | Tier ID
payload = brevo_python.TierRequestPutPayload() # TierRequestPutPayload | 

try:
    # Update tier
    api_response = api_instance.update_tier(pid, tid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->update_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **tid** | [**str**](.md)| Tier ID | 
 **payload** | [**TierRequestPutPayload**](TierRequestPutPayload.md)|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tier_group**
> TierGroup update_tier_group(pid, gid, payload)

Update tier group

Updates a tier group from a loyalty program. *(The changes will take effect with the next publication of the loyalty program)*

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
api_instance = brevo_python.TierApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
gid = 'gid_example' # str | Tier group ID
payload = brevo_python.UpdateTierGroupRequest() # UpdateTierGroupRequest | Tier group update payload

try:
    # Update tier group
    api_response = api_instance.update_tier_group(pid, gid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TierApi->update_tier_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **gid** | [**str**](.md)| Tier group ID | 
 **payload** | [**UpdateTierGroupRequest**](UpdateTierGroupRequest.md)| Tier group update payload | 

### Return type

[**TierGroup**](TierGroup.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

