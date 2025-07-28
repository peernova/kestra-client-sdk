# WorkerGroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkerGroup**](WorkerGroupsApi.md#createWorkerGroup) | **POST** /api/v1/instance/workergroups | Create a worker group |
| [**deleteWorkerGroupById**](WorkerGroupsApi.md#deleteWorkerGroupById) | **DELETE** /api/v1/instance/workergroups/{id} | Delete a worker group |
| [**getWorkerGroupById**](WorkerGroupsApi.md#getWorkerGroupById) | **GET** /api/v1/instance/workergroups/{id} | Retrieve details of a specific worker group |
| [**listWorkerGroups**](WorkerGroupsApi.md#listWorkerGroups) | **GET** /api/v1/instance/workergroups | List all worker groups |
| [**updateWorkerGroupById**](WorkerGroupsApi.md#updateWorkerGroupById) | **PUT** /api/v1/instance/workergroups/{id} | Update a worker group |



## createWorkerGroup

> InstanceControllerApiWorkerGroup createWorkerGroup(instanceControllerApiCreateOrUpdateWorkerGroupRequest)

Create a worker group

Requires a role with the INFRASTRUCTURE permission (Superadmin-only).

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.auth.*;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.WorkerGroupsApi;

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
        InstanceControllerApiCreateOrUpdateWorkerGroupRequest instanceControllerApiCreateOrUpdateWorkerGroupRequest = new InstanceControllerApiCreateOrUpdateWorkerGroupRequest(); // InstanceControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition
        try {
            InstanceControllerApiWorkerGroup result = apiInstance.createWorkerGroup(instanceControllerApiCreateOrUpdateWorkerGroupRequest);
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
| **instanceControllerApiCreateOrUpdateWorkerGroupRequest** | [**InstanceControllerApiCreateOrUpdateWorkerGroupRequest**](InstanceControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | |

### Return type

[**InstanceControllerApiWorkerGroup**](InstanceControllerApiWorkerGroup.md)

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

> Object deleteWorkerGroupById(id)

Delete a worker group

Requires a role with the INFRASTRUCTURE permission (Superadmin-only).

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.auth.*;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.WorkerGroupsApi;

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
        try {
            Object result = apiInstance.deleteWorkerGroupById(id);
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

> InstanceControllerApiWorkerGroupDetails getWorkerGroupById(id)

Retrieve details of a specific worker group

Requires a role with the INFRASTRUCTURE permission (Superadmin-only).

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.auth.*;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.WorkerGroupsApi;

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
        try {
            InstanceControllerApiWorkerGroupDetails result = apiInstance.getWorkerGroupById(id);
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

### Return type

[**InstanceControllerApiWorkerGroupDetails**](InstanceControllerApiWorkerGroupDetails.md)

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

> InstanceControllerApiWorkerGroupList listWorkerGroups()

List all worker groups

Requires a role with the INFRASTRUCTURE permission (Superadmin-only).

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.auth.*;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.WorkerGroupsApi;

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
        try {
            InstanceControllerApiWorkerGroupList result = apiInstance.listWorkerGroups();
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

This endpoint does not need any parameter.

### Return type

[**InstanceControllerApiWorkerGroupList**](InstanceControllerApiWorkerGroupList.md)

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

> InstanceControllerApiWorkerGroup updateWorkerGroupById(id, instanceControllerApiCreateOrUpdateWorkerGroupRequest)

Update a worker group

Requires a role with the INFRASTRUCTURE permission (Superadmin-only).

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.auth.*;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.WorkerGroupsApi;

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
        InstanceControllerApiCreateOrUpdateWorkerGroupRequest instanceControllerApiCreateOrUpdateWorkerGroupRequest = new InstanceControllerApiCreateOrUpdateWorkerGroupRequest(); // InstanceControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition
        try {
            InstanceControllerApiWorkerGroup result = apiInstance.updateWorkerGroupById(id, instanceControllerApiCreateOrUpdateWorkerGroupRequest);
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
| **instanceControllerApiCreateOrUpdateWorkerGroupRequest** | [**InstanceControllerApiCreateOrUpdateWorkerGroupRequest**](InstanceControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | |

### Return type

[**InstanceControllerApiWorkerGroup**](InstanceControllerApiWorkerGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateWorkerGroupById 200 response |  -  |

