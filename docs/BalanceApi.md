# brevo_python.BalanceApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_transaction**](BalanceApi.md#begin_transaction) | **POST** /loyalty/balance/programs/{pid}/transactions | Create new transaction
[**cancel_transaction**](BalanceApi.md#cancel_transaction) | **POST** /loyalty/balance/programs/{pid}/transactions/{tid}/cancel | Cancel transaction
[**complete_transaction**](BalanceApi.md#complete_transaction) | **POST** /loyalty/balance/programs/{pid}/transactions/{tid}/complete | Complete transaction
[**create_balance_limit**](BalanceApi.md#create_balance_limit) | **POST** /loyalty/balance/programs/{pid}/balance-definitions/{bdid}/limits | Create balance limits
[**create_balance_order**](BalanceApi.md#create_balance_order) | **POST** /loyalty/balance/programs/{pid}/create-order | Create balance order
[**delete_balance_definition**](BalanceApi.md#delete_balance_definition) | **DELETE** /loyalty/balance/programs/{pid}/balance-definitions/{bdid} | Delete balance definition
[**delete_balance_limit**](BalanceApi.md#delete_balance_limit) | **DELETE** /loyalty/balance/programs/{pid}/balance-definitions/{bdid}/limits/{blid} | Delete balance limit
[**get_balance_definition**](BalanceApi.md#get_balance_definition) | **GET** /loyalty/balance/programs/{pid}/balance-definitions/{bdid} | Get balance definition
[**get_balance_definition_list**](BalanceApi.md#get_balance_definition_list) | **GET** /loyalty/balance/programs/{pid}/balance-definitions | Get balance definition list
[**get_balance_limit**](BalanceApi.md#get_balance_limit) | **GET** /loyalty/balance/programs/{pid}/balance-definitions/{bdid}/limits/{blid} | Get balance limits
[**get_contact_balances**](BalanceApi.md#get_contact_balances) | **GET** /loyalty/balance/programs/{pid}/contact-balances | Get balance list
[**get_subscription_balances**](BalanceApi.md#get_subscription_balances) | **GET** /loyalty/balance/programs/{pid}/subscriptions/{cid}/balances | Get subscription balances
[**loyalty_balance_programs_pid_active_balance_get**](BalanceApi.md#loyalty_balance_programs_pid_active_balance_get) | **GET** /loyalty/balance/programs/{pid}/active-balance | Get Active Balances API
[**loyalty_balance_programs_pid_balance_definitions_post**](BalanceApi.md#loyalty_balance_programs_pid_balance_definitions_post) | **POST** /loyalty/balance/programs/{pid}/balance-definitions | Create balance definition
[**loyalty_balance_programs_pid_subscriptions_cid_balances_post**](BalanceApi.md#loyalty_balance_programs_pid_subscriptions_cid_balances_post) | **POST** /loyalty/balance/programs/{pid}/subscriptions/{cid}/balances | Create subscription balances
[**loyalty_balance_programs_pid_transaction_history_get**](BalanceApi.md#loyalty_balance_programs_pid_transaction_history_get) | **GET** /loyalty/balance/programs/{pid}/transaction-history | Get Transaction History API
[**update_balance_definition**](BalanceApi.md#update_balance_definition) | **PUT** /loyalty/balance/programs/{pid}/balance-definitions/{bdid} | Update balance definition
[**update_balance_limit**](BalanceApi.md#update_balance_limit) | **PUT** /loyalty/balance/programs/{pid}/balance-definitions/{bdid}/limits/{blid} | Updates balance limit


# **begin_transaction**
> Transaction begin_transaction(pid, body)

Create new transaction

Creates new transaction and returns information

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.CreateTransactionPayload() # CreateTransactionPayload | Transaction Payload

try:
    # Create new transaction
    api_response = api_instance.begin_transaction(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->begin_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**CreateTransactionPayload**](CreateTransactionPayload.md)| Transaction Payload | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_transaction**
> Transaction cancel_transaction(pid, tid)

Cancel transaction

Cancels transaction

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
tid = 'tid_example' # str | Transaction Id

try:
    # Cancel transaction
    api_response = api_instance.cancel_transaction(pid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->cancel_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **tid** | [**str**](.md)| Transaction Id | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_transaction**
> Transaction complete_transaction(pid, tid)

Complete transaction

Completes transaction

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
tid = 'tid_example' # str | Transaction Id

try:
    # Complete transaction
    api_response = api_instance.complete_transaction(pid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->complete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **tid** | [**str**](.md)| Transaction Id | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_balance_limit**
> BalanceLimit create_balance_limit(pid, bdid, body)

Create balance limits

Creates balance limit and sends the created UUID along with the data

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
body = brevo_python.CreateBalanceLimitPayload() # CreateBalanceLimitPayload | Balance Definition Payload

try:
    # Create balance limits
    api_response = api_instance.create_balance_limit(pid, bdid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->create_balance_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **body** | [**CreateBalanceLimitPayload**](CreateBalanceLimitPayload.md)| Balance Definition Payload | 

### Return type

[**BalanceLimit**](BalanceLimit.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_balance_order**
> BalanceOrder create_balance_order(pid, body)

Create balance order

Returns created order

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.CreateOrderPayload() # CreateOrderPayload | Order Payload

try:
    # Create balance order
    api_response = api_instance.create_balance_order(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->create_balance_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**CreateOrderPayload**](CreateOrderPayload.md)| Order Payload | 

### Return type

[**BalanceOrder**](BalanceOrder.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balance_definition**
> delete_balance_definition(pid, bdid)

Delete balance definition

Delete Balance definition

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id

try:
    # Delete balance definition
    api_instance.delete_balance_definition(pid, bdid)
except ApiException as e:
    print("Exception when calling BalanceApi->delete_balance_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balance_limit**
> delete_balance_limit(pid, bdid, blid)

Delete balance limit

Delete balance limit

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
blid = 'blid_example' # str | Balance Limit Id

try:
    # Delete balance limit
    api_instance.delete_balance_limit(pid, bdid, blid)
except ApiException as e:
    print("Exception when calling BalanceApi->delete_balance_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **blid** | [**str**](.md)| Balance Limit Id | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_definition**
> BalanceDefinition get_balance_definition(pid, bdid, version=version)

Get balance definition

Returns balance definition

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
version = 'draft' # str | Version (optional) (default to draft)

try:
    # Get balance definition
    api_response = api_instance.get_balance_definition(pid, bdid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->get_balance_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **version** | **str**| Version | [optional] [default to draft]

### Return type

[**BalanceDefinition**](BalanceDefinition.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_definition_list**
> BalanceDefinitionPage get_balance_definition_list(pid, limit=limit, offset=offset, sort_field=sort_field, sort=sort, version=version)

Get balance definition list

Returns balance definition page

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
limit = 200 # int | Limit the number of records returned (optional) (default to 200)
offset = 0 # int | Offset to paginate records (optional) (default to 0)
sort_field = 'updated_at' # str | Field to sort by (optional) (default to updated_at)
sort = 'desc' # str | Sort direction (optional) (default to desc)
version = 'draft' # str | Version (optional) (default to draft)

try:
    # Get balance definition list
    api_response = api_instance.get_balance_definition_list(pid, limit=limit, offset=offset, sort_field=sort_field, sort=sort, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->get_balance_definition_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **limit** | **int**| Limit the number of records returned | [optional] [default to 200]
 **offset** | **int**| Offset to paginate records | [optional] [default to 0]
 **sort_field** | **str**| Field to sort by | [optional] [default to updated_at]
 **sort** | **str**| Sort direction | [optional] [default to desc]
 **version** | **str**| Version | [optional] [default to draft]

### Return type

[**BalanceDefinitionPage**](BalanceDefinitionPage.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_limit**
> BalanceLimit get_balance_limit(pid, bdid, blid, version=version)

Get balance limits

Fetches balance limits and send the created UUID along with the data

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
blid = 'blid_example' # str | Balance Limit Id
version = 'draft' # str | Version (optional) (default to draft)

try:
    # Get balance limits
    api_response = api_instance.get_balance_limit(pid, bdid, blid, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->get_balance_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **blid** | [**str**](.md)| Balance Limit Id | 
 **version** | **str**| Version | [optional] [default to draft]

### Return type

[**BalanceLimit**](BalanceLimit.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_balances**
> ContactBalancesResp get_contact_balances(pid)

Get balance list

Returns balance list

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id

try:
    # Get balance list
    api_response = api_instance.get_contact_balances(pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->get_contact_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 

### Return type

[**ContactBalancesResp**](ContactBalancesResp.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_balances**
> ModelSubscriptionBalanceResp get_subscription_balances(cid, pid)

Get subscription balances

Returns subscription balances

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
cid = 'cid_example' # str | Contact Id
pid = 'pid_example' # str | Loyalty Program Id

try:
    # Get subscription balances
    api_response = api_instance.get_subscription_balances(cid, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->get_subscription_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| Contact Id | 
 **pid** | [**str**](.md)| Loyalty Program Id | 

### Return type

[**ModelSubscriptionBalanceResp**](ModelSubscriptionBalanceResp.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_balance_programs_pid_active_balance_get**
> BalanceLimit loyalty_balance_programs_pid_active_balance_get(pid, contact_id, balance_definition_id, limit=limit, offset=offset, sort_field=sort_field, sort=sort)

Get Active Balances API

Returns Active Balances

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
contact_id = 56 # int | Contact ID
balance_definition_id = 'balance_definition_id_example' # str | Balance Definition ID
limit = 56 # int | Limit (optional)
offset = 56 # int | Offset (optional)
sort_field = 'sort_field_example' # str | Sort Field (optional)
sort = 'sort_example' # str | Sort Order (optional)

try:
    # Get Active Balances API
    api_response = api_instance.loyalty_balance_programs_pid_active_balance_get(pid, contact_id, balance_definition_id, limit=limit, offset=offset, sort_field=sort_field, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->loyalty_balance_programs_pid_active_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **contact_id** | **int**| Contact ID | 
 **balance_definition_id** | [**str**](.md)| Balance Definition ID | 
 **limit** | **int**| Limit | [optional] 
 **offset** | **int**| Offset | [optional] 
 **sort_field** | **str**| Sort Field | [optional] 
 **sort** | **str**| Sort Order | [optional] 

### Return type

[**BalanceLimit**](BalanceLimit.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_balance_programs_pid_balance_definitions_post**
> BalanceDefinition loyalty_balance_programs_pid_balance_definitions_post(pid, body)

Create balance definition

Creates balance definition and returns information

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
body = brevo_python.CreateBalanceDefinitionPayload() # CreateBalanceDefinitionPayload | Create Balance Definition Payload

try:
    # Create balance definition
    api_response = api_instance.loyalty_balance_programs_pid_balance_definitions_post(pid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->loyalty_balance_programs_pid_balance_definitions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **body** | [**CreateBalanceDefinitionPayload**](CreateBalanceDefinitionPayload.md)| Create Balance Definition Payload | 

### Return type

[**BalanceDefinition**](BalanceDefinition.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_balance_programs_pid_subscriptions_cid_balances_post**
> Balance loyalty_balance_programs_pid_subscriptions_cid_balances_post(pid, cid, body)

Create subscription balances

Creates a balance for a contact

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
cid = 'cid_example' # str | Contact Id
body = brevo_python.CreateBalancePayload() # CreateBalancePayload | Create Balnce Payload

try:
    # Create subscription balances
    api_response = api_instance.loyalty_balance_programs_pid_subscriptions_cid_balances_post(pid, cid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->loyalty_balance_programs_pid_subscriptions_cid_balances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **cid** | **str**| Contact Id | 
 **body** | [**CreateBalancePayload**](CreateBalancePayload.md)| Create Balnce Payload | 

### Return type

[**Balance**](Balance.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loyalty_balance_programs_pid_transaction_history_get**
> TransactionHistoryResp loyalty_balance_programs_pid_transaction_history_get(pid, contact_id, balance_definition_id, limit=limit, offset=offset, sort_field=sort_field, sort=sort, filters=filters)

Get Transaction History API

Returns transaction history

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
contact_id = 0 # int | Contact ID (default to 0)
balance_definition_id = 'balance_definition_id_example' # str | Balance Definition ID
limit = 20 # int | Limit the number of records returned (optional) (default to 20)
offset = 0 # int | Skip a number of records (optional) (default to 0)
sort_field = 'created_at' # str | Field to sort by (optional) (default to created_at)
sort = 'desc' # str | Sort order, either asc or desc (optional) (default to desc)
filters = ['filters_example'] # list[str] | Filters to apply (optional)

try:
    # Get Transaction History API
    api_response = api_instance.loyalty_balance_programs_pid_transaction_history_get(pid, contact_id, balance_definition_id, limit=limit, offset=offset, sort_field=sort_field, sort=sort, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->loyalty_balance_programs_pid_transaction_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **contact_id** | **int**| Contact ID | [default to 0]
 **balance_definition_id** | [**str**](.md)| Balance Definition ID | 
 **limit** | **int**| Limit the number of records returned | [optional] [default to 20]
 **offset** | **int**| Skip a number of records | [optional] [default to 0]
 **sort_field** | **str**| Field to sort by | [optional] [default to created_at]
 **sort** | **str**| Sort order, either asc or desc | [optional] [default to desc]
 **filters** | [**list[str]**](str.md)| Filters to apply | [optional] 

### Return type

[**TransactionHistoryResp**](TransactionHistoryResp.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_definition**
> BalanceDefinition update_balance_definition(pid, bdid, body)

Update balance definition

Updates Balance definition

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
body = brevo_python.UpdateBalanceDefinitionPayload() # UpdateBalanceDefinitionPayload | Update Balance Definition Payload

try:
    # Update balance definition
    api_response = api_instance.update_balance_definition(pid, bdid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->update_balance_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **body** | [**UpdateBalanceDefinitionPayload**](UpdateBalanceDefinitionPayload.md)| Update Balance Definition Payload | 

### Return type

[**BalanceDefinition**](BalanceDefinition.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_limit**
> BalanceLimit update_balance_limit(pid, bdid, blid, body)

Updates balance limit

Updates balance limit

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
api_instance = brevo_python.BalanceApi(brevo_python.ApiClient(configuration))
pid = 'pid_example' # str | Loyalty Program Id
bdid = 'bdid_example' # str | Balance Definition Id
blid = 'blid_example' # str | Balance Limit Id
body = brevo_python.UpdateBalanceLimitPayload() # UpdateBalanceLimitPayload | Balance Limits Payload

try:
    # Updates balance limit
    api_response = api_instance.update_balance_limit(pid, bdid, blid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->update_balance_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | [**str**](.md)| Loyalty Program Id | 
 **bdid** | [**str**](.md)| Balance Definition Id | 
 **blid** | [**str**](.md)| Balance Limit Id | 
 **body** | [**UpdateBalanceLimitPayload**](UpdateBalanceLimitPayload.md)| Balance Limits Payload | 

### Return type

[**BalanceLimit**](BalanceLimit.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

