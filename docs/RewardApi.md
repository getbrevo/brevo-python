# brevo_python.RewardApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_count**](RewardApi.md#get_code_count) | **GET** /loyalty/offer/programs/{pid}/code-pools/{cpid}/codes-count | Get code count
[**loyalty_offer_programs_pid_offers_get**](RewardApi.md#loyalty_offer_programs_pid_offers_get) | **GET** /loyalty/offer/programs/{pid}/offers | Get Reward Page API
[**loyalty_offer_programs_pid_offers_post**](RewardApi.md#loyalty_offer_programs_pid_offers_post) | **POST** /loyalty/offer/programs/{pid}/offers | Create a reward
[**loyalty_offer_programs_pid_rewards_attribute_post**](RewardApi.md#loyalty_offer_programs_pid_rewards_attribute_post) | **POST** /loyalty/offer/programs/{pid}/rewards/attribute | Create a voucher
[**loyalty_offer_programs_pid_rewards_redeem_post**](RewardApi.md#loyalty_offer_programs_pid_rewards_redeem_post) | **POST** /loyalty/offer/programs/{pid}/rewards/redeem | Create redeem voucher request
[**loyalty_offer_programs_pid_rewards_redeem_tid_complete_post**](RewardApi.md#loyalty_offer_programs_pid_rewards_redeem_tid_complete_post) | **POST** /loyalty/offer/programs/{pid}/rewards/redeem/{tid}/complete | Complete redeem voucher request
[**loyalty_offer_programs_pid_rewards_revoke_delete**](RewardApi.md#loyalty_offer_programs_pid_rewards_revoke_delete) | **DELETE** /loyalty/offer/programs/{pid}/rewards/revoke | Revoke vouchers
[**loyalty_offer_programs_pid_rewards_rid_get**](RewardApi.md#loyalty_offer_programs_pid_rewards_rid_get) | **GET** /loyalty/offer/programs/{pid}/rewards/{rid} | Get reward information
[**loyalty_offer_programs_pid_rewards_validate_post**](RewardApi.md#loyalty_offer_programs_pid_rewards_validate_post) | **POST** /loyalty/offer/programs/{pid}/rewards/validate | Validate a reward
[**loyalty_offer_programs_pid_vouchers_get**](RewardApi.md#loyalty_offer_programs_pid_vouchers_get) | **GET** /loyalty/offer/programs/{pid}/vouchers | Get voucher for a contact


# **get_code_count**
> MainCodeCountHttpResponse get_code_count(pid, cpid)

Get code count

Get code count

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
cpid = 'cpid_example' # str | Code Pool ID

try:
    # Get code count
    api_response = api_instance.get_code_count(pid, cpid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->get_code_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **cpid** | [**str**](.md)| Code Pool ID | 

### Return type

[**MainCodeCountHttpResponse**](MainCodeCountHttpResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_offers_get**
> MainRewardPage loyalty_offer_programs_pid_offers_get(pid, limit=limit, offset=offset, state=state, version=version)

Get Reward Page API

Returns a reward page

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
limit = 25 # int | Page size (optional) (default to 25)
offset = 0 # int | Pagination offset (optional) (default to 0)
state = 'all' # str | State of the reward (optional) (default to all)
version = 'draft' # str | Version (optional) (default to draft)

try:
    # Get Reward Page API
    api_response = api_instance.loyalty_offer_programs_pid_offers_get(pid, limit=limit, offset=offset, state=state, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_offers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **limit** | **int**| Page size | [optional] [default to 25]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **state** | **str**| State of the reward | [optional] [default to all]
 **version** | **str**| Version | [optional] [default to draft]

### Return type

[**MainRewardPage**](MainRewardPage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_offers_post**
> MainCreateRewardResponse loyalty_offer_programs_pid_offers_post(pid, payload)

Create a reward

Creates a new reward in loyalty program.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
payload = brevo_python.MainCreateRewardPayload() # MainCreateRewardPayload | Reward creation payload

try:
    # Create a reward
    api_response = api_instance.loyalty_offer_programs_pid_offers_post(pid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_offers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **payload** | [**MainCreateRewardPayload**](MainCreateRewardPayload.md)| Reward creation payload | 

### Return type

[**MainCreateRewardResponse**](MainCreateRewardResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_attribute_post**
> MainRewardAttribution loyalty_offer_programs_pid_rewards_attribute_post(pid, payload)

Create a voucher

Create a voucher and attribute it to a specific membership.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
payload = brevo_python.MainAttributeRewardPayload() # MainAttributeRewardPayload | Voucher creation payload

try:
    # Create a voucher
    api_response = api_instance.loyalty_offer_programs_pid_rewards_attribute_post(pid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_attribute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **payload** | [**MainAttributeRewardPayload**](MainAttributeRewardPayload.md)| Voucher creation payload | 

### Return type

[**MainRewardAttribution**](MainRewardAttribution.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_redeem_post**
> MainRedeem loyalty_offer_programs_pid_rewards_redeem_post(pid, payload)

Create redeem voucher request

Creates a request to redeem a voucher.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
payload = brevo_python.MainCreateRedeemPayload() # MainCreateRedeemPayload | Redeem transaction creation payload

try:
    # Create redeem voucher request
    api_response = api_instance.loyalty_offer_programs_pid_rewards_redeem_post(pid, payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **payload** | [**MainCreateRedeemPayload**](MainCreateRedeemPayload.md)| Redeem transaction creation payload | 

### Return type

[**MainRedeem**](MainRedeem.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_redeem_tid_complete_post**
> MainRedeem loyalty_offer_programs_pid_rewards_redeem_tid_complete_post(pid, tid)

Complete redeem voucher request

Completes voucher redeem request.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
tid = 'tid_example' # str | Redeem transaction ID

try:
    # Complete redeem voucher request
    api_response = api_instance.loyalty_offer_programs_pid_rewards_redeem_tid_complete_post(pid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_redeem_tid_complete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **tid** | **str**| Redeem transaction ID | 

### Return type

[**MainRedeem**](MainRedeem.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_revoke_delete**
> str loyalty_offer_programs_pid_rewards_revoke_delete(pid, attributed_reward_ids=attributed_reward_ids)

Revoke vouchers

Revoke attributed vouchers.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
attributed_reward_ids = 'attributed_reward_ids_example' # str | Reward Attribution IDs (comma seperated) (optional)

try:
    # Revoke vouchers
    api_response = api_instance.loyalty_offer_programs_pid_rewards_revoke_delete(pid, attributed_reward_ids=attributed_reward_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_revoke_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **attributed_reward_ids** | **str**| Reward Attribution IDs (comma seperated) | [optional] 

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_rid_get**
> MainReward loyalty_offer_programs_pid_rewards_rid_get(pid, rid, version=version)

Get reward information

Returns reward information.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
rid = 'rid_example' # str | Reward ID
version = 'draft' # str | Version (optional) (default to draft)

try:
    # Get reward information
    api_response = api_instance.loyalty_offer_programs_pid_rewards_rid_get(pid, rid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_rid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **rid** | [**str**](.md)| Reward ID | 
 **version** | **str**| Version | [optional] [default to draft]

### Return type

[**MainReward**](MainReward.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_rewards_validate_post**
> MainRewardValidate loyalty_offer_programs_pid_rewards_validate_post(pid, body)

Validate a reward

Validates a reward.

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
body = brevo_python.MainValidateRewardPayload() # MainValidateRewardPayload | Reward validation payload

try:
    # Validate a reward
    api_response = api_instance.loyalty_offer_programs_pid_rewards_validate_post(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_rewards_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **body** | [**MainValidateRewardPayload**](MainValidateRewardPayload.md)| Reward validation payload | 

### Return type

[**MainRewardValidate**](MainRewardValidate.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_offer_programs_pid_vouchers_get**
> MainModelContactRewardsResp loyalty_offer_programs_pid_vouchers_get(pid, contact_id, limit=limit, offset=offset, sort=sort, sort_field=sort_field, metadata_key_value=metadata_key_value, reward_id=reward_id)

Get voucher for a contact

Get voucher for a contact

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
api_instance = brevo_python.RewardApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program ID
contact_id = 56 # int | Contact ID
limit = 25 # int | Page size (optional) (default to 25)
offset = 0 # int | Pagination offset (optional) (default to 0)
sort = 'desc' # str | Sort order (optional) (default to desc)
sort_field = 'updatedAt' # str | Sort field (optional) (default to updatedAt)
metadata_key_value = 'metadata_key_value_example' # str | Metadata value for a Key filter (optional)
reward_id = 'reward_id_example' # str | Reward ID (optional)

try:
    # Get voucher for a contact
    api_response = api_instance.loyalty_offer_programs_pid_vouchers_get(pid, contact_id, limit=limit, offset=offset, sort=sort, sort_field=sort_field, metadata_key_value=metadata_key_value, reward_id=reward_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardApi->loyalty_offer_programs_pid_vouchers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program ID | 
 **contact_id** | **int**| Contact ID | 
 **limit** | **int**| Page size | [optional] [default to 25]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **sort** | **str**| Sort order | [optional] [default to desc]
 **sort_field** | **str**| Sort field | [optional] [default to updatedAt]
 **metadata_key_value** | **str**| Metadata value for a Key filter | [optional] 
 **reward_id** | **str**| Reward ID | [optional] 

### Return type

[**MainModelContactRewardsResp**](MainModelContactRewardsResp.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

