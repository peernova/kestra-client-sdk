# ScimApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSCIMResourceByIdGroups**](ScimApi.md#createSCIMResourceByIdGroups) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**createSCIMResourceByIdUsers**](ScimApi.md#createSCIMResourceByIdUsers) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**deleteGroups**](ScimApi.md#deleteGroups) | **DELETE** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**deleteUsers**](ScimApi.md#deleteUsers) | **DELETE** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**findGroups**](ScimApi.md#findGroups) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/.search | {@inheritDoc} |
| [**findUsers**](ScimApi.md#findUsers) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/.search | {@inheritDoc} |
| [**getSCIMResourceByIdGroups**](ScimApi.md#getSCIMResourceByIdGroups) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**getSCIMResourceByIdUsers**](ScimApi.md#getSCIMResourceByIdUsers) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**patchGroups**](ScimApi.md#patchGroups) | **PATCH** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**patchUsers**](ScimApi.md#patchUsers) | **PATCH** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |
| [**queryGroups**](ScimApi.md#queryGroups) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups | {@inheritDoc} |
| [**queryUsers**](ScimApi.md#queryUsers) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | {@inheritDoc} |
| [**updateGroups**](ScimApi.md#updateGroups) | **PUT** /api/v1/{tenant}/integrations/{integration}/scim/v2/Groups/{id} | {@inheritDoc} |
| [**updateUsers**](ScimApi.md#updateUsers) | **PUT** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | {@inheritDoc} |



## createSCIMResourceByIdGroups

> Object createSCIMResourceByIdGroups(integration, tenant, scimUser, attributes, excludedAttributes)

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
            Object result = apiInstance.createSCIMResourceByIdGroups(integration, tenant, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#createSCIMResourceByIdGroups");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | createSCIMResourceByIdGroups 200 response |  -  |


## createSCIMResourceByIdUsers

> Object createSCIMResourceByIdUsers(integration, tenant, scimUser, attributes, excludedAttributes)

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
            Object result = apiInstance.createSCIMResourceByIdUsers(integration, tenant, scimUser, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#createSCIMResourceByIdUsers");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | createSCIMResourceByIdUsers 200 response |  -  |


## deleteGroups

> Object deleteGroups(id, integration, tenant)

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
            Object result = apiInstance.deleteGroups(id, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#deleteGroups");
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
| **200** | deleteGroups 200 response |  -  |


## deleteUsers

> Object deleteUsers(id, integration, tenant)

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
            Object result = apiInstance.deleteUsers(id, integration, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#deleteUsers");
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
| **200** | deleteUsers 200 response |  -  |


## findGroups

> ScimResource findGroups(integration, tenant, searchRequest)

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
            ScimResource result = apiInstance.findGroups(integration, tenant, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#findGroups");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## findUsers

> ScimResource findUsers(integration, tenant, searchRequest)

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
            ScimResource result = apiInstance.findUsers(integration, tenant, searchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#findUsers");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## getSCIMResourceByIdGroups

> ScimResource getSCIMResourceByIdGroups(id, integration, tenant, attributes, excludedAttributes)

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
            ScimResource result = apiInstance.getSCIMResourceByIdGroups(id, integration, tenant, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getSCIMResourceByIdGroups");
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


## getSCIMResourceByIdUsers

> ScimResource getSCIMResourceByIdUsers(id, integration, tenant, attributes, excludedAttributes)

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
            ScimResource result = apiInstance.getSCIMResourceByIdUsers(id, integration, tenant, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#getSCIMResourceByIdUsers");
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


## patchGroups

> Object patchGroups(id, integration, tenant, patchRequest, attributes, excludedAttributes)

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
            Object result = apiInstance.patchGroups(id, integration, tenant, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patchGroups");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patchGroups 200 response |  -  |


## patchUsers

> Object patchUsers(id, integration, tenant, patchRequest, attributes, excludedAttributes)

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
            Object result = apiInstance.patchUsers(id, integration, tenant, patchRequest, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#patchUsers");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | patchUsers 200 response |  -  |


## queryGroups

> ScimResource queryGroups(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

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
            ScimResource result = apiInstance.queryGroups(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#queryGroups");
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


## queryUsers

> ScimResource queryUsers(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count)

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
            ScimResource result = apiInstance.queryUsers(integration, tenant, attributes, excludedAttributes, filter, sortBy, sortOrder, startIndex, count);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#queryUsers");
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


## updateGroups

> ScimResource updateGroups(id, integration, tenant, scimResource, attributes, excludedAttributes)

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
            ScimResource result = apiInstance.updateGroups(id, integration, tenant, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#updateGroups");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |


## updateUsers

> ScimResource updateUsers(id, integration, tenant, scimResource, attributes, excludedAttributes)

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
            ScimResource result = apiInstance.updateUsers(id, integration, tenant, scimResource, attributes, excludedAttributes);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ScimApi#updateUsers");
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

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |
| **501** | Not Implemented |  -  |
| **200** | OK response |  -  |

