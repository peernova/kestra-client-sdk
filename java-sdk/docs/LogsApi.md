# LogsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLogsFromExecution**](LogsApi.md#deleteLogsFromExecution) | **DELETE** /api/v1/{tenant}/logs/{executionId} | Delete logs for a specific execution, taskrun or task |
| [**deleteLogsFromFlow**](LogsApi.md#deleteLogsFromFlow) | **DELETE** /api/v1/{tenant}/logs/{namespace}/{flowId} | Delete logs for a specific execution, taskrun or task |
| [**downloadLogsFromExecution**](LogsApi.md#downloadLogsFromExecution) | **GET** /api/v1/{tenant}/logs/{executionId}/download | Download logs for a specific execution, taskrun or task |
| [**followLogsFromExecution**](LogsApi.md#followLogsFromExecution) | **GET** /api/v1/{tenant}/logs/{executionId}/follow | Follow logs for a specific execution |
| [**listLogsFromExecution**](LogsApi.md#listLogsFromExecution) | **GET** /api/v1/{tenant}/logs/{executionId} | Get logs for a specific execution, taskrun or task |
| [**searchLogs**](LogsApi.md#searchLogs) | **GET** /api/v1/{tenant}/logs/search | Search for logs |



## deleteLogsFromExecution

> deleteLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String |
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            apiInstance.deleteLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#deleteLogsFromExecution");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteLogsFromExecution 200 response |  -  |


## deleteLogsFromFlow

> deleteLogsFromFlow(namespace, flowId, triggerId, tenant)

Delete logs for a specific execution, taskrun or task

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow identifier
        String triggerId = "triggerId_example"; // String | The trigger id
        String tenant = "tenant_example"; // String |
        try {
            apiInstance.deleteLogsFromFlow(namespace, flowId, triggerId, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#deleteLogsFromFlow");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteLogsFromFlow 200 response |  -  |


## downloadLogsFromExecution

> File downloadLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Download logs for a specific execution, taskrun or task

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String |
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            File result = apiInstance.downloadLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#downloadLogsFromExecution");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | downloadLogsFromExecution 200 response |  -  |


## followLogsFromExecution

> EventLogEntry followLogsFromExecution(executionId, tenant, minLevel)

Follow logs for a specific execution

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String |
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        try {
            EventLogEntry result = apiInstance.followLogsFromExecution(executionId, tenant, minLevel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#followLogsFromExecution");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | followLogsFromExecution 200 response |  -  |


## listLogsFromExecution

> List&lt;LogEntry&gt; listLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt)

Get logs for a specific execution, taskrun or task

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String |
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        Integer attempt = 56; // Integer | The attempt number
        try {
            List<LogEntry> result = apiInstance.listLogsFromExecution(executionId, tenant, minLevel, taskRunId, taskId, attempt);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#listLogsFromExecution");
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

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listLogsFromExecution 200 response |  -  |


## searchLogs

> PagedResultsLogEntry searchLogs(page, size, tenant, sort, filters, q, namespace, flowId, triggerId, minLevel, startDate, endDate)

Search for logs

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.LogsApi;

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

        LogsApi apiInstance = new LogsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        List<QueryFilter> filters = Arrays.asList(); // List<QueryFilter> | Filters
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        String triggerId = "triggerId_example"; // String | A trigger id filter
        Level minLevel = Level.fromValue("ERROR"); // Level | The min log level filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        try {
            PagedResultsLogEntry result = apiInstance.searchLogs(page, size, tenant, sort, filters, q, namespace, flowId, triggerId, minLevel, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#searchLogs");
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
| **filters** | [**List&lt;QueryFilter&gt;**](QueryFilter.md)| Filters | [optional] |
| **q** | **String**| A string filter | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **triggerId** | **String**| A trigger id filter | [optional] |
| **minLevel** | [**Level**](.md)| The min log level filter | [optional] [enum: ERROR, WARN, INFO, DEBUG, TRACE] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |

### Return type

[**PagedResultsLogEntry**](PagedResultsLogEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchLogs 200 response |  -  |

