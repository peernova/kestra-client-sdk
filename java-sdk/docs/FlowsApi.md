# FlowsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkUpdate**](FlowsApi.md#bulkUpdate) | **POST** /api/v1/flows/bulk | Update from multiples yaml sources |
| [**bulkUpdate1**](FlowsApi.md#bulkUpdate1) | **POST** /api/v1/{tenant}/flows/bulk | Update from multiples yaml sources |
| [**create30**](FlowsApi.md#create30) | **POST** /api/v1/{tenant}/flows | Create a flow from json object |
| [**create5**](FlowsApi.md#create5) | **POST** /api/v1/flows | Create a flow from json object |
| [**delete33**](FlowsApi.md#delete33) | **DELETE** /api/v1/{tenant}/flows/{namespace}/{id} | Delete a flow |
| [**delete5**](FlowsApi.md#delete5) | **DELETE** /api/v1/flows/{namespace}/{id} | Delete a flow |
| [**deleteByIds1**](FlowsApi.md#deleteByIds1) | **DELETE** /api/v1/flows/delete/by-ids | Delete flows by their IDs. |
| [**deleteByIds4**](FlowsApi.md#deleteByIds4) | **DELETE** /api/v1/{tenant}/flows/delete/by-ids | Delete flows by their IDs. |
| [**deleteByQuery1**](FlowsApi.md#deleteByQuery1) | **DELETE** /api/v1/flows/delete/by-query | Delete flows returned by the query parameters. |
| [**deleteByQuery4**](FlowsApi.md#deleteByQuery4) | **DELETE** /api/v1/{tenant}/flows/delete/by-query | Delete flows returned by the query parameters. |
| [**dependencies**](FlowsApi.md#dependencies) | **GET** /api/v1/flows/{namespace}/{id}/dependencies | Get flow dependencies |
| [**dependencies1**](FlowsApi.md#dependencies1) | **GET** /api/v1/namespaces/{namespace}/dependencies | Get flow dependencies |
| [**dependencies2**](FlowsApi.md#dependencies2) | **GET** /api/v1/{tenant}/flows/{namespace}/{id}/dependencies | Get flow dependencies |
| [**dependencies3**](FlowsApi.md#dependencies3) | **GET** /api/v1/{tenant}/namespaces/{namespace}/dependencies | Get flow dependencies |
| [**disableByIds**](FlowsApi.md#disableByIds) | **POST** /api/v1/flows/disable/by-ids | Disable flows by their IDs. |
| [**disableByIds1**](FlowsApi.md#disableByIds1) | **POST** /api/v1/{tenant}/flows/disable/by-ids | Disable flows by their IDs. |
| [**disableByQuery**](FlowsApi.md#disableByQuery) | **POST** /api/v1/flows/disable/by-query | Disable flows returned by the query parameters. |
| [**disableByQuery1**](FlowsApi.md#disableByQuery1) | **POST** /api/v1/{tenant}/flows/disable/by-query | Disable flows returned by the query parameters. |
| [**enableByIds**](FlowsApi.md#enableByIds) | **POST** /api/v1/flows/enable/by-ids | Enable flows by their IDs. |
| [**enableByIds1**](FlowsApi.md#enableByIds1) | **POST** /api/v1/{tenant}/flows/enable/by-ids | Enable flows by their IDs. |
| [**enableByQuery**](FlowsApi.md#enableByQuery) | **POST** /api/v1/flows/enable/by-query | Enable flows returned by the query parameters. |
| [**enableByQuery1**](FlowsApi.md#enableByQuery1) | **POST** /api/v1/{tenant}/flows/enable/by-query | Enable flows returned by the query parameters. |
| [**exportByIds**](FlowsApi.md#exportByIds) | **POST** /api/v1/flows/export/by-ids | Export flows as a ZIP archive of yaml sources. |
| [**exportByIds2**](FlowsApi.md#exportByIds2) | **POST** /api/v1/{tenant}/flows/export/by-ids | Export flows as a ZIP archive of yaml sources. |
| [**exportByQuery**](FlowsApi.md#exportByQuery) | **GET** /api/v1/flows/export/by-query | Export flows as a ZIP archive of yaml sources. |
| [**exportByQuery2**](FlowsApi.md#exportByQuery2) | **GET** /api/v1/{tenant}/flows/export/by-query | Export flows as a ZIP archive of yaml sources. |
| [**find31**](FlowsApi.md#find31) | **GET** /api/v1/{tenant}/flows/search | Search for flows |
| [**find5**](FlowsApi.md#find5) | **GET** /api/v1/flows/search | Search for flows |
| [**flowGraph1**](FlowsApi.md#flowGraph1) | **GET** /api/v1/flows/{namespace}/{id}/graph | Generate a graph for a flow |
| [**flowGraph3**](FlowsApi.md#flowGraph3) | **GET** /api/v1/{tenant}/flows/{namespace}/{id}/graph | Generate a graph for a flow |
| [**flowGraphSource**](FlowsApi.md#flowGraphSource) | **POST** /api/v1/flows/graph | Generate a graph for a flow source |
| [**flowGraphSource1**](FlowsApi.md#flowGraphSource1) | **POST** /api/v1/{tenant}/flows/graph | Generate a graph for a flow source |
| [**flowTask**](FlowsApi.md#flowTask) | **GET** /api/v1/flows/{namespace}/{id}/tasks/{taskId} | Get a flow task |
| [**flowTask1**](FlowsApi.md#flowTask1) | **GET** /api/v1/{tenant}/flows/{namespace}/{id}/tasks/{taskId} | Get a flow task |
| [**getFlowsByNamespace1**](FlowsApi.md#getFlowsByNamespace1) | **GET** /api/v1/flows/{namespace} | Retrieve all flows from a given namespace |
| [**getFlowsByNamespace3**](FlowsApi.md#getFlowsByNamespace3) | **GET** /api/v1/{tenant}/flows/{namespace} | Retrieve all flows from a given namespace |
| [**importFlows**](FlowsApi.md#importFlows) | **POST** /api/v1/flows/import |     Import flows as a ZIP archive of yaml sources or a multi-objects YAML file.     When sending a Yaml that contains one or more flows, a list of index is returned.     When sending a ZIP archive, a list of files that couldn&#39;t be imported is returned.  |
| [**importFlows1**](FlowsApi.md#importFlows1) | **POST** /api/v1/{tenant}/flows/import |     Import flows as a ZIP archive of yaml sources or a multi-objects YAML file.     When sending a Yaml that contains one or more flows, a list of index is returned.     When sending a ZIP archive, a list of files that couldn&#39;t be imported is returned.  |
| [**index24**](FlowsApi.md#index24) | **GET** /api/v1/{tenant}/flows/{namespace}/{id} | Get a flow |
| [**index3**](FlowsApi.md#index3) | **GET** /api/v1/flows/{namespace}/{id} | Get a flow |
| [**listDistinctNamespace1**](FlowsApi.md#listDistinctNamespace1) | **GET** /api/v1/flows/distinct-namespaces | List all distinct namespaces |
| [**listDistinctNamespace4**](FlowsApi.md#listDistinctNamespace4) | **GET** /api/v1/{tenant}/flows/distinct-namespaces | List all distinct namespaces |
| [**revisions**](FlowsApi.md#revisions) | **GET** /api/v1/flows/{namespace}/{id}/revisions | Get revisions for a flow |
| [**revisions1**](FlowsApi.md#revisions1) | **GET** /api/v1/{tenant}/flows/{namespace}/{id}/revisions | Get revisions for a flow |
| [**source**](FlowsApi.md#source) | **GET** /api/v1/flows/source | Search for flows source code |
| [**source1**](FlowsApi.md#source1) | **GET** /api/v1/{tenant}/flows/source | Search for flows source code |
| [**update21**](FlowsApi.md#update21) | **PUT** /api/v1/{tenant}/flows/{namespace}/{id} | Update a flow |
| [**update3**](FlowsApi.md#update3) | **PUT** /api/v1/flows/{namespace}/{id} | Update a flow |
| [**updateNamespace**](FlowsApi.md#updateNamespace) | **POST** /api/v1/flows/{namespace} | Update a complete namespace from json object |
| [**updateNamespace2**](FlowsApi.md#updateNamespace2) | **POST** /api/v1/{tenant}/flows/{namespace} | Update a complete namespace from json object |
| [**updateTask**](FlowsApi.md#updateTask) | **PATCH** /api/v1/flows/{namespace}/{id}/{taskId} | Update a single task on a flow |
| [**updateTask1**](FlowsApi.md#updateTask1) | **PATCH** /api/v1/{tenant}/flows/{namespace}/{id}/{taskId} | Update a single task on a flow |
| [**validateFlows**](FlowsApi.md#validateFlows) | **POST** /api/v1/flows/validate | Validate a list of flows |
| [**validateFlows1**](FlowsApi.md#validateFlows1) | **POST** /api/v1/{tenant}/flows/validate | Validate a list of flows |
| [**validateTask**](FlowsApi.md#validateTask) | **POST** /api/v1/flows/validate/task | Validate a list of flows |
| [**validateTask1**](FlowsApi.md#validateTask1) | **POST** /api/v1/{tenant}/flows/validate/task | Validate a list of flows |
| [**validateTrigger**](FlowsApi.md#validateTrigger) | **POST** /api/v1/flows/validate/trigger | Validate trigger |
| [**validateTrigger1**](FlowsApi.md#validateTrigger1) | **POST** /api/v1/{tenant}/flows/validate/trigger | Validate trigger |



## bulkUpdate

> List&lt;FlowWithSource&gt; bulkUpdate(delete, body)

Update from multiples yaml sources

All flow will be created / updated for this namespace. Flow that already created but not in &#x60;flows&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Boolean delete = true; // Boolean | If missing flow should be deleted
        String body = "body_example"; // String | 
        try {
            List<FlowWithSource> result = apiInstance.bulkUpdate(delete, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#bulkUpdate");
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
| **delete** | **Boolean**| If missing flow should be deleted | [default to true] |
| **body** | **String**|  | |

### Return type

[**List&lt;FlowWithSource&gt;**](FlowWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkUpdate 200 response |  -  |


## bulkUpdate1

> List&lt;FlowWithSource&gt; bulkUpdate1(delete, tenant, body)

Update from multiples yaml sources

All flow will be created / updated for this namespace. Flow that already created but not in &#x60;flows&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Boolean delete = true; // Boolean | If missing flow should be deleted
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            List<FlowWithSource> result = apiInstance.bulkUpdate1(delete, tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#bulkUpdate1");
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
| **delete** | **Boolean**| If missing flow should be deleted | [default to true] |
| **tenant** | **String**|  | |
| **body** | **String**|  | |

### Return type

[**List&lt;FlowWithSource&gt;**](FlowWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkUpdate_1 200 response |  -  |


## create30

> Create5200Response create30(tenant, flow)

Create a flow from json object

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Flow flow = new Flow(); // Flow | 
        try {
            Create5200Response result = apiInstance.create30(tenant, flow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#create30");
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
| **flow** | [**Flow**](Flow.md)|  | |

### Return type

[**Create5200Response**](Create5200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_30 200 response |  -  |


## create5

> Create5200Response create5(flow)

Create a flow from json object

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Flow flow = new Flow(); // Flow | 
        try {
            Create5200Response result = apiInstance.create5(flow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#create5");
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
| **flow** | [**Flow**](Flow.md)|  | |

### Return type

[**Create5200Response**](Create5200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_5 200 response |  -  |


## delete33

> delete33(namespace, id, tenant)

Delete a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete33(namespace, id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#delete33");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **tenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | delete_33 200 response |  -  |


## delete5

> delete5(namespace, id)

Delete a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        try {
            apiInstance.delete5(namespace, id);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#delete5");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | delete_5 200 response |  -  |


## deleteByIds1

> BulkResponse deleteByIds1(idWithNamespace)

Delete flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.deleteByIds1(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteByIds1");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByIds_1 200 response |  -  |


## deleteByIds4

> BulkResponse deleteByIds4(tenant, idWithNamespace)

Delete flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.deleteByIds4(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteByIds4");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByIds_4 200 response |  -  |


## deleteByQuery1

> BulkResponse deleteByQuery1(q, scope, namespace, labels)

Delete flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.deleteByQuery1(q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteByQuery1");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByQuery_1 200 response |  -  |


## deleteByQuery4

> BulkResponse deleteByQuery4(tenant, q, scope, namespace, labels)

Delete flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.deleteByQuery4(tenant, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#deleteByQuery4");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByQuery_4 200 response |  -  |


## dependencies

> FlowTopologyGraph dependencies(namespace, id, destinationOnly)

Get flow dependencies

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean destinationOnly = false; // Boolean | if true, list only destination dependencies, otherwise list also source dependencies
        try {
            FlowTopologyGraph result = apiInstance.dependencies(namespace, id, destinationOnly);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#dependencies");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **destinationOnly** | **Boolean**| if true, list only destination dependencies, otherwise list also source dependencies | [default to false] |

### Return type

[**FlowTopologyGraph**](FlowTopologyGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dependencies 200 response |  -  |


## dependencies1

> FlowTopologyGraph dependencies1(namespace, destinationOnly)

Get flow dependencies

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        Boolean destinationOnly = false; // Boolean | if true, list only destination dependencies, otherwise list also source dependencies
        try {
            FlowTopologyGraph result = apiInstance.dependencies1(namespace, destinationOnly);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#dependencies1");
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
| **namespace** | **String**| The flow namespace | |
| **destinationOnly** | **Boolean**| if true, list only destination dependencies, otherwise list also source dependencies | [default to false] |

### Return type

[**FlowTopologyGraph**](FlowTopologyGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dependencies_1 200 response |  -  |


## dependencies2

> FlowTopologyGraph dependencies2(namespace, id, destinationOnly, tenant)

Get flow dependencies

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean destinationOnly = false; // Boolean | if true, list only destination dependencies, otherwise list also source dependencies
        String tenant = "tenant_example"; // String | 
        try {
            FlowTopologyGraph result = apiInstance.dependencies2(namespace, id, destinationOnly, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#dependencies2");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **destinationOnly** | **Boolean**| if true, list only destination dependencies, otherwise list also source dependencies | [default to false] |
| **tenant** | **String**|  | |

### Return type

[**FlowTopologyGraph**](FlowTopologyGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dependencies_2 200 response |  -  |


## dependencies3

> FlowTopologyGraph dependencies3(namespace, destinationOnly, tenant)

Get flow dependencies

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        Boolean destinationOnly = false; // Boolean | if true, list only destination dependencies, otherwise list also source dependencies
        String tenant = "tenant_example"; // String | 
        try {
            FlowTopologyGraph result = apiInstance.dependencies3(namespace, destinationOnly, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#dependencies3");
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
| **namespace** | **String**| The flow namespace | |
| **destinationOnly** | **Boolean**| if true, list only destination dependencies, otherwise list also source dependencies | [default to false] |
| **tenant** | **String**|  | |

### Return type

[**FlowTopologyGraph**](FlowTopologyGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dependencies_3 200 response |  -  |


## disableByIds

> BulkResponse disableByIds(idWithNamespace)

Disable flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.disableByIds(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#disableByIds");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disableByIds 200 response |  -  |


## disableByIds1

> BulkResponse disableByIds1(tenant, idWithNamespace)

Disable flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.disableByIds1(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#disableByIds1");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disableByIds_1 200 response |  -  |


## disableByQuery

> BulkResponse disableByQuery(q, scope, namespace, labels)

Disable flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.disableByQuery(q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#disableByQuery");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disableByQuery 200 response |  -  |


## disableByQuery1

> BulkResponse disableByQuery1(tenant, q, scope, namespace, labels)

Disable flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.disableByQuery1(tenant, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#disableByQuery1");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disableByQuery_1 200 response |  -  |


## enableByIds

> BulkResponse enableByIds(idWithNamespace)

Enable flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.enableByIds(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#enableByIds");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enableByIds 200 response |  -  |


## enableByIds1

> BulkResponse enableByIds1(tenant, idWithNamespace)

Enable flows by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.enableByIds1(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#enableByIds1");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enableByIds_1 200 response |  -  |


## enableByQuery

> BulkResponse enableByQuery(q, scope, namespace, labels)

Enable flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.enableByQuery(q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#enableByQuery");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enableByQuery 200 response |  -  |


## enableByQuery1

> BulkResponse enableByQuery1(tenant, q, scope, namespace, labels)

Enable flows returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            BulkResponse result = apiInstance.enableByQuery1(tenant, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#enableByQuery1");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enableByQuery_1 200 response |  -  |


## exportByIds

> List&lt;byte[]&gt; exportByIds(idWithNamespace)

Export flows as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            List<byte[]> result = apiInstance.exportByIds(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#exportByIds");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByIds 200 response |  -  |


## exportByIds2

> List&lt;byte[]&gt; exportByIds2(tenant, idWithNamespace)

Export flows as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            List<byte[]> result = apiInstance.exportByIds2(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#exportByIds2");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByIds_2 200 response |  -  |


## exportByQuery

> List&lt;byte[]&gt; exportByQuery(q, scope, namespace, labels)

Export flows as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            List<byte[]> result = apiInstance.exportByQuery(q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#exportByQuery");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByQuery 200 response |  -  |


## exportByQuery2

> List&lt;byte[]&gt; exportByQuery2(tenant, q, scope, namespace, labels)

Export flows as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            List<byte[]> result = apiInstance.exportByQuery2(tenant, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#exportByQuery2");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByQuery_2 200 response |  -  |


## find31

> PagedResultsFlow find31(page, size, tenant, sort, q, scope, namespace, labels)

Search for flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            PagedResultsFlow result = apiInstance.find31(page, size, tenant, sort, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#find31");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**PagedResultsFlow**](PagedResultsFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_31 200 response |  -  |


## find5

> PagedResultsFlow find5(page, size, sort, q, scope, namespace, labels)

Search for flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the flows to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        try {
            PagedResultsFlow result = apiInstance.find5(page, size, sort, q, scope, namespace, labels);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#find5");
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
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the flows to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |

### Return type

[**PagedResultsFlow**](PagedResultsFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_5 200 response |  -  |


## flowGraph1

> FlowGraph flowGraph1(namespace, id, revision, subflows)

Generate a graph for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Integer revision = 56; // Integer | The flow revision
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraph1(namespace, id, revision, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowGraph1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **revision** | **Integer**| The flow revision | [optional] |
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraph_1 200 response |  -  |


## flowGraph3

> FlowGraph flowGraph3(namespace, id, tenant, revision, subflows)

Generate a graph for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | The flow revision
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraph3(namespace, id, tenant, revision, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowGraph3");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **tenant** | **String**|  | |
| **revision** | **Integer**| The flow revision | [optional] |
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraph_3 200 response |  -  |


## flowGraphSource

> FlowGraph flowGraphSource(body, subflows)

Generate a graph for a flow source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String body = "body_example"; // String | 
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraphSource(body, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowGraphSource");
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
| **body** | **String**|  | |
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraphSource 200 response |  -  |


## flowGraphSource1

> FlowGraph flowGraphSource1(tenant, body, subflows)

Generate a graph for a flow source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraphSource1(tenant, body, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowGraphSource1");
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
| **body** | **String**|  | |
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraphSource_1 200 response |  -  |


## flowTask

> Task flowTask(namespace, id, taskId, revision)

Get a flow task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String taskId = "taskId_example"; // String | The task id
        Integer revision = 56; // Integer | The flow revision
        try {
            Task result = apiInstance.flowTask(namespace, id, taskId, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowTask");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **taskId** | **String**| The task id | |
| **revision** | **Integer**| The flow revision | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowTask 200 response |  -  |


## flowTask1

> Task flowTask1(namespace, id, taskId, tenant, revision)

Get a flow task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String taskId = "taskId_example"; // String | The task id
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | The flow revision
        try {
            Task result = apiInstance.flowTask1(namespace, id, taskId, tenant, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#flowTask1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **taskId** | **String**| The task id | |
| **tenant** | **String**|  | |
| **revision** | **Integer**| The flow revision | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowTask_1 200 response |  -  |


## getFlowsByNamespace1

> List&lt;Flow&gt; getFlowsByNamespace1(namespace)

Retrieve all flows from a given namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | Namespace to filter flows
        try {
            List<Flow> result = apiInstance.getFlowsByNamespace1(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlowsByNamespace1");
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
| **namespace** | **String**| Namespace to filter flows | |

### Return type

[**List&lt;Flow&gt;**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowsByNamespace_1 200 response |  -  |


## getFlowsByNamespace3

> List&lt;Flow&gt; getFlowsByNamespace3(namespace, tenant)

Retrieve all flows from a given namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | Namespace to filter flows
        String tenant = "tenant_example"; // String | 
        try {
            List<Flow> result = apiInstance.getFlowsByNamespace3(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#getFlowsByNamespace3");
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
| **namespace** | **String**| Namespace to filter flows | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;Flow&gt;**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowsByNamespace_3 200 response |  -  |


## importFlows

> List&lt;String&gt; importFlows(fileUpload)

    Import flows as a ZIP archive of yaml sources or a multi-objects YAML file.     When sending a Yaml that contains one or more flows, a list of index is returned.     When sending a ZIP archive, a list of files that couldn&#39;t be imported is returned. 

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        File fileUpload = new File("/path/to/file"); // File | The file to import, can be a ZIP archive or a multi-objects YAML file
        try {
            List<String> result = apiInstance.importFlows(fileUpload);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#importFlows");
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
| **fileUpload** | **File**| The file to import, can be a ZIP archive or a multi-objects YAML file | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | importFlows 200 response |  -  |


## importFlows1

> List&lt;String&gt; importFlows1(tenant, fileUpload)

    Import flows as a ZIP archive of yaml sources or a multi-objects YAML file.     When sending a Yaml that contains one or more flows, a list of index is returned.     When sending a ZIP archive, a list of files that couldn&#39;t be imported is returned. 

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        File fileUpload = new File("/path/to/file"); // File | The file to import, can be a ZIP archive or a multi-objects YAML file
        try {
            List<String> result = apiInstance.importFlows1(tenant, fileUpload);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#importFlows1");
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
| **fileUpload** | **File**| The file to import, can be a ZIP archive or a multi-objects YAML file | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | importFlows_1 200 response |  -  |


## index24

> Object index24(namespace, id, source, allowDeleted, tenant, revision)

Get a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean source = false; // Boolean | Include the source code
        Boolean allowDeleted = false; // Boolean | Get flow even if deleted
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | Get latest revision by default
        try {
            Object result = apiInstance.index24(namespace, id, source, allowDeleted, tenant, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#index24");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **source** | **Boolean**| Include the source code | [default to false] |
| **allowDeleted** | **Boolean**| Get flow even if deleted | [default to false] |
| **tenant** | **String**|  | |
| **revision** | **Integer**| Get latest revision by default | [optional] |

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
| **200** | index_24 200 response |  -  |


## index3

> Object index3(namespace, id, source, allowDeleted, revision)

Get a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean source = false; // Boolean | Include the source code
        Boolean allowDeleted = false; // Boolean | Get flow even if deleted
        Integer revision = 56; // Integer | Get latest revision by default
        try {
            Object result = apiInstance.index3(namespace, id, source, allowDeleted, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#index3");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **source** | **Boolean**| Include the source code | [default to false] |
| **allowDeleted** | **Boolean**| Get flow even if deleted | [default to false] |
| **revision** | **Integer**| Get latest revision by default | [optional] |

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
| **200** | index_3 200 response |  -  |


## listDistinctNamespace1

> List&lt;String&gt; listDistinctNamespace1(q)

List all distinct namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        try {
            List<String> result = apiInstance.listDistinctNamespace1(q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listDistinctNamespace1");
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
| **q** | **String**| A string filter | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listDistinctNamespace_1 200 response |  -  |


## listDistinctNamespace4

> List&lt;String&gt; listDistinctNamespace4(tenant, q)

List all distinct namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        try {
            List<String> result = apiInstance.listDistinctNamespace4(tenant, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#listDistinctNamespace4");
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
| **q** | **String**| A string filter | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listDistinctNamespace_4 200 response |  -  |


## revisions

> List&lt;FlowWithSource&gt; revisions(namespace, id)

Get revisions for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        try {
            List<FlowWithSource> result = apiInstance.revisions(namespace, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#revisions");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |

### Return type

[**List&lt;FlowWithSource&gt;**](FlowWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | revisions 200 response |  -  |


## revisions1

> List&lt;FlowWithSource&gt; revisions1(namespace, id, tenant)

Get revisions for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String tenant = "tenant_example"; // String | 
        try {
            List<FlowWithSource> result = apiInstance.revisions1(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#revisions1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;FlowWithSource&gt;**](FlowWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | revisions_1 200 response |  -  |


## source

> PagedResultsSearchResultFlow source(page, size, sort, q, namespace)

Search for flows source code

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            PagedResultsSearchResultFlow result = apiInstance.source(page, size, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#source");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**PagedResultsSearchResultFlow**](PagedResultsSearchResultFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source 200 response |  -  |


## source1

> PagedResultsSearchResultFlow source1(page, size, tenant, sort, q, namespace)

Search for flows source code

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            PagedResultsSearchResultFlow result = apiInstance.source1(page, size, tenant, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#source1");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**PagedResultsSearchResultFlow**](PagedResultsSearchResultFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source_1 200 response |  -  |


## update21

> Update3200Response update21(tenant, namespace, id, body)

Update a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String body = "body_example"; // String | 
        try {
            Update3200Response result = apiInstance.update21(tenant, namespace, id, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#update21");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **body** | **String**|  | |

### Return type

[**Update3200Response**](Update3200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_21 200 response |  -  |


## update3

> Update3200Response update3(namespace, id, body)

Update a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String body = "body_example"; // String | 
        try {
            Update3200Response result = apiInstance.update3(namespace, id, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#update3");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **body** | **String**|  | |

### Return type

[**Update3200Response**](Update3200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_3 200 response |  -  |


## updateNamespace

> UpdateNamespace200Response updateNamespace(namespace, delete, flow)

Update a complete namespace from json object

All flow will be created / updated for this namespace. Flow that already created but not in &#x60;flows&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        Boolean delete = true; // Boolean | If missing flow should be deleted
        List<Flow> flow = Arrays.asList(); // List<Flow> | 
        try {
            UpdateNamespace200Response result = apiInstance.updateNamespace(namespace, delete, flow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateNamespace");
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
| **namespace** | **String**| The flow namespace | |
| **delete** | **Boolean**| If missing flow should be deleted | [default to true] |
| **flow** | [**List&lt;Flow&gt;**](Flow.md)|  | |

### Return type

[**UpdateNamespace200Response**](UpdateNamespace200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateNamespace 200 response |  -  |


## updateNamespace2

> UpdateNamespace200Response updateNamespace2(tenant, namespace, delete, flow)

Update a complete namespace from json object

All flow will be created / updated for this namespace. Flow that already created but not in &#x60;flows&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String namespace = "namespace_example"; // String | The flow namespace
        Boolean delete = true; // Boolean | If missing flow should be deleted
        List<Flow> flow = Arrays.asList(); // List<Flow> | 
        try {
            UpdateNamespace200Response result = apiInstance.updateNamespace2(tenant, namespace, delete, flow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateNamespace2");
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
| **namespace** | **String**| The flow namespace | |
| **delete** | **Boolean**| If missing flow should be deleted | [default to true] |
| **flow** | [**List&lt;Flow&gt;**](Flow.md)|  | |

### Return type

[**UpdateNamespace200Response**](UpdateNamespace200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateNamespace_2 200 response |  -  |


## updateTask

> Flow updateTask(namespace, id, taskId, task)

Update a single task on a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String taskId = "taskId_example"; // String | The task id
        Task task = new Task(); // Task | 
        try {
            Flow result = apiInstance.updateTask(namespace, id, taskId, task);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateTask");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **taskId** | **String**| The task id | |
| **task** | [**Task**](Task.md)|  | |

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateTask 200 response |  -  |


## updateTask1

> Flow updateTask1(namespace, id, taskId, tenant, task)

Update a single task on a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String taskId = "taskId_example"; // String | The task id
        String tenant = "tenant_example"; // String | 
        Task task = new Task(); // Task | 
        try {
            Flow result = apiInstance.updateTask1(namespace, id, taskId, tenant, task);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#updateTask1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **taskId** | **String**| The task id | |
| **tenant** | **String**|  | |
| **task** | [**Task**](Task.md)|  | |

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateTask_1 200 response |  -  |


## validateFlows

> List&lt;ValidateConstraintViolation&gt; validateFlows(body)

Validate a list of flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            List<ValidateConstraintViolation> result = apiInstance.validateFlows(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateFlows");
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
| **body** | **String**|  | |

### Return type

[**List&lt;ValidateConstraintViolation&gt;**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateFlows 200 response |  -  |


## validateFlows1

> List&lt;ValidateConstraintViolation&gt; validateFlows1(tenant, body)

Validate a list of flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            List<ValidateConstraintViolation> result = apiInstance.validateFlows1(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateFlows1");
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
| **body** | **String**|  | |

### Return type

[**List&lt;ValidateConstraintViolation&gt;**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateFlows_1 200 response |  -  |


## validateTask

> ValidateConstraintViolation validateTask(section, body)

Validate a list of flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        FlowControllerTaskValidationType section = FlowControllerTaskValidationType.fromValue("TASKS"); // FlowControllerTaskValidationType | Type of task
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validateTask(section, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateTask");
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
| **section** | [**FlowControllerTaskValidationType**](.md)| Type of task | [enum: TASKS, TRIGGERS] |
| **body** | **String**|  | |

### Return type

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml, application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTask 200 response |  -  |


## validateTask1

> ValidateConstraintViolation validateTask1(tenant, section, body)

Validate a list of flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        FlowControllerTaskValidationType section = FlowControllerTaskValidationType.fromValue("TASKS"); // FlowControllerTaskValidationType | Type of task
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validateTask1(tenant, section, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateTask1");
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
| **section** | [**FlowControllerTaskValidationType**](.md)| Type of task | [enum: TASKS, TRIGGERS] |
| **body** | **String**|  | |

### Return type

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml, application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTask_1 200 response |  -  |


## validateTrigger

> ValidateConstraintViolation validateTrigger(body)

Validate trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validateTrigger(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateTrigger");
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
| **body** | **String**|  | |

### Return type

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTrigger 200 response |  -  |


## validateTrigger1

> ValidateConstraintViolation validateTrigger1(tenant, body)

Validate trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FlowsApi apiInstance = new FlowsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validateTrigger1(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FlowsApi#validateTrigger1");
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
| **body** | **String**|  | |

### Return type

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTrigger_1 200 response |  -  |

