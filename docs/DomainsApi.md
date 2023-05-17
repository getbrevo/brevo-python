# brevo_python.DomainsApi

All URIs are relative to *https://api.brevo.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_domain**](DomainsApi.md#authenticate_domain) | **PUT** /senders/domains/{domainName}/authenticate | Authenticate a domain
[**create_domain**](DomainsApi.md#create_domain) | **POST** /senders/domains | Create a new domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /senders/domains/{domainName} | Delete a domain
[**get_domain_configuration**](DomainsApi.md#get_domain_configuration) | **GET** /senders/domains/{domainName} | Validate domain configuration
[**get_domains**](DomainsApi.md#get_domains) | **GET** /senders/domains | Get the list of all your domains


# **authenticate_domain**
> AuthenticateDomainModel authenticate_domain(domain_name)

Authenticate a domain

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
api_instance = brevo_python.DomainsApi(brevo_python.ApiClient(configuration))
domain_name = 'domain_name_example' # str | Domain name

try:
    # Authenticate a domain
    api_response = api_instance.authenticate_domain(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->authenticate_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Domain name | 

### Return type

[**AuthenticateDomainModel**](AuthenticateDomainModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain**
> CreateDomainModel create_domain(domain_name=domain_name)

Create a new domain

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
api_instance = brevo_python.DomainsApi(brevo_python.ApiClient(configuration))
domain_name = brevo_python.CreateDomain() # CreateDomain | domain's name (optional)

try:
    # Create a new domain
    api_response = api_instance.create_domain(domain_name=domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | [**CreateDomain**](CreateDomain.md)| domain&#39;s name | [optional] 

### Return type

[**CreateDomainModel**](CreateDomainModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(domain_name)

Delete a domain

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
api_instance = brevo_python.DomainsApi(brevo_python.ApiClient(configuration))
domain_name = 'domain_name_example' # str | Domain name

try:
    # Delete a domain
    api_instance.delete_domain(domain_name)
except ApiException as e:
    print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Domain name | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_configuration**
> GetDomainConfigurationModel get_domain_configuration(domain_name)

Validate domain configuration

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
api_instance = brevo_python.DomainsApi(brevo_python.ApiClient(configuration))
domain_name = 'domain_name_example' # str | Domain name

try:
    # Validate domain configuration
    api_response = api_instance.get_domain_configuration(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Domain name | 

### Return type

[**GetDomainConfigurationModel**](GetDomainConfigurationModel.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains**
> GetDomainsList get_domains()

Get the list of all your domains

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
api_instance = brevo_python.DomainsApi(brevo_python.ApiClient(configuration))

try:
    # Get the list of all your domains
    api_response = api_instance.get_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDomainsList**](GetDomainsList.md)

### Authorization

[api-key](../README.md#api-key), [partner-key](../README.md#partner-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

