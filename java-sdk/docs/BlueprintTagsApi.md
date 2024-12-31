# BlueprintTagsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blueprintTags**](BlueprintTagsApi.md#blueprintTags) | **GET** /api/v1/blueprints/community/tags | List blueprint tags matching the filter |
| [**blueprintTags1**](BlueprintTagsApi.md#blueprintTags1) | **GET** /api/v1/{tenant}/blueprints/community/tags | List blueprint tags matching the filter |
| [**internalBlueprintTags**](BlueprintTagsApi.md#internalBlueprintTags) | **GET** /api/v1/blueprints/custom/tags | List all internal blueprint tags |
| [**internalBlueprintTags1**](BlueprintTagsApi.md#internalBlueprintTags1) | **GET** /api/v1/{tenant}/blueprints/custom/tags | List all internal blueprint tags |



## blueprintTags

> List&lt;BlueprintControllerBlueprintTagItem&gt; blueprintTags(q)

List blueprint tags matching the filter

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintTagsApi apiInstance = new BlueprintTagsApi(defaultClient);
        String q = "q_example"; // String | A string filter to get tags with matching blueprints only
        try {
            List<BlueprintControllerBlueprintTagItem> result = apiInstance.blueprintTags(q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintTagsApi#blueprintTags");
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
| **q** | **String**| A string filter to get tags with matching blueprints only | [optional] |

### Return type

[**List&lt;BlueprintControllerBlueprintTagItem&gt;**](BlueprintControllerBlueprintTagItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprintTags 200 response |  -  |


## blueprintTags1

> List&lt;BlueprintControllerBlueprintTagItem&gt; blueprintTags1(tenant, q)

List blueprint tags matching the filter

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintTagsApi apiInstance = new BlueprintTagsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter to get tags with matching blueprints only
        try {
            List<BlueprintControllerBlueprintTagItem> result = apiInstance.blueprintTags1(tenant, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintTagsApi#blueprintTags1");
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
| **q** | **String**| A string filter to get tags with matching blueprints only | [optional] |

### Return type

[**List&lt;BlueprintControllerBlueprintTagItem&gt;**](BlueprintControllerBlueprintTagItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | blueprintTags_1 200 response |  -  |


## internalBlueprintTags

> List&lt;String&gt; internalBlueprintTags(q)

List all internal blueprint tags

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintTagsApi apiInstance = new BlueprintTagsApi(defaultClient);
        String q = "q_example"; // String | A string filter to get tags with matching blueprints only
        try {
            List<String> result = apiInstance.internalBlueprintTags(q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintTagsApi#internalBlueprintTags");
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
| **q** | **String**| A string filter to get tags with matching blueprints only | [optional] |

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
| **200** | internalBlueprintTags 200 response |  -  |


## internalBlueprintTags1

> List&lt;String&gt; internalBlueprintTags1(tenant, q)

List all internal blueprint tags

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.BlueprintTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        BlueprintTagsApi apiInstance = new BlueprintTagsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter to get tags with matching blueprints only
        try {
            List<String> result = apiInstance.internalBlueprintTags1(tenant, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintTagsApi#internalBlueprintTags1");
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
| **q** | **String**| A string filter to get tags with matching blueprints only | [optional] |

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
| **200** | internalBlueprintTags_1 200 response |  -  |

