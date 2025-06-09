# BindingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateBinding**](BindingsApi.md#bulkCreateBinding) | **POST** /api/v1/{tenant}/bindings/bulk | Create multiple bindings |
| [**bulkCreateBindingapsSuperAdmin**](BindingsApi.md#bulkCreateBindingapsSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/bindings/bulk | Create multiple bindings |
| [**createBinding**](BindingsApi.md#createBinding) | **POST** /api/v1/{tenant}/bindings | Create a binding |
| [**createBindingapsSuperAdmin**](BindingsApi.md#createBindingapsSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/bindings | Create a binding |
| [**deleteBinding**](BindingsApi.md#deleteBinding) | **DELETE** /api/v1/{tenant}/bindings/{id} | Delete a binding |
| [**deleteBindingapsSuperAdmin**](BindingsApi.md#deleteBindingapsSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/bindings/{id} | Delete a binding |
| [**getBinding**](BindingsApi.md#getBinding) | **GET** /api/v1/{tenant}/bindings/{id} | Get a binding |
| [**getBindingapsSuperAdmin**](BindingsApi.md#getBindingapsSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/bindings/{id} | Get a binding |
| [**searchBindings**](BindingsApi.md#searchBindings) | **GET** /api/v1/{tenant}/bindings/search | Search for bindings |
| [**searchBindingsapsSuperAdmin**](BindingsApi.md#searchBindingsapsSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/bindings/search | Search for bindings |



## bulkCreateBinding

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreateBinding(tenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | The bindings
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreateBinding(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreateBinding");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)| The bindings | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreateBinding 200 response |  -  |


## bulkCreateBindingapsSuperAdmin

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreateBindingapsSuperAdmin(resourceTenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | The bindings
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreateBindingapsSuperAdmin(resourceTenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreateBindingapsSuperAdmin");
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
| **resourceTenant** | **String**|  | |
| **binding** | [**List&lt;Binding&gt;**](Binding.md)| The bindings | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreateBindingapsSuperAdmin 200 response |  -  |


## createBinding

> AbstractBindingControllerBindingDetail createBinding(tenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Binding binding = new Binding(); // Binding | The binding
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.createBinding(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#createBinding");
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
| **binding** | [**Binding**](Binding.md)| The binding | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createBinding 200 response |  -  |


## createBindingapsSuperAdmin

> AbstractBindingControllerBindingDetail createBindingapsSuperAdmin(resourceTenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String | 
        Binding binding = new Binding(); // Binding | The binding
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.createBindingapsSuperAdmin(resourceTenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#createBindingapsSuperAdmin");
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
| **resourceTenant** | **String**|  | |
| **binding** | [**Binding**](Binding.md)| The binding | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createBindingapsSuperAdmin 200 response |  -  |


## deleteBinding

> deleteBinding(id, tenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.deleteBinding(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#deleteBinding");
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
| **id** | **String**| The binding id | |
| **tenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## deleteBindingapsSuperAdmin

> deleteBindingapsSuperAdmin(id, resourceTenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String resourceTenant = "resourceTenant_example"; // String | 
        try {
            apiInstance.deleteBindingapsSuperAdmin(id, resourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#deleteBindingapsSuperAdmin");
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
| **id** | **String**| The binding id | |
| **resourceTenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## getBinding

> AbstractBindingControllerBindingDetail getBinding(id, tenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.getBinding(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#getBinding");
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
| **id** | **String**| The binding id | |
| **tenant** | **String**|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBinding 200 response |  -  |


## getBindingapsSuperAdmin

> AbstractBindingControllerBindingDetail getBindingapsSuperAdmin(id, resourceTenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String resourceTenant = "resourceTenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.getBindingapsSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#getBindingapsSuperAdmin");
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
| **id** | **String**| The binding id | |
| **resourceTenant** | **String**|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBindingapsSuperAdmin 200 response |  -  |


## searchBindings

> PagedResultsAbstractBindingControllerBindingDetail searchBindings(page, size, tenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.searchBindings(page, size, tenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#searchBindings");
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
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchBindings 200 response |  -  |


## searchBindingsapsSuperAdmin

> PagedResultsAbstractBindingControllerBindingDetail searchBindingsapsSuperAdmin(page, size, resourceTenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

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

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.searchBindingsapsSuperAdmin(page, size, resourceTenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#searchBindingsapsSuperAdmin");
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
| **resourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchBindingsapsSuperAdmin 200 response |  -  |

