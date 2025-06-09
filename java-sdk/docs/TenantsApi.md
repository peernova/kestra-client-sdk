# TenantsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create**](TenantsApi.md#create) | **POST** /api/v1/tenants | Create a tenant |
| [**delete**](TenantsApi.md#delete) | **DELETE** /api/v1/tenants/{id} | Delete a tenant and all its resources (flows, namespaces, apps, ... |
| [**find**](TenantsApi.md#find) | **GET** /api/v1/tenants/search | Search for tenants |
| [**get**](TenantsApi.md#get) | **GET** /api/v1/tenants/{id} | Get a tenant |
| [**setLogo**](TenantsApi.md#setLogo) | **POST** /api/v1/tenants/{id}/logo | Set a tenant logo |
| [**update**](TenantsApi.md#update) | **PUT** /api/v1/tenants/{id} | Update a tenant |



## create

> Tenant create(tenant)

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
            Tenant result = apiInstance.create(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#create");
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
| **200** | create 200 response |  -  |


## delete

> delete(id)

Delete a tenant and all its resources (flows, namespaces, apps, ...

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
            apiInstance.delete(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#delete");
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


## find

> PagedResultsTenant find(page, size, q, sort)

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
            PagedResultsTenant result = apiInstance.find(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#find");
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
| **200** | find 200 response |  -  |


## get

> Tenant get(id)

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
            Tenant result = apiInstance.get(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#get");
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
| **200** | get 200 response |  -  |


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


## update

> Tenant update(id, tenant)

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
            Tenant result = apiInstance.update(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TenantsApi#update");
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
| **200** | update 200 response |  -  |

