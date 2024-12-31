# KvApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delete13**](KvApi.md#delete13) | **DELETE** /api/v1/namespaces/{namespace}/kv/{key} | Delete a key-value pair |
| [**delete41**](KvApi.md#delete41) | **DELETE** /api/v1/{tenant}/namespaces/{namespace}/kv/{key} | Delete a key-value pair |
| [**deleteKeys**](KvApi.md#deleteKeys) | **DELETE** /api/v1/namespaces/{namespace}/kv | Bulk-delete multiple key/value pairs from the given namespace. |
| [**deleteKeys1**](KvApi.md#deleteKeys1) | **DELETE** /api/v1/{tenant}/namespaces/{namespace}/kv | Bulk-delete multiple key/value pairs from the given namespace. |
| [**get12**](KvApi.md#get12) | **GET** /api/v1/{tenant}/namespaces/{namespace}/kv/{key} | Get value for a key |
| [**get4**](KvApi.md#get4) | **GET** /api/v1/namespaces/{namespace}/kv/{key} | Get value for a key |
| [**list2**](KvApi.md#list2) | **GET** /api/v1/namespaces/{namespace}/kv | List all keys for a namespace |
| [**list6**](KvApi.md#list6) | **GET** /api/v1/{tenant}/namespaces/{namespace}/kv | List all keys for a namespace |
| [**put**](KvApi.md#put) | **PUT** /api/v1/namespaces/{namespace}/kv/{key} | Puts a key-value pair in store |
| [**put1**](KvApi.md#put1) | **PUT** /api/v1/{tenant}/namespaces/{namespace}/kv/{key} | Puts a key-value pair in store |



## delete13

> Boolean delete13(namespace, key)

Delete a key-value pair

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        try {
            Boolean result = apiInstance.delete13(namespace, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#delete13");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_13 200 response |  -  |


## delete41

> Boolean delete41(namespace, key, tenant)

Delete a key-value pair

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        String tenant = "tenant_example"; // String | 
        try {
            Boolean result = apiInstance.delete41(namespace, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#delete41");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |
| **tenant** | **String**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_41 200 response |  -  |


## deleteKeys

> KVControllerApiDeleteBulkResponse deleteKeys(namespace, kvControllerApiDeleteBulkRequest)

Bulk-delete multiple key/value pairs from the given namespace.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        KVControllerApiDeleteBulkRequest kvControllerApiDeleteBulkRequest = new KVControllerApiDeleteBulkRequest(); // KVControllerApiDeleteBulkRequest | 
        try {
            KVControllerApiDeleteBulkResponse result = apiInstance.deleteKeys(namespace, kvControllerApiDeleteBulkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#deleteKeys");
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
| **namespace** | **String**| The namespace id | |
| **kvControllerApiDeleteBulkRequest** | [**KVControllerApiDeleteBulkRequest**](KVControllerApiDeleteBulkRequest.md)|  | |

### Return type

[**KVControllerApiDeleteBulkResponse**](KVControllerApiDeleteBulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteKeys 200 response |  -  |


## deleteKeys1

> KVControllerApiDeleteBulkResponse deleteKeys1(namespace, tenant, kvControllerApiDeleteBulkRequest)

Bulk-delete multiple key/value pairs from the given namespace.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        KVControllerApiDeleteBulkRequest kvControllerApiDeleteBulkRequest = new KVControllerApiDeleteBulkRequest(); // KVControllerApiDeleteBulkRequest | 
        try {
            KVControllerApiDeleteBulkResponse result = apiInstance.deleteKeys1(namespace, tenant, kvControllerApiDeleteBulkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#deleteKeys1");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |
| **kvControllerApiDeleteBulkRequest** | [**KVControllerApiDeleteBulkRequest**](KVControllerApiDeleteBulkRequest.md)|  | |

### Return type

[**KVControllerApiDeleteBulkResponse**](KVControllerApiDeleteBulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteKeys_1 200 response |  -  |


## get12

> KVControllerTypedValue get12(namespace, key, tenant)

Get value for a key

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        String tenant = "tenant_example"; // String | 
        try {
            KVControllerTypedValue result = apiInstance.get12(namespace, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#get12");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |
| **tenant** | **String**|  | |

### Return type

[**KVControllerTypedValue**](KVControllerTypedValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_12 200 response |  -  |


## get4

> KVControllerTypedValue get4(namespace, key)

Get value for a key

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        try {
            KVControllerTypedValue result = apiInstance.get4(namespace, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#get4");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |

### Return type

[**KVControllerTypedValue**](KVControllerTypedValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_4 200 response |  -  |


## list2

> List&lt;KVEntry&gt; list2(namespace)

List all keys for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        try {
            List<KVEntry> result = apiInstance.list2(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#list2");
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
| **namespace** | **String**| The namespace id | |

### Return type

[**List&lt;KVEntry&gt;**](KVEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list_2 200 response |  -  |


## list6

> List&lt;KVEntry&gt; list6(namespace, tenant)

List all keys for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            List<KVEntry> result = apiInstance.list6(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#list6");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;KVEntry&gt;**](KVEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list_6 200 response |  -  |


## put

> put(namespace, key, body)

Puts a key-value pair in store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        String body = "body_example"; // String | 
        try {
            apiInstance.put(namespace, key, body);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#put");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |
| **body** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | put 200 response |  -  |


## put1

> put1(namespace, key, tenant, body)

Puts a key-value pair in store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.KvApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        KvApi apiInstance = new KvApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The key
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            apiInstance.put1(namespace, key, tenant, body);
        } catch (ApiException e) {
            System.err.println("Exception when calling KvApi#put1");
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
| **namespace** | **String**| The namespace id | |
| **key** | **String**| The key | |
| **tenant** | **String**|  | |
| **body** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/plain
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | put_1 200 response |  -  |

