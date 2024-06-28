# brevo_python.PaymentsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_request**](PaymentsApi.md#create_payment_request) | **POST** /payments/requests | Create a payment request
[**delete_payment_request**](PaymentsApi.md#delete_payment_request) | **DELETE** /payments/requests/{id} | Delete a payment request.
[**get_payment_request**](PaymentsApi.md#get_payment_request) | **GET** /payments/requests/{id} | Get payment request details


# **create_payment_request**
> CreatePaymentResponse create_payment_request(create_payment_rquest)

Create a payment request

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
api_instance = brevo_python.PaymentsApi(brevo_python.ApiClient(configuration))
create_payment_rquest = brevo_python.CreatePaymentRequest() # CreatePaymentRequest | Create a payment request 

try:
    # Create a payment request
    api_response = api_instance.create_payment_request(create_payment_rquest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_rquest** | [**CreatePaymentRequest**](CreatePaymentRequest.md)| Create a payment request  | 

### Return type

[**CreatePaymentResponse**](CreatePaymentResponse.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_request**
> delete_payment_request(id)

Delete a payment request.

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
api_instance = brevo_python.PaymentsApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | ID of the payment request.

try:
    # Delete a payment request.
    api_instance.delete_payment_request(id)
except ApiException as e:
    print("Exception when calling PaymentsApi->delete_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the payment request. | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_request**
> GetPaymentRequest get_payment_request(id)

Get payment request details

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
api_instance = brevo_python.PaymentsApi(brevo_python.ApiClient(configuration))
id = 'id_example' # str | Id of the payment Request

try:
    # Get payment request details
    api_response = api_instance.get_payment_request(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the payment Request | 

### Return type

[**GetPaymentRequest**](GetPaymentRequest.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

