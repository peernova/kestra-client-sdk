# TemplatesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create12**](TemplatesApi.md#create12) | **POST** /api/v1/templates | Create a template |
| [**createWithTenant11**](TemplatesApi.md#createWithTenant11) | **POST** /api/v1/{tenant}/templates | Create a template |
| [**delete15**](TemplatesApi.md#delete15) | **DELETE** /api/v1/templates/{namespace}/{id} | Delete a template |
| [**deleteByIds1**](TemplatesApi.md#deleteByIds1) | **DELETE** /api/v1/templates/delete/by-ids | Delete templates by their IDs. |
| [**deleteByIdsWithTenant1**](TemplatesApi.md#deleteByIdsWithTenant1) | **DELETE** /api/v1/{tenant}/templates/delete/by-ids | Delete templates by their IDs. |
| [**deleteByQuery1**](TemplatesApi.md#deleteByQuery1) | **DELETE** /api/v1/templates/delete/by-query | Delete templates returned by the query parameters. |
| [**deleteByQueryWithTenant1**](TemplatesApi.md#deleteByQueryWithTenant1) | **DELETE** /api/v1/{tenant}/templates/delete/by-query | Delete templates returned by the query parameters. |
| [**deleteWithTenant14**](TemplatesApi.md#deleteWithTenant14) | **DELETE** /api/v1/{tenant}/templates/{namespace}/{id} | Delete a template |
| [**exportByIds**](TemplatesApi.md#exportByIds) | **POST** /api/v1/templates/export/by-ids | Export templates as a ZIP archive of yaml sources. |
| [**exportByIdsWithTenant**](TemplatesApi.md#exportByIdsWithTenant) | **POST** /api/v1/{tenant}/templates/export/by-ids | Export templates as a ZIP archive of yaml sources. |
| [**exportByQuery**](TemplatesApi.md#exportByQuery) | **GET** /api/v1/templates/export/by-query | Export templates as a ZIP archive of yaml sources. |
| [**exportByQueryWithTenant**](TemplatesApi.md#exportByQueryWithTenant) | **GET** /api/v1/{tenant}/templates/export/by-query | Export templates as a ZIP archive of yaml sources. |
| [**find12**](TemplatesApi.md#find12) | **GET** /api/v1/templates/search | Search for templates |
| [**findWithTenant11**](TemplatesApi.md#findWithTenant11) | **GET** /api/v1/{tenant}/templates/search | Search for templates |
| [**importTemplates**](TemplatesApi.md#importTemplates) | **POST** /api/v1/templates/import | Import templates as a ZIP archive of yaml sources or a multi-objects YAML file. |
| [**importTemplatesWithTenant**](TemplatesApi.md#importTemplatesWithTenant) | **POST** /api/v1/{tenant}/templates/import | Import templates as a ZIP archive of yaml sources or a multi-objects YAML file. |
| [**index8**](TemplatesApi.md#index8) | **GET** /api/v1/templates/{namespace}/{id} | Get a template |
| [**indexWithTenant7**](TemplatesApi.md#indexWithTenant7) | **GET** /api/v1/{tenant}/templates/{namespace}/{id} | Get a template |
| [**listDistinctNamespace1**](TemplatesApi.md#listDistinctNamespace1) | **GET** /api/v1/templates/distinct-namespaces | List all distinct namespaces |
| [**listDistinctNamespaceWithTenant1**](TemplatesApi.md#listDistinctNamespaceWithTenant1) | **GET** /api/v1/{tenant}/templates/distinct-namespaces | List all distinct namespaces |
| [**update8**](TemplatesApi.md#update8) | **PUT** /api/v1/templates/{namespace}/{id} | Update a template |
| [**updateNamespace**](TemplatesApi.md#updateNamespace) | **POST** /api/v1/templates/{namespace} | Update a complete namespace from json object |
| [**updateNamespaceWithTenant**](TemplatesApi.md#updateNamespaceWithTenant) | **POST** /api/v1/{tenant}/templates/{namespace} | Update a complete namespace from json object |
| [**updateWithTenant7**](TemplatesApi.md#updateWithTenant7) | **PUT** /api/v1/{tenant}/templates/{namespace}/{id} | Update a template |
| [**validateTemplates**](TemplatesApi.md#validateTemplates) | **POST** /api/v1/templates/validate | Validate a list of templates |
| [**validateTemplatesWithTenant**](TemplatesApi.md#validateTemplatesWithTenant) | **POST** /api/v1/{tenant}/templates/validate | Validate a list of templates |



## create12

> Template create12(template)

Create a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        Template template = new Template(); // Template | 
        try {
            Template result = apiInstance.create12(template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#create12");
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
| **template** | [**Template**](Template.md)|  | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_12 200 response |  -  |


## createWithTenant11

> Template createWithTenant11(tenant, template)

Create a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Template template = new Template(); // Template | 
        try {
            Template result = apiInstance.createWithTenant11(tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#createWithTenant11");
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
| **template** | [**Template**](Template.md)|  | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createWithTenant_11 200 response |  -  |


## delete15

> delete15(namespace, id)

Delete a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        try {
            apiInstance.delete15(namespace, id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#delete15");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | delete_15 200 response |  -  |


## deleteByIds1

> BulkResponse deleteByIds1(idWithNamespace)

Delete templates by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.deleteByIds1(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByIds1");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByIds_1 200 response |  -  |


## deleteByIdsWithTenant1

> BulkResponse deleteByIdsWithTenant1(tenant, idWithNamespace)

Delete templates by their IDs.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            BulkResponse result = apiInstance.deleteByIdsWithTenant1(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByIdsWithTenant1");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByIdsWithTenant_1 200 response |  -  |


## deleteByQuery1

> BulkResponse deleteByQuery1(q, namespace)

Delete templates returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            BulkResponse result = apiInstance.deleteByQuery1(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByQuery1");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByQuery_1 200 response |  -  |


## deleteByQueryWithTenant1

> BulkResponse deleteByQueryWithTenant1(tenant, q, namespace)

Delete templates returned by the query parameters.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            BulkResponse result = apiInstance.deleteByQueryWithTenant1(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByQueryWithTenant1");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteByQueryWithTenant_1 200 response |  -  |


## deleteWithTenant14

> deleteWithTenant14(namespace, id, tenant)

Delete a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.deleteWithTenant14(namespace, id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteWithTenant14");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |
| **tenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | deleteWithTenant_14 200 response |  -  |


## exportByIds

> List&lt;byte[]&gt; exportByIds(idWithNamespace)

Export templates as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            List<byte[]> result = apiInstance.exportByIds(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByIds");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByIds 200 response |  -  |


## exportByIdsWithTenant

> List&lt;byte[]&gt; exportByIdsWithTenant(tenant, idWithNamespace)

Export templates as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<IdWithNamespace> idWithNamespace = Arrays.asList(); // List<IdWithNamespace> | 
        try {
            List<byte[]> result = apiInstance.exportByIdsWithTenant(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByIdsWithTenant");
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
| **idWithNamespace** | [**List&lt;IdWithNamespace&gt;**](IdWithNamespace.md)|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByIdsWithTenant 200 response |  -  |


## exportByQuery

> List&lt;byte[]&gt; exportByQuery(q, namespace)

Export templates as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            List<byte[]> result = apiInstance.exportByQuery(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByQuery");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByQuery 200 response |  -  |


## exportByQueryWithTenant

> List&lt;byte[]&gt; exportByQueryWithTenant(tenant, q, namespace)

Export templates as a ZIP archive of yaml sources.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            List<byte[]> result = apiInstance.exportByQueryWithTenant(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByQueryWithTenant");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | exportByQueryWithTenant 200 response |  -  |


## find12

> PagedResultsTemplate find12(page, size, sort, q, namespace)

Search for templates

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            PagedResultsTemplate result = apiInstance.find12(page, size, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#find12");
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
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**PagedResultsTemplate**](PagedResultsTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_12 200 response |  -  |


## findWithTenant11

> PagedResultsTemplate findWithTenant11(page, size, tenant, sort, q, namespace)

Search for templates

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        try {
            PagedResultsTemplate result = apiInstance.findWithTenant11(page, size, tenant, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#findWithTenant11");
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
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |

### Return type

[**PagedResultsTemplate**](PagedResultsTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findWithTenant_11 200 response |  -  |


## importTemplates

> importTemplates(fileUpload)

Import templates as a ZIP archive of yaml sources or a multi-objects YAML file.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        File fileUpload = new File("/path/to/file"); // File | The file to import, can be a ZIP archive or a multi-objects YAML file
        try {
            apiInstance.importTemplates(fileUpload);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#importTemplates");
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
| **fileUpload** | **File**| The file to import, can be a ZIP archive or a multi-objects YAML file | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | importTemplates 200 response |  -  |


## importTemplatesWithTenant

> importTemplatesWithTenant(tenant, fileUpload)

Import templates as a ZIP archive of yaml sources or a multi-objects YAML file.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        File fileUpload = new File("/path/to/file"); // File | The file to import, can be a ZIP archive or a multi-objects YAML file
        try {
            apiInstance.importTemplatesWithTenant(tenant, fileUpload);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#importTemplatesWithTenant");
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
| **fileUpload** | **File**| The file to import, can be a ZIP archive or a multi-objects YAML file | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **200** | importTemplatesWithTenant 200 response |  -  |


## index8

> Template index8(namespace, id)

Get a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        try {
            Template result = apiInstance.index8(namespace, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#index8");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_8 200 response |  -  |


## indexWithTenant7

> Template indexWithTenant7(namespace, id, tenant)

Get a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        String tenant = "tenant_example"; // String | 
        try {
            Template result = apiInstance.indexWithTenant7(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#indexWithTenant7");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |
| **tenant** | **String**|  | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | indexWithTenant_7 200 response |  -  |


## listDistinctNamespace1

> List&lt;String&gt; listDistinctNamespace1()

List all distinct namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        try {
            List<String> result = apiInstance.listDistinctNamespace1();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#listDistinctNamespace1");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listDistinctNamespace_1 200 response |  -  |


## listDistinctNamespaceWithTenant1

> List&lt;String&gt; listDistinctNamespaceWithTenant1(tenant)

List all distinct namespaces

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.listDistinctNamespaceWithTenant1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#listDistinctNamespaceWithTenant1");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listDistinctNamespaceWithTenant_1 200 response |  -  |


## update8

> Template update8(namespace, id, template)

Update a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        Template template = new Template(); // Template | 
        try {
            Template result = apiInstance.update8(namespace, id, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#update8");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |
| **template** | [**Template**](Template.md)|  | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_8 200 response |  -  |


## updateNamespace

> List&lt;Template&gt; updateNamespace(namespace, delete, template)

Update a complete namespace from json object

All Template will be created / updated for this namespace. Template already created but not in &#x60;templates&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        Boolean delete = true; // Boolean | If missing template should be deleted
        List<Template> template = Arrays.asList(); // List<Template> | 
        try {
            List<Template> result = apiInstance.updateNamespace(namespace, delete, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#updateNamespace");
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
| **namespace** | **String**| The template namespace | |
| **delete** | **Boolean**| If missing template should be deleted | [default to true] |
| **template** | [**List&lt;Template&gt;**](Template.md)|  | |

### Return type

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateNamespace 200 response |  -  |


## updateNamespaceWithTenant

> List&lt;Template&gt; updateNamespaceWithTenant(namespace, delete, tenant, template)

Update a complete namespace from json object

All Template will be created / updated for this namespace. Template already created but not in &#x60;templates&#x60; will be deleted if the query delete is &#x60;true&#x60;

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        Boolean delete = true; // Boolean | If missing template should be deleted
        String tenant = "tenant_example"; // String | 
        List<Template> template = Arrays.asList(); // List<Template> | 
        try {
            List<Template> result = apiInstance.updateNamespaceWithTenant(namespace, delete, tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#updateNamespaceWithTenant");
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
| **namespace** | **String**| The template namespace | |
| **delete** | **Boolean**| If missing template should be deleted | [default to true] |
| **tenant** | **String**|  | |
| **template** | [**List&lt;Template&gt;**](Template.md)|  | |

### Return type

[**List&lt;Template&gt;**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateNamespaceWithTenant 200 response |  -  |


## updateWithTenant7

> Template updateWithTenant7(namespace, id, tenant, template)

Update a template

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String namespace = "namespace_example"; // String | The template namespace
        String id = "id_example"; // String | The template id
        String tenant = "tenant_example"; // String | 
        Template template = new Template(); // Template | 
        try {
            Template result = apiInstance.updateWithTenant7(namespace, id, tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#updateWithTenant7");
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
| **namespace** | **String**| The template namespace | |
| **id** | **String**| The template id | |
| **tenant** | **String**|  | |
| **template** | [**Template**](Template.md)|  | |

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateWithTenant_7 200 response |  -  |


## validateTemplates

> List&lt;ValidateConstraintViolation&gt; validateTemplates(body)

Validate a list of templates

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            List<ValidateConstraintViolation> result = apiInstance.validateTemplates(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#validateTemplates");
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
| **body** | **String**|  | |

### Return type

[**List&lt;ValidateConstraintViolation&gt;**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTemplates 200 response |  -  |


## validateTemplatesWithTenant

> List&lt;ValidateConstraintViolation&gt; validateTemplatesWithTenant(tenant, body)

Validate a list of templates

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.TemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        TemplatesApi apiInstance = new TemplatesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            List<ValidateConstraintViolation> result = apiInstance.validateTemplatesWithTenant(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#validateTemplatesWithTenant");
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
| **body** | **String**|  | |

### Return type

[**List&lt;ValidateConstraintViolation&gt;**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateTemplatesWithTenant 200 response |  -  |

