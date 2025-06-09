# BlueprintTagsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**internalBlueprintTags**](BlueprintTagsApi.md#internalBlueprintTags) | **GET** /api/v1/{tenant}/blueprints/custom/tags | List all internal blueprint tags |
| [**listBlueprintTags**](BlueprintTagsApi.md#listBlueprintTags) | **GET** /api/v1/{tenant}/blueprints/community/{kind}/tags | List blueprint tags matching the filter |



## internalBlueprintTags

> List&lt;String&gt; internalBlueprintTags(tenant, q)

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
            List<String> result = apiInstance.internalBlueprintTags(tenant, q);
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
| **200** | internalBlueprintTags 200 response |  -  |


## listBlueprintTags

> List&lt;BlueprintControllerApiBlueprintTagItem&gt; listBlueprintTags(kind, tenant, q)

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
        BlueprintControllerKind kind = BlueprintControllerKind.fromValue("APP"); // BlueprintControllerKind | The blueprint kind
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter to get tags with matching blueprints only
        try {
            List<BlueprintControllerApiBlueprintTagItem> result = apiInstance.listBlueprintTags(kind, tenant, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlueprintTagsApi#listBlueprintTags");
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
| **kind** | [**BlueprintControllerKind**](.md)| The blueprint kind | [enum: APP, DASHBOARD, FLOW] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter to get tags with matching blueprints only | [optional] |

### Return type

[**List&lt;BlueprintControllerApiBlueprintTagItem&gt;**](BlueprintControllerApiBlueprintTagItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listBlueprintTags 200 response |  -  |

