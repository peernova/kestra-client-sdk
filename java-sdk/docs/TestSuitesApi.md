# TestSuitesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTestSuite**](TestSuitesApi.md#createTestSuite) | **POST** /api/v1/{tenant}/tests | Create a TestSuite from yaml source |
| [**deleteTestSuite**](TestSuitesApi.md#deleteTestSuite) | **DELETE** /api/v1/{tenant}/tests/{namespace}/{id} |  |
| [**getTestSuite**](TestSuitesApi.md#getTestSuite) | **GET** /api/v1/{tenant}/tests/{namespace}/{id} |  |
| [**runTestSuite**](TestSuitesApi.md#runTestSuite) | **POST** /api/v1/{tenant}/tests/{namespace}/{id}/run | Run a full TestSuite |
| [**searchTestSuites**](TestSuitesApi.md#searchTestSuites) | **GET** /api/v1/{tenant}/tests/search |  |
| [**updateTestSuite**](TestSuitesApi.md#updateTestSuite) | **PUT** /api/v1/{tenant}/tests/{namespace}/{id} |  |
| [**validateTestSuite**](TestSuitesApi.md#validateTestSuite) | **POST** /api/v1/{tenant}/tests/validate | Run a full TestSuite |



## createTestSuite

> TestSuite createTestSuite(tenant, body)

Create a TestSuite from yaml source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | The TestSuite source code
        try {
            TestSuite result = apiInstance.createTestSuite(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#createTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **String**|  | |
| **body** | **String**| The TestSuite source code | |

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
| **200** | createTestSuite 200 response |  -  |


## deleteTestSuite

> Object deleteTestSuite(namespace, id, tenant)



### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String namespace = "namespace_example"; // String | The TestSuite namespace
        String id = "id_example"; // String | The TestSuite ID
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.deleteTestSuite(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#deleteTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **namespace** | **String**| The TestSuite namespace | |
| **id** | **String**| The TestSuite ID | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteTestSuite 200 response |  -  |


## getTestSuite

> TestSuite getTestSuite(namespace, id, tenant)



### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String namespace = "namespace_example"; // String | The TestSuite namespace
        String id = "id_example"; // String | The TestSuite ID
        String tenant = "tenant_example"; // String | 
        try {
            TestSuite result = apiInstance.getTestSuite(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#getTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **namespace** | **String**| The TestSuite namespace | |
| **id** | **String**| The TestSuite ID | |
| **tenant** | **String**|  | |

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
| **200** | getTestSuite 200 response |  -  |


## runTestSuite

> List&lt;TestSuiteRunResult&gt; runTestSuite(namespace, id, tenant)

Run a full TestSuite

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String namespace = "namespace_example"; // String | The TestSuite namespace
        String id = "id_example"; // String | The TestSuite ID
        String tenant = "tenant_example"; // String | 
        try {
            List<TestSuiteRunResult> result = apiInstance.runTestSuite(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#runTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **namespace** | **String**| The TestSuite namespace | |
| **id** | **String**| The TestSuite ID | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;TestSuiteRunResult&gt;**](TestSuiteRunResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | runTestSuite 200 response |  -  |


## searchTestSuites

> PagedResultsTestSuite searchTestSuites(page, size, tenant, sort, namespace, flowId)



### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String namespace = "namespace_example"; // String | The namespace to filter on
        String flowId = "flowId_example"; // String | The flow id to filter on
        try {
            PagedResultsTestSuite result = apiInstance.searchTestSuites(page, size, tenant, sort, namespace, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#searchTestSuites");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **tenant** | **String**|  | |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **namespace** | **String**| The namespace to filter on | [optional] |
| **flowId** | **String**| The flow id to filter on | [optional] |

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
| **200** | searchTestSuites 200 response |  -  |


## updateTestSuite

> TestSuite updateTestSuite(namespace, id, tenant, body)



### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String namespace = "namespace_example"; // String | The TestSuite namespace
        String id = "id_example"; // String | The TestSuite ID
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | The TestSuite source code
        try {
            TestSuite result = apiInstance.updateTestSuite(namespace, id, tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#updateTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **namespace** | **String**| The TestSuite namespace | |
| **id** | **String**| The TestSuite ID | |
| **tenant** | **String**|  | |
| **body** | **String**| The TestSuite source code | |

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
| **200** | updateTestSuite 200 response |  -  |


## validateTestSuite

> ValidateConstraintViolation validateTestSuite(tenant, body)

Run a full TestSuite

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TestSuitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TestSuitesApi apiInstance = new TestSuitesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | The TestSuite source code
        try {
            ValidateConstraintViolation result = apiInstance.validateTestSuite(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TestSuitesApi#validateTestSuite");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **String**|  | |
| **body** | **String**| The TestSuite source code | |

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
| **200** | validateTestSuite 200 response |  -  |

