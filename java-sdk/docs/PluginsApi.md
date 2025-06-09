# PluginsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllInputTypes**](PluginsApi.md#getAllInputTypes) | **GET** /api/v1/{tenant}/plugins/inputs | Get all types for an inputs |
| [**getPluginBySubgroups**](PluginsApi.md#getPluginBySubgroups) | **GET** /api/v1/{tenant}/plugins/groups/subgroups | Get plugins group by subgroups |
| [**getPluginDocumentation**](PluginsApi.md#getPluginDocumentation) | **GET** /api/v1/{tenant}/plugins/{cls} | Get plugin documentation |
| [**getPluginDocumentationFromVersion**](PluginsApi.md#getPluginDocumentationFromVersion) | **GET** /api/v1/{tenant}/plugins/{cls}/versions/{version} | Get plugin documentation |
| [**getPluginGroupIcons**](PluginsApi.md#getPluginGroupIcons) | **GET** /api/v1/{tenant}/plugins/icons/groups | Get plugins icons |
| [**getPluginIcons**](PluginsApi.md#getPluginIcons) | **GET** /api/v1/{tenant}/plugins/icons | Get plugins icons |
| [**getPluginVersions**](PluginsApi.md#getPluginVersions) | **GET** /api/v1/{tenant}/plugins/{cls}/versions | Get all versions for a plugin |
| [**getSchemaFromInputType**](PluginsApi.md#getSchemaFromInputType) | **GET** /api/v1/{tenant}/plugins/inputs/{type} | Get json schemas for an input type |
| [**getSchemasFromType**](PluginsApi.md#getSchemasFromType) | **GET** /api/v1/{tenant}/plugins/schemas/{type} | Get all json schemas for a type |
| [**getVersionedPluginDetails**](PluginsApi.md#getVersionedPluginDetails) | **GET** /api/v1/{tenant}/cluster/versioned-plugins/{groupId}/{artifactId} | Get details about a Kestra&#39;s plugin artifact. |
| [**getVersionedPluginDetailsFromVersion**](PluginsApi.md#getVersionedPluginDetailsFromVersion) | **GET** /api/v1/{tenant}/cluster/versioned-plugins/{groupId}/{artifactId}/{version} | Get details about a specific Kestra&#39;s plugin artifact version. |
| [**installVersionedPlugins**](PluginsApi.md#installVersionedPlugins) | **POST** /api/v1/{tenant}/cluster/versioned-plugins/install | Install a specific Kestra&#39;s plugin artifact |
| [**listAvailableVersionedPlugins**](PluginsApi.md#listAvailableVersionedPlugins) | **GET** /api/v1/{tenant}/cluster/versioned-plugins/available | Get the list of available Kestra&#39;s plugin artifact. |
| [**listPlugins**](PluginsApi.md#listPlugins) | **GET** /api/v1/{tenant}/plugins | Get list of plugins |
| [**listVersionedPlugin**](PluginsApi.md#listVersionedPlugin) | **GET** /api/v1/{tenant}/cluster/versioned-plugins | Get the list of installed Kestra&#39;s plugin artifact. |
| [**resolveVersionedPlugins**](PluginsApi.md#resolveVersionedPlugins) | **POST** /api/v1/{tenant}/cluster/versioned-plugins/resolve | Resolve a specific Kestra&#39;s plugin artifact |
| [**uninstallVersionedPlugins**](PluginsApi.md#uninstallVersionedPlugins) | **DELETE** /api/v1/{tenant}/cluster/versioned-plugins/uninstall | Uninstall Kestra&#39;s plugin artifacts |
| [**uploadVersionedPlugins**](PluginsApi.md#uploadVersionedPlugins) | **POST** /api/v1/{tenant}/cluster/versioned-plugins/upload | Upload a Kestra&#39;s plugin artifact |



## getAllInputTypes

> List&lt;InputType&gt; getAllInputTypes(tenant)

Get all types for an inputs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<InputType> result = apiInstance.getAllInputTypes(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getAllInputTypes");
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

[**List&lt;InputType&gt;**](InputType.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAllInputTypes 200 response |  -  |


## getPluginBySubgroups

> List&lt;Plugin&gt; getPluginBySubgroups(includeDeprecated, tenant)

Get plugins group by subgroups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        Boolean includeDeprecated = true; // Boolean | Whether to include deprecated plugins
        String tenant = "tenant_example"; // String | 
        try {
            List<Plugin> result = apiInstance.getPluginBySubgroups(includeDeprecated, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginBySubgroups");
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
| **includeDeprecated** | **Boolean**| Whether to include deprecated plugins | [default to true] |
| **tenant** | **String**|  | |

### Return type

[**List&lt;Plugin&gt;**](Plugin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginBySubgroups 200 response |  -  |


## getPluginDocumentation

> DocumentationWithSchema getPluginDocumentation(cls, all, tenant)

Get plugin documentation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String cls = "cls_example"; // String | The plugin full class name
        Boolean all = false; // Boolean | Include all the properties
        String tenant = "tenant_example"; // String | 
        try {
            DocumentationWithSchema result = apiInstance.getPluginDocumentation(cls, all, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginDocumentation");
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
| **cls** | **String**| The plugin full class name | |
| **all** | **Boolean**| Include all the properties | [default to false] |
| **tenant** | **String**|  | |

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginDocumentation 200 response |  -  |


## getPluginDocumentationFromVersion

> DocumentationWithSchema getPluginDocumentationFromVersion(cls, version, all, tenant)

Get plugin documentation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String cls = "cls_example"; // String | The plugin type
        String version = "version_example"; // String | The plugin version
        Boolean all = false; // Boolean | Include all the properties
        String tenant = "tenant_example"; // String | 
        try {
            DocumentationWithSchema result = apiInstance.getPluginDocumentationFromVersion(cls, version, all, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginDocumentationFromVersion");
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
| **cls** | **String**| The plugin type | |
| **version** | **String**| The plugin version | |
| **all** | **Boolean**| Include all the properties | [default to false] |
| **tenant** | **String**|  | |

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginDocumentationFromVersion 200 response |  -  |


## getPluginGroupIcons

> Map&lt;String, PluginIcon&gt; getPluginGroupIcons(tenant)

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, PluginIcon> result = apiInstance.getPluginGroupIcons(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginGroupIcons");
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

[**Map&lt;String, PluginIcon&gt;**](PluginIcon.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginGroupIcons 200 response |  -  |


## getPluginIcons

> Map&lt;String, PluginIcon&gt; getPluginIcons(tenant)

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, PluginIcon> result = apiInstance.getPluginIcons(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginIcons");
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

[**Map&lt;String, PluginIcon&gt;**](PluginIcon.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginIcons 200 response |  -  |


## getPluginVersions

> PluginControllerApiPluginVersions getPluginVersions(cls, tenant)

Get all versions for a plugin

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String cls = "cls_example"; // String | The plugin type
        String tenant = "tenant_example"; // String | 
        try {
            PluginControllerApiPluginVersions result = apiInstance.getPluginVersions(cls, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getPluginVersions");
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
| **cls** | **String**| The plugin type | |
| **tenant** | **String**|  | |

### Return type

[**PluginControllerApiPluginVersions**](PluginControllerApiPluginVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPluginVersions 200 response |  -  |


## getSchemaFromInputType

> DocumentationWithSchema getSchemaFromInputType(type, tenant)

Get json schemas for an input type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        Type type = Type.fromValue("STRING"); // Type | The schema needed
        String tenant = "tenant_example"; // String | 
        try {
            DocumentationWithSchema result = apiInstance.getSchemaFromInputType(type, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getSchemaFromInputType");
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
| **type** | [**Type**](.md)| The schema needed | [enum: STRING, ENUM, SELECT, INT, FLOAT, BOOLEAN, BOOL, DATETIME, DATE, TIME, DURATION, FILE, JSON, URI, SECRET, ARRAY, MULTISELECT, YAML, EMAIL] |
| **tenant** | **String**|  | |

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSchemaFromInputType 200 response |  -  |


## getSchemasFromType

> Map&lt;String, Object&gt; getSchemasFromType(type, arrayOf, tenant)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        SchemaType type = SchemaType.fromValue("FLOW"); // SchemaType | The schema needed
        Boolean arrayOf = false; // Boolean | If schema should be an array of requested type
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, Object> result = apiInstance.getSchemasFromType(type, arrayOf, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getSchemasFromType");
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
| **type** | [**SchemaType**](.md)| The schema needed | [enum: FLOW, TEMPLATE, TASK, TRIGGER, PLUGINDEFAULT, APPS, TESTSUITES, DASHBOARD] |
| **arrayOf** | **Boolean**| If schema should be an array of requested type | [default to false] |
| **tenant** | **String**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSchemasFromType 200 response |  -  |


## getVersionedPluginDetails

> ClusterControllerApiPluginVersions getVersionedPluginDetails(groupId, artifactId, tenant)

Get details about a Kestra&#39;s plugin artifact.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String groupId = "groupId_example"; // String | 
        String artifactId = "artifactId_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ClusterControllerApiPluginVersions result = apiInstance.getVersionedPluginDetails(groupId, artifactId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getVersionedPluginDetails");
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
| **groupId** | **String**|  | |
| **artifactId** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ClusterControllerApiPluginVersions**](ClusterControllerApiPluginVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getVersionedPluginDetails 200 response |  -  |


## getVersionedPluginDetailsFromVersion

> ClusterControllerApiPluginVersionDetails getVersionedPluginDetailsFromVersion(groupId, artifactId, version, tenant)

Get details about a specific Kestra&#39;s plugin artifact version.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String groupId = "groupId_example"; // String | 
        String artifactId = "artifactId_example"; // String | 
        String version = "version_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ClusterControllerApiPluginVersionDetails result = apiInstance.getVersionedPluginDetailsFromVersion(groupId, artifactId, version, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#getVersionedPluginDetailsFromVersion");
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
| **groupId** | **String**|  | |
| **artifactId** | **String**|  | |
| **version** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ClusterControllerApiPluginVersionDetails**](ClusterControllerApiPluginVersionDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getVersionedPluginDetailsFromVersion 200 response |  -  |


## installVersionedPlugins

> ClusterControllerApiPluginArtifactListPluginArtifact installVersionedPlugins(tenant, clusterControllerApiPluginListRequest)

Install a specific Kestra&#39;s plugin artifact

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ClusterControllerApiPluginListRequest clusterControllerApiPluginListRequest = new ClusterControllerApiPluginListRequest(); // ClusterControllerApiPluginListRequest | List of plugins
        try {
            ClusterControllerApiPluginArtifactListPluginArtifact result = apiInstance.installVersionedPlugins(tenant, clusterControllerApiPluginListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#installVersionedPlugins");
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
| **clusterControllerApiPluginListRequest** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | |

### Return type

[**ClusterControllerApiPluginArtifactListPluginArtifact**](ClusterControllerApiPluginArtifactListPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | installVersionedPlugins 200 response |  -  |


## listAvailableVersionedPlugins

> Object listAvailableVersionedPlugins(tenant)

Get the list of available Kestra&#39;s plugin artifact.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.listAvailableVersionedPlugins(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#listAvailableVersionedPlugins");
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
| **200** | listAvailableVersionedPlugins 200 response |  -  |


## listPlugins

> List&lt;Plugin&gt; listPlugins(tenant)

Get list of plugins

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Plugin> result = apiInstance.listPlugins(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#listPlugins");
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

[**List&lt;Plugin&gt;**](Plugin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listPlugins 200 response |  -  |


## listVersionedPlugin

> PagedResultsClusterControllerApiPluginArtifact listVersionedPlugin(page, size, tenant, sort, q)

Get the list of installed Kestra&#39;s plugin artifact.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | The query
        try {
            PagedResultsClusterControllerApiPluginArtifact result = apiInstance.listVersionedPlugin(page, size, tenant, sort, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#listVersionedPlugin");
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
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **q** | **String**| The query | [optional] |

### Return type

[**PagedResultsClusterControllerApiPluginArtifact**](PagedResultsClusterControllerApiPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listVersionedPlugin 200 response |  -  |


## resolveVersionedPlugins

> ClusterControllerApiPluginArtifactListPluginResolutionResult resolveVersionedPlugins(tenant, clusterControllerApiPluginListRequest)

Resolve a specific Kestra&#39;s plugin artifact

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ClusterControllerApiPluginListRequest clusterControllerApiPluginListRequest = new ClusterControllerApiPluginListRequest(); // ClusterControllerApiPluginListRequest | List of plugins
        try {
            ClusterControllerApiPluginArtifactListPluginResolutionResult result = apiInstance.resolveVersionedPlugins(tenant, clusterControllerApiPluginListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#resolveVersionedPlugins");
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
| **clusterControllerApiPluginListRequest** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | |

### Return type

[**ClusterControllerApiPluginArtifactListPluginResolutionResult**](ClusterControllerApiPluginArtifactListPluginResolutionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resolveVersionedPlugins 200 response |  -  |


## uninstallVersionedPlugins

> ClusterControllerApiPluginArtifactListPluginArtifact uninstallVersionedPlugins(tenant, clusterControllerApiPluginListRequest)

Uninstall Kestra&#39;s plugin artifacts

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ClusterControllerApiPluginListRequest clusterControllerApiPluginListRequest = new ClusterControllerApiPluginListRequest(); // ClusterControllerApiPluginListRequest | List of plugins
        try {
            ClusterControllerApiPluginArtifactListPluginArtifact result = apiInstance.uninstallVersionedPlugins(tenant, clusterControllerApiPluginListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#uninstallVersionedPlugins");
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
| **clusterControllerApiPluginListRequest** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | |

### Return type

[**ClusterControllerApiPluginArtifactListPluginArtifact**](ClusterControllerApiPluginArtifactListPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | uninstallVersionedPlugins 200 response |  -  |


## uploadVersionedPlugins

> PluginArtifact uploadVersionedPlugins(tenant, _file)

Upload a Kestra&#39;s plugin artifact

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.auth.*;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

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

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        File _file = new File("/path/to/file"); // File | 
        try {
            PluginArtifact result = apiInstance.uploadVersionedPlugins(tenant, _file);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#uploadVersionedPlugins");
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
| **_file** | **File**|  | [optional] |

### Return type

[**PluginArtifact**](PluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | uploadVersionedPlugins 200 response |  -  |

