# DashboardsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callList**](DashboardsApi.md#callList) | **GET** /api/v1/dashboards | List all dashboards |
| [**create28**](DashboardsApi.md#create28) | **POST** /api/v1/{tenant}/dashboards | Create a dashboard from yaml source |
| [**create3**](DashboardsApi.md#create3) | **POST** /api/v1/dashboards | Create a dashboard from yaml source |
| [**dashboardChart**](DashboardsApi.md#dashboardChart) | **POST** /api/v1/dashboards/{id}/charts/{chartId} | Generate a dashboard chart data |
| [**dashboardChart1**](DashboardsApi.md#dashboardChart1) | **POST** /api/v1/{tenant}/dashboards/{id}/charts/{chartId} | Generate a dashboard chart data |
| [**delete3**](DashboardsApi.md#delete3) | **DELETE** /api/v1/dashboards/{id} | Delete a dashboard |
| [**delete31**](DashboardsApi.md#delete31) | **DELETE** /api/v1/{tenant}/dashboards/{id} | Delete a dashboard |
| [**get1**](DashboardsApi.md#get1) | **GET** /api/v1/dashboards/{id} | Retrieve a dashboard |
| [**get9**](DashboardsApi.md#get9) | **GET** /api/v1/{tenant}/dashboards/{id} | Retrieve a dashboard |
| [**list4**](DashboardsApi.md#list4) | **GET** /api/v1/{tenant}/dashboards | List all dashboards |
| [**update2**](DashboardsApi.md#update2) | **PUT** /api/v1/dashboards/{id} | Update a dashboard |
| [**update20**](DashboardsApi.md#update20) | **PUT** /api/v1/{tenant}/dashboards/{id} | Update a dashboard |
| [**validate**](DashboardsApi.md#validate) | **POST** /api/v1/dashboards/validate | Validate dashboard from yaml source |
| [**validate1**](DashboardsApi.md#validate1) | **POST** /api/v1/{tenant}/dashboards/validate | Validate dashboard from yaml source |



## callList

> PagedResultsDashboard callList(page, size, q, sort)

List all dashboards

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | The filter query
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsDashboard result = apiInstance.callList(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#callList");
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
| **q** | **String**| The filter query | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsDashboard**](PagedResultsDashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list 200 response |  -  |


## create28

> Dashboard create28(tenant, body)

Create a dashboard from yaml source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            Dashboard result = apiInstance.create28(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#create28");
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

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_28 200 response |  -  |


## create3

> Dashboard create3(body)

Create a dashboard from yaml source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            Dashboard result = apiInstance.create3(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#create3");
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

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_3 200 response |  -  |


## dashboardChart

> PagedResultsMapStringObject dashboardChart(id, chartId, requestBody)

Generate a dashboard chart data

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String chartId = "chartId_example"; // String | The chart id
        Map<String, Object> requestBody = null; // Map<String, Object> | 
        try {
            PagedResultsMapStringObject result = apiInstance.dashboardChart(id, chartId, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#dashboardChart");
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
| **id** | **String**| The dashboard id | |
| **chartId** | **String**| The chart id | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

### Return type

[**PagedResultsMapStringObject**](PagedResultsMapStringObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dashboardChart 200 response |  -  |


## dashboardChart1

> PagedResultsMapStringObject dashboardChart1(id, chartId, tenant, requestBody)

Generate a dashboard chart data

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String chartId = "chartId_example"; // String | The chart id
        String tenant = "tenant_example"; // String | 
        Map<String, Object> requestBody = null; // Map<String, Object> | 
        try {
            PagedResultsMapStringObject result = apiInstance.dashboardChart1(id, chartId, tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#dashboardChart1");
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
| **id** | **String**| The dashboard id | |
| **chartId** | **String**| The chart id | |
| **tenant** | **String**|  | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

### Return type

[**PagedResultsMapStringObject**](PagedResultsMapStringObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | dashboardChart_1 200 response |  -  |


## delete3

> delete3(id)

Delete a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        try {
            apiInstance.delete3(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#delete3");
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
| **id** | **String**| The dashboard id | |

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
| **200** | delete_3 200 response |  -  |


## delete31

> delete31(id, tenant)

Delete a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete31(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#delete31");
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
| **id** | **String**| The dashboard id | |
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
| **200** | delete_31 200 response |  -  |


## get1

> Dashboard get1(id)

Retrieve a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        try {
            Dashboard result = apiInstance.get1(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#get1");
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
| **id** | **String**| The dashboard id | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_1 200 response |  -  |


## get9

> Dashboard get9(id, tenant)

Retrieve a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String tenant = "tenant_example"; // String | 
        try {
            Dashboard result = apiInstance.get9(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#get9");
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
| **id** | **String**| The dashboard id | |
| **tenant** | **String**|  | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_9 200 response |  -  |


## list4

> PagedResultsDashboard list4(page, size, tenant, q, sort)

List all dashboards

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | The filter query
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsDashboard result = apiInstance.list4(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#list4");
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
| **q** | **String**| The filter query | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsDashboard**](PagedResultsDashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list_4 200 response |  -  |


## update2

> Dashboard update2(id, body)

Update a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String body = "body_example"; // String | 
        try {
            Dashboard result = apiInstance.update2(id, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#update2");
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
| **id** | **String**| The dashboard id | |
| **body** | **String**|  | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_2 200 response |  -  |


## update20

> Dashboard update20(id, tenant, body)

Update a dashboard

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String id = "id_example"; // String | The dashboard id
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            Dashboard result = apiInstance.update20(id, tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#update20");
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
| **id** | **String**| The dashboard id | |
| **tenant** | **String**|  | |
| **body** | **String**|  | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_20 200 response |  -  |


## validate

> ValidateConstraintViolation validate(body)

Validate dashboard from yaml source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validate(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#validate");
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

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validate 200 response |  -  |


## validate1

> ValidateConstraintViolation validate1(tenant, body)

Validate dashboard from yaml source

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.DashboardsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        DashboardsApi apiInstance = new DashboardsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            ValidateConstraintViolation result = apiInstance.validate1(tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DashboardsApi#validate1");
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

[**ValidateConstraintViolation**](ValidateConstraintViolation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validate_1 200 response |  -  |

