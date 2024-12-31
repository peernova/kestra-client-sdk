# BindingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreate**](BindingsApi.md#bulkCreate) | **POST** /api/v1/bindings/bulk | Create multiple bindings |
| [**bulkCreate1**](BindingsApi.md#bulkCreate1) | **POST** /api/v1/tenants/bindings/bulk | Create multiple bindings |
| [**bulkCreate2**](BindingsApi.md#bulkCreate2) | **POST** /api/v1/tenants/{ressourceTenant}/bindings/bulk | Create multiple bindings |
| [**bulkCreate3**](BindingsApi.md#bulkCreate3) | **POST** /api/v1/{tenant}/bindings/bulk | Create multiple bindings |
| [**bulkCreate4**](BindingsApi.md#bulkCreate4) | **POST** /api/v1/{tenant}/tenants/bindings/bulk | Create multiple bindings |
| [**bulkCreate5**](BindingsApi.md#bulkCreate5) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/bindings/bulk | Create multiple bindings |
| [**create15**](BindingsApi.md#create15) | **POST** /api/v1/tenants/bindings | Create a binding |
| [**create2**](BindingsApi.md#create2) | **POST** /api/v1/bindings | Create a binding |
| [**create20**](BindingsApi.md#create20) | **POST** /api/v1/tenants/{ressourceTenant}/bindings | Create a binding |
| [**create27**](BindingsApi.md#create27) | **POST** /api/v1/{tenant}/bindings | Create a binding |
| [**create40**](BindingsApi.md#create40) | **POST** /api/v1/{tenant}/tenants/bindings | Create a binding |
| [**create45**](BindingsApi.md#create45) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/bindings | Create a binding |
| [**delete17**](BindingsApi.md#delete17) | **DELETE** /api/v1/tenants/bindings/{id} | Delete a binding |
| [**delete2**](BindingsApi.md#delete2) | **DELETE** /api/v1/bindings/{id} | Delete a binding |
| [**delete23**](BindingsApi.md#delete23) | **DELETE** /api/v1/tenants/{ressourceTenant}/bindings/{id} | Delete a binding |
| [**delete30**](BindingsApi.md#delete30) | **DELETE** /api/v1/{tenant}/bindings/{id} | Delete a binding |
| [**delete45**](BindingsApi.md#delete45) | **DELETE** /api/v1/{tenant}/tenants/bindings/{id} | Delete a binding |
| [**delete51**](BindingsApi.md#delete51) | **DELETE** /api/v1/{tenant}/tenants/{ressourceTenant}/bindings/{id} | Delete a binding |
| [**find14**](BindingsApi.md#find14) | **GET** /api/v1/tenants/bindings/search | Search for bindings |
| [**find2**](BindingsApi.md#find2) | **GET** /api/v1/bindings/search | Search for bindings |
| [**find20**](BindingsApi.md#find20) | **GET** /api/v1/tenants/{ressourceTenant}/bindings/search | Search for bindings |
| [**find28**](BindingsApi.md#find28) | **GET** /api/v1/{tenant}/bindings/search | Search for bindings |
| [**find40**](BindingsApi.md#find40) | **GET** /api/v1/{tenant}/tenants/bindings/search | Search for bindings |
| [**find46**](BindingsApi.md#find46) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/bindings/search | Search for bindings |
| [**index1**](BindingsApi.md#index1) | **GET** /api/v1/bindings/{id} | Get a binding |
| [**index10**](BindingsApi.md#index10) | **GET** /api/v1/tenants/bindings/{id} | Get a binding |
| [**index15**](BindingsApi.md#index15) | **GET** /api/v1/tenants/{ressourceTenant}/bindings/{id} | Get a binding |
| [**index22**](BindingsApi.md#index22) | **GET** /api/v1/{tenant}/bindings/{id} | Get a binding |
| [**index31**](BindingsApi.md#index31) | **GET** /api/v1/{tenant}/tenants/bindings/{id} | Get a binding |
| [**index36**](BindingsApi.md#index36) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/bindings/{id} | Get a binding |



## bulkCreate

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate(binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate(binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate 200 response |  -  |


## bulkCreate1

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate1(binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate1(binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate1");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate_1 200 response |  -  |


## bulkCreate2

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate2(ressourceTenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate2(ressourceTenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate2");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate_2 200 response |  -  |


## bulkCreate3

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate3(tenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate3(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate3");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate_3 200 response |  -  |


## bulkCreate4

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate4(tenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate4(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate4");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate_4 200 response |  -  |


## bulkCreate5

> List&lt;AbstractBindingControllerBindingDetail&gt; bulkCreate5(ressourceTenant, tenant, binding)

Create multiple bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        List<Binding> binding = Arrays.asList(); // List<Binding> | 
        try {
            List<AbstractBindingControllerBindingDetail> result = apiInstance.bulkCreate5(ressourceTenant, tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#bulkCreate5");
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
| **binding** | [**List&lt;Binding&gt;**](Binding.md)|  | |

### Return type

[**List&lt;AbstractBindingControllerBindingDetail&gt;**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | bulkCreate_5 200 response |  -  |


## create15

> AbstractBindingControllerBindingDetail create15(binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create15(binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create15");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_15 200 response |  -  |


## create2

> AbstractBindingControllerBindingDetail create2(binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create2(binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create2");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_2 200 response |  -  |


## create20

> AbstractBindingControllerBindingDetail create20(ressourceTenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create20(ressourceTenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create20");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_20 200 response |  -  |


## create27

> AbstractBindingControllerBindingDetail create27(tenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create27(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create27");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_27 200 response |  -  |


## create40

> AbstractBindingControllerBindingDetail create40(tenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create40(tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create40");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_40 200 response |  -  |


## create45

> AbstractBindingControllerBindingDetail create45(ressourceTenant, tenant, binding)

Create a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        Binding binding = new Binding(); // Binding | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.create45(ressourceTenant, tenant, binding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#create45");
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
| **binding** | [**Binding**](Binding.md)|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_45 200 response |  -  |


## delete17

> delete17(id)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        try {
            apiInstance.delete17(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete17");
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


## delete2

> delete2(id)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        try {
            apiInstance.delete2(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete2");
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


## delete23

> delete23(id, ressourceTenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            apiInstance.delete23(id, ressourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete23");
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
| **ressourceTenant** | **String**|  | |

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


## delete30

> delete30(id, tenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete30(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete30");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete45

> delete45(id, tenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete45(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete45");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete51

> delete51(id, ressourceTenant, tenant)

Delete a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete51(id, ressourceTenant, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#delete51");
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
| **ressourceTenant** | **String**|  | |
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


## find14

> PagedResultsAbstractBindingControllerBindingDetail find14(page, size, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find14(page, size, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find14");
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
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_14 200 response |  -  |


## find2

> PagedResultsAbstractBindingControllerBindingDetail find2(page, size, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find2(page, size, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find2");
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
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_2 200 response |  -  |


## find20

> PagedResultsAbstractBindingControllerBindingDetail find20(page, size, ressourceTenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find20(page, size, ressourceTenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find20");
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
| **ressourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_20 200 response |  -  |


## find28

> PagedResultsAbstractBindingControllerBindingDetail find28(page, size, tenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

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
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find28(page, size, tenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find28");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_28 200 response |  -  |


## find40

> PagedResultsAbstractBindingControllerBindingDetail find40(page, size, tenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

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
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find40(page, size, tenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find40");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_40 200 response |  -  |


## find46

> PagedResultsAbstractBindingControllerBindingDetail find46(page, size, ressourceTenant, tenant, q, sort, type, id, namespace)

Search for bindings

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        BindingType type = BindingType.fromValue("USER"); // BindingType | Binding type filter
        String id = "id_example"; // String | External id filter
        String namespace = "namespace_example"; // String | A namespace filter
        try {
            PagedResultsAbstractBindingControllerBindingDetail result = apiInstance.find46(page, size, ressourceTenant, tenant, q, sort, type, id, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#find46");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **type** | [**BindingType**](.md)| Binding type filter | [optional] [enum: USER, GROUP] |
| **id** | **String**| External id filter | [optional] |
| **namespace** | **String**| A namespace filter | [optional] |

### Return type

[**PagedResultsAbstractBindingControllerBindingDetail**](PagedResultsAbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_46 200 response |  -  |


## index1

> AbstractBindingControllerBindingDetail index1(id)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index1(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index1");
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

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_1 200 response |  -  |


## index10

> AbstractBindingControllerBindingDetail index10(id)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index10(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index10");
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

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_10 200 response |  -  |


## index15

> AbstractBindingControllerBindingDetail index15(id, ressourceTenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index15(id, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index15");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_15 200 response |  -  |


## index22

> AbstractBindingControllerBindingDetail index22(id, tenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index22(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index22");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_22 200 response |  -  |


## index31

> AbstractBindingControllerBindingDetail index31(id, tenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String tenant = "tenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index31(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index31");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_31 200 response |  -  |


## index36

> AbstractBindingControllerBindingDetail index36(id, ressourceTenant, tenant)

Get a binding

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BindingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BindingsApi apiInstance = new BindingsApi(defaultClient);
        String id = "id_example"; // String | The binding id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            AbstractBindingControllerBindingDetail result = apiInstance.index36(id, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BindingsApi#index36");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**AbstractBindingControllerBindingDetail**](AbstractBindingControllerBindingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_36 200 response |  -  |

