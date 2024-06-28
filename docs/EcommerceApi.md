# brevo_python.EcommerceApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_order**](EcommerceApi.md#create_batch_order) | **POST** /orders/status/batch | Create orders in batch
[**create_order**](EcommerceApi.md#create_order) | **POST** /orders/status | Managing the status of the order
[**create_update_batch_category**](EcommerceApi.md#create_update_batch_category) | **POST** /categories/batch | Create categories in batch
[**create_update_batch_products**](EcommerceApi.md#create_update_batch_products) | **POST** /products/batch | Create products in batch
[**create_update_category**](EcommerceApi.md#create_update_category) | **POST** /categories | Create/Update a category
[**create_update_product**](EcommerceApi.md#create_update_product) | **POST** /products | Create/Update a product
[**ecommerce_activate_post**](EcommerceApi.md#ecommerce_activate_post) | **POST** /ecommerce/activate | Activate the eCommerce app
[**ecommerce_attribution_metrics_conversion_source_conversion_source_id_get**](EcommerceApi.md#ecommerce_attribution_metrics_conversion_source_conversion_source_id_get) | **GET** /ecommerce/attribution/metrics/{conversionSource}/{conversionSourceId} | Get detailed attribution metrics for a single Brevo campaign
[**ecommerce_attribution_metrics_get**](EcommerceApi.md#ecommerce_attribution_metrics_get) | **GET** /ecommerce/attribution/metrics | Get attribution metrics for one or more Brevo campaigns
[**ecommerce_attribution_products_conversion_source_conversion_source_id_get**](EcommerceApi.md#ecommerce_attribution_products_conversion_source_conversion_source_id_get) | **GET** /ecommerce/attribution/products/{conversionSource}/{conversionSourceId} | Get attributed product sales for a single Brevo campaign
[**ecommerce_config_display_currency_get**](EcommerceApi.md#ecommerce_config_display_currency_get) | **GET** /ecommerce/config/displayCurrency | Get the ISO 4217 compliant display currency code for your Brevo account
[**get_categories**](EcommerceApi.md#get_categories) | **GET** /categories | Return all your categories
[**get_category_info**](EcommerceApi.md#get_category_info) | **GET** /categories/{id} | Get a category details
[**get_orders**](EcommerceApi.md#get_orders) | **GET** /orders | Get order details
[**get_product_info**](EcommerceApi.md#get_product_info) | **GET** /products/{id} | Get a product&#39;s details
[**get_products**](EcommerceApi.md#get_products) | **GET** /products | Return all your products
[**set_config_display_currency**](EcommerceApi.md#set_config_display_currency) | **POST** /ecommerce/config/displayCurrency | Set the ISO 4217 compliant display currency code for your Brevo account


# **create_batch_order**
> create_batch_order(order_batch)

Create orders in batch

Create multiple orders at one time instead of one order at a time

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
order_batch = brevo_python.OrderBatch() # OrderBatch | 

try:
    # Create orders in batch
    api_instance.create_batch_order(order_batch)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_batch_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_batch** | [**OrderBatch**](OrderBatch.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> create_order(order)

Managing the status of the order

Manages the transactional status of the order

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
order = brevo_python.Order() # Order | 

try:
    # Managing the status of the order
    api_instance.create_order(order)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_batch_category**
> CreateUpdateBatchCategoryModel create_update_batch_category(create_update_batch_category)

Create categories in batch

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
create_update_batch_category = brevo_python.CreateUpdateBatchCategory() # CreateUpdateBatchCategory | Values to create a batch of categories

try:
    # Create categories in batch
    api_response = api_instance.create_update_batch_category(create_update_batch_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_batch_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_batch_category** | [**CreateUpdateBatchCategory**](CreateUpdateBatchCategory.md)| Values to create a batch of categories | 

### Return type

[**CreateUpdateBatchCategoryModel**](CreateUpdateBatchCategoryModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_batch_products**
> CreateUpdateBatchProductsModel create_update_batch_products(create_update_batch_products)

Create products in batch

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
create_update_batch_products = brevo_python.CreateUpdateBatchProducts() # CreateUpdateBatchProducts | Values to create a batch of products

try:
    # Create products in batch
    api_response = api_instance.create_update_batch_products(create_update_batch_products)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_batch_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_batch_products** | [**CreateUpdateBatchProducts**](CreateUpdateBatchProducts.md)| Values to create a batch of products | 

### Return type

[**CreateUpdateBatchProductsModel**](CreateUpdateBatchProductsModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_category**
> CreateCategoryModel create_update_category(create_update_category)

Create/Update a category

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
create_update_category = brevo_python.CreateUpdateCategory() # CreateUpdateCategory | Values to create/update a category

try:
    # Create/Update a category
    api_response = api_instance.create_update_category(create_update_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_category** | [**CreateUpdateCategory**](CreateUpdateCategory.md)| Values to create/update a category | 

### Return type

[**CreateCategoryModel**](CreateCategoryModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_product**
> CreateProductModel create_update_product(create_update_product)

Create/Update a product

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
create_update_product = brevo_python.CreateUpdateProduct() # CreateUpdateProduct | Values to create/update a product

try:
    # Create/Update a product
    api_response = api_instance.create_update_product(create_update_product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_product** | [**CreateUpdateProduct**](CreateUpdateProduct.md)| Values to create/update a product | 

### Return type

[**CreateProductModel**](CreateProductModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_activate_post**
> ecommerce_activate_post()

Activate the eCommerce app

Getting access to Brevo eCommerce.

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))

try:
    # Activate the eCommerce app
    api_instance.ecommerce_activate_post()
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_activate_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_attribution_metrics_conversion_source_conversion_source_id_get**
> InlineResponse2006 ecommerce_attribution_metrics_conversion_source_conversion_source_id_get(conversion_source, conversion_source_id)

Get detailed attribution metrics for a single Brevo campaign

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
conversion_source = 'conversion_source_example' # str | The Brevo campaign type for which data will be retrieved
conversion_source_id = 8.14 # float | The Brevo campaign id for which data will be retrieved

try:
    # Get detailed attribution metrics for a single Brevo campaign
    api_response = api_instance.ecommerce_attribution_metrics_conversion_source_conversion_source_id_get(conversion_source, conversion_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_attribution_metrics_conversion_source_conversion_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_source** | **str**| The Brevo campaign type for which data will be retrieved | 
 **conversion_source_id** | **float**| The Brevo campaign id for which data will be retrieved | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_attribution_metrics_get**
> InlineResponse2005 ecommerce_attribution_metrics_get(period_from=period_from, period_to=period_to, email_campaign_id=email_campaign_id)

Get attribution metrics for one or more Brevo campaigns

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
period_from = '2013-10-20T19:20:30+01:00' # datetime | When getting metrics for a specific period, define the starting datetime in RFC3339 format (optional)
period_to = '2013-10-20T19:20:30+01:00' # datetime | When getting metrics for a specific period, define the end datetime in RFC3339 format (optional)
email_campaign_id = [3.4] # list[float] | The email campaign id(s) to get metrics for (optional)

try:
    # Get attribution metrics for one or more Brevo campaigns
    api_response = api_instance.ecommerce_attribution_metrics_get(period_from=period_from, period_to=period_to, email_campaign_id=email_campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_attribution_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_from** | **datetime**| When getting metrics for a specific period, define the starting datetime in RFC3339 format | [optional] 
 **period_to** | **datetime**| When getting metrics for a specific period, define the end datetime in RFC3339 format | [optional] 
 **email_campaign_id** | [**list[float]**](float.md)| The email campaign id(s) to get metrics for | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_attribution_products_conversion_source_conversion_source_id_get**
> InlineResponse2007 ecommerce_attribution_products_conversion_source_conversion_source_id_get(conversion_source, conversion_source_id)

Get attributed product sales for a single Brevo campaign

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
conversion_source = 'conversion_source_example' # str | The Brevo campaign type for which data will be retrieved
conversion_source_id = 8.14 # float | The Brevo campaign id for which data will be retrieved

try:
    # Get attributed product sales for a single Brevo campaign
    api_response = api_instance.ecommerce_attribution_products_conversion_source_conversion_source_id_get(conversion_source, conversion_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_attribution_products_conversion_source_conversion_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversion_source** | **str**| The Brevo campaign type for which data will be retrieved | 
 **conversion_source_id** | **float**| The Brevo campaign id for which data will be retrieved | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ecommerce_config_display_currency_get**
> InlineResponse2004 ecommerce_config_display_currency_get()

Get the ISO 4217 compliant display currency code for your Brevo account

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))

try:
    # Get the ISO 4217 compliant display currency code for your Brevo account
    api_response = api_instance.ecommerce_config_display_currency_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->ecommerce_config_display_currency_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> GetCategories get_categories(limit=limit, offset=offset, sort=sort, ids=ids, name=name, modified_since=modified_since, created_since=created_since)

Return all your categories

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
ids = ['ids_example'] # list[str] | Filter by category ids (optional)
name = 'name_example' # str | Filter by category name (optional)
modified_since = 'modified_since_example' # str | Filter (urlencoded) the categories modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)
created_since = 'created_since_example' # str | Filter (urlencoded) the categories created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)

try:
    # Return all your categories
    api_response = api_instance.get_categories(limit=limit, offset=offset, sort=sort, ids=ids, name=name, modified_since=modified_since, created_since=created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **ids** | [**list[str]**](str.md)| Filter by category ids | [optional] 
 **name** | **str**| Filter by category name | [optional] 
 **modified_since** | **str**| Filter (urlencoded) the categories modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 
 **created_since** | **str**| Filter (urlencoded) the categories created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 

### Return type

[**GetCategories**](GetCategories.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_info**
> GetCategoryDetails get_category_info(id)

Get a category details

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | Category ID

try:
    # Get a category details
    api_response = api_instance.get_category_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_category_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID | 

### Return type

[**GetCategoryDetails**](GetCategoryDetails.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> GetOrders get_orders(limit=limit, offset=offset, sort=sort, modified_since=modified_since, created_since=created_since)

Get order details

Get all the orders

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
modified_since = 'modified_since_example' # str | Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)
created_since = 'created_since_example' # str | Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)

try:
    # Get order details
    api_response = api_instance.get_orders(limit=limit, offset=offset, sort=sort, modified_since=modified_since, created_since=created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **modified_since** | **str**| Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 
 **created_since** | **str**| Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_info**
> GetProductDetails get_product_info(id)

Get a product's details

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | Product ID

try:
    # Get a product's details
    api_response = api_instance.get_product_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_product_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Product ID | 

### Return type

[**GetProductDetails**](GetProductDetails.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> GetProducts get_products(limit=limit, offset=offset, sort=sort, ids=ids, name=name, price_lte=price_lte, price_gte=price_gte, price_lt=price_lt, price_gt=price_gt, price_eq=price_eq, price_ne=price_ne, categories=categories, modified_since=modified_since, created_since=created_since)

Return all your products

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
limit = 50 # int | Number of documents per page (optional) (default to 50)
offset = 0 # int | Index of the first document in the page (optional) (default to 0)
sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)
ids = ['ids_example'] # list[str] | Filter by product ids (optional)
name = 'name_example' # str | Filter by product name, minimum 3 characters should be present for search (optional)
price_lte = 8.14 # float | Price filter for products less than and equals to particular amount (optional)
price_gte = 8.14 # float | Price filter for products greater than and equals to particular amount (optional)
price_lt = 8.14 # float | Price filter for products less than particular amount (optional)
price_gt = 8.14 # float | Price filter for products greater than particular amount (optional)
price_eq = 8.14 # float | Price filter for products equals to particular amount (optional)
price_ne = 8.14 # float | Price filter for products not equals to particular amount (optional)
categories = ['categories_example'] # list[str] | Filter by category ids (optional)
modified_since = 'modified_since_example' # str | Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)
created_since = 'created_since_example' # str | Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  (optional)

try:
    # Return all your products
    api_response = api_instance.get_products(limit=limit, offset=offset, sort=sort, ids=ids, name=name, price_lte=price_lte, price_gte=price_gte, price_lt=price_lt, price_gt=price_gt, price_eq=price_eq, price_ne=price_ne, categories=categories, modified_since=modified_since, created_since=created_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of documents per page | [optional] [default to 50]
 **offset** | **int**| Index of the first document in the page | [optional] [default to 0]
 **sort** | **str**| Sort the results in the ascending/descending order of record creation. Default order is **descending** if &#x60;sort&#x60; is not passed | [optional] [default to desc]
 **ids** | [**list[str]**](str.md)| Filter by product ids | [optional] 
 **name** | **str**| Filter by product name, minimum 3 characters should be present for search | [optional] 
 **price_lte** | **float**| Price filter for products less than and equals to particular amount | [optional] 
 **price_gte** | **float**| Price filter for products greater than and equals to particular amount | [optional] 
 **price_lt** | **float**| Price filter for products less than particular amount | [optional] 
 **price_gt** | **float**| Price filter for products greater than particular amount | [optional] 
 **price_eq** | **float**| Price filter for products equals to particular amount | [optional] 
 **price_ne** | **float**| Price filter for products not equals to particular amount | [optional] 
 **categories** | [**list[str]**](str.md)| Filter by category ids | [optional] 
 **modified_since** | **str**| Filter (urlencoded) the orders modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 
 **created_since** | **str**| Filter (urlencoded) the orders created after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). **Prefer to pass your timezone in date-time format for accurate result.**  | [optional] 

### Return type

[**GetProducts**](GetProducts.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_config_display_currency**
> SetConfigDisplayCurrency set_config_display_currency(set_config_display_currency)

Set the ISO 4217 compliant display currency code for your Brevo account

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
api_instance = brevo_python.EcommerceApi(brevo_python.ApiClient(configuration))
set_config_display_currency = brevo_python.SetConfigDisplayCurrency() # SetConfigDisplayCurrency | set ISO 4217 compliant display currency code payload

try:
    # Set the ISO 4217 compliant display currency code for your Brevo account
    api_response = api_instance.set_config_display_currency(set_config_display_currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->set_config_display_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_config_display_currency** | [**SetConfigDisplayCurrency**](SetConfigDisplayCurrency.md)| set ISO 4217 compliant display currency code payload | 

### Return type

[**SetConfigDisplayCurrency**](SetConfigDisplayCurrency.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

