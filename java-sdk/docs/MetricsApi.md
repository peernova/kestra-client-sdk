# MetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aggregateByFlowId**](MetricsApi.md#aggregateByFlowId) | **GET** /api/v1/metrics/aggregates/{namespace}/{flowId}/{metric} | Get metrics aggregations for a specific flow |
| [**aggregateByFlowId1**](MetricsApi.md#aggregateByFlowId1) | **GET** /api/v1/{tenant}/metrics/aggregates/{namespace}/{flowId}/{metric} | Get metrics aggregations for a specific flow |
| [**aggregateByFlowIdAndTaskId**](MetricsApi.md#aggregateByFlowIdAndTaskId) | **GET** /api/v1/metrics/aggregates/{namespace}/{flowId}/{taskId}/{metric} | Get metrics aggregations for a specific flow |
| [**aggregateByFlowIdAndTaskId1**](MetricsApi.md#aggregateByFlowIdAndTaskId1) | **GET** /api/v1/{tenant}/metrics/aggregates/{namespace}/{flowId}/{taskId}/{metric} | Get metrics aggregations for a specific flow |
| [**findByExecution1**](MetricsApi.md#findByExecution1) | **GET** /api/v1/metrics/{executionId} | Get metrics for a specific execution |
| [**findByExecution3**](MetricsApi.md#findByExecution3) | **GET** /api/v1/{tenant}/metrics/{executionId} | Get metrics for a specific execution |
| [**flowMetrics**](MetricsApi.md#flowMetrics) | **GET** /api/v1/metrics/names/{namespace}/{flowId} | Get metrics names for a specific flow |
| [**flowMetrics1**](MetricsApi.md#flowMetrics1) | **GET** /api/v1/{tenant}/metrics/names/{namespace}/{flowId} | Get metrics names for a specific flow |
| [**taskMetrics**](MetricsApi.md#taskMetrics) | **GET** /api/v1/metrics/names/{namespace}/{flowId}/{taskId} | Get metrics names for a specific task in a flow |
| [**taskMetrics1**](MetricsApi.md#taskMetrics1) | **GET** /api/v1/{tenant}/metrics/names/{namespace}/{flowId}/{taskId} | Get metrics names for a specific task in a flow |
| [**tasks**](MetricsApi.md#tasks) | **GET** /api/v1/metrics/tasks/{namespace}/{flowId} | Get tasks id that have metrics for a specific flow, include deleted or renamed tasks |
| [**tasks1**](MetricsApi.md#tasks1) | **GET** /api/v1/{tenant}/metrics/tasks/{namespace}/{flowId} | Get tasks id that have metrics for a specific flow, include deleted or renamed tasks |



## aggregateByFlowId

> MetricAggregations aggregateByFlowId(namespace, flowId, metric, aggregation, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String metric = "metric_example"; // String | The metric name
        String aggregation = "sum"; // String | The type of aggregation: avg, sum, min or max
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime, default to now - 30 days
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime, default to now
        try {
            MetricAggregations result = apiInstance.aggregateByFlowId(namespace, flowId, metric, aggregation, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateByFlowId");
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
| **startDate** | **OffsetDateTime**| The start datetime, default to now - 30 days | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime, default to now | [optional] |

### Return type

[**MetricAggregations**](MetricAggregations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateByFlowId 200 response |  -  |


## aggregateByFlowId1

> MetricAggregations aggregateByFlowId1(namespace, flowId, metric, aggregation, tenant, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String metric = "metric_example"; // String | The metric name
        String aggregation = "sum"; // String | The type of aggregation: avg, sum, min or max
        String tenant = "tenant_example"; // String | 
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime, default to now - 30 days
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime, default to now
        try {
            MetricAggregations result = apiInstance.aggregateByFlowId1(namespace, flowId, metric, aggregation, tenant, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateByFlowId1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateByFlowId_1 200 response |  -  |


## aggregateByFlowIdAndTaskId

> MetricAggregations aggregateByFlowIdAndTaskId(namespace, flowId, taskId, metric, aggregation, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String taskId = "taskId_example"; // String | The task Id
        String metric = "metric_example"; // String | The metric name
        String aggregation = "sum"; // String | The type of aggregation: avg, sum, min or max
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime, default to now - 30 days
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime, default to now
        try {
            MetricAggregations result = apiInstance.aggregateByFlowIdAndTaskId(namespace, flowId, taskId, metric, aggregation, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateByFlowIdAndTaskId");
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
| **startDate** | **OffsetDateTime**| The start datetime, default to now - 30 days | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime, default to now | [optional] |

### Return type

[**MetricAggregations**](MetricAggregations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateByFlowIdAndTaskId 200 response |  -  |


## aggregateByFlowIdAndTaskId1

> MetricAggregations aggregateByFlowIdAndTaskId1(namespace, flowId, taskId, metric, aggregation, tenant, startDate, endDate)

Get metrics aggregations for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

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
            MetricAggregations result = apiInstance.aggregateByFlowIdAndTaskId1(namespace, flowId, taskId, metric, aggregation, tenant, startDate, endDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#aggregateByFlowIdAndTaskId1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | aggregateByFlowIdAndTaskId_1 200 response |  -  |


## findByExecution1

> PagedResultsMetricEntry findByExecution1(page, size, executionId, sort, taskRunId, taskId)

Get metrics for a specific execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String executionId = "executionId_example"; // String | The execution id
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        try {
            PagedResultsMetricEntry result = apiInstance.findByExecution1(page, size, executionId, sort, taskRunId, taskId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#findByExecution1");
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
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **taskId** | **String**| The task id | [optional] |

### Return type

[**PagedResultsMetricEntry**](PagedResultsMetricEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByExecution_1 200 response |  -  |


## findByExecution3

> PagedResultsMetricEntry findByExecution3(page, size, executionId, tenant, sort, taskRunId, taskId)

Get metrics for a specific execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String taskId = "taskId_example"; // String | The task id
        try {
            PagedResultsMetricEntry result = apiInstance.findByExecution3(page, size, executionId, tenant, sort, taskRunId, taskId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#findByExecution3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByExecution_3 200 response |  -  |


## flowMetrics

> List&lt;String&gt; flowMetrics(namespace, flowId)

Get metrics names for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        try {
            List<String> result = apiInstance.flowMetrics(namespace, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#flowMetrics");
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
| **200** | flowMetrics 200 response |  -  |


## flowMetrics1

> List&lt;String&gt; flowMetrics1(namespace, flowId, tenant)

Get metrics names for a specific flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.flowMetrics1(namespace, flowId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#flowMetrics1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowMetrics_1 200 response |  -  |


## taskMetrics

> List&lt;String&gt; taskMetrics(namespace, flowId, taskId)

Get metrics names for a specific task in a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String taskId = "taskId_example"; // String | The flow Id
        try {
            List<String> result = apiInstance.taskMetrics(namespace, flowId, taskId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#taskMetrics");
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
| **taskId** | **String**| The flow Id | |

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
| **200** | taskMetrics 200 response |  -  |


## taskMetrics1

> List&lt;String&gt; taskMetrics1(namespace, flowId, taskId, tenant)

Get metrics names for a specific task in a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String taskId = "taskId_example"; // String | The flow Id
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.taskMetrics1(namespace, flowId, taskId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#taskMetrics1");
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
| **taskId** | **String**| The flow Id | |
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
| **200** | taskMetrics_1 200 response |  -  |


## tasks

> List&lt;String&gt; tasks(namespace, flowId)

Get tasks id that have metrics for a specific flow, include deleted or renamed tasks

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        try {
            List<String> result = apiInstance.tasks(namespace, flowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#tasks");
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
| **200** | tasks 200 response |  -  |


## tasks1

> List&lt;String&gt; tasks1(namespace, flowId, tenant)

Get tasks id that have metrics for a specific flow, include deleted or renamed tasks

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String flowId = "flowId_example"; // String | The flow Id
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.tasks1(namespace, flowId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#tasks1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tasks_1 200 response |  -  |

