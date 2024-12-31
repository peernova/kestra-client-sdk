# MiscApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actions**](MiscApi.md#actions) | **GET** /api/v1/acls/actions | Get list of actions |
| [**actions1**](MiscApi.md#actions1) | **GET** /api/v1/{tenant}/acls/actions | Get list of actions |
| [**addBasicAuth**](MiscApi.md#addBasicAuth) | **POST** /api/v1/basicAuth | Add basic auth to current instance |
| [**addBasicAuth1**](MiscApi.md#addBasicAuth1) | **POST** /api/v1/{tenant}/basicAuth | Add basic auth to current instance |
| [**callConfiguration**](MiscApi.md#callConfiguration) | **GET** /api/v1/configs | Get current configurations |
| [**configuration1**](MiscApi.md#configuration1) | **GET** /api/v1/{tenant}/configs | Get current configurations |
| [**licenseInfo**](MiscApi.md#licenseInfo) | **GET** /api/v1/license-info | Get current license information |
| [**permissions**](MiscApi.md#permissions) | **GET** /api/v1/acls/permissions | Get list of permissions |
| [**permissions1**](MiscApi.md#permissions1) | **GET** /api/v1/{tenant}/acls/permissions | Get list of permissions |
| [**setupConfiguration**](MiscApi.md#setupConfiguration) | **GET** /api/v1/setup | Currently running configuration |
| [**setupKestra**](MiscApi.md#setupKestra) | **POST** /api/v1/setup | Create the first user |
| [**tenantUsage**](MiscApi.md#tenantUsage) | **GET** /api/v1/usages | Get instance usage information for the current tenant |
| [**tenantUsage1**](MiscApi.md#tenantUsage1) | **GET** /api/v1/{tenant}/usages | Get instance usage information for the current tenant |
| [**usages**](MiscApi.md#usages) | **GET** /api/v1/usages/all | Get instance usage information |
| [**usages1**](MiscApi.md#usages1) | **GET** /api/v1/{tenant}/usages/all | Get instance usage information |



## actions

> List&lt;Action&gt; actions()

Get list of actions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            List<Action> result = apiInstance.actions();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#actions");
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

[**List&lt;Action&gt;**](Action.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | actions 200 response |  -  |


## actions1

> List&lt;Action&gt; actions1(tenant)

Get list of actions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Action> result = apiInstance.actions1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#actions1");
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

[**List&lt;Action&gt;**](Action.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | actions_1 200 response |  -  |


## addBasicAuth

> addBasicAuth(miscControllerBasicAuthCredentials)

Add basic auth to current instance

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        MiscControllerBasicAuthCredentials miscControllerBasicAuthCredentials = new MiscControllerBasicAuthCredentials(); // MiscControllerBasicAuthCredentials | 
        try {
            apiInstance.addBasicAuth(miscControllerBasicAuthCredentials);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#addBasicAuth");
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
| **miscControllerBasicAuthCredentials** | [**MiscControllerBasicAuthCredentials**](MiscControllerBasicAuthCredentials.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addBasicAuth 200 response |  -  |


## addBasicAuth1

> addBasicAuth1(tenant, miscControllerBasicAuthCredentials)

Add basic auth to current instance

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        MiscControllerBasicAuthCredentials miscControllerBasicAuthCredentials = new MiscControllerBasicAuthCredentials(); // MiscControllerBasicAuthCredentials | 
        try {
            apiInstance.addBasicAuth1(tenant, miscControllerBasicAuthCredentials);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#addBasicAuth1");
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
| **miscControllerBasicAuthCredentials** | [**MiscControllerBasicAuthCredentials**](MiscControllerBasicAuthCredentials.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addBasicAuth_1 200 response |  -  |


## callConfiguration

> MiscControllerConfigurationEe callConfiguration()

Get current configurations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            MiscControllerConfigurationEe result = apiInstance.callConfiguration();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#callConfiguration");
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

[**MiscControllerConfigurationEe**](MiscControllerConfigurationEe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | configuration 200 response |  -  |


## configuration1

> MiscControllerConfigurationEe configuration1(tenant)

Get current configurations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            MiscControllerConfigurationEe result = apiInstance.configuration1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#configuration1");
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

[**MiscControllerConfigurationEe**](MiscControllerConfigurationEe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | configuration_1 200 response |  -  |


## licenseInfo

> MiscControllerLicenseInfo licenseInfo()

Get current license information

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            MiscControllerLicenseInfo result = apiInstance.licenseInfo();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#licenseInfo");
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

[**MiscControllerLicenseInfo**](MiscControllerLicenseInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | licenseInfo 200 response |  -  |


## permissions

> List&lt;Permission&gt; permissions()

Get list of permissions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            List<Permission> result = apiInstance.permissions();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#permissions");
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

[**List&lt;Permission&gt;**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | permissions 200 response |  -  |


## permissions1

> List&lt;Permission&gt; permissions1(tenant)

Get list of permissions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Permission> result = apiInstance.permissions1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#permissions1");
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

[**List&lt;Permission&gt;**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | permissions_1 200 response |  -  |


## setupConfiguration

> SetupConfiguration setupConfiguration()

Currently running configuration

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            SetupConfiguration result = apiInstance.setupConfiguration();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#setupConfiguration");
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

[**SetupConfiguration**](SetupConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setupConfiguration 200 response |  -  |


## setupKestra

> ApiUser setupKestra(setupConfigurationSetupData)

Create the first user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        SetupConfigurationSetupData setupConfigurationSetupData = new SetupConfigurationSetupData(); // SetupConfigurationSetupData | 
        try {
            ApiUser result = apiInstance.setupKestra(setupConfigurationSetupData);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#setupKestra");
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
| **setupConfigurationSetupData** | [**SetupConfigurationSetupData**](SetupConfigurationSetupData.md)|  | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setupKestra 200 response |  -  |


## tenantUsage

> TenantUsage200Response tenantUsage()

Get instance usage information for the current tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            TenantUsage200Response result = apiInstance.tenantUsage();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#tenantUsage");
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

[**TenantUsage200Response**](TenantUsage200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tenantUsage 200 response |  -  |


## tenantUsage1

> TenantUsage1200Response tenantUsage1(tenant)

Get instance usage information for the current tenant

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            TenantUsage1200Response result = apiInstance.tenantUsage1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#tenantUsage1");
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

[**TenantUsage1200Response**](TenantUsage1200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tenantUsage_1 200 response |  -  |


## usages

> Usage usages()

Get instance usage information

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        try {
            Usage result = apiInstance.usages();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#usages");
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

[**Usage**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | usages 200 response |  -  |


## usages1

> Usage usages1(tenant)

Get instance usage information

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MiscApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MiscApi apiInstance = new MiscApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Usage result = apiInstance.usages1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MiscApi#usages1");
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

[**Usage**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | usages_1 200 response |  -  |

