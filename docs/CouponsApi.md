# brevo_python.CouponsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_collection**](CouponsApi.md#create_coupon_collection) | **POST** /couponCollections | Create а coupon collection
[**create_coupons**](CouponsApi.md#create_coupons) | **POST** /coupons | Create coupons for a coupon collection
[**get_coupon_collection**](CouponsApi.md#get_coupon_collection) | **GET** /couponCollections/{id} | Get a coupon collection by id
[**get_coupon_collections**](CouponsApi.md#get_coupon_collections) | **GET** /couponCollections | Get all your coupon collections
[**update_coupon_collection**](CouponsApi.md#update_coupon_collection) | **PATCH** /couponCollections/{id} | Update a coupon collection by id


# **create_coupon_collection**
> InlineResponse2013 create_coupon_collection(create_coupon_collection)

Create а coupon collection

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
api_instance = brevo_python.CouponsApi(brevo_python.ApiClient(configuration))
create_coupon_collection = brevo_python.CreateCouponCollection() # CreateCouponCollection | Values to create a coupon collection

try:
    # Create а coupon collection
    api_response = api_instance.create_coupon_collection(create_coupon_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponsApi->create_coupon_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_coupon_collection** | [**CreateCouponCollection**](CreateCouponCollection.md)| Values to create a coupon collection | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupons**
> create_coupons(create_coupons)

Create coupons for a coupon collection

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
api_instance = brevo_python.CouponsApi(brevo_python.ApiClient(configuration))
create_coupons = brevo_python.CreateCoupons() # CreateCoupons | Values to create coupons

try:
    # Create coupons for a coupon collection
    api_instance.create_coupons(create_coupons)
except ApiException as e:
    print("Exception when calling CouponsApi->create_coupons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_coupons** | [**CreateCoupons**](CreateCoupons.md)| Values to create coupons | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_collection**
> GetCouponCollection get_coupon_collection(id)

Get a coupon collection by id

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
api_instance = brevo_python.CouponsApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | Id of the collection to return

try:
    # Get a coupon collection by id
    api_response = api_instance.get_coupon_collection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponsApi->get_coupon_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the collection to return | 

### Return type

[**GetCouponCollection**](GetCouponCollection.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_collections**
> GetCouponCollection get_coupon_collections(limit=limit, offset=offset, sort=sort, sort_by=sort_by)

Get all your coupon collections

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
api_instance = brevo_python.CouponsApi(brevo_python.ApiClient(configuration))
limit = 50 # int | Number of documents returned per page (optional) (default to 50)
offset = 0 # int | Index of the first document on the page (optional) (default to 0)
sort = 'desc' # str | Sort the results by creation time in ascending/descending order (optional) (default to desc)
sort_by = 'createdAt' # str | The field used to sort coupon collections (optional) (default to createdAt)

try:
    # Get all your coupon collections
    api_response = api_instance.get_coupon_collections(limit=limit, offset=offset, sort=sort, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponsApi->get_coupon_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents returned per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document on the page | [optional] [default to 0]
 **sort** | **str**| Sort the results by creation time in ascending/descending order | [optional] [default to desc]
 **sort_by** | **str**| The field used to sort coupon collections | [optional] [default to createdAt]

### Return type

[**GetCouponCollection**](GetCouponCollection.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_collection**
> InlineResponse2009 update_coupon_collection(id, update_coupon_collection=update_coupon_collection)

Update a coupon collection by id

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
api_instance = brevo_python.CouponsApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | Id of the collection to update
update_coupon_collection = brevo_python.UpdateCouponCollection() # UpdateCouponCollection | Values to update the coupon collection (optional)

try:
    # Update a coupon collection by id
    api_response = api_instance.update_coupon_collection(id, update_coupon_collection=update_coupon_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponsApi->update_coupon_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the collection to update | 
 **update_coupon_collection** | [**UpdateCouponCollection**](UpdateCouponCollection.md)| Values to update the coupon collection | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

