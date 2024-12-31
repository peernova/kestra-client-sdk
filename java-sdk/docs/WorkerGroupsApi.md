# WorkerGroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkerGroup**](WorkerGroupsApi.md#createWorkerGroup) | **POST** /api/v1/cluster/workergroups | Create a new worker group. |
| [**createWorkerGroup1**](WorkerGroupsApi.md#createWorkerGroup1) | **POST** /api/v1/{tenant}/cluster/workergroups | Create a new worker group. |
| [**deleteWorkerGroupById**](WorkerGroupsApi.md#deleteWorkerGroupById) | **DELETE** /api/v1/cluster/workergroups/{id} | Delete an existing worker group. |
| [**deleteWorkerGroupById1**](WorkerGroupsApi.md#deleteWorkerGroupById1) | **DELETE** /api/v1/{tenant}/cluster/workergroups/{id} | Delete an existing worker group. |
| [**getWorkerGroupById**](WorkerGroupsApi.md#getWorkerGroupById) | **GET** /api/v1/cluster/workergroups/{id} | Get details about a worker group. |
| [**getWorkerGroupById1**](WorkerGroupsApi.md#getWorkerGroupById1) | **GET** /api/v1/{tenant}/cluster/workergroups/{id} | Get details about a worker group. |
| [**listWorkerGroups**](WorkerGroupsApi.md#listWorkerGroups) | **GET** /api/v1/cluster/workergroups | List all Worker Groups |
| [**listWorkerGroups1**](WorkerGroupsApi.md#listWorkerGroups1) | **GET** /api/v1/{tenant}/cluster/workergroups | List all Worker Groups |
| [**updateWorkerGroupById**](WorkerGroupsApi.md#updateWorkerGroupById) | **PUT** /api/v1/cluster/workergroups/{id} | Update an existing worker group. |
| [**updateWorkerGroupById1**](WorkerGroupsApi.md#updateWorkerGroupById1) | **PUT** /api/v1/{tenant}/cluster/workergroups/{id} | Update an existing worker group. |



## createWorkerGroup

> ClusterControllerApiWorkerGroup createWorkerGroup(clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Create a new worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | 
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.createWorkerGroup(clusterControllerApiCreateOrUpdateWorkerGroupRequest);
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)|  | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createWorkerGroup 200 response |  -  |


## createWorkerGroup1

> ClusterControllerApiWorkerGroup createWorkerGroup1(tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Create a new worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | 
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.createWorkerGroup1(tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#createWorkerGroup1");
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)|  | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createWorkerGroup_1 200 response |  -  |


## deleteWorkerGroupById

> Object deleteWorkerGroupById(id)

Delete an existing worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteWorkerGroupById 200 response |  -  |


## deleteWorkerGroupById1

> Object deleteWorkerGroupById1(id, tenant)

Delete an existing worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.deleteWorkerGroupById1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#deleteWorkerGroupById1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteWorkerGroupById_1 200 response |  -  |


## getWorkerGroupById

> ClusterControllerApiWorkerGroupDetails getWorkerGroupById(id)

Get details about a worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ClusterControllerApiWorkerGroupDetails result = apiInstance.getWorkerGroupById(id);
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

[**ClusterControllerApiWorkerGroupDetails**](ClusterControllerApiWorkerGroupDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getWorkerGroupById 200 response |  -  |


## getWorkerGroupById1

> ClusterControllerApiWorkerGroupDetails getWorkerGroupById1(id, tenant)

Get details about a worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ClusterControllerApiWorkerGroupDetails result = apiInstance.getWorkerGroupById1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#getWorkerGroupById1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getWorkerGroupById_1 200 response |  -  |


## listWorkerGroups

> ClusterControllerApiWorkerGroupList listWorkerGroups()

List all Worker Groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        try {
            ClusterControllerApiWorkerGroupList result = apiInstance.listWorkerGroups();
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

[**ClusterControllerApiWorkerGroupList**](ClusterControllerApiWorkerGroupList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listWorkerGroups 200 response |  -  |


## listWorkerGroups1

> ClusterControllerApiWorkerGroupList listWorkerGroups1(tenant)

List all Worker Groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            ClusterControllerApiWorkerGroupList result = apiInstance.listWorkerGroups1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#listWorkerGroups1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listWorkerGroups_1 200 response |  -  |


## updateWorkerGroupById

> ClusterControllerApiWorkerGroup updateWorkerGroupById(id, clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Update an existing worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String | 
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | 
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.updateWorkerGroupById(id, clusterControllerApiCreateOrUpdateWorkerGroupRequest);
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)|  | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateWorkerGroupById 200 response |  -  |


## updateWorkerGroupById1

> ClusterControllerApiWorkerGroup updateWorkerGroupById1(id, tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest)

Update an existing worker group.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.WorkerGroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        WorkerGroupsApi apiInstance = new WorkerGroupsApi(defaultClient);
        String id = "id_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ClusterControllerApiCreateOrUpdateWorkerGroupRequest clusterControllerApiCreateOrUpdateWorkerGroupRequest = new ClusterControllerApiCreateOrUpdateWorkerGroupRequest(); // ClusterControllerApiCreateOrUpdateWorkerGroupRequest | 
        try {
            ClusterControllerApiWorkerGroup result = apiInstance.updateWorkerGroupById1(id, tenant, clusterControllerApiCreateOrUpdateWorkerGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkerGroupsApi#updateWorkerGroupById1");
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
| **clusterControllerApiCreateOrUpdateWorkerGroupRequest** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)|  | |

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateWorkerGroupById_1 200 response |  -  |

