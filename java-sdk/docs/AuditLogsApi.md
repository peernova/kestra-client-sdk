# AuditLogsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diff**](AuditLogsApi.md#diff) | **GET** /api/v1/auditlogs/{id}/diff | Get the diff of an audit log |
| [**diff1**](AuditLogsApi.md#diff1) | **GET** /api/v1/{tenant}/auditlogs/{id}/diff | Get the diff of an audit log |
| [**find**](AuditLogsApi.md#find) | **POST** /api/v1/auditlogs/find | Find audit logs |
| [**find27**](AuditLogsApi.md#find27) | **POST** /api/v1/{tenant}/auditlogs/find | Find audit logs |
| [**search1**](AuditLogsApi.md#search1) | **GET** /api/v1/auditlogs/search | Search for audit logs |
| [**search6**](AuditLogsApi.md#search6) | **GET** /api/v1/{tenant}/auditlogs/search | Search for audit logs |



## diff

> AuditLogControllerAuditLogDiff diff(id)

Get the diff of an audit log

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        String id = "id_example"; // String | The id of the audit log
        try {
            AuditLogControllerAuditLogDiff result = apiInstance.diff(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#diff");
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
| **id** | **String**| The id of the audit log | |

### Return type

[**AuditLogControllerAuditLogDiff**](AuditLogControllerAuditLogDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | diff 200 response |  -  |


## diff1

> AuditLogControllerAuditLogDiff diff1(id, tenant)

Get the diff of an audit log

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        String id = "id_example"; // String | The id of the audit log
        String tenant = "tenant_example"; // String | 
        try {
            AuditLogControllerAuditLogDiff result = apiInstance.diff1(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#diff1");
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
| **id** | **String**| The id of the audit log | |
| **tenant** | **String**|  | |

### Return type

[**AuditLogControllerAuditLogDiff**](AuditLogControllerAuditLogDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | diff_1 200 response |  -  |


## find

> AuditLogControllerAuditLogWithUser find(auditLogControllerFindRequest)

Find audit logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        AuditLogControllerFindRequest auditLogControllerFindRequest = new AuditLogControllerFindRequest(); // AuditLogControllerFindRequest | 
        try {
            AuditLogControllerAuditLogWithUser result = apiInstance.find(auditLogControllerFindRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#find");
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
| **auditLogControllerFindRequest** | [**AuditLogControllerFindRequest**](AuditLogControllerFindRequest.md)|  | |

### Return type

[**AuditLogControllerAuditLogWithUser**](AuditLogControllerAuditLogWithUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find 200 response |  -  |


## find27

> AuditLogControllerAuditLogWithUser find27(tenant, auditLogControllerFindRequest)

Find audit logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        AuditLogControllerFindRequest auditLogControllerFindRequest = new AuditLogControllerFindRequest(); // AuditLogControllerFindRequest | 
        try {
            AuditLogControllerAuditLogWithUser result = apiInstance.find27(tenant, auditLogControllerFindRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#find27");
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
| **auditLogControllerFindRequest** | [**AuditLogControllerFindRequest**](AuditLogControllerFindRequest.md)|  | |

### Return type

[**AuditLogControllerAuditLogWithUser**](AuditLogControllerAuditLogWithUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_27 200 response |  -  |


## search1

> PagedResultsAuditLogControllerAuditLogWithUser search1(page, size, q, sort, namespace, flowId, executionId, userId, id, permission, startDate, endDate, details, type)

Search for audit logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String namespace = "namespace_example"; // String | A namespace filter
        String flowId = "flowId_example"; // String | A flow id filter
        String executionId = "executionId_example"; // String | An execution filter
        String userId = "userId_example"; // String | A user id filter
        String id = "id_example"; // String | A id filter
        Permission permission = Permission.fromValue("FLOW"); // Permission | A permission filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        Map<String, String> details = new HashMap(); // Map<String, String> | A list of auditLog details
        CrudEventType type = CrudEventType.fromValue("READ"); // CrudEventType | The event that create the audit log
        try {
            PagedResultsAuditLogControllerAuditLogWithUser result = apiInstance.search1(page, size, q, sort, namespace, flowId, executionId, userId, id, permission, startDate, endDate, details, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#search1");
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
| **namespace** | **String**| A namespace filter | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **executionId** | **String**| An execution filter | [optional] |
| **userId** | **String**| A user id filter | [optional] |
| **id** | **String**| A id filter | [optional] |
| **permission** | [**Permission**](.md)| A permission filter | [optional] [enum: FLOW, BLUEPRINT, TEMPLATE, NAMESPACE, EXECUTION, USER, GROUP, ROLE, BINDING, AUDITLOG, SECRET, KVSTORE, IMPERSONATE, SETTING, INFRASTRUCTURE, APP, APPEXECUTION, ME, APITOKEN, DASHBOARD, TENANT] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **details** | [**Map&lt;String, String&gt;**](String.md)| A list of auditLog details | [optional] |
| **type** | [**CrudEventType**](.md)| The event that create the audit log | [optional] [enum: READ, CREATE, UPDATE, DELETE, LOGIN, LOGOUT, IMPERSONATE] |

### Return type

[**PagedResultsAuditLogControllerAuditLogWithUser**](PagedResultsAuditLogControllerAuditLogWithUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_1 200 response |  -  |


## search6

> PagedResultsAuditLogControllerAuditLogWithUser search6(page, size, tenant, q, sort, namespace, flowId, executionId, userId, id, permission, startDate, endDate, details, type)

Search for audit logs

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.AuditLogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String namespace = "namespace_example"; // String | A namespace filter
        String flowId = "flowId_example"; // String | A flow id filter
        String executionId = "executionId_example"; // String | An execution filter
        String userId = "userId_example"; // String | A user id filter
        String id = "id_example"; // String | A id filter
        Permission permission = Permission.fromValue("FLOW"); // Permission | A permission filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        Map<String, String> details = new HashMap(); // Map<String, String> | A list of auditLog details
        CrudEventType type = CrudEventType.fromValue("READ"); // CrudEventType | The event that create the audit log
        try {
            PagedResultsAuditLogControllerAuditLogWithUser result = apiInstance.search6(page, size, tenant, q, sort, namespace, flowId, executionId, userId, id, permission, startDate, endDate, details, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AuditLogsApi#search6");
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
| **namespace** | **String**| A namespace filter | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **executionId** | **String**| An execution filter | [optional] |
| **userId** | **String**| A user id filter | [optional] |
| **id** | **String**| A id filter | [optional] |
| **permission** | [**Permission**](.md)| A permission filter | [optional] [enum: FLOW, BLUEPRINT, TEMPLATE, NAMESPACE, EXECUTION, USER, GROUP, ROLE, BINDING, AUDITLOG, SECRET, KVSTORE, IMPERSONATE, SETTING, INFRASTRUCTURE, APP, APPEXECUTION, ME, APITOKEN, DASHBOARD, TENANT] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **details** | [**Map&lt;String, String&gt;**](String.md)| A list of auditLog details | [optional] |
| **type** | [**CrudEventType**](.md)| The event that create the audit log | [optional] [enum: READ, CREATE, UPDATE, DELETE, LOGIN, LOGOUT, IMPERSONATE] |

### Return type

[**PagedResultsAuditLogControllerAuditLogWithUser**](PagedResultsAuditLogControllerAuditLogWithUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search_6 200 response |  -  |

