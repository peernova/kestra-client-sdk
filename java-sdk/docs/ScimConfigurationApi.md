# ScimConfigurationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllResourceTypes**](ScimConfigurationApi.md#getAllResourceTypes) | **GET** /api/v1/integrations/{integration}/scim/v2/ResourceTypes |  |
| [**getAllResourceTypes1**](ScimConfigurationApi.md#getAllResourceTypes1) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/ResourceTypes |  |
| [**getAllSchemas**](ScimConfigurationApi.md#getAllSchemas) | **GET** /api/v1/integrations/{integration}/scim/v2/Schemas |  |
| [**getAllSchemas1**](ScimConfigurationApi.md#getAllSchemas1) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Schemas |  |
| [**getResourceType**](ScimConfigurationApi.md#getResourceType) | **GET** /api/v1/integrations/{integration}/scim/v2/ResourceTypes/{name} |  |
| [**getResourceType1**](ScimConfigurationApi.md#getResourceType1) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/ResourceTypes/{name} |  |
| [**getSchema**](ScimConfigurationApi.md#getSchema) | **GET** /api/v1/integrations/{integration}/scim/v2/Schemas/{uri} |  |
| [**getSchema1**](ScimConfigurationApi.md#getSchema1) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Schemas/{uri} |  |
| [**getServiceProviderConfiguration**](ScimConfigurationApi.md#getServiceProviderConfiguration) | **GET** /api/v1/integrations/{integration}/scim/v2/ServiceProviderConfig |  |
| [**getServiceProviderConfiguration1**](ScimConfigurationApi.md#getServiceProviderConfiguration1) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/ServiceProviderConfig |  |



## getAllResourceTypes

> List&lt;ResourceType&gt; getAllResourceTypes(integration)



Get All Resource Types

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        try {
            List<ResourceType> result = apiInstance.getAllResourceTypes(integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getAllResourceTypes");
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
| **integration** | **String**|  | |

### Return type

[**List&lt;ResourceType&gt;**](ResourceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getAllResourceTypes1

> List&lt;ResourceType&gt; getAllResourceTypes1(integration, tenant)



Get All Resource Types

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            List<ResourceType> result = apiInstance.getAllResourceTypes1(integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getAllResourceTypes1");
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
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;ResourceType&gt;**](ResourceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getAllSchemas

> List&lt;Schema&gt; getAllSchemas(integration)



Get All Schemas

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        try {
            List<Schema> result = apiInstance.getAllSchemas(integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getAllSchemas");
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
| **integration** | **String**|  | |

### Return type

[**List&lt;Schema&gt;**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getAllSchemas1

> List&lt;Schema&gt; getAllSchemas1(integration, tenant)



Get All Schemas

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            List<Schema> result = apiInstance.getAllSchemas1(integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getAllSchemas1");
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
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;Schema&gt;**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getResourceType

> ResourceType getResourceType(name, integration)



Get Resource Type by URN

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String name = "name_example"; // String | 
        String integration = "integration_example"; // String | 
        try {
            ResourceType result = apiInstance.getResourceType(name, integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getResourceType");
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
| **name** | **String**|  | |
| **integration** | **String**|  | |

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getResourceType1

> ResourceType getResourceType1(name, integration, tenant)



Get Resource Type by URN

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String name = "name_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ResourceType result = apiInstance.getResourceType1(name, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getResourceType1");
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
| **name** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getSchema

> Schema getSchema(uri, integration)



Get Schemas by URN

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String uri = "uri_example"; // String | 
        String integration = "integration_example"; // String | 
        try {
            Schema result = apiInstance.getSchema(uri, integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getSchema");
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
| **uri** | **String**|  | |
| **integration** | **String**|  | |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getSchema1

> Schema getSchema1(uri, integration, tenant)



Get Schemas by URN

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String uri = "uri_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Schema result = apiInstance.getSchema1(uri, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getSchema1");
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
| **uri** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getServiceProviderConfiguration

> ServiceProviderConfiguration getServiceProviderConfiguration(integration)



Get Service Provider Configuration

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        try {
            ServiceProviderConfiguration result = apiInstance.getServiceProviderConfiguration(integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getServiceProviderConfiguration");
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
| **integration** | **String**|  | |

### Return type

[**ServiceProviderConfiguration**](ServiceProviderConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |


## getServiceProviderConfiguration1

> ServiceProviderConfiguration getServiceProviderConfiguration1(integration, tenant)



Get Service Provider Configuration

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimConfigurationApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimConfigurationApi apiInstance = new ScimConfigurationApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ServiceProviderConfiguration result = apiInstance.getServiceProviderConfiguration1(integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimConfigurationApi#getServiceProviderConfiguration1");
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
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ServiceProviderConfiguration**](ServiceProviderConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response |  -  |

