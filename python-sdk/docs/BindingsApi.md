# kestra_api_client.BindingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_binding**](BindingsApi.md#bulk_create_binding) | **POST** /api/v1/{tenant}/bindings/bulk | Create multiple bindings
[**bulk_create_bindingaps_super_admin**](BindingsApi.md#bulk_create_bindingaps_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/bindings/bulk | Create multiple bindings
[**create_binding**](BindingsApi.md#create_binding) | **POST** /api/v1/{tenant}/bindings | Create a binding
[**create_bindingaps_super_admin**](BindingsApi.md#create_bindingaps_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/bindings | Create a binding
[**delete_binding**](BindingsApi.md#delete_binding) | **DELETE** /api/v1/{tenant}/bindings/{id} | Delete a binding
[**delete_bindingaps_super_admin**](BindingsApi.md#delete_bindingaps_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/bindings/{id} | Delete a binding
[**get_binding**](BindingsApi.md#get_binding) | **GET** /api/v1/{tenant}/bindings/{id} | Get a binding
[**get_bindingaps_super_admin**](BindingsApi.md#get_bindingaps_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/bindings/{id} | Get a binding
[**search_bindings**](BindingsApi.md#search_bindings) | **GET** /api/v1/{tenant}/bindings/search | Search for bindings
[**search_bindingsaps_super_admin**](BindingsApi.md#search_bindingsaps_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/bindings/search | Search for bindings


# **bulk_create_binding**
> List[AbstractBindingControllerBindingDetail] bulk_create_binding(tenant, binding)

Create multiple bindings

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.models.binding import Binding
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    tenant = 'tenant_example' # str | 
    binding = [kestra_api_client.Binding()] # List[Binding] | The bindings

    try:
        # Create multiple bindings
        api_response = api_instance.bulk_create_binding(tenant, binding)
        print("The response of BindingsApi->bulk_create_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->bulk_create_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **binding** | [**List[Binding]**](Binding.md)| The bindings | 

### Return type

[**List[AbstractBindingControllerBindingDetail]**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bulkCreateBinding 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_create_bindingaps_super_admin**
> List[AbstractBindingControllerBindingDetail] bulk_create_bindingaps_super_admin(resource_tenant, binding)

Create multiple bindings

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.models.binding import Binding
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    binding = [kestra_api_client.Binding()] # List[Binding] | The bindings

    try:
        # Create multiple bindings
        api_response = api_instance.bulk_create_bindingaps_super_admin(resource_tenant, binding)
        print("The response of BindingsApi->bulk_create_bindingaps_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->bulk_create_bindingaps_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **binding** | [**List[Binding]**](Binding.md)| The bindings | 

### Return type

[**List[AbstractBindingControllerBindingDetail]**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bulkCreateBindingapsSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_binding**
> AbstractBindingControllerBindingDetail create_binding(tenant, binding)

Create a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.models.binding import Binding
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    tenant = 'tenant_example' # str | 
    binding = kestra_api_client.Binding() # Binding | The binding

    try:
        # Create a binding
        api_response = api_instance.create_binding(tenant, binding)
        print("The response of BindingsApi->create_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->create_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **binding** | [**Binding**](Binding.md)| The binding | 

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createBinding 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bindingaps_super_admin**
> AbstractBindingControllerBindingDetail create_bindingaps_super_admin(resource_tenant, binding)

Create a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.models.binding import Binding
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    binding = kestra_api_client.Binding() # Binding | The binding

    try:
        # Create a binding
        api_response = api_instance.create_bindingaps_super_admin(resource_tenant, binding)
        print("The response of BindingsApi->create_bindingaps_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->create_bindingaps_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **binding** | [**Binding**](Binding.md)| The binding | 

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createBindingapsSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_binding**
> delete_binding(id, tenant)

Delete a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    id = 'id_example' # str | The binding id
    tenant = 'tenant_example' # str | 

    try:
        # Delete a binding
        api_instance.delete_binding(id, tenant)
    except Exception as e:
        print("Exception when calling BindingsApi->delete_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The binding id | 
 **tenant** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | On success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bindingaps_super_admin**
> delete_bindingaps_super_admin(id, resource_tenant)

Delete a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    id = 'id_example' # str | The binding id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete a binding
        api_instance.delete_bindingaps_super_admin(id, resource_tenant)
    except Exception as e:
        print("Exception when calling BindingsApi->delete_bindingaps_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The binding id | 
 **resource_tenant** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | On success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binding**
> AbstractBindingControllerBindingDetail get_binding(id, tenant)

Get a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    id = 'id_example' # str | The binding id
    tenant = 'tenant_example' # str | 

    try:
        # Get a binding
        api_response = api_instance.get_binding(id, tenant)
        print("The response of BindingsApi->get_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->get_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The binding id | 
 **tenant** | **str**|  | 

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getBinding 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bindingaps_super_admin**
> AbstractBindingControllerBindingDetail get_bindingaps_super_admin(id, resource_tenant)

Get a binding

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    id = 'id_example' # str | The binding id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Get a binding
        api_response = api_instance.get_bindingaps_super_admin(id, resource_tenant)
        print("The response of BindingsApi->get_bindingaps_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->get_bindingaps_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The binding id | 
 **resource_tenant** | **str**|  | 

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getBindingapsSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_bindings**
> PagedResultsAbstractBindingControllerBindingDetail search_bindings(page, size, tenant, q=q, sort=sort, type=type, id=id, namespace=namespace)

Search for bindings

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_abstract_binding_controller_binding_detail import PagedResultsAbstractBindingControllerBindingDetail
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    type = kestra_api_client.BindingType() # BindingType | Binding type filter (optional)
    id = 'id_example' # str | External id filter (optional)
    namespace = 'namespace_example' # str | A namespace filter (optional)

    try:
        # Search for bindings
        api_response = api_instance.search_bindings(page, size, tenant, q=q, sort=sort, type=type, id=id, namespace=namespace)
        print("The response of BindingsApi->search_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->search_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **type** | [**BindingType**](.md)| Binding type filter | [optional] 
 **id** | **str**| External id filter | [optional] 
 **namespace** | **str**| A namespace filter | [optional] 

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchBindings 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_bindingsaps_super_admin**
> PagedResultsAbstractBindingControllerBindingDetail search_bindingsaps_super_admin(page, size, resource_tenant, q=q, sort=sort, type=type, id=id, namespace=namespace)

Search for bindings

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_abstract_binding_controller_binding_detail import PagedResultsAbstractBindingControllerBindingDetail
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.BindingsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    type = kestra_api_client.BindingType() # BindingType | Binding type filter (optional)
    id = 'id_example' # str | External id filter (optional)
    namespace = 'namespace_example' # str | A namespace filter (optional)

    try:
        # Search for bindings
        api_response = api_instance.search_bindingsaps_super_admin(page, size, resource_tenant, q=q, sort=sort, type=type, id=id, namespace=namespace)
        print("The response of BindingsApi->search_bindingsaps_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BindingsApi->search_bindingsaps_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **type** | [**BindingType**](.md)| Binding type filter | [optional] 
 **id** | **str**| External id filter | [optional] 
 **namespace** | **str**| A namespace filter | [optional] 

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchBindingsapsSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

