# BannersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create1**](BannersApi.md#create1) | **POST** /api/v1/banners | Create a new banner |
| [**delete1**](BannersApi.md#delete1) | **DELETE** /api/v1/banners/{id} | Delete a banner |
| [**find1**](BannersApi.md#find1) | **GET** /api/v1/banners/search | Get banners |
| [**update1**](BannersApi.md#update1) | **PUT** /api/v1/banners/{id} | Update a banner |



## create1

> Banner create1(banner)

Create a new banner

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BannersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BannersApi apiInstance = new BannersApi(defaultClient);
        Banner banner = new Banner(); // Banner | 
        try {
            Banner result = apiInstance.create1(banner);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BannersApi#create1");
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
| **banner** | [**Banner**](Banner.md)|  | |

### Return type

[**Banner**](Banner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_1 200 response |  -  |


## delete1

> delete1(id)

Delete a banner

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BannersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BannersApi apiInstance = new BannersApi(defaultClient);
        String id = "id_example"; // String | The banner id
        try {
            apiInstance.delete1(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling BannersApi#delete1");
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
| **id** | **String**| The banner id | |

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
| **200** | delete_1 200 response |  -  |


## find1

> List&lt;Banner&gt; find1()

Get banners

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BannersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BannersApi apiInstance = new BannersApi(defaultClient);
        try {
            List<Banner> result = apiInstance.find1();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BannersApi#find1");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List&lt;Banner&gt;**](Banner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_1 200 response |  -  |


## update1

> Banner update1(id, banner)

Update a banner

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BannersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BannersApi apiInstance = new BannersApi(defaultClient);
        String id = "id_example"; // String | The banner id
        Banner banner = new Banner(); // Banner | 
        try {
            Banner result = apiInstance.update1(id, banner);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BannersApi#update1");
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
| **id** | **String**| The banner id | |
| **banner** | [**Banner**](Banner.md)|  | |

### Return type

[**Banner**](Banner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_1 200 response |  -  |

