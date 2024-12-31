# NamespacesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocomplete1**](NamespacesApi.md#autocomplete1) | **POST** /api/v1/namespaces/autocomplete | List namespaces for autocomplete |
| [**autocomplete13**](NamespacesApi.md#autocomplete13) | **POST** /api/v1/{tenant}/namespaces/autocomplete | List namespaces for autocomplete |
| [**autocomplete16**](NamespacesApi.md#autocomplete16) | **POST** /api/v1/{tenant}/tenants/namespaces/autocomplete | List namespaces for autocomplete |
| [**autocomplete20**](NamespacesApi.md#autocomplete20) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/namespaces/autocomplete | List namespaces for autocomplete |
| [**autocomplete4**](NamespacesApi.md#autocomplete4) | **POST** /api/v1/tenants/namespaces/autocomplete | List namespaces for autocomplete |
| [**autocomplete8**](NamespacesApi.md#autocomplete8) | **POST** /api/v1/tenants/{ressourceTenant}/namespaces/autocomplete | List namespaces for autocomplete |
| [**create10**](NamespacesApi.md#create10) | **POST** /api/v1/namespaces | Create a namespace |
| [**create35**](NamespacesApi.md#create35) | **POST** /api/v1/{tenant}/namespaces | Create a namespace |
| [**delete11**](NamespacesApi.md#delete11) | **DELETE** /api/v1/namespaces/{id} | Delete a flow |
| [**delete39**](NamespacesApi.md#delete39) | **DELETE** /api/v1/{tenant}/namespaces/{id} | Delete a flow |
| [**deleteSecret**](NamespacesApi.md#deleteSecret) | **DELETE** /api/v1/namespaces/{namespace}/secrets/{key} | Delete a secret for a namespace |
| [**deleteSecret1**](NamespacesApi.md#deleteSecret1) | **DELETE** /api/v1/{tenant}/namespaces/{namespace}/secrets/{key} | Delete a secret for a namespace |
| [**find11**](NamespacesApi.md#find11) | **GET** /api/v1/namespaces/search | Search for namespaces |
| [**find37**](NamespacesApi.md#find37) | **GET** /api/v1/{tenant}/namespaces/search | Search for namespaces |
| [**index27**](NamespacesApi.md#index27) | **GET** /api/v1/{tenant}/namespaces/{id} | Get a namespace |
| [**index6**](NamespacesApi.md#index6) | **GET** /api/v1/namespaces/{id} | Get a namespace |
| [**inheritedPluginDefaults**](NamespacesApi.md#inheritedPluginDefaults) | **GET** /api/v1/namespaces/{id}/inherited-plugindefaults | List inherited plugin defaults |
| [**inheritedPluginDefaults1**](NamespacesApi.md#inheritedPluginDefaults1) | **GET** /api/v1/{tenant}/namespaces/{id}/inherited-plugindefaults | List inherited plugin defaults |
| [**inheritedSecrets**](NamespacesApi.md#inheritedSecrets) | **GET** /api/v1/namespaces/{namespace}/inherited-secrets | List inherited secrets |
| [**inheritedSecrets1**](NamespacesApi.md#inheritedSecrets1) | **GET** /api/v1/{tenant}/namespaces/{namespace}/inherited-secrets | List inherited secrets |
| [**inheritedVariables**](NamespacesApi.md#inheritedVariables) | **GET** /api/v1/namespaces/{id}/inherited-variables | List inherited variables |
| [**inheritedVariables1**](NamespacesApi.md#inheritedVariables1) | **GET** /api/v1/{tenant}/namespaces/{id}/inherited-variables | List inherited variables |
| [**listSecret**](NamespacesApi.md#listSecret) | **GET** /api/v1/namespaces/{namespace}/secrets | Get secrets for a namespace |
| [**listSecret1**](NamespacesApi.md#listSecret1) | **GET** /api/v1/{tenant}/namespaces/{namespace}/secrets | Get secrets for a namespace |
| [**patchSecret**](NamespacesApi.md#patchSecret) | **PATCH** /api/v1/namespaces/{namespace}/secrets/{key} | Patch a secret metadata for a namespace |
| [**patchSecret1**](NamespacesApi.md#patchSecret1) | **PATCH** /api/v1/{tenant}/namespaces/{namespace}/secrets/{key} | Patch a secret metadata for a namespace |
| [**putSecrets**](NamespacesApi.md#putSecrets) | **PUT** /api/v1/namespaces/{namespace}/secrets | Update secrets for a namespace |
| [**putSecrets1**](NamespacesApi.md#putSecrets1) | **PUT** /api/v1/{tenant}/namespaces/{namespace}/secrets | Update secrets for a namespace |
| [**update25**](NamespacesApi.md#update25) | **PUT** /api/v1/{tenant}/namespaces/{id} | Update a namespace |
| [**update7**](NamespacesApi.md#update7) | **PUT** /api/v1/namespaces/{id} | Update a namespace |



## autocomplete1

> List&lt;String&gt; autocomplete1(q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete1(q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete1");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_1 200 response |  -  |


## autocomplete13

> List&lt;String&gt; autocomplete13(tenant, q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete13(tenant, q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete13");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_13 200 response |  -  |


## autocomplete16

> List&lt;String&gt; autocomplete16(tenant, q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete16(tenant, q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete16");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_16 200 response |  -  |


## autocomplete20

> List&lt;String&gt; autocomplete20(ressourceTenant, tenant, q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete20(ressourceTenant, tenant, q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete20");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_20 200 response |  -  |


## autocomplete4

> List&lt;String&gt; autocomplete4(q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete4(q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete4");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_4 200 response |  -  |


## autocomplete8

> List&lt;String&gt; autocomplete8(ressourceTenant, q, apiIds)

List namespaces for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<String> result = apiInstance.autocomplete8(ressourceTenant, q, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#autocomplete8");
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
| **ressourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **apiIds** | [**ApiIds**](ApiIds.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_8 200 response |  -  |


## create10

> Namespace create10(namespace)

Create a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        Namespace namespace = new Namespace(); // Namespace | 
        try {
            Namespace result = apiInstance.create10(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#create10");
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
| **namespace** | [**Namespace**](Namespace.md)|  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_10 200 response |  -  |


## create35

> Namespace create35(tenant, namespace)

Create a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Namespace namespace = new Namespace(); // Namespace | 
        try {
            Namespace result = apiInstance.create35(tenant, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#create35");
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
| **namespace** | [**Namespace**](Namespace.md)|  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_35 200 response |  -  |


## delete11

> delete11(id)

Delete a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        try {
            apiInstance.delete11(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#delete11");
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
| **id** | **String**| The namespace id | |

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


## delete39

> delete39(id, tenant)

Delete a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete39(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#delete39");
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
| **id** | **String**| The namespace id | |
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


## deleteSecret

> List&lt;String&gt; deleteSecret(namespace, key)

Delete a secret for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The secret key
        try {
            List<String> result = apiInstance.deleteSecret(namespace, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#deleteSecret");
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
| **key** | **String**| The secret key | |

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
| **200** | deleteSecret 200 response |  -  |


## deleteSecret1

> List&lt;String&gt; deleteSecret1(namespace, key, tenant)

Delete a secret for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | The secret key
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.deleteSecret1(namespace, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#deleteSecret1");
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
| **key** | **String**| The secret key | |
| **tenant** | **String**|  | |

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
| **200** | deleteSecret_1 200 response |  -  |


## find11

> PagedResultsNamespaceWithDisabled find11(page, size, q, sort, existing)

Search for namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        Boolean existing = false; // Boolean | Return only existing namespace
        try {
            PagedResultsNamespaceWithDisabled result = apiInstance.find11(page, size, q, sort, existing);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#find11");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **existing** | **Boolean**| Return only existing namespace | [optional] [default to false] |

### Return type

[**PagedResultsNamespaceWithDisabled**](PagedResultsNamespaceWithDisabled.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_11 200 response |  -  |


## find37

> PagedResultsNamespaceWithDisabled find37(page, size, tenant, q, sort, existing)

Search for namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        Boolean existing = false; // Boolean | Return only existing namespace
        try {
            PagedResultsNamespaceWithDisabled result = apiInstance.find37(page, size, tenant, q, sort, existing);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#find37");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **existing** | **Boolean**| Return only existing namespace | [optional] [default to false] |

### Return type

[**PagedResultsNamespaceWithDisabled**](PagedResultsNamespaceWithDisabled.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_37 200 response |  -  |


## index27

> Namespace index27(id, tenant)

Get a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            Namespace result = apiInstance.index27(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#index27");
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
| **id** | **String**| The namespace id | |
| **tenant** | **String**|  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_27 200 response |  -  |


## index6

> Namespace index6(id)

Get a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        try {
            Namespace result = apiInstance.index6(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#index6");
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
| **id** | **String**| The namespace id | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_6 200 response |  -  |


## inheritedPluginDefaults

> List&lt;PluginDefault&gt; inheritedPluginDefaults(id)

List inherited plugin defaults

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        try {
            List<PluginDefault> result = apiInstance.inheritedPluginDefaults(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedPluginDefaults");
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
| **id** | **String**| The namespace id | |

### Return type

[**List&lt;PluginDefault&gt;**](PluginDefault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inheritedPluginDefaults 200 response |  -  |


## inheritedPluginDefaults1

> List&lt;PluginDefault&gt; inheritedPluginDefaults1(id, tenant)

List inherited plugin defaults

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            List<PluginDefault> result = apiInstance.inheritedPluginDefaults1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedPluginDefaults1");
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
| **id** | **String**| The namespace id | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;PluginDefault&gt;**](PluginDefault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inheritedPluginDefaults_1 200 response |  -  |


## inheritedSecrets

> Map&lt;String, List&lt;String&gt;&gt; inheritedSecrets(namespace)

List inherited secrets

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        try {
            Map<String, List<String>> result = apiInstance.inheritedSecrets(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedSecrets");
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

[**Map&lt;String, List&lt;String&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inheritedSecrets 200 response |  -  |


## inheritedSecrets1

> Map&lt;String, List&lt;String&gt;&gt; inheritedSecrets1(namespace, tenant)

List inherited secrets

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, List<String>> result = apiInstance.inheritedSecrets1(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedSecrets1");
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

[**Map&lt;String, List&lt;String&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inheritedSecrets_1 200 response |  -  |


## inheritedVariables

> Map&lt;String, Object&gt; inheritedVariables(id)

List inherited variables

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        try {
            Map<String, Object> result = apiInstance.inheritedVariables(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedVariables");
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
| **id** | **String**| The namespace id | |

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
| **200** | inheritedVariables 200 response |  -  |


## inheritedVariables1

> Map&lt;String, Object&gt; inheritedVariables1(id, tenant)

List inherited variables

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, Object> result = apiInstance.inheritedVariables1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#inheritedVariables1");
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
| **id** | **String**| The namespace id | |
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
| **200** | inheritedVariables_1 200 response |  -  |


## listSecret

> List&lt;ApiSecretMeta&gt; listSecret(namespace)

Get secrets for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        try {
            List<ApiSecretMeta> result = apiInstance.listSecret(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#listSecret");
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

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listSecret 200 response |  -  |


## listSecret1

> List&lt;ApiSecretMeta&gt; listSecret1(namespace, tenant)

Get secrets for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            List<ApiSecretMeta> result = apiInstance.listSecret1(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#listSecret1");
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

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listSecret_1 200 response |  -  |


## patchSecret

> List&lt;ApiSecretMeta&gt; patchSecret(namespace, key, apiSecretMeta)

Patch a secret metadata for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String key = "key_example"; // String | 
        ApiSecretMeta apiSecretMeta = new ApiSecretMeta(); // ApiSecretMeta | 
        try {
            List<ApiSecretMeta> result = apiInstance.patchSecret(namespace, key, apiSecretMeta);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#patchSecret");
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
| **key** | **String**|  | |
| **apiSecretMeta** | [**ApiSecretMeta**](ApiSecretMeta.md)|  | |

### Return type

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | patchSecret 200 response |  -  |


## patchSecret1

> List&lt;ApiSecretMeta&gt; patchSecret1(namespace, tenant, key, apiSecretMeta)

Patch a secret metadata for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        String key = "key_example"; // String | 
        ApiSecretMeta apiSecretMeta = new ApiSecretMeta(); // ApiSecretMeta | 
        try {
            List<ApiSecretMeta> result = apiInstance.patchSecret1(namespace, tenant, key, apiSecretMeta);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#patchSecret1");
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
| **key** | **String**|  | |
| **apiSecretMeta** | [**ApiSecretMeta**](ApiSecretMeta.md)|  | |

### Return type

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | patchSecret_1 200 response |  -  |


## putSecrets

> List&lt;ApiSecretMeta&gt; putSecrets(namespace, apiSecretValue)

Update secrets for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        ApiSecretValue apiSecretValue = new ApiSecretValue(); // ApiSecretValue | 
        try {
            List<ApiSecretMeta> result = apiInstance.putSecrets(namespace, apiSecretValue);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#putSecrets");
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
| **apiSecretValue** | [**ApiSecretValue**](ApiSecretValue.md)|  | |

### Return type

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | putSecrets 200 response |  -  |


## putSecrets1

> List&lt;ApiSecretMeta&gt; putSecrets1(namespace, tenant, apiSecretValue)

Update secrets for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        ApiSecretValue apiSecretValue = new ApiSecretValue(); // ApiSecretValue | 
        try {
            List<ApiSecretMeta> result = apiInstance.putSecrets1(namespace, tenant, apiSecretValue);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#putSecrets1");
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
| **apiSecretValue** | [**ApiSecretValue**](ApiSecretValue.md)|  | |

### Return type

[**List&lt;ApiSecretMeta&gt;**](ApiSecretMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | putSecrets_1 200 response |  -  |


## update25

> Namespace update25(id, tenant, namespace)

Update a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        Namespace namespace = new Namespace(); // Namespace | 
        try {
            Namespace result = apiInstance.update25(id, tenant, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#update25");
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
| **id** | **String**| The namespace id | |
| **tenant** | **String**|  | |
| **namespace** | [**Namespace**](Namespace.md)|  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_25 200 response |  -  |


## update7

> Namespace update7(id, namespace)

Update a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.NamespacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        NamespacesApi apiInstance = new NamespacesApi(defaultClient);
        String id = "id_example"; // String | The namespace id
        Namespace namespace = new Namespace(); // Namespace | 
        try {
            Namespace result = apiInstance.update7(id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling NamespacesApi#update7");
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
| **id** | **String**| The namespace id | |
| **namespace** | [**Namespace**](Namespace.md)|  | |

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_7 200 response |  -  |

