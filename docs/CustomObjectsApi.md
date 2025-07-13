# brevo_python.CustomObjectsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getrecords**](CustomObjectsApi.md#getrecords) | **GET** /objects/{object_type}/records | Get the list of object records and total records count for an object.
[**upsertrecords**](CustomObjectsApi.md#upsertrecords) | **POST** /objects/{object_type}/batch/upsert | Create/Update object records in bulk


# **getrecords**
> getrecords(object_type, limit, page_num, sort=sort, association=association)

Get the list of object records and total records count for an object.

This API retrieves a list of object records along with their associated records and provides the total count of records for the specified object. 

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
api_instance = brevo_python.CustomObjectsApi(brevo_python.ApiClient(configuration))
object_type = NULL # object | object type for the attribute
limit = NULL # object | Number of records returned per page
page_num = NULL # object | Page number for pagination. It's used to fetch the object records on a provided page number. Must be a valid positive integer.
sort = NULL # object | Sort order, must be 'asc' or 'desc'. Default to 'desc' if not provided. (optional)
association = NULL # object | Whether to include associations, must be 'true' or 'false'. Default to 'false' if not provided. (optional)

try:
    # Get the list of object records and total records count for an object.
    api_instance.getrecords(object_type, limit, page_num, sort=sort, association=association)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->getrecords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | [**object**](.md)| object type for the attribute | 
 **limit** | [**object**](.md)| Number of records returned per page | 
 **page_num** | [**object**](.md)| Page number for pagination. It&#39;s used to fetch the object records on a provided page number. Must be a valid positive integer. | 
 **sort** | [**object**](.md)| Sort order, must be &#39;asc&#39; or &#39;desc&#39;. Default to &#39;desc&#39; if not provided. | [optional] 
 **association** | [**object**](.md)| Whether to include associations, must be &#39;true&#39; or &#39;false&#39;. Default to &#39;false&#39; if not provided. | [optional] 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsertrecords**
> upsertrecords(object_type)

Create/Update object records in bulk

This API allows bulk upsert of object records in a single request. Each object record may include   - Attributes   - Identifiers   - Associations  **Response:**   The API processes the request asynchronously and returns a processId that you can use to track the background process status.  **API and Schema Limitation:**   - Size:       - Max 1000 objects records per request       - Max request body size: 1 MB    - Max 500 attributes defined per object record upsert request     - This is coherent with schema limitation: an object cannot have more than 500 attributes.     - Worth noting: Nothing happens If an attribute is mentioned in the request, but was not previously defined for the object schema (no error, no attribute creation)    - Max 10 associations defined per object record upsert request     - This is coherent with schema limitation: an object cannot have more than 10 associations with other objects. and each object record can be linked to max 10 other records.  **Errors:**     - Make sure both object records exist before associating them, else the API will return an error.     - This route does not create objects. The object where the object records are upserted by this API must be created already else the API will return an error \"invalid object type\". 

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
api_instance = brevo_python.CustomObjectsApi(brevo_python.ApiClient(configuration))
object_type = NULL # object | object type for the attribute

try:
    # Create/Update object records in bulk
    api_instance.upsertrecords(object_type)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->upsertrecords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | [**object**](.md)| object type for the attribute | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

