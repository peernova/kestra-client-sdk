# ServicesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**active**](ServicesApi.md#active) | **GET** /api/v1/cluster/services/active | Get details about active services |
| [**active1**](ServicesApi.md#active1) | **GET** /api/v1/{tenant}/cluster/services/active | Get details about active services |
| [**find29**](ServicesApi.md#find29) | **GET** /api/v1/{tenant}/cluster/services/search | Search for service |
| [**find3**](ServicesApi.md#find3) | **GET** /api/v1/cluster/services/search | Search for service |
| [**index2**](ServicesApi.md#index2) | **GET** /api/v1/cluster/services/{id} | Get details about a service |
| [**index23**](ServicesApi.md#index23) | **GET** /api/v1/{tenant}/cluster/services/{id} | Get details about a service |



## active

> ClusterControllerApiActiveServiceList active()

Get details about active services

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        try {
            ClusterControllerApiActiveServiceList result = apiInstance.active();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#active");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterControllerApiActiveServiceList**](ClusterControllerApiActiveServiceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | active 200 response |  -  |


## active1

> ClusterControllerApiActiveServiceList active1(tenant)

Get details about active services

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            ClusterControllerApiActiveServiceList result = apiInstance.active1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#active1");
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

### Return type

[**ClusterControllerApiActiveServiceList**](ClusterControllerApiActiveServiceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | active_1 200 response |  -  |


## find29

> PagedResultsClusterControllerApiServiceInstance find29(page, size, tenant, sort, state, type)

Search for service

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<ServiceServiceState> state = Arrays.asList(); // List<ServiceServiceState> | The state filter
        List<ServiceServiceType> type = Arrays.asList(); // List<ServiceServiceType> | The server type filter
        try {
            PagedResultsClusterControllerApiServiceInstance result = apiInstance.find29(page, size, tenant, sort, state, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#find29");
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
| **state** | [**List&lt;ServiceServiceState&gt;**](ServiceServiceState.md)| The state filter | [optional] |
| **type** | [**List&lt;ServiceServiceType&gt;**](ServiceServiceType.md)| The server type filter | [optional] |

### Return type

[**PagedResultsClusterControllerApiServiceInstance**](PagedResultsClusterControllerApiServiceInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_29 200 response |  -  |


## find3

> PagedResultsClusterControllerApiServiceInstance find3(page, size, sort, state, type)

Search for service

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<ServiceServiceState> state = Arrays.asList(); // List<ServiceServiceState> | The state filter
        List<ServiceServiceType> type = Arrays.asList(); // List<ServiceServiceType> | The server type filter
        try {
            PagedResultsClusterControllerApiServiceInstance result = apiInstance.find3(page, size, sort, state, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#find3");
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
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **state** | [**List&lt;ServiceServiceState&gt;**](ServiceServiceState.md)| The state filter | [optional] |
| **type** | [**List&lt;ServiceServiceType&gt;**](ServiceServiceType.md)| The server type filter | [optional] |

### Return type

[**PagedResultsClusterControllerApiServiceInstance**](PagedResultsClusterControllerApiServiceInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_3 200 response |  -  |


## index2

> ServiceInstance index2(id)

Get details about a service

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ServiceInstance result = apiInstance.index2(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#index2");
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
| **id** | **String**|  | |

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_2 200 response |  -  |


## index23

> ServiceInstance index23(id, tenant)

Get details about a service

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        String id = "id_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ServiceInstance result = apiInstance.index23(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#index23");
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
| **id** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_23 200 response |  -  |

