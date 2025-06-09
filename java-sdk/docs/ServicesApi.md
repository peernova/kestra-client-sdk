# ServicesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActiveServices**](ServicesApi.md#getActiveServices) | **GET** /api/v1/{tenant}/cluster/services/active | Get details about active services |
| [**getService**](ServicesApi.md#getService) | **GET** /api/v1/{tenant}/cluster/services/{id} | Get details about a service |
| [**searchServices**](ServicesApi.md#searchServices) | **GET** /api/v1/{tenant}/cluster/services/search | Search for service |



## getActiveServices

> ClusterControllerApiActiveServiceList getActiveServices(tenant)

Get details about active services

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        String tenant = "tenant_example"; // String |
        try {
            ClusterControllerApiActiveServiceList result = apiInstance.getActiveServices(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#getActiveServices");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getActiveServices 200 response |  -  |


## getService

> ServiceInstance getService(id, tenant)

Get details about a service

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        String id = "id_example"; // String |
        String tenant = "tenant_example"; // String |
        try {
            ServiceInstance result = apiInstance.getService(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#getService");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getService 200 response |  -  |


## searchServices

> PagedResultsClusterControllerApiServiceInstance searchServices(page, size, tenant, sort, state, type)

Search for service

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.ServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ServicesApi apiInstance = new ServicesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<ServiceServiceState> state = Arrays.asList(); // List<ServiceServiceState> | The state filter
        List<ServiceType> type = Arrays.asList(); // List<ServiceType> | The server type filter
        try {
            PagedResultsClusterControllerApiServiceInstance result = apiInstance.searchServices(page, size, tenant, sort, state, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ServicesApi#searchServices");
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
| **type** | [**List&lt;ServiceType&gt;**](ServiceType.md)| The server type filter | [optional] |

### Return type

[**PagedResultsClusterControllerApiServiceInstance**](PagedResultsClusterControllerApiServiceInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchServices 200 response |  -  |

