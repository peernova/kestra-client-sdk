# BlueprintsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInternalBlueprints**](BlueprintsApi.md#createInternalBlueprints) | **POST** /api/v1/{tenant}/blueprints/custom | Create a new internal blueprint |
| [**deleteInternalBlueprints**](BlueprintsApi.md#deleteInternalBlueprints) | **DELETE** /api/v1/{tenant}/blueprints/custom/{id} | Delete an internal blueprint |
| [**getBlueprint**](BlueprintsApi.md#getBlueprint) | **GET** /api/v1/{tenant}/blueprints/community/{kind}/{id} | Retrieve a blueprint |
| [**getBlueprintGraph**](BlueprintsApi.md#getBlueprintGraph) | **GET** /api/v1/{tenant}/blueprints/community/{kind}/{id}/graph | Retrieve a blueprint graph |
| [**getBlueprintSource**](BlueprintsApi.md#getBlueprintSource) | **GET** /api/v1/{tenant}/blueprints/community/{kind}/{id}/source | Retrieve a blueprint source code |
| [**internalBlueprint**](BlueprintsApi.md#internalBlueprint) | **GET** /api/v1/{tenant}/blueprints/custom/{id} | Retrieve an internal blueprint |
| [**internalBlueprintFlow**](BlueprintsApi.md#internalBlueprintFlow) | **GET** /api/v1/{tenant}/blueprints/custom/{id}/source | Retrieve an internal blueprint source code |
| [**searchBlueprints**](BlueprintsApi.md#searchBlueprints) | **GET** /api/v1/{tenant}/blueprints/community/{kind} | List all blueprints |
| [**searchInternalBlueprints**](BlueprintsApi.md#searchInternalBlueprints) | **GET** /api/v1/{tenant}/blueprints/custom | List all internal blueprints |
| [**updateInternalBlueprints**](BlueprintsApi.md#updateInternalBlueprints) | **PUT** /api/v1/{tenant}/blueprints/custom/{id} | Update an internal blueprint |



## createInternalBlueprints

> BlueprintControllerApiBlueprintItemWithSource createInternalBlueprints(tenant, blueprintControllerApiBlueprintItemWithSource)

Create a new internal blueprint

Creates a new internal (custom) blueprint for the current tenant. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        BlueprintControllerApiBlueprintItemWithSource blueprintControllerApiBlueprintItemWithSource = new BlueprintControllerApiBlueprintItemWithSource(); // BlueprintControllerApiBlueprintItemWithSource | The internal blueprint to create
        try {
            BlueprintControllerApiBlueprintItemWithSource result = apiInstance.createInternalBlueprints(tenant, blueprintControllerApiBlueprintItemWithSource);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#createInternalBlueprints");
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
| **blueprintControllerApiBlueprintItemWithSource** | [**BlueprintControllerApiBlueprintItemWithSource**](BlueprintControllerApiBlueprintItemWithSource.md)| The internal blueprint to create | |

### Return type

[**BlueprintControllerApiBlueprintItemWithSource**](BlueprintControllerApiBlueprintItemWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createInternalBlueprints 200 response |  -  |


## deleteInternalBlueprints

> deleteInternalBlueprints(id, tenant)

Delete an internal blueprint

Deletes an internal (custom) blueprint for the current tenant. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The internal blueprint id to delete
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.deleteInternalBlueprints(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#deleteInternalBlueprints");
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
| **id** | **String**| The internal blueprint id to delete | |
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
| **200** | deleteInternalBlueprints 200 response |  -  |


## getBlueprint

> BlueprintControllerApiBlueprintItemWithSource getBlueprint(id, kind, tenant)

Retrieve a blueprint

Retrieves details of a specific community blueprint.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        BlueprintControllerKind kind = BlueprintControllerKind.fromValue("APP"); // BlueprintControllerKind | The blueprint kind
        String tenant = "tenant_example"; // String | 
        try {
            BlueprintControllerApiBlueprintItemWithSource result = apiInstance.getBlueprint(id, kind, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#getBlueprint");
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
| **id** | **String**| The blueprint id | |
| **kind** | [**BlueprintControllerKind**](.md)| The blueprint kind | [enum: APP, DASHBOARD, FLOW] |
| **tenant** | **String**|  | |

### Return type

[**BlueprintControllerApiBlueprintItemWithSource**](BlueprintControllerApiBlueprintItemWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBlueprint 200 response |  -  |


## getBlueprintGraph

> Map&lt;String, Object&gt; getBlueprintGraph(id, kind, tenant)

Retrieve a blueprint graph

Retrieves the topology graph representation of a specific community blueprint.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        BlueprintControllerKind kind = BlueprintControllerKind.fromValue("APP"); // BlueprintControllerKind | The blueprint kind
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, Object> result = apiInstance.getBlueprintGraph(id, kind, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#getBlueprintGraph");
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
| **id** | **String**| The blueprint id | |
| **kind** | [**BlueprintControllerKind**](.md)| The blueprint kind | [enum: APP, DASHBOARD, FLOW] |
| **tenant** | **String**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBlueprintGraph 200 response |  -  |


## getBlueprintSource

> String getBlueprintSource(id, kind, tenant)

Retrieve a blueprint source code

Retrieves the YAML source code for a specific community blueprint.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        BlueprintControllerKind kind = BlueprintControllerKind.fromValue("APP"); // BlueprintControllerKind | The blueprint kind
        String tenant = "tenant_example"; // String | 
        try {
            String result = apiInstance.getBlueprintSource(id, kind, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#getBlueprintSource");
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
| **id** | **String**| The blueprint id | |
| **kind** | [**BlueprintControllerKind**](.md)| The blueprint kind | [enum: APP, DASHBOARD, FLOW] |
| **tenant** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/yaml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBlueprintSource 200 response |  -  |


## internalBlueprint

> BlueprintControllerApiBlueprintItemWithSource internalBlueprint(id, tenant)

Retrieve an internal blueprint

Retrieves details of a specific internal (custom) blueprint. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            BlueprintControllerApiBlueprintItemWithSource result = apiInstance.internalBlueprint(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprint");
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
| **id** | **String**| The blueprint id | |
| **tenant** | **String**|  | |

### Return type

[**BlueprintControllerApiBlueprintItemWithSource**](BlueprintControllerApiBlueprintItemWithSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | internalBlueprint 200 response |  -  |


## internalBlueprintFlow

> String internalBlueprintFlow(id, tenant)

Retrieve an internal blueprint source code

Retrieves the YAML source code for a specific internal (custom) blueprint. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            String result = apiInstance.internalBlueprintFlow(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprintFlow");
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
| **id** | **String**| The blueprint id | |
| **tenant** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/yaml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | internalBlueprintFlow 200 response |  -  |


## searchBlueprints

> PagedResultsBlueprintControllerApiBlueprintItem searchBlueprints(page, size, kind, tenant, q, sort, tags)

List all blueprints

Lists all community blueprints of the specified kind. Community blueprints are shared and versioned.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 1; // Integer | The current page size
        BlueprintControllerKind kind = BlueprintControllerKind.fromValue("APP"); // BlueprintControllerKind | The blueprint kind
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String sort = "sort_example"; // String | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        try {
            PagedResultsBlueprintControllerApiBlueprintItem result = apiInstance.searchBlueprints(page, size, kind, tenant, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#searchBlueprints");
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
| **size** | **Integer**| The current page size | [default to 1] |
| **kind** | [**BlueprintControllerKind**](.md)| The blueprint kind | [enum: APP, DASHBOARD, FLOW] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | **String**| The sort of current page | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| A tags filter | [optional] |

### Return type

[**PagedResultsBlueprintControllerApiBlueprintItem**](PagedResultsBlueprintControllerApiBlueprintItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchBlueprints 200 response |  -  |


## searchInternalBlueprints

> PagedResultsBlueprint searchInternalBlueprints(page, size, tenant, q, sort, tags)

List all internal blueprints

Lists all internal (custom) blueprints for the current tenant. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 1; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String sort = "sort_example"; // String | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        try {
            PagedResultsBlueprint result = apiInstance.searchInternalBlueprints(page, size, tenant, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#searchInternalBlueprints");
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
| **size** | **Integer**| The current page size | [default to 1] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | **String**| The sort of current page | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| A tags filter | [optional] |

### Return type

[**PagedResultsBlueprint**](PagedResultsBlueprint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchInternalBlueprints 200 response |  -  |


## updateInternalBlueprints

> BlueprintWithFlow updateInternalBlueprints(id, tenant, blueprintControllerApiBlueprintItemWithSource)

Update an internal blueprint

Updates an existing internal (custom) blueprint for the current tenant. Requires BLUEPRINT permission.

### Example

```java
// Import classes:
import io.kestra.sdk.internal.ApiClient;
import io.kestra.sdk.internal.ApiException;
import io.kestra.sdk.internal.Configuration;
import io.kestra.sdk.internal.models.*;
import io.kestra.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The id of the internal blueprint to update
        String tenant = "tenant_example"; // String | 
        BlueprintControllerApiBlueprintItemWithSource blueprintControllerApiBlueprintItemWithSource = new BlueprintControllerApiBlueprintItemWithSource(); // BlueprintControllerApiBlueprintItemWithSource | The new internal blueprint for update
        try {
            BlueprintWithFlow result = apiInstance.updateInternalBlueprints(id, tenant, blueprintControllerApiBlueprintItemWithSource);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#updateInternalBlueprints");
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
| **id** | **String**| The id of the internal blueprint to update | |
| **tenant** | **String**|  | |
| **blueprintControllerApiBlueprintItemWithSource** | [**BlueprintControllerApiBlueprintItemWithSource**](BlueprintControllerApiBlueprintItemWithSource.md)| The new internal blueprint for update | |

### Return type

[**BlueprintWithFlow**](BlueprintWithFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateInternalBlueprints 200 response |  -  |

