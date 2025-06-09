# WorkerGroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkerGroup**](WorkerGroupsApi.md#createWorkerGroup) | **POST** /api/v1/{tenant}/cluster/workergroups | Create a new worker group. |
| [**deleteWorkerGroupById**](WorkerGroupsApi.md#deleteWorkerGroupById) | **DELETE** /api/v1/{tenant}/cluster/workergroups/{id} | Delete an existing worker group. |
| [**getWorkerGroupById**](WorkerGroupsApi.md#getWorkerGroupById) | **GET** /api/v1/{tenant}/cluster/workergroups/{id} | Get details about a worker group. |
| [**listWorkerGroups**](WorkerGroupsApi.md#listWorkerGroups) | **GET** /api/v1/{tenant}/cluster/workergroups | List all Worker Groups |
| [**updateWorkerGroupById**](WorkerGroupsApi.md#updateWorkerGroupById) | **PUT** /api/v1/{tenant}/cluster/workergroups/{id} | Update an existing worker group. |



## createWorkerGroup

> ClusterControllerApiWorkerGroup createWorkerGroup(tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Create a new worker group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.WorkerGroupsApi;

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

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.createWorkerGroup(tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#createWorkerGroup");
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createWorkerGroup 200 response |  -  |


## deleteWorkerGroupById

> Object deleteWorkerGroupById(id, tenant)

Delete an existing worker group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.WorkerGroupsApi;

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

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String |
        String tenant = "tenant_example"; // String |
        try {
            Object result = apiInstance.deleteWorkerGroupById(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#deleteWorkerGroupById");
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

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteWorkerGroupById 200 response |  -  |


## getWorkerGroupById

> ClusterControllerApiWorkerGroupDetails getWorkerGroupById(id, tenant)

Get details about a worker group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.WorkerGroupsApi;

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

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String |
        String tenant = "tenant_example"; // String |
        try {
            ClusterControllerApiWorkerGroupDetails result = apiInstance.getWorkerGroupById(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#getWorkerGroupById");
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

[**ClusterControllerApiWorkerGroupDetails**](ClusterControllerApiWorkerGroupDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getWorkerGroupById 200 response |  -  |


## listWorkerGroups

> ClusterControllerApiWorkerGroupList listWorkerGroups(tenant)

List all Worker Groups

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.WorkerGroupsApi;

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

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        try {
            ClusterControllerApiWorkerGroupList result = apiInstance.listWorkerGroups(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#listWorkerGroups");
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

[**ClusterControllerApiWorkerGroupList**](ClusterControllerApiWorkerGroupList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listWorkerGroups 200 response |  -  |


## updateWorkerGroupById

> ClusterControllerApiWorkerGroup updateWorkerGroupById(id, tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Update an existing worker group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.WorkerGroupsApi;

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

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String |
        String tenant = "tenant_example"; // String |
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.updateWorkerGroupById(id, tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#updateWorkerGroupById");
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateWorkerGroupById 200 response |  -  |

