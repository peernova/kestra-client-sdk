# AuthsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApiToken**](AuthsApi.md#createApiToken) | **POST** /api/v1/me/api-tokens | Create new API Token for authenticated user |
| [**createApiToken1**](AuthsApi.md#createApiToken1) | **POST** /api/v1/{tenant}/me/api-tokens | Create new API Token for authenticated user |
| [**deleteApiToken**](AuthsApi.md#deleteApiToken) | **DELETE** /api/v1/me/api-tokens/{tokenId} | Delete an API Token for authenticated user |
| [**deleteApiToken4**](AuthsApi.md#deleteApiToken4) | **DELETE** /api/v1/{tenant}/me/api-tokens/{tokenId} | Delete an API Token for authenticated user |
| [**index**](AuthsApi.md#index) | **GET** /api/v1/auths | Get list of authentification methods |
| [**index26**](AuthsApi.md#index26) | **GET** /api/v1/{tenant}/me | Get current user |
| [**index5**](AuthsApi.md#index5) | **GET** /api/v1/me | Get current user |
| [**listApiTokens**](AuthsApi.md#listApiTokens) | **GET** /api/v1/me/api-tokens | List all API Tokens for the authenticated user |
| [**listApiTokens4**](AuthsApi.md#listApiTokens4) | **GET** /api/v1/{tenant}/me/api-tokens | List all API Tokens for the authenticated user |
| [**patch2**](AuthsApi.md#patch2) | **PATCH** /api/v1/me | Updates details for the current user. Returns user&#39;s updated information upon success. |
| [**patch5**](AuthsApi.md#patch5) | **PATCH** /api/v1/{tenant}/me | Updates details for the current user. Returns user&#39;s updated information upon success. |



## createApiToken

> Object createApiToken(createApiTokenRequest)

Create new API Token for authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        CreateApiTokenRequest createApiTokenRequest = new CreateApiTokenRequest(); // CreateApiTokenRequest | 
        try {
            Object result = apiInstance.createApiToken(createApiTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#createApiToken");
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
| **createApiTokenRequest** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)|  | |

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
| **200** | createApiToken 200 response |  -  |


## createApiToken1

> Object createApiToken1(tenant, createApiTokenRequest)

Create new API Token for authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        CreateApiTokenRequest createApiTokenRequest = new CreateApiTokenRequest(); // CreateApiTokenRequest | 
        try {
            Object result = apiInstance.createApiToken1(tenant, createApiTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#createApiToken1");
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
| **createApiTokenRequest** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)|  | |

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
| **200** | createApiToken_1 200 response |  -  |


## deleteApiToken

> Object deleteApiToken(tokenId)

Delete an API Token for authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tokenId = "tokenId_example"; // String | The token id
        try {
            Object result = apiInstance.deleteApiToken(tokenId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#deleteApiToken");
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
| **tokenId** | **String**| The token id | |

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
| **200** | deleteApiToken 200 response |  -  |


## deleteApiToken4

> Object deleteApiToken4(tokenId, tenant)

Delete an API Token for authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tokenId = "tokenId_example"; // String | The token id
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.deleteApiToken4(tokenId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#deleteApiToken4");
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
| **tokenId** | **String**| The token id | |
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
| **200** | deleteApiToken_4 200 response |  -  |


## index

> AuthControllerAuth index()

Get list of authentification methods

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        try {
            AuthControllerAuth result = apiInstance.index();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#index");
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

[**AuthControllerAuth**](AuthControllerAuth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index 200 response |  -  |


## index26

> MeControllerMe index26(tenant)

Get current user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            MeControllerMe result = apiInstance.index26(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#index26");
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

### Return type

[**MeControllerMe**](MeControllerMe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_26 200 response |  -  |


## index5

> MeControllerMe index5()

Get current user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        try {
            MeControllerMe result = apiInstance.index5();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#index5");
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

[**MeControllerMe**](MeControllerMe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_5 200 response |  -  |


## listApiTokens

> Object listApiTokens()

List all API Tokens for the authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        try {
            Object result = apiInstance.listApiTokens();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#listApiTokens");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listApiTokens 200 response |  -  |


## listApiTokens4

> Object listApiTokens4(tenant)

List all API Tokens for the authenticated user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.listApiTokens4(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#listApiTokens4");
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
| **200** | listApiTokens_4 200 response |  -  |


## patch2

> Object patch2(meControllerUserDetailsRequest)

Updates details for the current user. Returns user&#39;s updated information upon success.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        MeControllerUserDetailsRequest meControllerUserDetailsRequest = new MeControllerUserDetailsRequest(); // MeControllerUserDetailsRequest | 
        try {
            Object result = apiInstance.patch2(meControllerUserDetailsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#patch2");
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
| **meControllerUserDetailsRequest** | [**MeControllerUserDetailsRequest**](MeControllerUserDetailsRequest.md)|  | |

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
| **200** | patch_2 200 response |  -  |


## patch5

> Object patch5(tenant, meControllerUserDetailsRequest)

Updates details for the current user. Returns user&#39;s updated information upon success.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuthsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuthsApi apiInstance = new AuthsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        MeControllerUserDetailsRequest meControllerUserDetailsRequest = new MeControllerUserDetailsRequest(); // MeControllerUserDetailsRequest | 
        try {
            Object result = apiInstance.patch5(tenant, meControllerUserDetailsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthsApi#patch5");
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
| **meControllerUserDetailsRequest** | [**MeControllerUserDetailsRequest**](MeControllerUserDetailsRequest.md)|  | |

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
| **200** | patch_5 200 response |  -  |

