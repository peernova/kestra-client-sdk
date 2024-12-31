# TriggersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteBackfill**](TriggersApi.md#deleteBackfill) | **POST** /api/v1/triggers/backfill/delete | Delete a backfill |
| [**deleteBackfill1**](TriggersApi.md#deleteBackfill1) | **POST** /api/v1/{tenant}/triggers/backfill/delete | Delete a backfill |
| [**deleteBackfillByIds**](TriggersApi.md#deleteBackfillByIds) | **POST** /api/v1/triggers/backfill/delete/by-triggers | Delete backfill for given triggers |
| [**deleteBackfillByIds1**](TriggersApi.md#deleteBackfillByIds1) | **POST** /api/v1/{tenant}/triggers/backfill/delete/by-triggers | Delete backfill for given triggers |
| [**deleteBackfillByQuery**](TriggersApi.md#deleteBackfillByQuery) | **POST** /api/v1/triggers/backfill/delete/by-query | Delete backfill for given triggers |
| [**deleteBackfillByQuery1**](TriggersApi.md#deleteBackfillByQuery1) | **POST** /api/v1/{tenant}/triggers/backfill/delete/by-query | Delete backfill for given triggers |
| [**find25**](TriggersApi.md#find25) | **GET** /api/v1/triggers/{namespace}/{flowId} | Get all triggers for a flow |
| [**find51**](TriggersApi.md#find51) | **GET** /api/v1/{tenant}/triggers/{namespace}/{flowId} | Get all triggers for a flow |
| [**pauseBackfill**](TriggersApi.md#pauseBackfill) | **PUT** /api/v1/triggers/backfill/pause | Pause a backfill |
| [**pauseBackfill1**](TriggersApi.md#pauseBackfill1) | **PUT** /api/v1/{tenant}/triggers/backfill/pause | Pause a backfill |
| [**pauseBackfillByIds**](TriggersApi.md#pauseBackfillByIds) | **POST** /api/v1/triggers/backfill/pause/by-triggers | Pause backfill for given triggers |
| [**pauseBackfillByIds1**](TriggersApi.md#pauseBackfillByIds1) | **POST** /api/v1/{tenant}/triggers/backfill/pause/by-triggers | Pause backfill for given triggers |
| [**pauseBackfillByQuery**](TriggersApi.md#pauseBackfillByQuery) | **POST** /api/v1/triggers/backfill/pause/by-query | Pause backfill for given triggers |
| [**pauseBackfillByQuery1**](TriggersApi.md#pauseBackfillByQuery1) | **POST** /api/v1/{tenant}/triggers/backfill/pause/by-query | Pause backfill for given triggers |
| [**restart1**](TriggersApi.md#restart1) | **POST** /api/v1/triggers/{namespace}/{flowId}/{triggerId}/restart | Restart a trigger |
| [**restart3**](TriggersApi.md#restart3) | **POST** /api/v1/{tenant}/triggers/{namespace}/{flowId}/{triggerId}/restart | Restart a trigger |
| [**search4**](TriggersApi.md#search4) | **GET** /api/v1/triggers/search | Search for triggers |
| [**search9**](TriggersApi.md#search9) | **GET** /api/v1/{tenant}/triggers/search | Search for triggers |
| [**setDisabledByIds**](TriggersApi.md#setDisabledByIds) | **POST** /api/v1/triggers/set-disabled/by-triggers | Delete backfill for given triggers |
| [**setDisabledByIds1**](TriggersApi.md#setDisabledByIds1) | **POST** /api/v1/{tenant}/triggers/set-disabled/by-triggers | Delete backfill for given triggers |
| [**setDisabledByQuery**](TriggersApi.md#setDisabledByQuery) | **POST** /api/v1/triggers/set-disabled/by-query | Delete backfill for given triggers |
| [**setDisabledByQuery1**](TriggersApi.md#setDisabledByQuery1) | **POST** /api/v1/{tenant}/triggers/set-disabled/by-query | Delete backfill for given triggers |
| [**unlock**](TriggersApi.md#unlock) | **POST** /api/v1/triggers/{namespace}/{flowId}/{triggerId}/unlock | Unlock a trigger |
| [**unlock1**](TriggersApi.md#unlock1) | **POST** /api/v1/{tenant}/triggers/{namespace}/{flowId}/{triggerId}/unlock | Unlock a trigger |
| [**unlockByIds**](TriggersApi.md#unlockByIds) | **POST** /api/v1/triggers/unlock/by-triggers | Unlock given triggers |
| [**unlockByIds1**](TriggersApi.md#unlockByIds1) | **POST** /api/v1/{tenant}/triggers/unlock/by-triggers | Unlock given triggers |
| [**unlockByQuery**](TriggersApi.md#unlockByQuery) | **POST** /api/v1/triggers/unlock/by-query | Unlock triggers by query parameters |
| [**unlockByQuery1**](TriggersApi.md#unlockByQuery1) | **POST** /api/v1/{tenant}/triggers/unlock/by-query | Unlock triggers by query parameters |
| [**unpauseBackfill**](TriggersApi.md#unpauseBackfill) | **PUT** /api/v1/triggers/backfill/unpause | Unpause a backfill |
| [**unpauseBackfill1**](TriggersApi.md#unpauseBackfill1) | **PUT** /api/v1/{tenant}/triggers/backfill/unpause | Unpause a backfill |
| [**unpauseBackfillByIds**](TriggersApi.md#unpauseBackfillByIds) | **POST** /api/v1/triggers/backfill/unpause/by-triggers | Unpause backfill for given triggers |
| [**unpauseBackfillByIds1**](TriggersApi.md#unpauseBackfillByIds1) | **POST** /api/v1/{tenant}/triggers/backfill/unpause/by-triggers | Unpause backfill for given triggers |
| [**unpauseBackfillByQuery**](TriggersApi.md#unpauseBackfillByQuery) | **POST** /api/v1/triggers/backfill/unpause/by-query | Unpause backfill for given triggers |
| [**unpauseBackfillByQuery1**](TriggersApi.md#unpauseBackfillByQuery1) | **POST** /api/v1/{tenant}/triggers/backfill/unpause/by-query | Unpause backfill for given triggers |
| [**update17**](TriggersApi.md#update17) | **PUT** /api/v1/triggers | Update a trigger |
| [**update35**](TriggersApi.md#update35) | **PUT** /api/v1/{tenant}/triggers | Update a trigger |



## deleteBackfill

> Trigger deleteBackfill(trigger)

Delete a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.deleteBackfill(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfill");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteBackfill 200 response |  -  |


## deleteBackfill1

> Trigger deleteBackfill1(tenant, trigger)

Delete a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.deleteBackfill1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfill1");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteBackfill_1 200 response |  -  |


## deleteBackfillByIds

> Object deleteBackfillByIds(trigger)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.deleteBackfillByIds(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfillByIds");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteBackfillByIds 200 response |  -  |


## deleteBackfillByIds1

> Object deleteBackfillByIds1(tenant, trigger)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.deleteBackfillByIds1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfillByIds1");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteBackfillByIds_1 200 response |  -  |


## deleteBackfillByQuery

> Object deleteBackfillByQuery(q, namespace)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.deleteBackfillByQuery(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfillByQuery");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | deleteBackfillByQuery 200 response |  -  |


## deleteBackfillByQuery1

> Object deleteBackfillByQuery1(tenant, q, namespace)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.deleteBackfillByQuery1(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#deleteBackfillByQuery1");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | deleteBackfillByQuery_1 200 response |  -  |


## find25

> PagedResultsTrigger find25(page, size, namespace, flowId, sort, q)

Get all triggers for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        try {
            PagedResultsTrigger result = apiInstance.find25(page, size, namespace, flowId, sort, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#find25");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **q** | **String**| A string filter | [optional] |

### Return type

[**PagedResultsTrigger**](PagedResultsTrigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_25 200 response |  -  |


## find51

> PagedResultsTrigger find51(page, size, namespace, flowId, tenant, sort, q)

Get all triggers for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        try {
            PagedResultsTrigger result = apiInstance.find51(page, size, namespace, flowId, tenant, sort, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#find51");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **tenant** | **String**|  | |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **q** | **String**| A string filter | [optional] |

### Return type

[**PagedResultsTrigger**](PagedResultsTrigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_51 200 response |  -  |


## pauseBackfill

> Trigger pauseBackfill(trigger)

Pause a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.pauseBackfill(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfill");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pauseBackfill 200 response |  -  |


## pauseBackfill1

> Trigger pauseBackfill1(tenant, trigger)

Pause a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.pauseBackfill1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfill1");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pauseBackfill_1 200 response |  -  |


## pauseBackfillByIds

> Object pauseBackfillByIds(trigger)

Pause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.pauseBackfillByIds(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfillByIds");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pauseBackfillByIds 200 response |  -  |


## pauseBackfillByIds1

> Object pauseBackfillByIds1(tenant, trigger)

Pause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.pauseBackfillByIds1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfillByIds1");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pauseBackfillByIds_1 200 response |  -  |


## pauseBackfillByQuery

> Object pauseBackfillByQuery(q, namespace)

Pause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.pauseBackfillByQuery(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfillByQuery");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | pauseBackfillByQuery 200 response |  -  |


## pauseBackfillByQuery1

> Object pauseBackfillByQuery1(tenant, q, namespace)

Pause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.pauseBackfillByQuery1(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#pauseBackfillByQuery1");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | pauseBackfillByQuery_1 200 response |  -  |


## restart1

> Object restart1(namespace, flowId, triggerId)

Restart a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        String triggerId = "triggerId_example"; // String | The trigger id
        try {
            Object result = apiInstance.restart1(namespace, flowId, triggerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#restart1");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **triggerId** | **String**| The trigger id | |

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
| **200** | restart_1 200 response |  -  |


## restart3

> Object restart3(namespace, flowId, triggerId, tenant)

Restart a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        String triggerId = "triggerId_example"; // String | The trigger id
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.restart3(namespace, flowId, triggerId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#restart3");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **triggerId** | **String**| The trigger id | |
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
| **200** | restart_3 200 response |  -  |


## search4

> PagedResultsTriggerControllerTriggers search4(page, size, sort, q, namespace, workerId, flowId)

Search for triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String workerId = "workerId_example"; // String | The identifier of the worker currently evaluating the trigger
        String flowId = "flowId_example"; // String | The flow identifier
        try {
            PagedResultsTriggerControllerTriggers result = apiInstance.search4(page, size, sort, q, namespace, workerId, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#search4");
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
| **workerId** | **String**| The identifier of the worker currently evaluating the trigger | [optional] |
| **flowId** | **String**| The flow identifier | [optional] |

### Return type

[**PagedResultsTriggerControllerTriggers**](PagedResultsTriggerControllerTriggers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_4 200 response |  -  |


## search9

> PagedResultsTriggerControllerTriggers search9(page, size, tenant, sort, q, namespace, workerId, flowId)

Search for triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String workerId = "workerId_example"; // String | The identifier of the worker currently evaluating the trigger
        String flowId = "flowId_example"; // String | The flow identifier
        try {
            PagedResultsTriggerControllerTriggers result = apiInstance.search9(page, size, tenant, sort, q, namespace, workerId, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#search9");
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
| **workerId** | **String**| The identifier of the worker currently evaluating the trigger | [optional] |
| **flowId** | **String**| The flow identifier | [optional] |

### Return type

[**PagedResultsTriggerControllerTriggers**](PagedResultsTriggerControllerTriggers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_9 200 response |  -  |


## setDisabledByIds

> Object setDisabledByIds(triggerControllerSetDisabledRequest)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        TriggerControllerSetDisabledRequest triggerControllerSetDisabledRequest = new TriggerControllerSetDisabledRequest(); // TriggerControllerSetDisabledRequest | 
        try {
            Object result = apiInstance.setDisabledByIds(triggerControllerSetDisabledRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#setDisabledByIds");
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
| **triggerControllerSetDisabledRequest** | [**TriggerControllerSetDisabledRequest**](TriggerControllerSetDisabledRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setDisabledByIds 200 response |  -  |


## setDisabledByIds1

> Object setDisabledByIds1(tenant, triggerControllerSetDisabledRequest)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        TriggerControllerSetDisabledRequest triggerControllerSetDisabledRequest = new TriggerControllerSetDisabledRequest(); // TriggerControllerSetDisabledRequest | 
        try {
            Object result = apiInstance.setDisabledByIds1(tenant, triggerControllerSetDisabledRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#setDisabledByIds1");
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
| **triggerControllerSetDisabledRequest** | [**TriggerControllerSetDisabledRequest**](TriggerControllerSetDisabledRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setDisabledByIds_1 200 response |  -  |


## setDisabledByQuery

> Object setDisabledByQuery(disabled, q, namespace)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Boolean disabled = true; // Boolean | The disabled state
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.setDisabledByQuery(disabled, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#setDisabledByQuery");
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
| **disabled** | **Boolean**| The disabled state | [default to true] |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | setDisabledByQuery 200 response |  -  |


## setDisabledByQuery1

> Object setDisabledByQuery1(disabled, tenant, q, namespace)

Delete backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Boolean disabled = true; // Boolean | The disabled state
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.setDisabledByQuery1(disabled, tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#setDisabledByQuery1");
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
| **disabled** | **Boolean**| The disabled state | [default to true] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | setDisabledByQuery_1 200 response |  -  |


## unlock

> Trigger unlock(namespace, flowId, triggerId)

Unlock a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        String triggerId = "triggerId_example"; // String | The trigger id
        try {
            Trigger result = apiInstance.unlock(namespace, flowId, triggerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlock");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **triggerId** | **String**| The trigger id | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlock 200 response |  -  |


## unlock1

> Trigger unlock1(namespace, flowId, triggerId, tenant)

Unlock a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow id
        String triggerId = "triggerId_example"; // String | The trigger id
        String tenant = "tenant_example"; // String | 
        try {
            Trigger result = apiInstance.unlock1(namespace, flowId, triggerId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlock1");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow id | |
| **triggerId** | **String**| The trigger id | |
| **tenant** | **String**|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlock_1 200 response |  -  |


## unlockByIds

> Object unlockByIds(trigger)

Unlock given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.unlockByIds(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlockByIds");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlockByIds 200 response |  -  |


## unlockByIds1

> Object unlockByIds1(tenant, trigger)

Unlock given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.unlockByIds1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlockByIds1");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlockByIds_1 200 response |  -  |


## unlockByQuery

> Object unlockByQuery(q, namespace)

Unlock triggers by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.unlockByQuery(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlockByQuery");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | unlockByQuery 200 response |  -  |


## unlockByQuery1

> Object unlockByQuery1(tenant, q, namespace)

Unlock triggers by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.unlockByQuery1(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unlockByQuery1");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | unlockByQuery_1 200 response |  -  |


## unpauseBackfill

> Trigger unpauseBackfill(trigger)

Unpause a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.unpauseBackfill(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfill");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unpauseBackfill 200 response |  -  |


## unpauseBackfill1

> Trigger unpauseBackfill1(tenant, trigger)

Unpause a backfill

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.unpauseBackfill1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfill1");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unpauseBackfill_1 200 response |  -  |


## unpauseBackfillByIds

> Object unpauseBackfillByIds(trigger)

Unpause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.unpauseBackfillByIds(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfillByIds");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unpauseBackfillByIds 200 response |  -  |


## unpauseBackfillByIds1

> Object unpauseBackfillByIds1(tenant, trigger)

Unpause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Trigger> trigger = Arrays.asList(); // List<Trigger> | 
        try {
            Object result = apiInstance.unpauseBackfillByIds1(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfillByIds1");
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
| **trigger** | [**List&lt;Trigger&gt;**](Trigger.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unpauseBackfillByIds_1 200 response |  -  |


## unpauseBackfillByQuery

> Object unpauseBackfillByQuery(q, namespace)

Unpause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.unpauseBackfillByQuery(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfillByQuery");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | unpauseBackfillByQuery 200 response |  -  |


## unpauseBackfillByQuery1

> Object unpauseBackfillByQuery1(tenant, q, namespace)

Unpause backfill for given triggers

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            Object result = apiInstance.unpauseBackfillByQuery1(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#unpauseBackfillByQuery1");
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
| **namespace** | **String**| A namespace filter prefix | [optional] |

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
| **200** | unpauseBackfillByQuery_1 200 response |  -  |


## update17

> Trigger update17(trigger)

Update a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.update17(trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#update17");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_17 200 response |  -  |


## update35

> Trigger update35(tenant, trigger)

Update a trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TriggersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TriggersApi apiInstance = new TriggersApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Trigger trigger = new Trigger(); // Trigger | 
        try {
            Trigger result = apiInstance.update35(tenant, trigger);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TriggersApi#update35");
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
| **trigger** | [**Trigger**](Trigger.md)|  | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_35 200 response |  -  |

