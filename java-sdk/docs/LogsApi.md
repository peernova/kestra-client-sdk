# LogsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delete10**](LogsApi.md#delete10) | **DELETE** /api/v1/logs/{executionId} | Delete logs for a specific execution, taskrun or task |
| [**delete38**](LogsApi.md#delete38) | **DELETE** /api/v1/{tenant}/logs/{executionId} | Delete logs for a specific execution, taskrun or task |
| [**deleteFromFlow**](LogsApi.md#deleteFromFlow) | **DELETE** /api/v1/logs/{namespace}/{flowId} | Delete logs for a specific execution, taskrun or task |
| [**deleteFromFlow1**](LogsApi.md#deleteFromFlow1) | **DELETE** /api/v1/{tenant}/logs/{namespace}/{flowId} | Delete logs for a specific execution, taskrun or task |
| [**download1**](LogsApi.md#download1) | **GET** /api/v1/logs/{executionId}/download | Download logs for a specific execution, taskrun or task |
| [**download3**](LogsApi.md#download3) | **GET** /api/v1/{tenant}/logs/{executionId}/download | Download logs for a specific execution, taskrun or task |
| [**find10**](LogsApi.md#find10) | **GET** /api/v1/logs/search | Search for logs |
| [**find36**](LogsApi.md#find36) | **GET** /api/v1/{tenant}/logs/search | Search for logs |
| [**findByExecution**](LogsApi.md#findByExecution) | **GET** /api/v1/logs/{executionId} | Get logs for a specific execution, taskrun or task |
| [**findByExecution2**](LogsApi.md#findByExecution2) | **GET** /api/v1/{tenant}/logs/{executionId} | Get logs for a specific execution, taskrun or task |
| [**follow1**](LogsApi.md#follow1) | **GET** /api/v1/logs/{executionId}/follow | Follow logs for a specific execution |
| [**follow3**](LogsApi.md#follow3) | **GET** /api/v1/{tenant}/logs/{executionId}/follow | Follow logs for a specific execution |



## delete10

> delete10(executionId, minLevel, taskRunId, taskId, attempt)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            apiInstance.delete10(executionId, minLevel, taskRunId, taskId, attempt);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#delete10");
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
| **executionId** | **String**| The execution id | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

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
| **200** | delete_10 200 response |  -  |


## delete38

> delete38(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            apiInstance.delete38(executionId, tenant, minLevel, taskRunId, taskId, attempt);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#delete38");
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
| **executionId** | **String**| The execution id | |
| **tenant** | **String**|  | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

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
| **200** | delete_38 200 response |  -  |


## deleteFromFlow

> deleteFromFlow(namespace, flowId, triggerId)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow identifier
        String triggerId = "triggerId_example"; // String | The trigger id
        try {
            apiInstance.deleteFromFlow(namespace, flowId, triggerId);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#deleteFromFlow");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow identifier | |
| **triggerId** | **String**| The trigger id | |

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
| **200** | deleteFromFlow 200 response |  -  |


## deleteFromFlow1

> deleteFromFlow1(namespace, flowId, triggerId, tenant)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow identifier
        String triggerId = "triggerId_example"; // String | The trigger id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.deleteFromFlow1(namespace, flowId, triggerId, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#deleteFromFlow1");
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
| **namespace** | **String**| The namespace | |
| **flowId** | **String**| The flow identifier | |
| **triggerId** | **String**| The trigger id | |
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
| **200** | deleteFromFlow_1 200 response |  -  |


## download1

> File download1(executionId, minLevel, taskRunId, taskId, attempt)

Download logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            File result = apiInstance.download1(executionId, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#download1");
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
| **executionId** | **String**| The execution id | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | download_1 200 response |  -  |


## download3

> File download3(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Download logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            File result = apiInstance.download3(executionId, tenant, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#download3");
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
| **executionId** | **String**| The execution id | |
| **tenant** | **String**|  | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | download_3 200 response |  -  |


## find10

> PagedResultsLogEntry find10(page, size, q, sort, namespace, flowId, triggerId, minLevel, startDate, endDate)

Search for logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        String triggerId = "triggerId_example"; // String | A trigger id filter
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        try {
            PagedResultsLogEntry result = apiInstance.find10(page, size, q, sort, namespace, flowId, triggerId, minLevel, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#find10");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **triggerId** | **String**| A trigger id filter | [optional] |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |

### Return type

[**PagedResultsLogEntry**](PagedResultsLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_10 200 response |  -  |


## find36

> PagedResultsLogEntry find36(page, size, tenant, q, sort, namespace, flowId, triggerId, minLevel, startDate, endDate)

Search for logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        String triggerId = "triggerId_example"; // String | A trigger id filter
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        try {
            PagedResultsLogEntry result = apiInstance.find36(page, size, tenant, q, sort, namespace, flowId, triggerId, minLevel, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#find36");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **triggerId** | **String**| A trigger id filter | [optional] |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |

### Return type

[**PagedResultsLogEntry**](PagedResultsLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_36 200 response |  -  |


## findByExecution

> List&lt;LogEntry&gt; findByExecution(executionId, minLevel, taskRunId, taskId, attempt)

Get logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            List<LogEntry> result = apiInstance.findByExecution(executionId, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#findByExecution");
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
| **executionId** | **String**| The execution id | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

### Return type

[**List&lt;LogEntry&gt;**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByExecution 200 response |  -  |


## findByExecution2

> List&lt;LogEntry&gt; findByExecution2(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Get logs for a specific execution, taskrun or task

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            List<LogEntry> result = apiInstance.findByExecution2(executionId, tenant, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#findByExecution2");
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
| **executionId** | **String**| The execution id | |
| **tenant** | **String**|  | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |
| **attempt** | **Integer**| The attempt number | [optional] |

### Return type

[**List&lt;LogEntry&gt;**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByExecution_2 200 response |  -  |


## follow1

> EventLogEntry follow1(executionId, minLevel)

Follow logs for a specific execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        try {
            EventLogEntry result = apiInstance.follow1(executionId, minLevel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#follow1");
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
| **executionId** | **String**| The execution id | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |

### Return type

[**EventLogEntry**](EventLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | follow_1 200 response |  -  |


## follow3

> EventLogEntry follow3(executionId, tenant, minLevel)

Follow logs for a specific execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        try {
            EventLogEntry result = apiInstance.follow3(executionId, tenant, minLevel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#follow3");
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
| **executionId** | **String**| The execution id | |
| **tenant** | **String**|  | |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |

### Return type

[**EventLogEntry**](EventLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | follow_3 200 response |  -  |

