# TenantsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create14**](TenantsApi.md#create14) | **POST** /api/v1/tenants | Create a tenant |
| [**create39**](TenantsApi.md#create39) | **POST** /api/v1/{tenant}/tenants | Create a tenant |
| [**delete22**](TenantsApi.md#delete22) | **DELETE** /api/v1/tenants/{id} | Delete a tenant |
| [**delete50**](TenantsApi.md#delete50) | **DELETE** /api/v1/{tenant}/tenants/{id} | Delete a tenant |
| [**find18**](TenantsApi.md#find18) | **GET** /api/v1/tenants/search | Search for tenants |
| [**find44**](TenantsApi.md#find44) | **GET** /api/v1/{tenant}/tenants/search | Search for tenants |
| [**get14**](TenantsApi.md#get14) | **GET** /api/v1/{tenant}/tenants/{id} | Get a tenant |
| [**get6**](TenantsApi.md#get6) | **GET** /api/v1/tenants/{id} | Get a tenant |
| [**setLogo**](TenantsApi.md#setLogo) | **POST** /api/v1/tenants/{id}/logo | Set a tenant logo |
| [**setLogo1**](TenantsApi.md#setLogo1) | **POST** /api/v1/{tenant}/tenants/{id}/logo | Set a tenant logo |
| [**update13**](TenantsApi.md#update13) | **PUT** /api/v1/tenants/{id} | Update a tenant |
| [**update31**](TenantsApi.md#update31) | **PUT** /api/v1/{tenant}/tenants/{id} | Update a tenant |



## create14

> Tenant create14(tenant)

Create a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        Tenant tenant = new Tenant(); // Tenant | 
        try {
            Tenant result = apiInstance.create14(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#create14");
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
| **tenant** | [**Tenant**](Tenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_14 200 response |  -  |


## create39

> Tenant create39(tenant, tenant2)

Create a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Tenant tenant2 = new Tenant(); // Tenant | 
        try {
            Tenant result = apiInstance.create39(tenant, tenant2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#create39");
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
| **tenant2** | [**Tenant**](Tenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_39 200 response |  -  |


## delete22

> delete22(id)

Delete a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        try {
            apiInstance.delete22(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#delete22");
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
| **id** | **String**| The tenant id | |

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


## delete50

> delete50(id, tenant)

Delete a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete50(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#delete50");
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
| **id** | **String**| The tenant id | |
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


## find18

> PagedResultsTenant find18(page, size, q, sort)

Search for tenants

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsTenant result = apiInstance.find18(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#find18");
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

### Return type

[**PagedResultsTenant**](PagedResultsTenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_18 200 response |  -  |


## find44

> PagedResultsTenant find44(page, size, tenant, q, sort)

Search for tenants

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsTenant result = apiInstance.find44(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#find44");
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

### Return type

[**PagedResultsTenant**](PagedResultsTenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_44 200 response |  -  |


## get14

> Tenant get14(id, tenant)

Get a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        String tenant = "tenant_example"; // String | 
        try {
            Tenant result = apiInstance.get14(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#get14");
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
| **id** | **String**| The tenant id | |
| **tenant** | **String**|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_14 200 response |  -  |


## get6

> Tenant get6(id)

Get a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        try {
            Tenant result = apiInstance.get6(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#get6");
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
| **id** | **String**| The tenant id | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_6 200 response |  -  |


## setLogo

> ApiTenant setLogo(id, logo)

Set a tenant logo

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        File logo = new File("/path/to/file"); // File | The logo file
        try {
            ApiTenant result = apiInstance.setLogo(id, logo);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#setLogo");
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
| **id** | **String**| The tenant id | |
| **logo** | **File**| The logo file | [optional] |

### Return type

[**ApiTenant**](ApiTenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setLogo 200 response |  -  |


## setLogo1

> ApiTenant setLogo1(id, tenant, logo)

Set a tenant logo

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        String tenant = "tenant_example"; // String | 
        File logo = new File("/path/to/file"); // File | The logo file
        try {
            ApiTenant result = apiInstance.setLogo1(id, tenant, logo);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#setLogo1");
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
| **id** | **String**| The tenant id | |
| **tenant** | **String**|  | |
| **logo** | **File**| The logo file | [optional] |

### Return type

[**ApiTenant**](ApiTenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setLogo_1 200 response |  -  |


## update13

> Tenant update13(id, tenant)

Update a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        Tenant tenant = new Tenant(); // Tenant | 
        try {
            Tenant result = apiInstance.update13(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#update13");
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
| **id** | **String**| The tenant id | |
| **tenant** | [**Tenant**](Tenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_13 200 response |  -  |


## update31

> Tenant update31(id, tenant, tenant2)

Update a tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TenantsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TenantsApi apiInstance = new TenantsApi(defaultClient);
        String id = "id_example"; // String | The tenant id
        String tenant = "tenant_example"; // String | 
        Tenant tenant2 = new Tenant(); // Tenant | 
        try {
            Tenant result = apiInstance.update31(id, tenant, tenant2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#update31");
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
| **id** | **String**| The tenant id | |
| **tenant** | **String**|  | |
| **tenant2** | [**Tenant**](Tenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_31 200 response |  -  |

