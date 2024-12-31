# FilesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDirectory**](FilesApi.md#createDirectory) | **POST** /api/v1/namespaces/{namespace}/files/directory | Create a directory |
| [**createDirectory1**](FilesApi.md#createDirectory1) | **POST** /api/v1/{tenant}/namespaces/{namespace}/files/directory | Create a directory |
| [**createFile**](FilesApi.md#createFile) | **POST** /api/v1/namespaces/{namespace}/files | Create a file |
| [**createFile1**](FilesApi.md#createFile1) | **POST** /api/v1/{tenant}/namespaces/{namespace}/files | Create a file |
| [**delete12**](FilesApi.md#delete12) | **DELETE** /api/v1/namespaces/{namespace}/files | Delete a file or directory |
| [**delete40**](FilesApi.md#delete40) | **DELETE** /api/v1/{tenant}/namespaces/{namespace}/files | Delete a file or directory |
| [**export**](FilesApi.md#export) | **GET** /api/v1/namespaces/{namespace}/files/export | Export namespace files as a ZIP |
| [**export1**](FilesApi.md#export1) | **GET** /api/v1/{tenant}/namespaces/{namespace}/files/export | Export namespace files as a ZIP |
| [**file1**](FilesApi.md#file1) | **GET** /api/v1/namespaces/{namespace}/files | Get namespace file content |
| [**file3**](FilesApi.md#file3) | **GET** /api/v1/{tenant}/namespaces/{namespace}/files | Get namespace file content |
| [**list1**](FilesApi.md#list1) | **GET** /api/v1/namespaces/{namespace}/files/directory | List directory content |
| [**list5**](FilesApi.md#list5) | **GET** /api/v1/{tenant}/namespaces/{namespace}/files/directory | List directory content |
| [**move**](FilesApi.md#move) | **PUT** /api/v1/namespaces/{namespace}/files | Move a file or directory |
| [**move1**](FilesApi.md#move1) | **PUT** /api/v1/{tenant}/namespaces/{namespace}/files | Move a file or directory |
| [**search2**](FilesApi.md#search2) | **GET** /api/v1/namespaces/{namespace}/files/search | Find files which path contain the given string in their URI |
| [**search7**](FilesApi.md#search7) | **GET** /api/v1/{tenant}/namespaces/{namespace}/files/search | Find files which path contain the given string in their URI |
| [**stats**](FilesApi.md#stats) | **GET** /api/v1/namespaces/{namespace}/files/stats | Get namespace file stats such as size, creation &amp; modification dates and type |
| [**stats1**](FilesApi.md#stats1) | **GET** /api/v1/{tenant}/namespaces/{namespace}/files/stats | Get namespace file stats such as size, creation &amp; modification dates and type |



## createDirectory

> createDirectory(namespace, path)

Create a directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        try {
            apiInstance.createDirectory(namespace, path);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createDirectory");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | [optional] |

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
| **200** | createDirectory 200 response |  -  |


## createDirectory1

> createDirectory1(namespace, tenant, path)

Create a directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        String path = "path_example"; // String | The internal storage uri
        try {
            apiInstance.createDirectory1(namespace, tenant, path);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createDirectory1");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |
| **path** | **String**| The internal storage uri | [optional] |

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
| **200** | createDirectory_1 200 response |  -  |


## createFile

> createFile(namespace, path, fileContent)

Create a file

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        File fileContent = new File("/path/to/file"); // File | 
        try {
            apiInstance.createFile(namespace, path, fileContent);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFile");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | |
| **fileContent** | **File**|  | [optional] |

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
| **200** | createFile 200 response |  -  |


## createFile1

> createFile1(namespace, path, tenant, fileContent)

Create a file

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        String tenant = "tenant_example"; // String | 
        File fileContent = new File("/path/to/file"); // File | 
        try {
            apiInstance.createFile1(namespace, path, tenant, fileContent);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFile1");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | |
| **tenant** | **String**|  | |
| **fileContent** | **File**|  | [optional] |

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
| **200** | createFile_1 200 response |  -  |


## delete12

> delete12(namespace, path)

Delete a file or directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri of the file / directory to delete
        try {
            apiInstance.delete12(namespace, path);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#delete12");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri of the file / directory to delete | |

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
| **200** | delete_12 200 response |  -  |


## delete40

> delete40(namespace, path, tenant)

Delete a file or directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri of the file / directory to delete
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete40(namespace, path, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#delete40");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri of the file / directory to delete | |
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
| **200** | delete_40 200 response |  -  |


## export

> List&lt;byte[]&gt; export(namespace)

Export namespace files as a ZIP

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        try {
            List<byte[]> result = apiInstance.export(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#export");
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
| **namespace** | **String**| The namespace id | |

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
| **200** | export 200 response |  -  |


## export1

> List&lt;byte[]&gt; export1(namespace, tenant)

Export namespace files as a ZIP

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        try {
            List<byte[]> result = apiInstance.export1(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#export1");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |

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
| **200** | export_1 200 response |  -  |


## file1

> File file1(namespace, path)

Get namespace file content

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        try {
            File result = apiInstance.file1(namespace, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#file1");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | file_1 200 response |  -  |


## file3

> File file3(namespace, path, tenant)

Get namespace file content

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        String tenant = "tenant_example"; // String | 
        try {
            File result = apiInstance.file3(namespace, path, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#file3");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | |
| **tenant** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | file_3 200 response |  -  |


## list1

> List&lt;FileAttributes&gt; list1(namespace, path)

List directory content

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        try {
            List<FileAttributes> result = apiInstance.list1(namespace, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#list1");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | [optional] |

### Return type

[**List&lt;FileAttributes&gt;**](FileAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list_1 200 response |  -  |


## list5

> List&lt;FileAttributes&gt; list5(namespace, tenant, path)

List directory content

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        String path = "path_example"; // String | The internal storage uri
        try {
            List<FileAttributes> result = apiInstance.list5(namespace, tenant, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#list5");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |
| **path** | **String**| The internal storage uri | [optional] |

### Return type

[**List&lt;FileAttributes&gt;**](FileAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list_5 200 response |  -  |


## move

> move(namespace, from, to)

Move a file or directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        URI from = new URI(); // URI | The internal storage uri to move from
        URI to = new URI(); // URI | The internal storage uri to move to
        try {
            apiInstance.move(namespace, from, to);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#move");
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
| **namespace** | **String**| The namespace id | |
| **from** | **URI**| The internal storage uri to move from | |
| **to** | **URI**| The internal storage uri to move to | |

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
| **200** | move 200 response |  -  |


## move1

> move1(namespace, from, to, tenant)

Move a file or directory

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        URI from = new URI(); // URI | The internal storage uri to move from
        URI to = new URI(); // URI | The internal storage uri to move to
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.move1(namespace, from, to, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#move1");
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
| **namespace** | **String**| The namespace id | |
| **from** | **URI**| The internal storage uri to move from | |
| **to** | **URI**| The internal storage uri to move to | |
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
| **200** | move_1 200 response |  -  |


## search2

> List&lt;String&gt; search2(namespace, q)

Find files which path contain the given string in their URI

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String q = "q_example"; // String | The string the file path should contain
        try {
            List<String> result = apiInstance.search2(namespace, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#search2");
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
| **namespace** | **String**| The namespace id | |
| **q** | **String**| The string the file path should contain | |

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
| **200** | search_2 200 response |  -  |


## search7

> List&lt;String&gt; search7(namespace, q, tenant)

Find files which path contain the given string in their URI

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String q = "q_example"; // String | The string the file path should contain
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.search7(namespace, q, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#search7");
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
| **namespace** | **String**| The namespace id | |
| **q** | **String**| The string the file path should contain | |
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
| **200** | search_7 200 response |  -  |


## stats

> FileAttributes stats(namespace, path)

Get namespace file stats such as size, creation &amp; modification dates and type

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String path = "path_example"; // String | The internal storage uri
        try {
            FileAttributes result = apiInstance.stats(namespace, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#stats");
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
| **namespace** | **String**| The namespace id | |
| **path** | **String**| The internal storage uri | [optional] |

### Return type

[**FileAttributes**](FileAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | stats 200 response |  -  |


## stats1

> FileAttributes stats1(namespace, tenant, path)

Get namespace file stats such as size, creation &amp; modification dates and type

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace id
        String tenant = "tenant_example"; // String | 
        String path = "path_example"; // String | The internal storage uri
        try {
            FileAttributes result = apiInstance.stats1(namespace, tenant, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#stats1");
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
| **namespace** | **String**| The namespace id | |
| **tenant** | **String**|  | |
| **path** | **String**| The internal storage uri | [optional] |

### Return type

[**FileAttributes**](FileAttributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | stats_1 200 response |  -  |

