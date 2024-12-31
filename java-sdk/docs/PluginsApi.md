# PluginsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**icons**](PluginsApi.md#icons) | **GET** /api/v1/plugins/icons | Get plugins icons |
| [**icons1**](PluginsApi.md#icons1) | **GET** /api/v1/{tenant}/plugins/icons | Get plugins icons |
| [**inputSchemas**](PluginsApi.md#inputSchemas) | **GET** /api/v1/plugins/inputs/{type} | Get all json schemas for a type |
| [**inputSchemas1**](PluginsApi.md#inputSchemas1) | **GET** /api/v1/{tenant}/plugins/inputs/{type} | Get all json schemas for a type |
| [**inputs**](PluginsApi.md#inputs) | **GET** /api/v1/plugins/inputs | Get all types for an inputs |
| [**inputs1**](PluginsApi.md#inputs1) | **GET** /api/v1/{tenant}/plugins/inputs | Get all types for an inputs |
| [**pluginDocumentation**](PluginsApi.md#pluginDocumentation) | **GET** /api/v1/plugins/{cls} | Get plugin documentation |
| [**pluginDocumentation1**](PluginsApi.md#pluginDocumentation1) | **GET** /api/v1/{tenant}/plugins/{cls} | Get plugin documentation |
| [**pluginGroupIcons**](PluginsApi.md#pluginGroupIcons) | **GET** /api/v1/plugins/icons/groups | Get plugins icons |
| [**pluginGroupIcons1**](PluginsApi.md#pluginGroupIcons1) | **GET** /api/v1/{tenant}/plugins/icons/groups | Get plugins icons |
| [**schemas**](PluginsApi.md#schemas) | **GET** /api/v1/plugins/schemas/{type} | Get all json schemas for a type |
| [**schemas1**](PluginsApi.md#schemas1) | **GET** /api/v1/{tenant}/plugins/schemas/{type} | Get all json schemas for a type |
| [**search3**](PluginsApi.md#search3) | **GET** /api/v1/plugins | Get list of plugins |
| [**search8**](PluginsApi.md#search8) | **GET** /api/v1/{tenant}/plugins | Get list of plugins |
| [**subgroups**](PluginsApi.md#subgroups) | **GET** /api/v1/plugins/groups/subgroups | Get plugins group by subgroups |
| [**subgroups1**](PluginsApi.md#subgroups1) | **GET** /api/v1/{tenant}/plugins/groups/subgroups | Get plugins group by subgroups |



## icons

> Map&lt;String, PluginIcon&gt; icons()

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        try {
            Map<String, PluginIcon> result = apiInstance.icons();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#icons");
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

[**Map&lt;String, PluginIcon&gt;**](PluginIcon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | icons 200 response |  -  |


## icons1

> Map&lt;String, PluginIcon&gt; icons1(tenant)

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, PluginIcon> result = apiInstance.icons1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#icons1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | icons_1 200 response |  -  |


## inputSchemas

> DocumentationWithSchema inputSchemas(type)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        Type type = Type.fromValue("STRING"); // Type | The schema needed
        try {
            DocumentationWithSchema result = apiInstance.inputSchemas(type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#inputSchemas");
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
| **type** | [**Type**](.md)| The schema needed | [enum: STRING, ENUM, SELECT, INT, FLOAT, BOOLEAN, DATETIME, DATE, TIME, DURATION, FILE, JSON, URI, SECRET, ARRAY, MULTISELECT, YAML, EMAIL] |

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inputSchemas 200 response |  -  |


## inputSchemas1

> DocumentationWithSchema inputSchemas1(type, tenant)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        Type type = Type.fromValue("STRING"); // Type | The schema needed
        String tenant = "tenant_example"; // String | 
        try {
            DocumentationWithSchema result = apiInstance.inputSchemas1(type, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#inputSchemas1");
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
| **type** | [**Type**](.md)| The schema needed | [enum: STRING, ENUM, SELECT, INT, FLOAT, BOOLEAN, DATETIME, DATE, TIME, DURATION, FILE, JSON, URI, SECRET, ARRAY, MULTISELECT, YAML, EMAIL] |
| **tenant** | **String**|  | |

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inputSchemas_1 200 response |  -  |


## inputs

> List&lt;InputType&gt; inputs()

Get all types for an inputs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        try {
            List<InputType> result = apiInstance.inputs();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#inputs");
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

[**List&lt;InputType&gt;**](InputType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inputs 200 response |  -  |


## inputs1

> List&lt;InputType&gt; inputs1(tenant)

Get all types for an inputs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<InputType> result = apiInstance.inputs1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#inputs1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | inputs_1 200 response |  -  |


## pluginDocumentation

> DocumentationWithSchema pluginDocumentation(cls, all)

Get plugin documentation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String cls = "cls_example"; // String | The plugin full class name
        Boolean all = false; // Boolean | Include all the properties
        try {
            DocumentationWithSchema result = apiInstance.pluginDocumentation(cls, all);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#pluginDocumentation");
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

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pluginDocumentation 200 response |  -  |


## pluginDocumentation1

> DocumentationWithSchema pluginDocumentation1(cls, all, tenant)

Get plugin documentation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String cls = "cls_example"; // String | The plugin full class name
        Boolean all = false; // Boolean | Include all the properties
        String tenant = "tenant_example"; // String | 
        try {
            DocumentationWithSchema result = apiInstance.pluginDocumentation1(cls, all, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#pluginDocumentation1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pluginDocumentation_1 200 response |  -  |


## pluginGroupIcons

> Map&lt;String, PluginIcon&gt; pluginGroupIcons()

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        try {
            Map<String, PluginIcon> result = apiInstance.pluginGroupIcons();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#pluginGroupIcons");
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

[**Map&lt;String, PluginIcon&gt;**](PluginIcon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pluginGroupIcons 200 response |  -  |


## pluginGroupIcons1

> Map&lt;String, PluginIcon&gt; pluginGroupIcons1(tenant)

Get plugins icons

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            Map<String, PluginIcon> result = apiInstance.pluginGroupIcons1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#pluginGroupIcons1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | pluginGroupIcons_1 200 response |  -  |


## schemas

> Map&lt;String, Object&gt; schemas(type, arrayOf)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        SchemaType type = SchemaType.fromValue("flow"); // SchemaType | The schema needed
        Boolean arrayOf = false; // Boolean | If schema should be an array of requested type
        try {
            Map<String, Object> result = apiInstance.schemas(type, arrayOf);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#schemas");
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
| **type** | [**SchemaType**](.md)| The schema needed | [enum: flow, template, task, trigger, plugindefault, apps, dashboard] |
| **arrayOf** | **Boolean**| If schema should be an array of requested type | [optional] [default to false] |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | schemas 200 response |  -  |


## schemas1

> Map&lt;String, Object&gt; schemas1(type, tenant, arrayOf)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        SchemaType type = SchemaType.fromValue("flow"); // SchemaType | The schema needed
        String tenant = "tenant_example"; // String | 
        Boolean arrayOf = false; // Boolean | If schema should be an array of requested type
        try {
            Map<String, Object> result = apiInstance.schemas1(type, tenant, arrayOf);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#schemas1");
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
| **type** | [**SchemaType**](.md)| The schema needed | [enum: flow, template, task, trigger, plugindefault, apps, dashboard] |
| **tenant** | **String**|  | |
| **arrayOf** | **Boolean**| If schema should be an array of requested type | [optional] [default to false] |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | schemas_1 200 response |  -  |


## search3

> List&lt;Plugin&gt; search3()

Get list of plugins

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        try {
            List<Plugin> result = apiInstance.search3();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#search3");
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

[**List&lt;Plugin&gt;**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_3 200 response |  -  |


## search8

> List&lt;Plugin&gt; search8(tenant)

Get list of plugins

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Plugin> result = apiInstance.search8(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#search8");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_8 200 response |  -  |


## subgroups

> List&lt;Plugin&gt; subgroups()

Get plugins group by subgroups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        try {
            List<Plugin> result = apiInstance.subgroups();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#subgroups");
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

[**List&lt;Plugin&gt;**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | subgroups 200 response |  -  |


## subgroups1

> List&lt;Plugin&gt; subgroups1(tenant)

Get plugins group by subgroups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.PluginsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        PluginsApi apiInstance = new PluginsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Plugin> result = apiInstance.subgroups1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PluginsApi#subgroups1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | subgroups_1 200 response |  -  |

