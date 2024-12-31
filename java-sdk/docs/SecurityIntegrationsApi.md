# SecurityIntegrationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create12**](SecurityIntegrationsApi.md#create12) | **POST** /api/v1/security-integrations | Create a security integration. |
| [**create37**](SecurityIntegrationsApi.md#create37) | **POST** /api/v1/{tenant}/security-integrations | Create a security integration. |
| [**delete15**](SecurityIntegrationsApi.md#delete15) | **DELETE** /api/v1/security-integrations/{id} | Delete the security integration. |
| [**delete43**](SecurityIntegrationsApi.md#delete43) | **DELETE** /api/v1/{tenant}/security-integrations/{id} | Delete the security integration. |
| [**disable1**](SecurityIntegrationsApi.md#disable1) | **POST** /api/v1/security-integrations/{id}/disable | Disable the security integration. |
| [**disable3**](SecurityIntegrationsApi.md#disable3) | **POST** /api/v1/{tenant}/security-integrations/{id}/disable | Disable the security integration. |
| [**enable1**](SecurityIntegrationsApi.md#enable1) | **POST** /api/v1/security-integrations/{id}/enable | Enable the security integration. |
| [**enable3**](SecurityIntegrationsApi.md#enable3) | **POST** /api/v1/{tenant}/security-integrations/{id}/enable | Enable the security integration. |
| [**index29**](SecurityIntegrationsApi.md#index29) | **GET** /api/v1/{tenant}/security-integrations/{id} | Get a security integration. |
| [**index8**](SecurityIntegrationsApi.md#index8) | **GET** /api/v1/security-integrations/{id} | Get a security integration. |
| [**list3**](SecurityIntegrationsApi.md#list3) | **GET** /api/v1/security-integrations | List all security integrations. |
| [**list7**](SecurityIntegrationsApi.md#list7) | **GET** /api/v1/{tenant}/security-integrations | List all security integrations. |



## create12

> Object create12(createSecurityIntegrationRequest)

Create a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        CreateSecurityIntegrationRequest createSecurityIntegrationRequest = new CreateSecurityIntegrationRequest(); // CreateSecurityIntegrationRequest | 
        try {
            Object result = apiInstance.create12(createSecurityIntegrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#create12");
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
| **createSecurityIntegrationRequest** | [**CreateSecurityIntegrationRequest**](CreateSecurityIntegrationRequest.md)|  | |

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
| **200** | create_12 200 response |  -  |


## create37

> Object create37(tenant, createSecurityIntegrationRequest)

Create a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        CreateSecurityIntegrationRequest createSecurityIntegrationRequest = new CreateSecurityIntegrationRequest(); // CreateSecurityIntegrationRequest | 
        try {
            Object result = apiInstance.create37(tenant, createSecurityIntegrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#create37");
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
| **createSecurityIntegrationRequest** | [**CreateSecurityIntegrationRequest**](CreateSecurityIntegrationRequest.md)|  | |

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
| **200** | create_37 200 response |  -  |


## delete15

> Object delete15(id)

Delete the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        try {
            Object result = apiInstance.delete15(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#delete15");
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
| **200** | delete_15 200 response |  -  |


## delete43

> Object delete43(id, tenant)

Delete the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.delete43(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#delete43");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_43 200 response |  -  |


## disable1

> Object disable1(id)

Disable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        try {
            Object result = apiInstance.disable1(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#disable1");
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
| **200** | disable_1 200 response |  -  |


## disable3

> Object disable3(id, tenant)

Disable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.disable3(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#disable3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disable_3 200 response |  -  |


## enable1

> Object enable1(id)

Enable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        try {
            Object result = apiInstance.enable1(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#enable1");
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
| **200** | enable_1 200 response |  -  |


## enable3

> Object enable3(id, tenant)

Enable the security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.enable3(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#enable3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enable_3 200 response |  -  |


## index29

> Object index29(id, tenant)

Get a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.index29(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#index29");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_29 200 response |  -  |


## index8

> Object index8(id)

Get a security integration.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String id = "id_example"; // String | The ID of security integration
        try {
            Object result = apiInstance.index8(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#index8");
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
| **200** | index_8 200 response |  -  |


## list3

> Object list3()

List all security integrations.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        try {
            Object result = apiInstance.list3();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#list3");
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
| **200** | list_3 200 response |  -  |


## list7

> Object list7(tenant)

List all security integrations.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.SecurityIntegrationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        SecurityIntegrationsApi apiInstance = new SecurityIntegrationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.list7(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SecurityIntegrationsApi#list7");
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
| **200** | list_7 200 response |  -  |

