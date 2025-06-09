# MetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aggregateMetricsFromFlow**](MetricsApi.md#aggregateMetricsFromFlow) | **GET** /api/v1/{tenant}/metrics/aggregates/{namespace}/{flowId}/{metric} | Get metrics aggregations for a specific flow |
| [**aggregateMetricsFromTask**](MetricsApi.md#aggregateMetricsFromTask) | **GET** /api/v1/{tenant}/metrics/aggregates/{namespace}/{flowId}/{taskId}/{metric} | Get metrics aggregations for a specific flow |
| [**listFlowMetrics**](MetricsApi.md#listFlowMetrics) | **GET** /api/v1/{tenant}/metrics/names/{namespace}/{flowId} | Get metrics names for a specific flow |
| [**listTaskMetrics**](MetricsApi.md#listTaskMetrics) | **GET** /api/v1/{tenant}/metrics/names/{namespace}/{flowId}/{taskId} | Get metrics names for a specific task in a flow |
| [**listTasksWithMetrics**](MetricsApi.md#listTasksWithMetrics) | **GET** /api/v1/{tenant}/metrics/tasks/{namespace}/{flowId} | Get tasks id that have metrics for a specific flow, include deleted or renamed tasks |
| [**searchByExecution**](MetricsApi.md#searchByExecution) | **GET** /api/v1/{tenant}/metrics/{executionId} | Get metrics for a specific execution |



## aggregateMetricsFromFlow

> MetricAggregations aggregateMetricsFromFlow(namespace, flowId, metric, aggregation, tenant, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String metric = "metric_example"; // String | The metric name
        String aggregation = "sum"; // String | The type of aggregation: avg, sum, min or max
        String tenant = "tenant_example"; // String |
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime, default to now - 30 days
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime, default to now
        try {
            MetricAggregations result = apiInstance.aggregateMetricsFromFlow(namespace, flowId, metric, aggregation, tenant, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateMetricsFromFlow");
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
| **flowId** | **String**| The flow Id | |
| **metric** | **String**| The metric name | |
| **aggregation** | **String**| The type of aggregation: avg, sum, min or max | [default to sum] |
| **tenant** | **String**|  | |
| **startDate** | **OffsetDateTime**| The start datetime, default to now - 30 days | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime, default to now | [optional] |

### Return type

[**MetricAggregations**](MetricAggregations.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateMetricsFromFlow 200 response |  -  |


## aggregateMetricsFromTask

> MetricAggregations aggregateMetricsFromTask(namespace, flowId, taskId, metric, aggregation, tenant, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String taskId = "taskId_example"; // String | The task Id
        String metric = "metric_example"; // String | The metric name
        String aggregation = "sum"; // String | The type of aggregation: avg, sum, min or max
        String tenant = "tenant_example"; // String |
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime, default to now - 30 days
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime, default to now
        try {
            MetricAggregations result = apiInstance.aggregateMetricsFromTask(namespace, flowId, taskId, metric, aggregation, tenant, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateMetricsFromTask");
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
| **flowId** | **String**| The flow Id | |
| **taskId** | **String**| The task Id | |
| **metric** | **String**| The metric name | |
| **aggregation** | **String**| The type of aggregation: avg, sum, min or max | [default to sum] |
| **tenant** | **String**|  | |
| **startDate** | **OffsetDateTime**| The start datetime, default to now - 30 days | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime, default to now | [optional] |

### Return type

[**MetricAggregations**](MetricAggregations.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateMetricsFromTask 200 response |  -  |


## listFlowMetrics

> List&lt;String&gt; listFlowMetrics(namespace, flowId, tenant)

Get metrics names for a specific flow

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String tenant = "tenant_example"; // String |
        try {
            List<String> result = apiInstance.listFlowMetrics(namespace, flowId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#listFlowMetrics");
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
| **flowId** | **String**| The flow Id | |
| **tenant** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listFlowMetrics 200 response |  -  |


## listTaskMetrics

> List&lt;String&gt; listTaskMetrics(namespace, flowId, taskId, tenant)

Get metrics names for a specific task in a flow

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String taskId = "taskId_example"; // String | The task Id
        String tenant = "tenant_example"; // String |
        try {
            List<String> result = apiInstance.listTaskMetrics(namespace, flowId, taskId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#listTaskMetrics");
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
| **flowId** | **String**| The flow Id | |
| **taskId** | **String**| The task Id | |
| **tenant** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listTaskMetrics 200 response |  -  |


## listTasksWithMetrics

> List&lt;String&gt; listTasksWithMetrics(namespace, flowId, tenant)

Get tasks id that have metrics for a specific flow, include deleted or renamed tasks

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String tenant = "tenant_example"; // String |
        try {
            List<String> result = apiInstance.listTasksWithMetrics(namespace, flowId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#listTasksWithMetrics");
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
| **flowId** | **String**| The flow Id | |
| **tenant** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listTasksWithMetrics 200 response |  -  |


## searchByExecution

> PagedResultsMetricEntry searchByExecution(page, size, executionId, tenant, sort, taskRunId, taskId)

Get metrics for a specific execution

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.MetricsApi;

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

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String |
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        try {
            PagedResultsMetricEntry result = apiInstance.searchByExecution(page, size, executionId, tenant, sort, taskRunId, taskId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#searchByExecution");
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
| **executionId** | **String**| The execution id | |
| **tenant** | **String**|  | |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |

### Return type

[**PagedResultsMetricEntry**](PagedResultsMetricEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchByExecution 200 response |  -  |

