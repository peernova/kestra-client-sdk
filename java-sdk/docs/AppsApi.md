# AppsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create**](AppsApi.md#create) | **POST** /api/v1/apps | Create a new app |
| [**create26**](AppsApi.md#create26) | **POST** /api/v1/{tenant}/apps | Create a new app |
| [**delete**](AppsApi.md#delete) | **DELETE** /api/v1/apps/{uid} | Delete an existing app |
| [**delete29**](AppsApi.md#delete29) | **DELETE** /api/v1/{tenant}/apps/{uid} | Delete an existing app |
| [**disable**](AppsApi.md#disable) | **POST** /api/v1/apps/{uid}/disable | Disable the app. |
| [**disable2**](AppsApi.md#disable2) | **POST** /api/v1/{tenant}/apps/{uid}/disable | Disable the app. |
| [**dispatch**](AppsApi.md#dispatch) | **POST** /api/v1/apps/view/{id}/dispatch/{dispatch} | Dispatch for a given app. |
| [**dispatch1**](AppsApi.md#dispatch1) | **POST** /api/v1/{tenant}/apps/view/{id}/dispatch/{dispatch} | Dispatch for a given app. |
| [**download**](AppsApi.md#download) | **GET** /api/v1/apps/view/{uid}/logs/download | Download logs for an app execution |
| [**download2**](AppsApi.md#download2) | **GET** /api/v1/{tenant}/apps/view/{uid}/logs/download | Download logs for an app execution |
| [**enable**](AppsApi.md#enable) | **POST** /api/v1/apps/{uid}/enable | Enable the app. |
| [**enable2**](AppsApi.md#enable2) | **POST** /api/v1/{tenant}/apps/{uid}/enable | Enable the app. |
| [**get**](AppsApi.md#get) | **GET** /api/v1/apps/{uid} | Get a app |
| [**get8**](AppsApi.md#get8) | **GET** /api/v1/{tenant}/apps/{uid} | Get a app |
| [**getFileDownload**](AppsApi.md#getFileDownload) | **GET** /api/v1/apps/view/{id}/file/download | Download file for an app execution |
| [**getFileDownload1**](AppsApi.md#getFileDownload1) | **GET** /api/v1/{tenant}/apps/view/{id}/file/download | Download file for an app execution |
| [**getFileMeta**](AppsApi.md#getFileMeta) | **GET** /api/v1/apps/view/{id}/file/meta | Get file meta information for an app execution |
| [**getFileMeta1**](AppsApi.md#getFileMeta1) | **GET** /api/v1/{tenant}/apps/view/{id}/file/meta | Get file meta information for an app execution |
| [**getFilePreview**](AppsApi.md#getFilePreview) | **GET** /api/v1/apps/view/{id}/file/preview | Get file preview for an app execution |
| [**getFilePreview1**](AppsApi.md#getFilePreview1) | **GET** /api/v1/{tenant}/apps/view/{id}/file/preview | Get file preview for an app execution |
| [**open**](AppsApi.md#open) | **GET** /api/v1/apps/view/{uid} | Open an app |
| [**open1**](AppsApi.md#open1) | **GET** /api/v1/{tenant}/apps/view/{uid} | Open an app |
| [**search**](AppsApi.md#search) | **GET** /api/v1/apps/search | Search for apps |
| [**search5**](AppsApi.md#search5) | **GET** /api/v1/{tenant}/apps/search | Search for apps |
| [**streams**](AppsApi.md#streams) | **GET** /api/v1/apps/view/{id}/streams/{stream} | Get an event stream from a given app. |
| [**streams1**](AppsApi.md#streams1) | **GET** /api/v1/{tenant}/apps/view/{id}/streams/{stream} | Get an event stream from a given app. |
| [**tags**](AppsApi.md#tags) | **GET** /api/v1/apps/tags | Get all the app tags |
| [**tags1**](AppsApi.md#tags1) | **GET** /api/v1/{tenant}/apps/tags | Get all the app tags |
| [**update**](AppsApi.md#update) | **PUT** /api/v1/apps/{uid} | Update an existing app |
| [**update19**](AppsApi.md#update19) | **PUT** /api/v1/{tenant}/apps/{uid} | Update an existing app |



## create

> AppsControllerApiAppSource create(body)

Create a new app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            AppsControllerApiAppSource result = apiInstance.create(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#create");
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

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create 200 response |  -  |


## create26

> AppsControllerApiAppSource create26(tenant, body)

Create a new app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            AppsControllerApiAppSource result = apiInstance.create26(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#create26");
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

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_26 200 response |  -  |


## delete

> Object delete(uid)

Delete an existing app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        try {
            Object result = apiInstance.delete(uid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#delete");
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
| **uid** | **String**| The ID of the app | |

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
| **200** | delete 200 response |  -  |


## delete29

> Object delete29(uid, tenant)

Delete an existing app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.delete29(uid, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#delete29");
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
| **uid** | **String**| The ID of the app | |
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
| **200** | delete_29 200 response |  -  |


## disable

> AppsControllerApiApp disable(uid)

Disable the app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of app
        try {
            AppsControllerApiApp result = apiInstance.disable(uid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#disable");
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
| **uid** | **String**| The ID of app | |

### Return type

[**AppsControllerApiApp**](AppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disable 200 response |  -  |


## disable2

> AppsControllerApiApp disable2(uid, tenant)

Disable the app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of app
        String tenant = "tenant_example"; // String | 
        try {
            AppsControllerApiApp result = apiInstance.disable2(uid, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#disable2");
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
| **uid** | **String**| The ID of app | |
| **tenant** | **String**|  | |

### Return type

[**AppsControllerApiApp**](AppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | disable_2 200 response |  -  |


## dispatch

> AppResponse dispatch(id, dispatch, parameters)

Dispatch for a given app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        String dispatch = "dispatch_example"; // String | The ID to dispatch
        HttpParameters parameters = new HttpParameters(); // HttpParameters | 
        try {
            AppResponse result = apiInstance.dispatch(id, dispatch, parameters);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#dispatch");
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
| **id** | **String**| The ID of the app. | |
| **dispatch** | **String**| The ID to dispatch | |
| **parameters** | [**HttpParameters**](HttpParameters.md)|  | [optional] |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dispatch 200 response |  -  |


## dispatch1

> AppResponse dispatch1(id, dispatch, tenant, parameters)

Dispatch for a given app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        String dispatch = "dispatch_example"; // String | The ID to dispatch
        String tenant = "tenant_example"; // String | 
        HttpParameters parameters = new HttpParameters(); // HttpParameters | 
        try {
            AppResponse result = apiInstance.dispatch1(id, dispatch, tenant, parameters);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#dispatch1");
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
| **id** | **String**| The ID of the app. | |
| **dispatch** | **String**| The ID to dispatch | |
| **tenant** | **String**|  | |
| **parameters** | [**HttpParameters**](HttpParameters.md)|  | [optional] |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dispatch_1 200 response |  -  |


## download

> File download(uid, executionId, minLevel, taskIds)

Download logs for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app.
        String executionId = "executionId_example"; // String | The ID of the execution.
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        List<String> taskIds = Arrays.asList(); // List<String> | The tasks' IDs
        try {
            File result = apiInstance.download(uid, executionId, minLevel, taskIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#download");
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
| **uid** | **String**| The ID of the app. | |
| **executionId** | **String**| The ID of the execution. | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskIds** | [**List&lt;String&gt;**](String.md)| The tasks&#39; IDs | [optional] |

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
| **200** | download 200 response |  -  |


## download2

> File download2(uid, executionId, tenant, minLevel, taskIds)

Download logs for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app.
        String executionId = "executionId_example"; // String | The ID of the execution.
        String tenant = "tenant_example"; // String | 
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        List<String> taskIds = Arrays.asList(); // List<String> | The tasks' IDs
        try {
            File result = apiInstance.download2(uid, executionId, tenant, minLevel, taskIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#download2");
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
| **uid** | **String**| The ID of the app. | |
| **executionId** | **String**| The ID of the execution. | |
| **tenant** | **String**|  | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskIds** | [**List&lt;String&gt;**](String.md)| The tasks&#39; IDs | [optional] |

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
| **200** | download_2 200 response |  -  |


## enable

> AppsControllerApiApp enable(uid)

Enable the app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of app
        try {
            AppsControllerApiApp result = apiInstance.enable(uid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#enable");
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
| **uid** | **String**| The ID of app | |

### Return type

[**AppsControllerApiApp**](AppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enable 200 response |  -  |


## enable2

> AppsControllerApiApp enable2(uid, tenant)

Enable the app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of app
        String tenant = "tenant_example"; // String | 
        try {
            AppsControllerApiApp result = apiInstance.enable2(uid, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#enable2");
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
| **uid** | **String**| The ID of app | |
| **tenant** | **String**|  | |

### Return type

[**AppsControllerApiApp**](AppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | enable_2 200 response |  -  |


## get

> AppsControllerApiAppSource get(uid)

Get a app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        try {
            AppsControllerApiAppSource result = apiInstance.get(uid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#get");
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
| **uid** | **String**| The ID of the app | |

### Return type

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get 200 response |  -  |


## get8

> AppsControllerApiAppSource get8(uid, tenant)

Get a app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        String tenant = "tenant_example"; // String | 
        try {
            AppsControllerApiAppSource result = apiInstance.get8(uid, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#get8");
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
| **uid** | **String**| The ID of the app | |
| **tenant** | **String**|  | |

### Return type

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_8 200 response |  -  |


## getFileDownload

> File getFileDownload(id, path)

Download file for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        try {
            File result = apiInstance.getFileDownload(id, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFileDownload");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFileDownload 200 response |  -  |


## getFileDownload1

> File getFileDownload1(id, path, tenant)

Download file for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        String tenant = "tenant_example"; // String | 
        try {
            File result = apiInstance.getFileDownload1(id, path, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFileDownload1");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |
| **tenant** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFileDownload_1 200 response |  -  |


## getFileMeta

> FileMetas getFileMeta(id, path)

Get file meta information for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        try {
            FileMetas result = apiInstance.getFileMeta(id, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFileMeta");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |

### Return type

[**FileMetas**](FileMetas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFileMeta 200 response |  -  |


## getFileMeta1

> FileMetas getFileMeta1(id, path, tenant)

Get file meta information for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        String tenant = "tenant_example"; // String | 
        try {
            FileMetas result = apiInstance.getFileMeta1(id, path, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFileMeta1");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |
| **tenant** | **String**|  | |

### Return type

[**FileMetas**](FileMetas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFileMeta_1 200 response |  -  |


## getFilePreview

> Object getFilePreview(id, path, encoding, maxRows)

Get file preview for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        String encoding = "UTF-8"; // String | The file encoding as Java charset name. Defaults to UTF-8
        Integer maxRows = 56; // Integer | The max row returns
        try {
            Object result = apiInstance.getFilePreview(id, path, encoding, maxRows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFilePreview");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |
| **encoding** | **String**| The file encoding as Java charset name. Defaults to UTF-8 | [default to UTF-8] |
| **maxRows** | **Integer**| The max row returns | [optional] |

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
| **200** | getFilePreview 200 response |  -  |


## getFilePreview1

> Object getFilePreview1(id, path, encoding, tenant, maxRows)

Get file preview for an app execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        URI path = new URI(); // URI | The internal storage uri
        String encoding = "UTF-8"; // String | The file encoding as Java charset name. Defaults to UTF-8
        String tenant = "tenant_example"; // String | 
        Integer maxRows = 56; // Integer | The max row returns
        try {
            Object result = apiInstance.getFilePreview1(id, path, encoding, tenant, maxRows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#getFilePreview1");
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
| **id** | **String**| The ID of the app. | |
| **path** | **URI**| The internal storage uri | |
| **encoding** | **String**| The file encoding as Java charset name. Defaults to UTF-8 | [default to UTF-8] |
| **tenant** | **String**|  | |
| **maxRows** | **Integer**| The max row returns | [optional] |

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
| **200** | getFilePreview_1 200 response |  -  |


## open

> AppResponse open(uid, parameters)

Open an app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        HttpParameters parameters = new HashMap(); // HttpParameters | 
        try {
            AppResponse result = apiInstance.open(uid, parameters);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#open");
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
| **uid** | **String**| The ID of the app | |
| **parameters** | [**HttpParameters**](.md)|  | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | open 200 response |  -  |


## open1

> AppResponse open1(uid, parameters, tenant)

Open an app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        HttpParameters parameters = new HashMap(); // HttpParameters | 
        String tenant = "tenant_example"; // String | 
        try {
            AppResponse result = apiInstance.open1(uid, parameters, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#open1");
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
| **uid** | **String**| The ID of the app | |
| **parameters** | [**HttpParameters**](.md)|  | |
| **tenant** | **String**|  | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | open_1 200 response |  -  |


## search

> PagedResultsAppsControllerApiApp search(page, size, sort, tags, q, namespace, flowId)

Search for apps

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        try {
            PagedResultsAppsControllerApiApp result = apiInstance.search(page, size, sort, tags, q, namespace, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#search");
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
| **tags** | [**List&lt;String&gt;**](String.md)| A tags filter | [optional] |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |

### Return type

[**PagedResultsAppsControllerApiApp**](PagedResultsAppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search 200 response |  -  |


## search5

> PagedResultsAppsControllerApiApp search5(page, size, tenant, sort, tags, q, namespace, flowId)

Search for apps

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<String> tags = Arrays.asList(); // List<String> | A tags filter
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        try {
            PagedResultsAppsControllerApiApp result = apiInstance.search5(page, size, tenant, sort, tags, q, namespace, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#search5");
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
| **tags** | [**List&lt;String&gt;**](String.md)| A tags filter | [optional] |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |

### Return type

[**PagedResultsAppsControllerApiApp**](PagedResultsAppsControllerApiApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_5 200 response |  -  |


## streams

> EventAppResponse streams(id, stream, parameters)

Get an event stream from a given app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        String stream = "stream_example"; // String | The ID of the stream to get
        HttpParameters parameters = new HashMap(); // HttpParameters | 
        try {
            EventAppResponse result = apiInstance.streams(id, stream, parameters);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#streams");
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
| **id** | **String**| The ID of the app. | |
| **stream** | **String**| The ID of the stream to get | |
| **parameters** | [**HttpParameters**](.md)|  | |

### Return type

[**EventAppResponse**](EventAppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | streams 200 response |  -  |


## streams1

> EventAppResponse streams1(id, stream, parameters, tenant)

Get an event stream from a given app.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String id = "id_example"; // String | The ID of the app.
        String stream = "stream_example"; // String | The ID of the stream to get
        HttpParameters parameters = new HashMap(); // HttpParameters | 
        String tenant = "tenant_example"; // String | 
        try {
            EventAppResponse result = apiInstance.streams1(id, stream, parameters, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#streams1");
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
| **id** | **String**| The ID of the app. | |
| **stream** | **String**| The ID of the stream to get | |
| **parameters** | [**HttpParameters**](.md)|  | |
| **tenant** | **String**|  | |

### Return type

[**EventAppResponse**](EventAppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | streams_1 200 response |  -  |


## tags

> AppsControllerApiAppTags tags()

Get all the app tags

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        try {
            AppsControllerApiAppTags result = apiInstance.tags();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#tags");
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

[**AppsControllerApiAppTags**](AppsControllerApiAppTags.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tags 200 response |  -  |


## tags1

> AppsControllerApiAppTags tags1(tenant)

Get all the app tags

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            AppsControllerApiAppTags result = apiInstance.tags1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#tags1");
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

[**AppsControllerApiAppTags**](AppsControllerApiAppTags.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tags_1 200 response |  -  |


## update

> AppsControllerApiAppSource update(uid, body)

Update an existing app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        String body = "body_example"; // String | 
        try {
            AppsControllerApiAppSource result = apiInstance.update(uid, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#update");
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
| **uid** | **String**| The ID of the app | |
| **body** | **String**|  | |

### Return type

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update 200 response |  -  |


## update19

> AppsControllerApiAppSource update19(uid, tenant, body)

Update an existing app

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AppsApi apiInstance = new AppsApi(defaultClient);
        String uid = "uid_example"; // String | The ID of the app
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            AppsControllerApiAppSource result = apiInstance.update19(uid, tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AppsApi#update19");
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
| **uid** | **String**| The ID of the app | |
| **tenant** | **String**|  | |
| **body** | **String**|  | |

### Return type

[**AppsControllerApiAppSource**](AppsControllerApiAppSource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_19 200 response |  -  |

