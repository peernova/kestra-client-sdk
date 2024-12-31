# TemplatesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create13**](TemplatesApi.md#create13) | **POST** /api/v1/templates | Create a template |
| [**create38**](TemplatesApi.md#create38) | **POST** /api/v1/{tenant}/templates | Create a template |
| [**delete16**](TemplatesApi.md#delete16) | **DELETE** /api/v1/templates/{namespace}/{id} | Delete a template |
| [**delete44**](TemplatesApi.md#delete44) | **DELETE** /api/v1/{tenant}/templates/{namespace}/{id} | Delete a template |
| [**deleteByIds2**](TemplatesApi.md#deleteByIds2) | **DELETE** /api/v1/templates/delete/by-ids | Delete templates by their IDs. |
| [**deleteByIds5**](TemplatesApi.md#deleteByIds5) | **DELETE** /api/v1/{tenant}/templates/delete/by-ids | Delete templates by their IDs. |
| [**deleteByQuery2**](TemplatesApi.md#deleteByQuery2) | **DELETE** /api/v1/templates/delete/by-query | Delete templates returned by the query parameters. |
| [**deleteByQuery5**](TemplatesApi.md#deleteByQuery5) | **DELETE** /api/v1/{tenant}/templates/delete/by-query | Delete templates returned by the query parameters. |
| [**exportByIds1**](TemplatesApi.md#exportByIds1) | **POST** /api/v1/templates/export/by-ids | Export templates as a ZIP archive of yaml sources. |
| [**exportByIds3**](TemplatesApi.md#exportByIds3) | **POST** /api/v1/{tenant}/templates/export/by-ids | Export templates as a ZIP archive of yaml sources. |
| [**exportByQuery1**](TemplatesApi.md#exportByQuery1) | **GET** /api/v1/templates/export/by-query | Export templates as a ZIP archive of yaml sources. |
| [**exportByQuery3**](TemplatesApi.md#exportByQuery3) | **GET** /api/v1/{tenant}/templates/export/by-query | Export templates as a ZIP archive of yaml sources. |
| [**find13**](TemplatesApi.md#find13) | **GET** /api/v1/templates/search | Search for templates |
| [**find39**](TemplatesApi.md#find39) | **GET** /api/v1/{tenant}/templates/search | Search for templates |
| [**importTemplates**](TemplatesApi.md#importTemplates) | **POST** /api/v1/templates/import | Import templates as a ZIP archive of yaml sources or a multi-objects YAML file. |
| [**importTemplates1**](TemplatesApi.md#importTemplates1) | **POST** /api/v1/{tenant}/templates/import | Import templates as a ZIP archive of yaml sources or a multi-objects YAML file. |
| [**index30**](TemplatesApi.md#index30) | **GET** /api/v1/{tenant}/templates/{namespace}/{id} | Get a template |
| [**index9**](TemplatesApi.md#index9) | **GET** /api/v1/templates/{namespace}/{id} | Get a template |
| [**listDistinctNamespace2**](TemplatesApi.md#listDistinctNamespace2) | **GET** /api/v1/templates/distinct-namespaces | List all distinct namespaces |
| [**listDistinctNamespace5**](TemplatesApi.md#listDistinctNamespace5) | **GET** /api/v1/{tenant}/templates/distinct-namespaces | List all distinct namespaces |
| [**update27**](TemplatesApi.md#update27) | **PUT** /api/v1/{tenant}/templates/{namespace}/{id} | Update a template |
| [**update9**](TemplatesApi.md#update9) | **PUT** /api/v1/templates/{namespace}/{id} | Update a template |
| [**updateNamespace1**](TemplatesApi.md#updateNamespace1) | **POST** /api/v1/templates/{namespace} | Update a complete namespace from json object |
| [**updateNamespace3**](TemplatesApi.md#updateNamespace3) | **POST** /api/v1/{tenant}/templates/{namespace} | Update a complete namespace from json object |
| [**validateTemplates**](TemplatesApi.md#validateTemplates) | **POST** /api/v1/templates/validate | Validate a list of templates |
| [**validateTemplates1**](TemplatesApi.md#validateTemplates1) | **POST** /api/v1/{tenant}/templates/validate | Validate a list of templates |



## create13

> Template create13(template)

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
            Template result = apiInstance.create13(template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#create13");
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
| **200** | create_13 200 response |  -  |


## create38

> Template create38(tenant, template)

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
            Template result = apiInstance.create38(tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#create38");
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
| **200** | create_38 200 response |  -  |


## delete16

> delete16(namespace, id)

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
            apiInstance.delete16(namespace, id);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#delete16");
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
| **200** | delete_16 200 response |  -  |


## delete44

> delete44(namespace, id, tenant)

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
            apiInstance.delete44(namespace, id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#delete44");
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
| **200** | delete_44 200 response |  -  |


## deleteByIds2

> BulkResponse deleteByIds2(idWithNamespace)

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
            BulkResponse result = apiInstance.deleteByIds2(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByIds2");
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
| **200** | deleteByIds_2 200 response |  -  |


## deleteByIds5

> BulkResponse deleteByIds5(tenant, idWithNamespace)

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
            BulkResponse result = apiInstance.deleteByIds5(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByIds5");
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
| **200** | deleteByIds_5 200 response |  -  |


## deleteByQuery2

> BulkResponse deleteByQuery2(q, namespace)

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
            BulkResponse result = apiInstance.deleteByQuery2(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByQuery2");
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
| **200** | deleteByQuery_2 200 response |  -  |


## deleteByQuery5

> BulkResponse deleteByQuery5(tenant, q, namespace)

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
            BulkResponse result = apiInstance.deleteByQuery5(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#deleteByQuery5");
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
| **200** | deleteByQuery_5 200 response |  -  |


## exportByIds1

> List&lt;byte[]&gt; exportByIds1(idWithNamespace)

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
            List<byte[]> result = apiInstance.exportByIds1(idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByIds1");
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
| **200** | exportByIds_1 200 response |  -  |


## exportByIds3

> List&lt;byte[]&gt; exportByIds3(tenant, idWithNamespace)

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
            List<byte[]> result = apiInstance.exportByIds3(tenant, idWithNamespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByIds3");
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
| **200** | exportByIds_3 200 response |  -  |


## exportByQuery1

> List&lt;byte[]&gt; exportByQuery1(q, namespace)

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
            List<byte[]> result = apiInstance.exportByQuery1(q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByQuery1");
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
| **200** | exportByQuery_1 200 response |  -  |


## exportByQuery3

> List&lt;byte[]&gt; exportByQuery3(tenant, q, namespace)

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
            List<byte[]> result = apiInstance.exportByQuery3(tenant, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#exportByQuery3");
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
| **200** | exportByQuery_3 200 response |  -  |


## find13

> PagedResultsTemplate find13(page, size, sort, q, namespace)

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
            PagedResultsTemplate result = apiInstance.find13(page, size, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#find13");
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
| **200** | find_13 200 response |  -  |


## find39

> PagedResultsTemplate find39(page, size, tenant, sort, q, namespace)

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
            PagedResultsTemplate result = apiInstance.find39(page, size, tenant, sort, q, namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#find39");
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
| **200** | find_39 200 response |  -  |


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


## importTemplates1

> importTemplates1(tenant, fileUpload)

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
            apiInstance.importTemplates1(tenant, fileUpload);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#importTemplates1");
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
| **200** | importTemplates_1 200 response |  -  |


## index30

> Template index30(namespace, id, tenant)

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
            Template result = apiInstance.index30(namespace, id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#index30");
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
| **200** | index_30 200 response |  -  |


## index9

> Template index9(namespace, id)

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
            Template result = apiInstance.index9(namespace, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#index9");
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
| **200** | index_9 200 response |  -  |


## listDistinctNamespace2

> List&lt;String&gt; listDistinctNamespace2()

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
            List<String> result = apiInstance.listDistinctNamespace2();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#listDistinctNamespace2");
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
| **200** | listDistinctNamespace_2 200 response |  -  |


## listDistinctNamespace5

> List&lt;String&gt; listDistinctNamespace5(tenant)

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
            List<String> result = apiInstance.listDistinctNamespace5(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#listDistinctNamespace5");
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
| **200** | listDistinctNamespace_5 200 response |  -  |


## update27

> Template update27(namespace, id, tenant, template)

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
            Template result = apiInstance.update27(namespace, id, tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#update27");
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
| **200** | update_27 200 response |  -  |


## update9

> Template update9(namespace, id, template)

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
            Template result = apiInstance.update9(namespace, id, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#update9");
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
| **200** | update_9 200 response |  -  |


## updateNamespace1

> List&lt;Template&gt; updateNamespace1(namespace, delete, template)

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
            List<Template> result = apiInstance.updateNamespace1(namespace, delete, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#updateNamespace1");
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
| **200** | updateNamespace_1 200 response |  -  |


## updateNamespace3

> List&lt;Template&gt; updateNamespace3(namespace, delete, tenant, template)

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
            List<Template> result = apiInstance.updateNamespace3(namespace, delete, tenant, template);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#updateNamespace3");
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
| **200** | updateNamespace_3 200 response |  -  |


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


## validateTemplates1

> List&lt;ValidateConstraintViolation&gt; validateTemplates1(tenant, body)

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
            List<ValidateConstraintViolation> result = apiInstance.validateTemplates1(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TemplatesApi#validateTemplates1");
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
| **200** | validateTemplates_1 200 response |  -  |

