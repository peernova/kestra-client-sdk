# SecurityIntegrationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSecurityIntegration**](SecurityIntegrationsApi.md#createSecurityIntegration) | **POST** /api/v1/{tenant}/security-integrations | Create a security integration. |
| [**deleteSecurityIntegration**](SecurityIntegrationsApi.md#deleteSecurityIntegration) | **DELETE** /api/v1/{tenant}/security-integrations/{id} | Delete the security integration. |
| [**disableSecurityIntegration**](SecurityIntegrationsApi.md#disableSecurityIntegration) | **POST** /api/v1/{tenant}/security-integrations/{id}/disable | Disable the security integration. |
| [**enableSecurityIntegration**](SecurityIntegrationsApi.md#enableSecurityIntegration) | **POST** /api/v1/{tenant}/security-integrations/{id}/enable | Enable the security integration. |
| [**getSecurityIntegration**](SecurityIntegrationsApi.md#getSecurityIntegration) | **GET** /api/v1/{tenant}/security-integrations/{id} | Get a security integration. |
| [**listSecurityIntegrations**](SecurityIntegrationsApi.md#listSecurityIntegrations) | **GET** /api/v1/{tenant}/security-integrations | List all security integrations. |



## createSecurityIntegration

> Object createSecurityIntegration(tenant, createSecurityIntegrationRequest)

Create a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        CreateSecurityIntegrationRequest createSecurityIntegrationRequest = new CreateSecurityIntegrationRequest(); // CreateSecurityIntegrationRequest | The security integration definition
        try {
            Object result = apiInstance.createSecurityIntegration(tenant, createSecurityIntegrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#createSecurityIntegration");
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
| **createSecurityIntegrationRequest** | [**CreateSecurityIntegrationRequest**](CreateSecurityIntegrationRequest.md)| The security integration definition | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createSecurityIntegration 200 response |  -  |


## deleteSecurityIntegration

> Object deleteSecurityIntegration(id, tenant)

Delete the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.deleteSecurityIntegration(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#deleteSecurityIntegration");
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
| **id** | **String**| The ID of security integration | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteSecurityIntegration 200 response |  -  |


## disableSecurityIntegration

> Object disableSecurityIntegration(id, tenant)

Disable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.disableSecurityIntegration(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#disableSecurityIntegration");
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
| **id** | **String**| The ID of security integration | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disableSecurityIntegration 200 response |  -  |


## enableSecurityIntegration

> Object enableSecurityIntegration(id, tenant)

Enable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.enableSecurityIntegration(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#enableSecurityIntegration");
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
| **id** | **String**| The ID of security integration | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enableSecurityIntegration 200 response |  -  |


## getSecurityIntegration

> Object getSecurityIntegration(id, tenant)

Get a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.getSecurityIntegration(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#getSecurityIntegration");
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
| **id** | **String**| The ID of security integration | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSecurityIntegration 200 response |  -  |


## listSecurityIntegrations

> Object listSecurityIntegrations(tenant)

List all security integrations.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

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

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.listSecurityIntegrations(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#listSecurityIntegrations");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listSecurityIntegrations 200 response |  -  |

