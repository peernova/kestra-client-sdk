# kestra_api_client.TestSuitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_suite**](TestSuitesApi.md#create_test_suite) | **POST** /api/v1/{tenant}/tests | Create a TestSuite from yaml source
[**delete_test_suite**](TestSuitesApi.md#delete_test_suite) | **DELETE** /api/v1/{tenant}/tests/{namespace}/{id} | 
[**get_test_suite**](TestSuitesApi.md#get_test_suite) | **GET** /api/v1/{tenant}/tests/{namespace}/{id} | 
[**run_test_suite**](TestSuitesApi.md#run_test_suite) | **POST** /api/v1/{tenant}/tests/{namespace}/{id}/run | Run a full TestSuite
[**search_test_suites**](TestSuitesApi.md#search_test_suites) | **GET** /api/v1/{tenant}/tests/search | 
[**update_test_suite**](TestSuitesApi.md#update_test_suite) | **PUT** /api/v1/{tenant}/tests/{namespace}/{id} | 
[**validate_test_suite**](TestSuitesApi.md#validate_test_suite) | **POST** /api/v1/{tenant}/tests/validate | Validate a TestSuite


# **create_test_suite**
> TestSuite create_test_suite(tenant, body)

Create a TestSuite from yaml source

### Example


```python
import kestra_api_client
from kestra_api_client.models.test_suite import TestSuite
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    tenant = 'tenant_example' # str | 
    body = 'body_example' # str | The TestSuite source code

    try:
        # Create a TestSuite from yaml source
        api_response = api_instance.create_test_suite(tenant, body)
        print("The response of TestSuitesApi->create_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->create_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **body** | **str**| The TestSuite source code | 

### Return type

[**TestSuite**](TestSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_suite**
> object delete_test_suite(namespace, id, tenant)

### Example


```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    namespace = 'namespace_example' # str | The TestSuite namespace
    id = 'id_example' # str | The TestSuite ID
    tenant = 'tenant_example' # str | 

    try:
        api_response = api_instance.delete_test_suite(namespace, id, tenant)
        print("The response of TestSuitesApi->delete_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->delete_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The TestSuite namespace | 
 **id** | **str**| The TestSuite ID | 
 **tenant** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suite**
> TestSuite get_test_suite(namespace, id, tenant)

### Example


```python
import kestra_api_client
from kestra_api_client.models.test_suite import TestSuite
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    namespace = 'namespace_example' # str | The TestSuite namespace
    id = 'id_example' # str | The TestSuite ID
    tenant = 'tenant_example' # str | 

    try:
        api_response = api_instance.get_test_suite(namespace, id, tenant)
        print("The response of TestSuitesApi->get_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->get_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The TestSuite namespace | 
 **id** | **str**| The TestSuite ID | 
 **tenant** | **str**|  | 

### Return type

[**TestSuite**](TestSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_test_suite**
> List[TestSuiteRunResult] run_test_suite(namespace, id, tenant)

Run a full TestSuite

### Example


```python
import kestra_api_client
from kestra_api_client.models.test_suite_run_result import TestSuiteRunResult
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    namespace = 'namespace_example' # str | The TestSuite namespace
    id = 'id_example' # str | The TestSuite ID
    tenant = 'tenant_example' # str | 

    try:
        # Run a full TestSuite
        api_response = api_instance.run_test_suite(namespace, id, tenant)
        print("The response of TestSuitesApi->run_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->run_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The TestSuite namespace | 
 **id** | **str**| The TestSuite ID | 
 **tenant** | **str**|  | 

### Return type

[**List[TestSuiteRunResult]**](TestSuiteRunResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | runTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_test_suites**
> PagedResultsTestSuite search_test_suites(page, size, tenant, sort=sort, namespace=namespace, flow_id=flow_id)

### Example


```python
import kestra_api_client
from kestra_api_client.models.paged_results_test_suite import PagedResultsTestSuite
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    namespace = 'namespace_example' # str | The namespace to filter on (optional)
    flow_id = 'flow_id_example' # str | The flow id to filter on (optional)

    try:
        api_response = api_instance.search_test_suites(page, size, tenant, sort=sort, namespace=namespace, flow_id=flow_id)
        print("The response of TestSuitesApi->search_test_suites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->search_test_suites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **namespace** | **str**| The namespace to filter on | [optional] 
 **flow_id** | **str**| The flow id to filter on | [optional] 

### Return type

[**PagedResultsTestSuite**](PagedResultsTestSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchTestSuites 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_suite**
> TestSuite update_test_suite(namespace, id, tenant, body)

### Example


```python
import kestra_api_client
from kestra_api_client.models.test_suite import TestSuite
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    namespace = 'namespace_example' # str | The TestSuite namespace
    id = 'id_example' # str | The TestSuite ID
    tenant = 'tenant_example' # str | 
    body = 'body_example' # str | The TestSuite source code

    try:
        api_response = api_instance.update_test_suite(namespace, id, tenant, body)
        print("The response of TestSuitesApi->update_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->update_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The TestSuite namespace | 
 **id** | **str**| The TestSuite ID | 
 **tenant** | **str**|  | 
 **body** | **str**| The TestSuite source code | 

### Return type

[**TestSuite**](TestSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_test_suite**
> ValidateConstraintViolation validate_test_suite(tenant, body)

Validate a TestSuite

### Example


```python
import kestra_api_client
from kestra_api_client.models.validate_constraint_violation import ValidateConstraintViolation
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.TestSuitesApi(api_client)
    tenant = 'tenant_example' # str | 
    body = 'body_example' # str | The TestSuite source code

    try:
        # Validate a TestSuite
        api_response = api_instance.validate_test_suite(tenant, body)
        print("The response of TestSuitesApi->validate_test_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->validate_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **body** | **str**| The TestSuite source code | 

### Return type

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-yaml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | validateTestSuite 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

