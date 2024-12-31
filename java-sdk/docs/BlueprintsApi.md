# BlueprintsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blueprint**](BlueprintsApi.md#blueprint) | **GET** /api/v1/blueprints/community/{id} | Get a blueprint |
| [**blueprint1**](BlueprintsApi.md#blueprint1) | **GET** /api/v1/{tenant}/blueprints/community/{id} | Get a blueprint |
| [**blueprintFlow**](BlueprintsApi.md#blueprintFlow) | **GET** /api/v1/blueprints/community/{id}/flow | Get a blueprint flow |
| [**blueprintFlow1**](BlueprintsApi.md#blueprintFlow1) | **GET** /api/v1/{tenant}/blueprints/community/{id}/flow | Get a blueprint flow |
| [**blueprintGraph**](BlueprintsApi.md#blueprintGraph) | **GET** /api/v1/blueprints/community/{id}/graph | Get a blueprint graph |
| [**blueprintGraph1**](BlueprintsApi.md#blueprintGraph1) | **GET** /api/v1/{tenant}/blueprints/community/{id}/graph | Get a blueprint graph |
| [**blueprints**](BlueprintsApi.md#blueprints) | **GET** /api/v1/blueprints/community | List all blueprints |
| [**blueprints1**](BlueprintsApi.md#blueprints1) | **GET** /api/v1/{tenant}/blueprints/community | List all blueprints |
| [**createInternalBlueprints**](BlueprintsApi.md#createInternalBlueprints) | **POST** /api/v1/blueprints/custom | Create a new internal blueprint |
| [**createInternalBlueprints1**](BlueprintsApi.md#createInternalBlueprints1) | **POST** /api/v1/{tenant}/blueprints/custom | Create a new internal blueprint |
| [**internalBlueprint**](BlueprintsApi.md#internalBlueprint) | **GET** /api/v1/blueprints/custom/{id} | Get an internal blueprint |
| [**internalBlueprint1**](BlueprintsApi.md#internalBlueprint1) | **GET** /api/v1/{tenant}/blueprints/custom/{id} | Get an internal blueprint |
| [**internalBlueprintFlow**](BlueprintsApi.md#internalBlueprintFlow) | **GET** /api/v1/blueprints/custom/{id}/flow | Get an internal blueprint flow |
| [**internalBlueprintFlow1**](BlueprintsApi.md#internalBlueprintFlow1) | **GET** /api/v1/{tenant}/blueprints/custom/{id}/flow | Get an internal blueprint flow |
| [**internalBlueprints**](BlueprintsApi.md#internalBlueprints) | **GET** /api/v1/blueprints/custom | List all internal blueprints |
| [**internalBlueprints1**](BlueprintsApi.md#internalBlueprints1) | **DELETE** /api/v1/blueprints/custom/{id} | Delete an internal blueprint |
| [**internalBlueprints2**](BlueprintsApi.md#internalBlueprints2) | **GET** /api/v1/{tenant}/blueprints/custom | List all internal blueprints |
| [**internalBlueprints3**](BlueprintsApi.md#internalBlueprints3) | **DELETE** /api/v1/{tenant}/blueprints/custom/{id} | Delete an internal blueprint |
| [**updateInternalBlueprints**](BlueprintsApi.md#updateInternalBlueprints) | **PUT** /api/v1/blueprints/custom/{id} | Update an internal blueprint |
| [**updateInternalBlueprints1**](BlueprintsApi.md#updateInternalBlueprints1) | **PUT** /api/v1/{tenant}/blueprints/custom/{id} | Update an internal blueprint |



## blueprint

> BlueprintControllerBlueprintItemWithFlow blueprint(id)

Get a blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        try {
            BlueprintControllerBlueprintItemWithFlow result = apiInstance.blueprint(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprint");
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

### Return type

[**BlueprintControllerBlueprintItemWithFlow**](BlueprintControllerBlueprintItemWithFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprint 200 response |  -  |


## blueprint1

> BlueprintControllerBlueprintItemWithFlow blueprint1(id, tenant)

Get a blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            BlueprintControllerBlueprintItemWithFlow result = apiInstance.blueprint1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprint1");
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

[**BlueprintControllerBlueprintItemWithFlow**](BlueprintControllerBlueprintItemWithFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprint_1 200 response |  -  |


## blueprintFlow

> String blueprintFlow(id)

Get a blueprint flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        try {
            String result = apiInstance.blueprintFlow(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprintFlow");
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
| **200** | blueprintFlow 200 response |  -  |


## blueprintFlow1

> String blueprintFlow1(id, tenant)

Get a blueprint flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            String result = apiInstance.blueprintFlow1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprintFlow1");
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
| **200** | blueprintFlow_1 200 response |  -  |


## blueprintGraph

> Map&lt;String, Object&gt; blueprintGraph(id)

Get a blueprint graph

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        try {
            Map<String, Object> result = apiInstance.blueprintGraph(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprintGraph");
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
| **200** | blueprintGraph 200 response |  -  |


## blueprintGraph1

> Map&lt;String, Object&gt; blueprintGraph1(id, tenant)

Get a blueprint graph

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, Object> result = apiInstance.blueprintGraph1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprintGraph1");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprintGraph_1 200 response |  -  |


## blueprints

> PagedResultsBlueprintControllerBlueprintItem blueprints(page, size, q, sort, tags)

List all blueprints

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 1; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        String sort = "sort_example"; // String | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        try {
            PagedResultsBlueprintControllerBlueprintItem result = apiInstance.blueprints(page, size, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprints");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | **String**| The sort of current page | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| A tags filter | [optional] |

### Return type

[**PagedResultsBlueprintControllerBlueprintItem**](PagedResultsBlueprintControllerBlueprintItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprints 200 response |  -  |


## blueprints1

> PagedResultsBlueprintControllerBlueprintItem blueprints1(page, size, tenant, q, sort, tags)

List all blueprints

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

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
            PagedResultsBlueprintControllerBlueprintItem result = apiInstance.blueprints1(page, size, tenant, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#blueprints1");
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

[**PagedResultsBlueprintControllerBlueprintItem**](PagedResultsBlueprintControllerBlueprintItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprints_1 200 response |  -  |


## createInternalBlueprints

> BlueprintWithFlow createInternalBlueprints(blueprintWithFlow)

Create a new internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        BlueprintWithFlow blueprintWithFlow = new BlueprintWithFlow(); // BlueprintWithFlow | 
        try {
            BlueprintWithFlow result = apiInstance.createInternalBlueprints(blueprintWithFlow);
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
| **blueprintWithFlow** | [**BlueprintWithFlow**](BlueprintWithFlow.md)|  | |

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
| **200** | createInternalBlueprints 200 response |  -  |


## createInternalBlueprints1

> BlueprintWithFlow createInternalBlueprints1(tenant, blueprintWithFlow)

Create a new internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        BlueprintWithFlow blueprintWithFlow = new BlueprintWithFlow(); // BlueprintWithFlow | 
        try {
            BlueprintWithFlow result = apiInstance.createInternalBlueprints1(tenant, blueprintWithFlow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#createInternalBlueprints1");
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
| **blueprintWithFlow** | [**BlueprintWithFlow**](BlueprintWithFlow.md)|  | |

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
| **200** | createInternalBlueprints_1 200 response |  -  |


## internalBlueprint

> BlueprintWithFlow internalBlueprint(id)

Get an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        try {
            BlueprintWithFlow result = apiInstance.internalBlueprint(id);
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

### Return type

[**BlueprintWithFlow**](BlueprintWithFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | internalBlueprint 200 response |  -  |


## internalBlueprint1

> BlueprintWithFlow internalBlueprint1(id, tenant)

Get an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            BlueprintWithFlow result = apiInstance.internalBlueprint1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprint1");
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

[**BlueprintWithFlow**](BlueprintWithFlow.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | internalBlueprint_1 200 response |  -  |


## internalBlueprintFlow

> String internalBlueprintFlow(id)

Get an internal blueprint flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        try {
            String result = apiInstance.internalBlueprintFlow(id);
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


## internalBlueprintFlow1

> String internalBlueprintFlow1(id, tenant)

Get an internal blueprint flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The blueprint id
        String tenant = "tenant_example"; // String | 
        try {
            String result = apiInstance.internalBlueprintFlow1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprintFlow1");
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
| **200** | internalBlueprintFlow_1 200 response |  -  |


## internalBlueprints

> PagedResultsBlueprint internalBlueprints(page, size, q, sort, tags)

List all internal blueprints

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 1; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        String sort = "sort_example"; // String | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        try {
            PagedResultsBlueprint result = apiInstance.internalBlueprints(page, size, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprints");
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
| **200** | internalBlueprints 200 response |  -  |


## internalBlueprints1

> internalBlueprints1(id)

Delete an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The internal blueprint id to delete
        try {
            apiInstance.internalBlueprints1(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprints1");
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
| **200** | internalBlueprints_1 200 response |  -  |


## internalBlueprints2

> PagedResultsBlueprint internalBlueprints2(page, size, tenant, q, sort, tags)

List all internal blueprints

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

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
            PagedResultsBlueprint result = apiInstance.internalBlueprints2(page, size, tenant, q, sort, tags);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprints2");
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
| **200** | internalBlueprints_2 200 response |  -  |


## internalBlueprints3

> internalBlueprints3(id, tenant)

Delete an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The internal blueprint id to delete
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.internalBlueprints3(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#internalBlueprints3");
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
| **200** | internalBlueprints_3 200 response |  -  |


## updateInternalBlueprints

> BlueprintWithFlow updateInternalBlueprints(id, blueprintWithFlow)

Update an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The id of the internal blueprint to update
        BlueprintWithFlow blueprintWithFlow = new BlueprintWithFlow(); // BlueprintWithFlow | 
        try {
            BlueprintWithFlow result = apiInstance.updateInternalBlueprints(id, blueprintWithFlow);
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
| **blueprintWithFlow** | [**BlueprintWithFlow**](BlueprintWithFlow.md)|  | |

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


## updateInternalBlueprints1

> BlueprintWithFlow updateInternalBlueprints1(id, tenant, blueprintWithFlow)

Update an internal blueprint

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintsApi apiInstance = new BlueprintsApi(defaultClient);
        String id = "id_example"; // String | The id of the internal blueprint to update
        String tenant = "tenant_example"; // String | 
        BlueprintWithFlow blueprintWithFlow = new BlueprintWithFlow(); // BlueprintWithFlow | 
        try {
            BlueprintWithFlow result = apiInstance.updateInternalBlueprints1(id, tenant, blueprintWithFlow);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintsApi#updateInternalBlueprints1");
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
| **blueprintWithFlow** | [**BlueprintWithFlow**](BlueprintWithFlow.md)|  | |

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
| **200** | updateInternalBlueprints_1 200 response |  -  |

