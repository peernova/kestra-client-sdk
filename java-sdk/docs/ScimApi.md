# ScimApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create32**](ScimApi.md#create32) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**create33**](ScimApi.md#create33) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**create7**](ScimApi.md#create7) | **POST** /api/v1/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**create8**](ScimApi.md#create8) | **POST** /api/v1/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**delete35**](ScimApi.md#delete35) | **DELETE** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**delete36**](ScimApi.md#delete36) | **DELETE** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**delete7**](ScimApi.md#delete7) | **DELETE** /api/v1/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**delete8**](ScimApi.md#delete8) | **DELETE** /api/v1/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**find33**](ScimApi.md#find33) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/.search | {@inheritDoc} |
| [**find34**](ScimApi.md#find34) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/.search | {@inheritDoc} |
| [**find7**](ScimApi.md#find7) | **POST** /api/v1/integrations/{integration}/scim/v2/Groups/.search | {@inheritDoc} |
| [**find8**](ScimApi.md#find8) | **POST** /api/v1/integrations/{integration}/scim/v2/Users/.search | {@inheritDoc} |
| [**getById**](ScimApi.md#getById) | **GET** /api/v1/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**getById1**](ScimApi.md#getById1) | **GET** /api/v1/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**getById2**](ScimApi.md#getById2) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**getById3**](ScimApi.md#getById3) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**patch**](ScimApi.md#patch) | **PATCH** /api/v1/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**patch1**](ScimApi.md#patch1) | **PATCH** /api/v1/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**patch3**](ScimApi.md#patch3) | **PATCH** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**patch4**](ScimApi.md#patch4) | **PATCH** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**query**](ScimApi.md#query) | **GET** /api/v1/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**query1**](ScimApi.md#query1) | **GET** /api/v1/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**query2**](ScimApi.md#query2) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**query3**](ScimApi.md#query3) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**update23**](ScimApi.md#update23) | **PUT** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**update24**](ScimApi.md#update24) | **PUT** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**update5**](ScimApi.md#update5) | **PUT** /api/v1/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**update6**](ScimApi.md#update6) | **PUT** /api/v1/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |



## create32

> Object create32(integration, tenant, scimUser, attributes, excludedAttributes)

{@inheritDoc}

Create

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ScimUser scimUser = new ScimUser(); // ScimUser | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.create32(integration, tenant, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#create32");
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
| **scimUser** | [**ScimUser**](ScimUser.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | create_32 200 response |  -  |


## create33

> Object create33(integration, tenant, scimUser, attributes, excludedAttributes)

{@inheritDoc}

Create

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ScimUser scimUser = new ScimUser(); // ScimUser | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.create33(integration, tenant, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#create33");
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
| **scimUser** | [**ScimUser**](ScimUser.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | create_33 200 response |  -  |


## create7

> Object create7(integration, scimUser, attributes, excludedAttributes)

{@inheritDoc}

Create

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        ScimUser scimUser = new ScimUser(); // ScimUser | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.create7(integration, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#create7");
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
| **scimUser** | [**ScimUser**](ScimUser.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | create_7 200 response |  -  |


## create8

> Object create8(integration, scimUser, attributes, excludedAttributes)

{@inheritDoc}

Create

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        ScimUser scimUser = new ScimUser(); // ScimUser | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.create8(integration, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#create8");
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
| **scimUser** | [**ScimUser**](ScimUser.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | create_8 200 response |  -  |


## delete35

> Object delete35(id, integration, tenant)

{@inheritDoc}

Delete from the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.delete35(id, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#delete35");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | delete_35 200 response |  -  |


## delete36

> Object delete36(id, integration, tenant)

{@inheritDoc}

Delete from the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.delete36(id, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#delete36");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | delete_36 200 response |  -  |


## delete7

> Object delete7(id, integration)

{@inheritDoc}

Delete from the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        try {
            Object result = apiInstance.delete7(id, integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#delete7");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | delete_7 200 response |  -  |


## delete8

> Object delete8(id, integration)

{@inheritDoc}

Delete from the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        try {
            Object result = apiInstance.delete8(id, integration);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#delete8");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | delete_8 200 response |  -  |


## find33

> ScimResource find33(integration, tenant, searchRequest)

{@inheritDoc}

Search

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        SearchRequest searchRequest = new SearchRequest(); // SearchRequest | 
        try {
            ScimResource result = apiInstance.find33(integration, tenant, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#find33");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## find34

> ScimResource find34(integration, tenant, searchRequest)

{@inheritDoc}

Search

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        SearchRequest searchRequest = new SearchRequest(); // SearchRequest | 
        try {
            ScimResource result = apiInstance.find34(integration, tenant, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#find34");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## find7

> ScimResource find7(integration, searchRequest)

{@inheritDoc}

Search

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        SearchRequest searchRequest = new SearchRequest(); // SearchRequest | 
        try {
            ScimResource result = apiInstance.find7(integration, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#find7");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## find8

> ScimResource find8(integration, searchRequest)

{@inheritDoc}

Search

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        SearchRequest searchRequest = new SearchRequest(); // SearchRequest | 
        try {
            ScimResource result = apiInstance.find8(integration, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#find8");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## getById

> ScimResource getById(id, integration, attributes, excludedAttributes)

{@inheritDoc}

Find by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.getById(id, integration, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getById");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## getById1

> ScimResource getById1(id, integration, attributes, excludedAttributes)

{@inheritDoc}

Find by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.getById1(id, integration, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getById1");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## getById2

> ScimResource getById2(id, integration, tenant, attributes, excludedAttributes)

{@inheritDoc}

Find by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.getById2(id, integration, tenant, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getById2");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## getById3

> ScimResource getById3(id, integration, tenant, attributes, excludedAttributes)

{@inheritDoc}

Find by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.getById3(id, integration, tenant, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getById3");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## patch

> Object patch(id, integration, patchRequest, attributes, excludedAttributes)

{@inheritDoc}

Patch a portion of the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        PatchRequest patchRequest = new PatchRequest(); // PatchRequest | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.patch(id, integration, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patch");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **patchRequest** | [**PatchRequest**](PatchRequest.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patch 200 response |  -  |


## patch1

> Object patch1(id, integration, patchRequest, attributes, excludedAttributes)

{@inheritDoc}

Patch a portion of the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        PatchRequest patchRequest = new PatchRequest(); // PatchRequest | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.patch1(id, integration, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patch1");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **patchRequest** | [**PatchRequest**](PatchRequest.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patch_1 200 response |  -  |


## patch3

> Object patch3(id, integration, tenant, patchRequest, attributes, excludedAttributes)

{@inheritDoc}

Patch a portion of the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        PatchRequest patchRequest = new PatchRequest(); // PatchRequest | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.patch3(id, integration, tenant, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patch3");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **patchRequest** | [**PatchRequest**](PatchRequest.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patch_3 200 response |  -  |


## patch4

> Object patch4(id, integration, tenant, patchRequest, attributes, excludedAttributes)

{@inheritDoc}

Patch a portion of the backing store

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        PatchRequest patchRequest = new PatchRequest(); // PatchRequest | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            Object result = apiInstance.patch4(id, integration, tenant, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patch4");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **patchRequest** | [**PatchRequest**](PatchRequest.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patch_4 200 response |  -  |


## query

> ScimResource query(integration, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

{@inheritDoc}

Find by a combination of query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        String filter = "filter_example"; // String | 
        String sortBy = "sortBy_example"; // String | 
        SortOrder sortOrder = SortOrder.fromValue("ASCENDING"); // SortOrder | 
        Integer startIndex = 56; // Integer | 
        Integer count = 56; // Integer | 
        try {
            ScimResource result = apiInstance.query(integration, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#query");
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
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **sortBy** | **String**|  | [optional] |
| **sortOrder** | [**SortOrder**](.md)|  | [optional] [enum: ASCENDING, DESCENDING] |
| **startIndex** | **Integer**|  | [optional] |
| **count** | **Integer**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## query1

> ScimResource query1(integration, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

{@inheritDoc}

Find by a combination of query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        String filter = "filter_example"; // String | 
        String sortBy = "sortBy_example"; // String | 
        SortOrder sortOrder = SortOrder.fromValue("ASCENDING"); // SortOrder | 
        Integer startIndex = 56; // Integer | 
        Integer count = 56; // Integer | 
        try {
            ScimResource result = apiInstance.query1(integration, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#query1");
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
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **sortBy** | **String**|  | [optional] |
| **sortOrder** | [**SortOrder**](.md)|  | [optional] [enum: ASCENDING, DESCENDING] |
| **startIndex** | **Integer**|  | [optional] |
| **count** | **Integer**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## query2

> ScimResource query2(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

{@inheritDoc}

Find by a combination of query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        String filter = "filter_example"; // String | 
        String sortBy = "sortBy_example"; // String | 
        SortOrder sortOrder = SortOrder.fromValue("ASCENDING"); // SortOrder | 
        Integer startIndex = 56; // Integer | 
        Integer count = 56; // Integer | 
        try {
            ScimResource result = apiInstance.query2(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#query2");
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
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **sortBy** | **String**|  | [optional] |
| **sortOrder** | [**SortOrder**](.md)|  | [optional] [enum: ASCENDING, DESCENDING] |
| **startIndex** | **Integer**|  | [optional] |
| **count** | **Integer**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## query3

> ScimResource query3(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

{@inheritDoc}

Find by a combination of query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        String filter = "filter_example"; // String | 
        String sortBy = "sortBy_example"; // String | 
        SortOrder sortOrder = SortOrder.fromValue("ASCENDING"); // SortOrder | 
        Integer startIndex = 56; // Integer | 
        Integer count = 56; // Integer | 
        try {
            ScimResource result = apiInstance.query3(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#query3");
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
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **sortBy** | **String**|  | [optional] |
| **sortOrder** | [**SortOrder**](.md)|  | [optional] [enum: ASCENDING, DESCENDING] |
| **startIndex** | **Integer**|  | [optional] |
| **count** | **Integer**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## update23

> ScimResource update23(id, integration, tenant, scimResource, attributes, excludedAttributes)

{@inheritDoc}

Update

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ScimResource scimResource = new ScimResource(); // ScimResource | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.update23(id, integration, tenant, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#update23");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **scimResource** | [**ScimResource**](ScimResource.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## update24

> ScimResource update24(id, integration, tenant, scimResource, attributes, excludedAttributes)

{@inheritDoc}

Update

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ScimResource scimResource = new ScimResource(); // ScimResource | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.update24(id, integration, tenant, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#update24");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **tenant** | **String**|  | |
| **scimResource** | [**ScimResource**](ScimResource.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## update5

> ScimResource update5(id, integration, scimResource, attributes, excludedAttributes)

{@inheritDoc}

Update

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        ScimResource scimResource = new ScimResource(); // ScimResource | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.update5(id, integration, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#update5");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **scimResource** | [**ScimResource**](ScimResource.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## update6

> ScimResource update6(id, integration, scimResource, attributes, excludedAttributes)

{@inheritDoc}

Update

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ScimApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ScimApi apiInstance = new ScimApi(defaultClient);
        String id = "id_example"; // String | 
        String integration = "integration_example"; // String | 
        ScimResource scimResource = new ScimResource(); // ScimResource | 
        String attributes = "attributes_example"; // String | 
        String excludedAttributes = "excludedAttributes_example"; // String | 
        try {
            ScimResource result = apiInstance.update6(id, integration, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#update6");
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
| **id** | **String**|  | |
| **integration** | **String**|  | |
| **scimResource** | [**ScimResource**](ScimResource.md)|  | |
| **attributes** | **String**|  | [optional] |
| **excludedAttributes** | **String**|  | [optional] |

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json, application/json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |

