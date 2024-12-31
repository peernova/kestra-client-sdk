# StatsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dailyGroupByFlowStatistics**](StatsApi.md#dailyGroupByFlowStatistics) | **POST** /api/v1/stats/executions/daily/group-by-flow | Get daily statistics for executions group by namespaces and flows |
| [**dailyGroupByFlowStatistics1**](StatsApi.md#dailyGroupByFlowStatistics1) | **POST** /api/v1/{tenant}/stats/executions/daily/group-by-flow | Get daily statistics for executions group by namespaces and flows |
| [**dailyStatistics**](StatsApi.md#dailyStatistics) | **POST** /api/v1/stats/executions/daily | Get daily statistics for executions |
| [**dailyStatistics1**](StatsApi.md#dailyStatistics1) | **POST** /api/v1/{tenant}/stats/executions/daily | Get daily statistics for executions |
| [**dailyStatisticsGroupByNamespace**](StatsApi.md#dailyStatisticsGroupByNamespace) | **POST** /api/v1/stats/executions/daily/group-by-namespace | Get daily statistics for executions grouped by namespace |
| [**dailyStatisticsGroupByNamespace1**](StatsApi.md#dailyStatisticsGroupByNamespace1) | **POST** /api/v1/{tenant}/stats/executions/daily/group-by-namespace | Get daily statistics for executions grouped by namespace |
| [**lastExecutions**](StatsApi.md#lastExecutions) | **POST** /api/v1/stats/executions/latest/group-by-flow | Get latest execution by flows |
| [**lastExecutions1**](StatsApi.md#lastExecutions1) | **POST** /api/v1/{tenant}/stats/executions/latest/group-by-flow | Get latest execution by flows |
| [**logsDailyStatistics**](StatsApi.md#logsDailyStatistics) | **POST** /api/v1/stats/logs/daily | Get daily statistics for logs |
| [**logsDailyStatistics1**](StatsApi.md#logsDailyStatistics1) | **POST** /api/v1/{tenant}/stats/logs/daily | Get daily statistics for logs |
| [**summary**](StatsApi.md#summary) | **POST** /api/v1/stats/summary | Get summary statistics |
| [**summary1**](StatsApi.md#summary1) | **POST** /api/v1/{tenant}/stats/summary | Get summary statistics |
| [**taskRunsDailyStatistics**](StatsApi.md#taskRunsDailyStatistics) | **POST** /api/v1/stats/taskruns/daily | Get daily statistics for taskRuns |
| [**taskRunsDailyStatistics1**](StatsApi.md#taskRunsDailyStatistics1) | **POST** /api/v1/{tenant}/stats/taskruns/daily | Get daily statistics for taskRuns |



## dailyGroupByFlowStatistics

> Map&lt;String, Map&lt;String, List&lt;DailyExecutionStatistics&gt;&gt;&gt; dailyGroupByFlowStatistics(statsControllerByFlowStatisticRequest)

Get daily statistics for executions group by namespaces and flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerByFlowStatisticRequest statsControllerByFlowStatisticRequest = new StatsControllerByFlowStatisticRequest(); // StatsControllerByFlowStatisticRequest | 
        try {
            Map<String, Map<String, List<DailyExecutionStatistics>>> result = apiInstance.dailyGroupByFlowStatistics(statsControllerByFlowStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyGroupByFlowStatistics");
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
| **statsControllerByFlowStatisticRequest** | [**StatsControllerByFlowStatisticRequest**](StatsControllerByFlowStatisticRequest.md)|  | |

### Return type

[**Map&lt;String, Map&lt;String, List&lt;DailyExecutionStatistics&gt;&gt;&gt;**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyGroupByFlowStatistics 200 response |  -  |


## dailyGroupByFlowStatistics1

> Map&lt;String, Map&lt;String, List&lt;DailyExecutionStatistics&gt;&gt;&gt; dailyGroupByFlowStatistics1(tenant, statsControllerByFlowStatisticRequest)

Get daily statistics for executions group by namespaces and flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerByFlowStatisticRequest statsControllerByFlowStatisticRequest = new StatsControllerByFlowStatisticRequest(); // StatsControllerByFlowStatisticRequest | 
        try {
            Map<String, Map<String, List<DailyExecutionStatistics>>> result = apiInstance.dailyGroupByFlowStatistics1(tenant, statsControllerByFlowStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyGroupByFlowStatistics1");
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
| **statsControllerByFlowStatisticRequest** | [**StatsControllerByFlowStatisticRequest**](StatsControllerByFlowStatisticRequest.md)|  | |

### Return type

[**Map&lt;String, Map&lt;String, List&lt;DailyExecutionStatistics&gt;&gt;&gt;**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyGroupByFlowStatistics_1 200 response |  -  |


## dailyStatistics

> List&lt;DailyExecutionStatistics&gt; dailyStatistics(statsControllerStatisticRequest)

Get daily statistics for executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerStatisticRequest statsControllerStatisticRequest = new StatsControllerStatisticRequest(); // StatsControllerStatisticRequest | 
        try {
            List<DailyExecutionStatistics> result = apiInstance.dailyStatistics(statsControllerStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyStatistics");
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
| **statsControllerStatisticRequest** | [**StatsControllerStatisticRequest**](StatsControllerStatisticRequest.md)|  | |

### Return type

[**List&lt;DailyExecutionStatistics&gt;**](DailyExecutionStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyStatistics 200 response |  -  |


## dailyStatistics1

> List&lt;DailyExecutionStatistics&gt; dailyStatistics1(tenant, statsControllerStatisticRequest)

Get daily statistics for executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerStatisticRequest statsControllerStatisticRequest = new StatsControllerStatisticRequest(); // StatsControllerStatisticRequest | 
        try {
            List<DailyExecutionStatistics> result = apiInstance.dailyStatistics1(tenant, statsControllerStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyStatistics1");
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
| **statsControllerStatisticRequest** | [**StatsControllerStatisticRequest**](StatsControllerStatisticRequest.md)|  | |

### Return type

[**List&lt;DailyExecutionStatistics&gt;**](DailyExecutionStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyStatistics_1 200 response |  -  |


## dailyStatisticsGroupByNamespace

> Map&lt;String, ExecutionCountStatistics&gt; dailyStatisticsGroupByNamespace(statsControllerByNamespaceStatisticRequest)

Get daily statistics for executions grouped by namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerByNamespaceStatisticRequest statsControllerByNamespaceStatisticRequest = new StatsControllerByNamespaceStatisticRequest(); // StatsControllerByNamespaceStatisticRequest | 
        try {
            Map<String, ExecutionCountStatistics> result = apiInstance.dailyStatisticsGroupByNamespace(statsControllerByNamespaceStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyStatisticsGroupByNamespace");
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
| **statsControllerByNamespaceStatisticRequest** | [**StatsControllerByNamespaceStatisticRequest**](StatsControllerByNamespaceStatisticRequest.md)|  | |

### Return type

[**Map&lt;String, ExecutionCountStatistics&gt;**](ExecutionCountStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyStatisticsGroupByNamespace 200 response |  -  |


## dailyStatisticsGroupByNamespace1

> Map&lt;String, ExecutionCountStatistics&gt; dailyStatisticsGroupByNamespace1(tenant, statsControllerByNamespaceStatisticRequest)

Get daily statistics for executions grouped by namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerByNamespaceStatisticRequest statsControllerByNamespaceStatisticRequest = new StatsControllerByNamespaceStatisticRequest(); // StatsControllerByNamespaceStatisticRequest | 
        try {
            Map<String, ExecutionCountStatistics> result = apiInstance.dailyStatisticsGroupByNamespace1(tenant, statsControllerByNamespaceStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#dailyStatisticsGroupByNamespace1");
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
| **statsControllerByNamespaceStatisticRequest** | [**StatsControllerByNamespaceStatisticRequest**](StatsControllerByNamespaceStatisticRequest.md)|  | |

### Return type

[**Map&lt;String, ExecutionCountStatistics&gt;**](ExecutionCountStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dailyStatisticsGroupByNamespace_1 200 response |  -  |


## lastExecutions

> List&lt;Execution&gt; lastExecutions(statsControllerLastExecutionsRequest)

Get latest execution by flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerLastExecutionsRequest statsControllerLastExecutionsRequest = new StatsControllerLastExecutionsRequest(); // StatsControllerLastExecutionsRequest | 
        try {
            List<Execution> result = apiInstance.lastExecutions(statsControllerLastExecutionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#lastExecutions");
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
| **statsControllerLastExecutionsRequest** | [**StatsControllerLastExecutionsRequest**](StatsControllerLastExecutionsRequest.md)|  | |

### Return type

[**List&lt;Execution&gt;**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lastExecutions 200 response |  -  |


## lastExecutions1

> List&lt;Execution&gt; lastExecutions1(tenant, statsControllerLastExecutionsRequest)

Get latest execution by flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerLastExecutionsRequest statsControllerLastExecutionsRequest = new StatsControllerLastExecutionsRequest(); // StatsControllerLastExecutionsRequest | 
        try {
            List<Execution> result = apiInstance.lastExecutions1(tenant, statsControllerLastExecutionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#lastExecutions1");
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
| **statsControllerLastExecutionsRequest** | [**StatsControllerLastExecutionsRequest**](StatsControllerLastExecutionsRequest.md)|  | |

### Return type

[**List&lt;Execution&gt;**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lastExecutions_1 200 response |  -  |


## logsDailyStatistics

> List&lt;LogStatistics&gt; logsDailyStatistics(statsControllerLogStatisticRequest)

Get daily statistics for logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerLogStatisticRequest statsControllerLogStatisticRequest = new StatsControllerLogStatisticRequest(); // StatsControllerLogStatisticRequest | 
        try {
            List<LogStatistics> result = apiInstance.logsDailyStatistics(statsControllerLogStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#logsDailyStatistics");
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
| **statsControllerLogStatisticRequest** | [**StatsControllerLogStatisticRequest**](StatsControllerLogStatisticRequest.md)|  | |

### Return type

[**List&lt;LogStatistics&gt;**](LogStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | logsDailyStatistics 200 response |  -  |


## logsDailyStatistics1

> List&lt;LogStatistics&gt; logsDailyStatistics1(tenant, statsControllerLogStatisticRequest)

Get daily statistics for logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerLogStatisticRequest statsControllerLogStatisticRequest = new StatsControllerLogStatisticRequest(); // StatsControllerLogStatisticRequest | 
        try {
            List<LogStatistics> result = apiInstance.logsDailyStatistics1(tenant, statsControllerLogStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#logsDailyStatistics1");
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
| **statsControllerLogStatisticRequest** | [**StatsControllerLogStatisticRequest**](StatsControllerLogStatisticRequest.md)|  | |

### Return type

[**List&lt;LogStatistics&gt;**](LogStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | logsDailyStatistics_1 200 response |  -  |


## summary

> SummaryStatistics summary(statsControllerSummaryRequest)

Get summary statistics

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerSummaryRequest statsControllerSummaryRequest = new StatsControllerSummaryRequest(); // StatsControllerSummaryRequest | 
        try {
            SummaryStatistics result = apiInstance.summary(statsControllerSummaryRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#summary");
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
| **statsControllerSummaryRequest** | [**StatsControllerSummaryRequest**](StatsControllerSummaryRequest.md)|  | |

### Return type

[**SummaryStatistics**](SummaryStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | summary 200 response |  -  |


## summary1

> SummaryStatistics summary1(tenant, statsControllerSummaryRequest)

Get summary statistics

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerSummaryRequest statsControllerSummaryRequest = new StatsControllerSummaryRequest(); // StatsControllerSummaryRequest | 
        try {
            SummaryStatistics result = apiInstance.summary1(tenant, statsControllerSummaryRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#summary1");
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
| **statsControllerSummaryRequest** | [**StatsControllerSummaryRequest**](StatsControllerSummaryRequest.md)|  | |

### Return type

[**SummaryStatistics**](SummaryStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | summary_1 200 response |  -  |


## taskRunsDailyStatistics

> List&lt;DailyExecutionStatistics&gt; taskRunsDailyStatistics(statsControllerStatisticRequest)

Get daily statistics for taskRuns

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        StatsControllerStatisticRequest statsControllerStatisticRequest = new StatsControllerStatisticRequest(); // StatsControllerStatisticRequest | 
        try {
            List<DailyExecutionStatistics> result = apiInstance.taskRunsDailyStatistics(statsControllerStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#taskRunsDailyStatistics");
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
| **statsControllerStatisticRequest** | [**StatsControllerStatisticRequest**](StatsControllerStatisticRequest.md)|  | |

### Return type

[**List&lt;DailyExecutionStatistics&gt;**](DailyExecutionStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | taskRunsDailyStatistics 200 response |  -  |


## taskRunsDailyStatistics1

> List&lt;DailyExecutionStatistics&gt; taskRunsDailyStatistics1(tenant, statsControllerStatisticRequest)

Get daily statistics for taskRuns

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.StatsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        StatsApi apiInstance = new StatsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        StatsControllerStatisticRequest statsControllerStatisticRequest = new StatsControllerStatisticRequest(); // StatsControllerStatisticRequest | 
        try {
            List<DailyExecutionStatistics> result = apiInstance.taskRunsDailyStatistics1(tenant, statsControllerStatisticRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling StatsApi#taskRunsDailyStatistics1");
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
| **statsControllerStatisticRequest** | [**StatsControllerStatisticRequest**](StatsControllerStatisticRequest.md)|  | |

### Return type

[**List&lt;DailyExecutionStatistics&gt;**](DailyExecutionStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | taskRunsDailyStatistics_1 200 response |  -  |

