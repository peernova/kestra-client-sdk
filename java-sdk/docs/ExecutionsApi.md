# ExecutionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callFile**](ExecutionsApi.md#callFile) | **GET** /api/v1/executions/{executionId}/file | Download file for an execution |
| [**changeState**](ExecutionsApi.md#changeState) | **POST** /api/v1/executions/{executionId}/state | Change state for a taskrun in an execution |
| [**changeState1**](ExecutionsApi.md#changeState1) | **POST** /api/v1/{tenant}/executions/{executionId}/state | Change state for a taskrun in an execution |
| [**changeStatus**](ExecutionsApi.md#changeStatus) | **POST** /api/v1/executions/{executionId}/change-status | Change the status of an execution |
| [**changeStatus1**](ExecutionsApi.md#changeStatus1) | **POST** /api/v1/{tenant}/executions/{executionId}/change-status | Change the status of an execution |
| [**changeStatusById**](ExecutionsApi.md#changeStatusById) | **POST** /api/v1/executions/change-status/by-ids | Change status of executions by id |
| [**changeStatusById1**](ExecutionsApi.md#changeStatusById1) | **POST** /api/v1/{tenant}/executions/change-status/by-ids | Change status of executions by id |
| [**changeStatusByQuery**](ExecutionsApi.md#changeStatusByQuery) | **POST** /api/v1/executions/change-status/by-query | Change executions status by query parameters |
| [**changeStatusByQuery1**](ExecutionsApi.md#changeStatusByQuery1) | **POST** /api/v1/{tenant}/executions/change-status/by-query | Change executions status by query parameters |
| [**create29**](ExecutionsApi.md#create29) | **POST** /api/v1/{tenant}/executions/{namespace}/{id} | Create a new execution for a flow |
| [**create4**](ExecutionsApi.md#create4) | **POST** /api/v1/executions/{namespace}/{id} | Create a new execution for a flow |
| [**delete32**](ExecutionsApi.md#delete32) | **DELETE** /api/v1/{tenant}/executions/{executionId} | Delete an execution |
| [**delete4**](ExecutionsApi.md#delete4) | **DELETE** /api/v1/executions/{executionId} | Delete an execution |
| [**deleteByIds**](ExecutionsApi.md#deleteByIds) | **DELETE** /api/v1/executions/by-ids | Delete a list of executions |
| [**deleteByIds3**](ExecutionsApi.md#deleteByIds3) | **DELETE** /api/v1/{tenant}/executions/by-ids | Delete a list of executions |
| [**deleteByQuery**](ExecutionsApi.md#deleteByQuery) | **DELETE** /api/v1/executions/by-query | Delete executions filter by query parameters |
| [**deleteByQuery3**](ExecutionsApi.md#deleteByQuery3) | **DELETE** /api/v1/{tenant}/executions/by-query | Delete executions filter by query parameters |
| [**eval**](ExecutionsApi.md#eval) | **POST** /api/v1/executions/{executionId}/eval/{taskRunId} | Evaluate a variable expression for this taskrun |
| [**eval1**](ExecutionsApi.md#eval1) | **POST** /api/v1/{tenant}/executions/{executionId}/eval/{taskRunId} | Evaluate a variable expression for this taskrun |
| [**file2**](ExecutionsApi.md#file2) | **GET** /api/v1/{tenant}/executions/{executionId}/file | Download file for an execution |
| [**filePreview**](ExecutionsApi.md#filePreview) | **GET** /api/v1/executions/{executionId}/file/preview | Get file preview for an execution |
| [**filePreview1**](ExecutionsApi.md#filePreview1) | **GET** /api/v1/{tenant}/executions/{executionId}/file/preview | Get file preview for an execution |
| [**filesize**](ExecutionsApi.md#filesize) | **GET** /api/v1/executions/{executionId}/file/metas | Get file meta information for an execution |
| [**filesize1**](ExecutionsApi.md#filesize1) | **GET** /api/v1/{tenant}/executions/{executionId}/file/metas | Get file meta information for an execution |
| [**find30**](ExecutionsApi.md#find30) | **GET** /api/v1/{tenant}/executions/search | Search for executions |
| [**find4**](ExecutionsApi.md#find4) | **GET** /api/v1/executions/search | Search for executions |
| [**findByFlowId**](ExecutionsApi.md#findByFlowId) | **GET** /api/v1/executions | Search for executions for a flow |
| [**findByFlowId1**](ExecutionsApi.md#findByFlowId1) | **GET** /api/v1/{tenant}/executions | Search for executions for a flow |
| [**findTaskRun**](ExecutionsApi.md#findTaskRun) | **GET** /api/v1/taskruns/search | Search for taskruns, only available with the Elasticsearch repository |
| [**findTaskRun1**](ExecutionsApi.md#findTaskRun1) | **GET** /api/v1/{tenant}/taskruns/search | Search for taskruns, only available with the Elasticsearch repository |
| [**flowGraph**](ExecutionsApi.md#flowGraph) | **GET** /api/v1/executions/{executionId}/graph | Generate a graph for an execution |
| [**flowGraph2**](ExecutionsApi.md#flowGraph2) | **GET** /api/v1/{tenant}/executions/{executionId}/graph | Generate a graph for an execution |
| [**follow**](ExecutionsApi.md#follow) | **GET** /api/v1/executions/{executionId}/follow | Follow an execution |
| [**follow2**](ExecutionsApi.md#follow2) | **GET** /api/v1/{tenant}/executions/{executionId}/follow | Follow an execution |
| [**forceRun**](ExecutionsApi.md#forceRun) | **POST** /api/v1/executions/{executionId}/force-run | Force run an execution |
| [**forceRun1**](ExecutionsApi.md#forceRun1) | **POST** /api/v1/{tenant}/executions/{executionId}/force-run | Force run an execution |
| [**forceRunByIds**](ExecutionsApi.md#forceRunByIds) | **POST** /api/v1/executions/force-run/by-ids | Force run a list of executions |
| [**forceRunByIds1**](ExecutionsApi.md#forceRunByIds1) | **POST** /api/v1/{tenant}/executions/force-run/by-ids | Force run a list of executions |
| [**forceRunByQuery**](ExecutionsApi.md#forceRunByQuery) | **POST** /api/v1/executions/force-run/by-query | Force run executions filter by query parameters |
| [**forceRunByQuery1**](ExecutionsApi.md#forceRunByQuery1) | **POST** /api/v1/{tenant}/executions/force-run/by-query | Force run executions filter by query parameters |
| [**get10**](ExecutionsApi.md#get10) | **GET** /api/v1/{tenant}/executions/{executionId} | Get an execution |
| [**get2**](ExecutionsApi.md#get2) | **GET** /api/v1/executions/{executionId} | Get an execution |
| [**getFlowForExecution**](ExecutionsApi.md#getFlowForExecution) | **GET** /api/v1/executions/flows/{namespace}/{flowId} | Get flow information&#39;s for an execution |
| [**getFlowForExecution1**](ExecutionsApi.md#getFlowForExecution1) | **GET** /api/v1/{tenant}/executions/flows/{namespace}/{flowId} | Get flow information&#39;s for an execution |
| [**getFlowForExecutionById**](ExecutionsApi.md#getFlowForExecutionById) | **GET** /api/v1/executions/{executionId}/flow | Get flow information&#39;s for an execution |
| [**getFlowForExecutionById1**](ExecutionsApi.md#getFlowForExecutionById1) | **GET** /api/v1/{tenant}/executions/{executionId}/flow | Get flow information&#39;s for an execution |
| [**getFlowsByNamespace**](ExecutionsApi.md#getFlowsByNamespace) | **GET** /api/v1/executions/namespaces/{namespace}/flows | Get all flow ids for a namespace |
| [**getFlowsByNamespace2**](ExecutionsApi.md#getFlowsByNamespace2) | **GET** /api/v1/{tenant}/executions/namespaces/{namespace}/flows | Get all flow ids for a namespace |
| [**kill**](ExecutionsApi.md#kill) | **DELETE** /api/v1/executions/{executionId}/kill | Kill an execution |
| [**kill1**](ExecutionsApi.md#kill1) | **DELETE** /api/v1/{tenant}/executions/{executionId}/kill | Kill an execution |
| [**killByIds**](ExecutionsApi.md#killByIds) | **DELETE** /api/v1/executions/kill/by-ids | Kill a list of executions |
| [**killByIds1**](ExecutionsApi.md#killByIds1) | **DELETE** /api/v1/{tenant}/executions/kill/by-ids | Kill a list of executions |
| [**killByQuery**](ExecutionsApi.md#killByQuery) | **DELETE** /api/v1/executions/kill/by-query | Kill executions filter by query parameters |
| [**killByQuery1**](ExecutionsApi.md#killByQuery1) | **DELETE** /api/v1/{tenant}/executions/kill/by-query | Kill executions filter by query parameters |
| [**listDistinctNamespace**](ExecutionsApi.md#listDistinctNamespace) | **GET** /api/v1/executions/namespaces | Get all namespaces that have executable flows |
| [**listDistinctNamespace3**](ExecutionsApi.md#listDistinctNamespace3) | **GET** /api/v1/{tenant}/executions/namespaces | Get all namespaces that have executable flows |
| [**pause**](ExecutionsApi.md#pause) | **POST** /api/v1/executions/{executionId}/pause | Pause a running execution. |
| [**pause1**](ExecutionsApi.md#pause1) | **POST** /api/v1/{tenant}/executions/{executionId}/pause | Pause a running execution. |
| [**pauseByIds**](ExecutionsApi.md#pauseByIds) | **POST** /api/v1/executions/pause/by-ids | Pause a list of running executions |
| [**pauseByIds1**](ExecutionsApi.md#pauseByIds1) | **POST** /api/v1/{tenant}/executions/pause/by-ids | Pause a list of running executions |
| [**pauseByQuery**](ExecutionsApi.md#pauseByQuery) | **POST** /api/v1/executions/pause/by-query | Pause executions filter by query parameters |
| [**pauseByQuery1**](ExecutionsApi.md#pauseByQuery1) | **POST** /api/v1/{tenant}/executions/pause/by-query | Pause executions filter by query parameters |
| [**replay**](ExecutionsApi.md#replay) | **POST** /api/v1/executions/{executionId}/replay | Create a new execution from an old one and start it from a specified task run id |
| [**replay1**](ExecutionsApi.md#replay1) | **POST** /api/v1/{tenant}/executions/{executionId}/replay | Create a new execution from an old one and start it from a specified task run id |
| [**replayByIds**](ExecutionsApi.md#replayByIds) | **POST** /api/v1/executions/replay/by-ids | Create new executions from old ones. Keep the flow revision |
| [**replayByIds1**](ExecutionsApi.md#replayByIds1) | **POST** /api/v1/{tenant}/executions/replay/by-ids | Create new executions from old ones. Keep the flow revision |
| [**replayByQuery**](ExecutionsApi.md#replayByQuery) | **POST** /api/v1/executions/replay/by-query | Create new executions from old ones filter by query parameters. Keep the flow revision |
| [**replayByQuery1**](ExecutionsApi.md#replayByQuery1) | **POST** /api/v1/{tenant}/executions/replay/by-query | Create new executions from old ones filter by query parameters. Keep the flow revision |
| [**restart**](ExecutionsApi.md#restart) | **POST** /api/v1/executions/{executionId}/restart | Restart a new execution from an old one |
| [**restart2**](ExecutionsApi.md#restart2) | **POST** /api/v1/{tenant}/executions/{executionId}/restart | Restart a new execution from an old one |
| [**restartByIds**](ExecutionsApi.md#restartByIds) | **POST** /api/v1/executions/restart/by-ids | Restart a list of executions |
| [**restartByIds1**](ExecutionsApi.md#restartByIds1) | **POST** /api/v1/{tenant}/executions/restart/by-ids | Restart a list of executions |
| [**restartByQuery**](ExecutionsApi.md#restartByQuery) | **POST** /api/v1/executions/restart/by-query | Restart executions filter by query parameters |
| [**restartByQuery1**](ExecutionsApi.md#restartByQuery1) | **POST** /api/v1/{tenant}/executions/restart/by-query | Restart executions filter by query parameters |
| [**resume**](ExecutionsApi.md#resume) | **POST** /api/v1/executions/{executionId}/resume | Resume a paused execution. |
| [**resume1**](ExecutionsApi.md#resume1) | **POST** /api/v1/{tenant}/executions/{executionId}/resume | Resume a paused execution. |
| [**resumeByIds**](ExecutionsApi.md#resumeByIds) | **POST** /api/v1/executions/resume/by-ids | Resume a list of paused executions |
| [**resumeByIds1**](ExecutionsApi.md#resumeByIds1) | **POST** /api/v1/{tenant}/executions/resume/by-ids | Resume a list of paused executions |
| [**resumeByQuery**](ExecutionsApi.md#resumeByQuery) | **POST** /api/v1/executions/resume/by-query | Resume executions filter by query parameters |
| [**resumeByQuery1**](ExecutionsApi.md#resumeByQuery1) | **POST** /api/v1/{tenant}/executions/resume/by-query | Resume executions filter by query parameters |
| [**setLabels**](ExecutionsApi.md#setLabels) | **POST** /api/v1/executions/{executionId}/labels | Add or update labels of a terminated execution |
| [**setLabels1**](ExecutionsApi.md#setLabels1) | **POST** /api/v1/{tenant}/executions/{executionId}/labels | Add or update labels of a terminated execution |
| [**setLabelsByIds**](ExecutionsApi.md#setLabelsByIds) | **POST** /api/v1/executions/labels/by-ids | Set labels on a list of executions |
| [**setLabelsByIds1**](ExecutionsApi.md#setLabelsByIds1) | **POST** /api/v1/{tenant}/executions/labels/by-ids | Set labels on a list of executions |
| [**setLabelsByQuery**](ExecutionsApi.md#setLabelsByQuery) | **POST** /api/v1/executions/labels/by-query | Set label on executions filter by query parameters |
| [**setLabelsByQuery1**](ExecutionsApi.md#setLabelsByQuery1) | **POST** /api/v1/{tenant}/executions/labels/by-query | Set label on executions filter by query parameters |
| [**trigger**](ExecutionsApi.md#trigger) | **POST** /api/v1/executions/trigger/{namespace}/{id} | Trigger a new execution for a flow |
| [**trigger1**](ExecutionsApi.md#trigger1) | **POST** /api/v1/{tenant}/executions/trigger/{namespace}/{id} | Trigger a new execution for a flow |
| [**unqueue**](ExecutionsApi.md#unqueue) | **POST** /api/v1/executions/{executionId}/unqueue | Unqueue an execution |
| [**unqueue1**](ExecutionsApi.md#unqueue1) | **POST** /api/v1/{tenant}/executions/{executionId}/unqueue | Unqueue an execution |
| [**unqueueByIds**](ExecutionsApi.md#unqueueByIds) | **POST** /api/v1/executions/unqueue/by-ids | Unqueue a list of executions |
| [**unqueueByIds1**](ExecutionsApi.md#unqueueByIds1) | **POST** /api/v1/{tenant}/executions/unqueue/by-ids | Unqueue a list of executions |
| [**unqueueByQuery**](ExecutionsApi.md#unqueueByQuery) | **POST** /api/v1/executions/unqueue/by-query | Unqueue executions filter by query parameters |
| [**unqueueByQuery1**](ExecutionsApi.md#unqueueByQuery1) | **POST** /api/v1/{tenant}/executions/unqueue/by-query | Unqueue executions filter by query parameters |
| [**validateInputsOnCreate**](ExecutionsApi.md#validateInputsOnCreate) | **POST** /api/v1/executions/{namespace}/{id}/validate | Validate the creation of a new execution for a flow |
| [**validateInputsOnCreate1**](ExecutionsApi.md#validateInputsOnCreate1) | **POST** /api/v1/{tenant}/executions/{namespace}/{id}/validate | Validate the creation of a new execution for a flow |
| [**validateInputsOnResume**](ExecutionsApi.md#validateInputsOnResume) | **POST** /api/v1/executions/{executionId}/resume/validate | Validate inputs to resume a paused execution. |
| [**validateInputsOnResume1**](ExecutionsApi.md#validateInputsOnResume1) | **POST** /api/v1/{tenant}/executions/{executionId}/resume/validate | Validate inputs to resume a paused execution. |
| [**webhookTriggerGet**](ExecutionsApi.md#webhookTriggerGet) | **GET** /api/v1/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by GET webhook trigger |
| [**webhookTriggerGet1**](ExecutionsApi.md#webhookTriggerGet1) | **GET** /api/v1/{tenant}/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by GET webhook trigger |
| [**webhookTriggerPost**](ExecutionsApi.md#webhookTriggerPost) | **POST** /api/v1/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by POST webhook trigger |
| [**webhookTriggerPost1**](ExecutionsApi.md#webhookTriggerPost1) | **POST** /api/v1/{tenant}/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by POST webhook trigger |
| [**webhookTriggerPut**](ExecutionsApi.md#webhookTriggerPut) | **PUT** /api/v1/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by PUT webhook trigger |
| [**webhookTriggerPut1**](ExecutionsApi.md#webhookTriggerPut1) | **PUT** /api/v1/{tenant}/executions/webhook/{namespace}/{id}/{key} | Trigger a new execution by PUT webhook trigger |



## callFile

> File callFile(executionId, path)

Download file for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        try {
            File result = apiInstance.callFile(executionId, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#callFile");
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
| **path** | **URI**| The internal storage uri | |

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
| **200** | file 200 response |  -  |


## changeState

> Execution changeState(executionId, executionControllerStateRequest)

Change state for a taskrun in an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        ExecutionControllerStateRequest executionControllerStateRequest = new ExecutionControllerStateRequest(); // ExecutionControllerStateRequest | 
        try {
            Execution result = apiInstance.changeState(executionId, executionControllerStateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeState");
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
| **executionControllerStateRequest** | [**ExecutionControllerStateRequest**](ExecutionControllerStateRequest.md)|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | changeState 200 response |  -  |


## changeState1

> Execution changeState1(executionId, tenant, executionControllerStateRequest)

Change state for a taskrun in an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        ExecutionControllerStateRequest executionControllerStateRequest = new ExecutionControllerStateRequest(); // ExecutionControllerStateRequest | 
        try {
            Execution result = apiInstance.changeState1(executionId, tenant, executionControllerStateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeState1");
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
| **executionControllerStateRequest** | [**ExecutionControllerStateRequest**](ExecutionControllerStateRequest.md)|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | changeState_1 200 response |  -  |


## changeStatus

> Execution changeStatus(executionId, status)

Change the status of an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        StateType status = StateType.fromValue("CREATED"); // StateType | The new status of the execution
        try {
            Execution result = apiInstance.changeStatus(executionId, status);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatus");
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
| **status** | [**StateType**](.md)| The new status of the execution | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | changeStatus 200 response |  -  |


## changeStatus1

> Execution changeStatus1(executionId, status, tenant)

Change the status of an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        StateType status = StateType.fromValue("CREATED"); // StateType | The new status of the execution
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.changeStatus1(executionId, status, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatus1");
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
| **status** | [**StateType**](.md)| The new status of the execution | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |
| **tenant** | **String**|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | changeStatus_1 200 response |  -  |


## changeStatusById

> BulkResponse changeStatusById(newStatus, requestBody)

Change status of executions by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        StateType newStatus = StateType.fromValue("CREATED"); // StateType | The new status of the executions
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.changeStatusById(newStatus, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatusById");
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
| **newStatus** | [**StateType**](.md)| The new status of the executions | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Changed status with errors |  -  |


## changeStatusById1

> BulkResponse changeStatusById1(newStatus, tenant, requestBody)

Change status of executions by id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        StateType newStatus = StateType.fromValue("CREATED"); // StateType | The new status of the executions
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.changeStatusById1(newStatus, tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatusById1");
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
| **newStatus** | [**StateType**](.md)| The new status of the executions | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |
| **tenant** | **String**|  | |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Changed status with errors |  -  |


## changeStatusByQuery

> BulkResponse changeStatusByQuery(newStatus, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Change executions status by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        StateType newStatus = StateType.fromValue("CREATED"); // StateType | The new status of the executions
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            BulkResponse result = apiInstance.changeStatusByQuery(newStatus, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatusByQuery");
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
| **newStatus** | [**StateType**](.md)| The new status of the executions | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | On success |  -  |
| **422** | Changed status with errors |  -  |


## changeStatusByQuery1

> BulkResponse changeStatusByQuery1(newStatus, tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Change executions status by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        StateType newStatus = StateType.fromValue("CREATED"); // StateType | The new status of the executions
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            BulkResponse result = apiInstance.changeStatusByQuery1(newStatus, tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#changeStatusByQuery1");
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
| **newStatus** | [**StateType**](.md)| The new status of the executions | [enum: CREATED, RUNNING, PAUSED, RESTARTED, KILLING, SUCCESS, WARNING, FAILED, KILLED, CANCELLED, QUEUED, RETRYING, RETRIED, SKIPPED] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | On success |  -  |
| **422** | Changed status with errors |  -  |


## create29

> List&lt;ExecutionControllerExecutionResponse&gt; create29(namespace, id, wait, tenant, labels, revision, scheduleDate)

Create a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean wait = false; // Boolean | If the server will wait the end of the execution
        String tenant = "tenant_example"; // String | 
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        Integer revision = 56; // Integer | The flow revision or latest if null
        OffsetDateTime scheduleDate = OffsetDateTime.now(); // OffsetDateTime | Schedule the flow on a specific date
        try {
            List<ExecutionControllerExecutionResponse> result = apiInstance.create29(namespace, id, wait, tenant, labels, revision, scheduleDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#create29");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **wait** | **Boolean**| If the server will wait the end of the execution | [default to false] |
| **tenant** | **String**|  | |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | [optional] |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |
| **scheduleDate** | **OffsetDateTime**| Schedule the flow on a specific date | [optional] |

### Return type

[**List&lt;ExecutionControllerExecutionResponse&gt;**](ExecutionControllerExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | create_29 200 response |  -  |


## create4

> List&lt;ExecutionControllerExecutionResponse&gt; create4(namespace, id, wait, labels, revision, scheduleDate)

Create a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean wait = false; // Boolean | If the server will wait the end of the execution
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        Integer revision = 56; // Integer | The flow revision or latest if null
        OffsetDateTime scheduleDate = OffsetDateTime.now(); // OffsetDateTime | Schedule the flow on a specific date
        try {
            List<ExecutionControllerExecutionResponse> result = apiInstance.create4(namespace, id, wait, labels, revision, scheduleDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#create4");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **wait** | **Boolean**| If the server will wait the end of the execution | [default to false] |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | [optional] |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |
| **scheduleDate** | **OffsetDateTime**| Schedule the flow on a specific date | [optional] |

### Return type

[**List&lt;ExecutionControllerExecutionResponse&gt;**](ExecutionControllerExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | create_4 200 response |  -  |


## delete32

> delete32(executionId, deleteLogs, deleteMetrics, deleteStorage, tenant)

Delete an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete32(executionId, deleteLogs, deleteMetrics, deleteStorage, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#delete32");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |
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
| **200** | delete_32 200 response |  -  |


## delete4

> delete4(executionId, deleteLogs, deleteMetrics, deleteStorage)

Delete an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        try {
            apiInstance.delete4(executionId, deleteLogs, deleteMetrics, deleteStorage);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#delete4");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |

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
| **200** | delete_4 200 response |  -  |


## deleteByIds

> BulkResponse deleteByIds(deleteLogs, deleteMetrics, deleteStorage, requestBody, includeNonTerminated)

Delete a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        List<String> requestBody = Arrays.asList(); // List<String> | 
        Boolean includeNonTerminated = false; // Boolean | Whether to delete non-terminated executions
        try {
            BulkResponse result = apiInstance.deleteByIds(deleteLogs, deleteMetrics, deleteStorage, requestBody, includeNonTerminated);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#deleteByIds");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |
| **includeNonTerminated** | **Boolean**| Whether to delete non-terminated executions | [optional] [default to false] |

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
| **200** | On success |  -  |
| **422** | Deleted with errors |  -  |


## deleteByIds3

> BulkResponse deleteByIds3(deleteLogs, deleteMetrics, deleteStorage, tenant, requestBody, includeNonTerminated)

Delete a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        Boolean includeNonTerminated = false; // Boolean | Whether to delete non-terminated executions
        try {
            BulkResponse result = apiInstance.deleteByIds3(deleteLogs, deleteMetrics, deleteStorage, tenant, requestBody, includeNonTerminated);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#deleteByIds3");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |
| **tenant** | **String**|  | |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |
| **includeNonTerminated** | **Boolean**| Whether to delete non-terminated executions | [optional] [default to false] |

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
| **200** | On success |  -  |
| **422** | Deleted with errors |  -  |


## deleteByQuery

> Object deleteByQuery(deleteLogs, deleteMetrics, deleteStorage, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter, includeNonTerminated)

Delete executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        Boolean includeNonTerminated = false; // Boolean | Whether to delete non-terminated executions
        try {
            Object result = apiInstance.deleteByQuery(deleteLogs, deleteMetrics, deleteStorage, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter, includeNonTerminated);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#deleteByQuery");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |
| **includeNonTerminated** | **Boolean**| Whether to delete non-terminated executions | [optional] [default to false] |

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
| **200** | deleteByQuery 200 response |  -  |


## deleteByQuery3

> Object deleteByQuery3(deleteLogs, deleteMetrics, deleteStorage, tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter, includeNonTerminated)

Delete executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Boolean deleteLogs = true; // Boolean | Whether to delete execution logs
        Boolean deleteMetrics = true; // Boolean | Whether to delete execution metrics
        Boolean deleteStorage = true; // Boolean | Whether to delete execution files in the internal storage
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        Boolean includeNonTerminated = false; // Boolean | Whether to delete non-terminated executions
        try {
            Object result = apiInstance.deleteByQuery3(deleteLogs, deleteMetrics, deleteStorage, tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter, includeNonTerminated);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#deleteByQuery3");
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
| **deleteLogs** | **Boolean**| Whether to delete execution logs | [default to true] |
| **deleteMetrics** | **Boolean**| Whether to delete execution metrics | [default to true] |
| **deleteStorage** | **Boolean**| Whether to delete execution files in the internal storage | [default to true] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |
| **includeNonTerminated** | **Boolean**| Whether to delete non-terminated executions | [optional] [default to false] |

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
| **200** | deleteByQuery_3 200 response |  -  |


## eval

> ExecutionControllerEvalResult eval(executionId, taskRunId, body)

Evaluate a variable expression for this taskrun

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String body = "body_example"; // String | 
        try {
            ExecutionControllerEvalResult result = apiInstance.eval(executionId, taskRunId, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#eval");
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
| **taskRunId** | **String**| The taskrun id | |
| **body** | **String**|  | |

### Return type

[**ExecutionControllerEvalResult**](ExecutionControllerEvalResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | eval 200 response |  -  |


## eval1

> ExecutionControllerEvalResult eval1(executionId, taskRunId, tenant, body)

Evaluate a variable expression for this taskrun

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        String tenant = "tenant_example"; // String | 
        String body = "body_example"; // String | 
        try {
            ExecutionControllerEvalResult result = apiInstance.eval1(executionId, taskRunId, tenant, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#eval1");
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
| **taskRunId** | **String**| The taskrun id | |
| **tenant** | **String**|  | |
| **body** | **String**|  | |

### Return type

[**ExecutionControllerEvalResult**](ExecutionControllerEvalResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | eval_1 200 response |  -  |


## file2

> File file2(executionId, path, tenant)

Download file for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        String tenant = "tenant_example"; // String | 
        try {
            File result = apiInstance.file2(executionId, path, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#file2");
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
| **path** | **URI**| The internal storage uri | |
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
| **200** | file_2 200 response |  -  |


## filePreview

> Object filePreview(executionId, path, maxRows, encoding)

Get file preview for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        Integer maxRows = 56; // Integer | The max row returns
        String encoding = "UTF-8"; // String | The file encoding as Java charset name. Defaults to UTF-8
        try {
            Object result = apiInstance.filePreview(executionId, path, maxRows, encoding);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#filePreview");
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
| **path** | **URI**| The internal storage uri | |
| **maxRows** | **Integer**| The max row returns | |
| **encoding** | **String**| The file encoding as Java charset name. Defaults to UTF-8 | [default to UTF-8] |

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
| **200** | filePreview 200 response |  -  |


## filePreview1

> Object filePreview1(executionId, path, maxRows, encoding, tenant)

Get file preview for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        Integer maxRows = 56; // Integer | The max row returns
        String encoding = "UTF-8"; // String | The file encoding as Java charset name. Defaults to UTF-8
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.filePreview1(executionId, path, maxRows, encoding, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#filePreview1");
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
| **path** | **URI**| The internal storage uri | |
| **maxRows** | **Integer**| The max row returns | |
| **encoding** | **String**| The file encoding as Java charset name. Defaults to UTF-8 | [default to UTF-8] |
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
| **200** | filePreview_1 200 response |  -  |


## filesize

> FileMetas filesize(executionId, path)

Get file meta information for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        try {
            FileMetas result = apiInstance.filesize(executionId, path);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#filesize");
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
| **200** | filesize 200 response |  -  |


## filesize1

> FileMetas filesize1(executionId, path, tenant)

Get file meta information for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        URI path = new URI(); // URI | The internal storage uri
        String tenant = "tenant_example"; // String | 
        try {
            FileMetas result = apiInstance.filesize1(executionId, path, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#filesize1");
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
| **200** | filesize_1 200 response |  -  |


## find30

> PagedResultsExecution find30(page, size, tenant, sort, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Search for executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            PagedResultsExecution result = apiInstance.find30(page, size, tenant, sort, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#find30");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

[**PagedResultsExecution**](PagedResultsExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_30 200 response |  -  |


## find4

> PagedResultsExecution find4(page, size, sort, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Search for executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            PagedResultsExecution result = apiInstance.find4(page, size, sort, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#find4");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

[**PagedResultsExecution**](PagedResultsExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_4 200 response |  -  |


## findByFlowId

> PagedResultsExecution findByFlowId(namespace, flowId, page, size)

Search for executions for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String flowId = "flowId_example"; // String | The flow id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        try {
            PagedResultsExecution result = apiInstance.findByFlowId(namespace, flowId, page, size);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#findByFlowId");
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
| **namespace** | **String**| The flow namespace | |
| **flowId** | **String**| The flow id | |
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |

### Return type

[**PagedResultsExecution**](PagedResultsExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByFlowId 200 response |  -  |


## findByFlowId1

> PagedResultsExecution findByFlowId1(namespace, flowId, page, size, tenant)

Search for executions for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String flowId = "flowId_example"; // String | The flow id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        try {
            PagedResultsExecution result = apiInstance.findByFlowId1(namespace, flowId, page, size, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#findByFlowId1");
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
| **namespace** | **String**| The flow namespace | |
| **flowId** | **String**| The flow id | |
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **tenant** | **String**|  | |

### Return type

[**PagedResultsExecution**](PagedResultsExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByFlowId_1 200 response |  -  |


## findTaskRun

> PagedResultsTaskRun findTaskRun(page, size, sort, q, namespace, flowId, startDate, endDate, state, labels, triggerExecutionId, childFilter)

Search for taskruns, only available with the Elasticsearch repository

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            PagedResultsTaskRun result = apiInstance.findTaskRun(page, size, sort, q, namespace, flowId, startDate, endDate, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#findTaskRun");
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
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

[**PagedResultsTaskRun**](PagedResultsTaskRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findTaskRun 200 response |  -  |


## findTaskRun1

> PagedResultsTaskRun findTaskRun1(page, size, tenant, sort, q, namespace, flowId, startDate, endDate, state, labels, triggerExecutionId, childFilter)

Search for taskruns, only available with the Elasticsearch repository

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        String q = "q_example"; // String | A string filter
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            PagedResultsTaskRun result = apiInstance.findTaskRun1(page, size, tenant, sort, q, namespace, flowId, startDate, endDate, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#findTaskRun1");
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
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

[**PagedResultsTaskRun**](PagedResultsTaskRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findTaskRun_1 200 response |  -  |


## flowGraph

> FlowGraph flowGraph(executionId, subflows)

Generate a graph for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraph(executionId, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#flowGraph");
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
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraph 200 response |  -  |


## flowGraph2

> FlowGraph flowGraph2(executionId, tenant, subflows)

Generate a graph for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        List<String> subflows = Arrays.asList(); // List<String> | The subflow tasks to display
        try {
            FlowGraph result = apiInstance.flowGraph2(executionId, tenant, subflows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#flowGraph2");
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
| **subflows** | [**List&lt;String&gt;**](String.md)| The subflow tasks to display | [optional] |

### Return type

[**FlowGraph**](FlowGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flowGraph_2 200 response |  -  |


## follow

> EventExecution follow(executionId)

Follow an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            EventExecution result = apiInstance.follow(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#follow");
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

### Return type

[**EventExecution**](EventExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | follow 200 response |  -  |


## follow2

> EventExecution follow2(executionId, tenant)

Follow an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            EventExecution result = apiInstance.follow2(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#follow2");
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

### Return type

[**EventExecution**](EventExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | follow_2 200 response |  -  |


## forceRun

> Execution forceRun(executionId)

Force run an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            Execution result = apiInstance.forceRun(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRun");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | forceRun 200 response |  -  |


## forceRun1

> Execution forceRun1(executionId, tenant)

Force run an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.forceRun1(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRun1");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | forceRun_1 200 response |  -  |


## forceRunByIds

> BulkResponse forceRunByIds(requestBody)

Force run a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.forceRunByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRunByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Force run with errors |  -  |


## forceRunByIds1

> BulkResponse forceRunByIds1(tenant, requestBody)

Force run a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.forceRunByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRunByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Force run with errors |  -  |


## forceRunByQuery

> Object forceRunByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Force run executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.forceRunByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRunByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | forceRunByQuery 200 response |  -  |


## forceRunByQuery1

> Object forceRunByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Force run executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.forceRunByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#forceRunByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | forceRunByQuery_1 200 response |  -  |


## get10

> Execution get10(executionId, tenant)

Get an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.get10(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#get10");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_10 200 response |  -  |


## get2

> Execution get2(executionId)

Get an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            Execution result = apiInstance.get2(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#get2");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_2 200 response |  -  |


## getFlowForExecution

> FlowForExecution getFlowForExecution(namespace, flowId, revision)

Get flow information&#39;s for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace of the flow
        String flowId = "flowId_example"; // String | The flow id
        Integer revision = 56; // Integer | The flow revision
        try {
            FlowForExecution result = apiInstance.getFlowForExecution(namespace, flowId, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowForExecution");
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
| **namespace** | **String**| The namespace of the flow | |
| **flowId** | **String**| The flow id | |
| **revision** | **Integer**| The flow revision | [optional] |

### Return type

[**FlowForExecution**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowForExecution 200 response |  -  |


## getFlowForExecution1

> FlowForExecution getFlowForExecution1(namespace, flowId, tenant, revision)

Get flow information&#39;s for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace of the flow
        String flowId = "flowId_example"; // String | The flow id
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | The flow revision
        try {
            FlowForExecution result = apiInstance.getFlowForExecution1(namespace, flowId, tenant, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowForExecution1");
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
| **namespace** | **String**| The namespace of the flow | |
| **flowId** | **String**| The flow id | |
| **tenant** | **String**|  | |
| **revision** | **Integer**| The flow revision | [optional] |

### Return type

[**FlowForExecution**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowForExecution_1 200 response |  -  |


## getFlowForExecutionById

> FlowForExecution getFlowForExecutionById(executionId)

Get flow information&#39;s for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution that you want flow information's
        try {
            FlowForExecution result = apiInstance.getFlowForExecutionById(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowForExecutionById");
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
| **executionId** | **String**| The execution that you want flow information&#39;s | |

### Return type

[**FlowForExecution**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowForExecutionById 200 response |  -  |


## getFlowForExecutionById1

> FlowForExecution getFlowForExecutionById1(executionId, tenant)

Get flow information&#39;s for an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution that you want flow information's
        String tenant = "tenant_example"; // String | 
        try {
            FlowForExecution result = apiInstance.getFlowForExecutionById1(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowForExecutionById1");
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
| **executionId** | **String**| The execution that you want flow information&#39;s | |
| **tenant** | **String**|  | |

### Return type

[**FlowForExecution**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowForExecutionById_1 200 response |  -  |


## getFlowsByNamespace

> List&lt;FlowForExecution&gt; getFlowsByNamespace(namespace)

Get all flow ids for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        try {
            List<FlowForExecution> result = apiInstance.getFlowsByNamespace(namespace);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowsByNamespace");
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

### Return type

[**List&lt;FlowForExecution&gt;**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowsByNamespace 200 response |  -  |


## getFlowsByNamespace2

> List&lt;FlowForExecution&gt; getFlowsByNamespace2(namespace, tenant)

Get all flow ids for a namespace

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The namespace
        String tenant = "tenant_example"; // String | 
        try {
            List<FlowForExecution> result = apiInstance.getFlowsByNamespace2(namespace, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#getFlowsByNamespace2");
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
| **tenant** | **String**|  | |

### Return type

[**List&lt;FlowForExecution&gt;**](FlowForExecution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFlowsByNamespace_2 200 response |  -  |


## kill

> Object kill(executionId, isOnKillCascade)

Kill an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Boolean isOnKillCascade = true; // Boolean | Specifies whether killing the execution also kill all subflow executions.
        try {
            Object result = apiInstance.kill(executionId, isOnKillCascade);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#kill");
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
| **isOnKillCascade** | **Boolean**| Specifies whether killing the execution also kill all subflow executions. | [default to true] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Execution kill was requested successfully |  -  |
| **409** | if the executions is already finished |  -  |
| **404** | if the executions is not found |  -  |
| **200** | kill 200 response |  -  |


## kill1

> Object kill1(executionId, isOnKillCascade, tenant)

Kill an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Boolean isOnKillCascade = true; // Boolean | Specifies whether killing the execution also kill all subflow executions.
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.kill1(executionId, isOnKillCascade, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#kill1");
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
| **isOnKillCascade** | **Boolean**| Specifies whether killing the execution also kill all subflow executions. | [default to true] |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Execution kill_1 was requested successfully |  -  |
| **409** | if the executions is already finished |  -  |
| **404** | if the executions is not found |  -  |
| **200** | kill_1 200 response |  -  |


## killByIds

> BulkResponse killByIds(requestBody)

Kill a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.killByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#killByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Killed with errors |  -  |


## killByIds1

> BulkResponse killByIds1(tenant, requestBody)

Kill a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.killByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#killByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Killed with errors |  -  |


## killByQuery

> Object killByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Kill executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.killByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#killByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | killByQuery 200 response |  -  |


## killByQuery1

> Object killByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Kill executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.killByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#killByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | killByQuery_1 200 response |  -  |


## listDistinctNamespace

> List&lt;String&gt; listDistinctNamespace()

Get all namespaces that have executable flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        try {
            List<String> result = apiInstance.listDistinctNamespace();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#listDistinctNamespace");
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
| **200** | listDistinctNamespace 200 response |  -  |


## listDistinctNamespace3

> List&lt;String&gt; listDistinctNamespace3(tenant)

Get all namespaces that have executable flows

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<String> result = apiInstance.listDistinctNamespace3(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#listDistinctNamespace3");
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
| **200** | listDistinctNamespace_3 200 response |  -  |


## pause

> pause(executionId)

Pause a running execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            apiInstance.pause(executionId);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pause");
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
| **409** | if the executions is not running |  -  |
| **200** | pause 200 response |  -  |


## pause1

> pause1(executionId, tenant)

Pause a running execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.pause1(executionId, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pause1");
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
| **409** | if the executions is not running |  -  |
| **200** | pause_1 200 response |  -  |


## pauseByIds

> BulkResponse pauseByIds(requestBody)

Pause a list of running executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.pauseByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pauseByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Paused with errors |  -  |


## pauseByIds1

> BulkResponse pauseByIds1(tenant, requestBody)

Pause a list of running executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.pauseByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pauseByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Paused with errors |  -  |


## pauseByQuery

> Object pauseByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Pause executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.pauseByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pauseByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | pauseByQuery 200 response |  -  |


## pauseByQuery1

> Object pauseByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Pause executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.pauseByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#pauseByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | pauseByQuery_1 200 response |  -  |


## replay

> Execution replay(executionId, taskRunId, revision)

Create a new execution from an old one and start it from a specified task run id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | the original execution id to clone
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        Integer revision = 56; // Integer | The flow revision to use for new execution
        try {
            Execution result = apiInstance.replay(executionId, taskRunId, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replay");
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
| **executionId** | **String**| the original execution id to clone | |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **revision** | **Integer**| The flow revision to use for new execution | [optional] |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | replay 200 response |  -  |


## replay1

> Execution replay1(executionId, tenant, taskRunId, revision)

Create a new execution from an old one and start it from a specified task run id

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | the original execution id to clone
        String tenant = "tenant_example"; // String | 
        String taskRunId = "taskRunId_example"; // String | The taskrun id
        Integer revision = 56; // Integer | The flow revision to use for new execution
        try {
            Execution result = apiInstance.replay1(executionId, tenant, taskRunId, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replay1");
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
| **executionId** | **String**| the original execution id to clone | |
| **tenant** | **String**|  | |
| **taskRunId** | **String**| The taskrun id | [optional] |
| **revision** | **Integer**| The flow revision to use for new execution | [optional] |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | replay_1 200 response |  -  |


## replayByIds

> BulkResponse replayByIds(requestBody)

Create new executions from old ones. Keep the flow revision

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.replayByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replayByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Replayed with errors |  -  |


## replayByIds1

> BulkResponse replayByIds1(tenant, requestBody)

Create new executions from old ones. Keep the flow revision

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.replayByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replayByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Replayed with errors |  -  |


## replayByQuery

> Object replayByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Create new executions from old ones filter by query parameters. Keep the flow revision

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.replayByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replayByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | replayByQuery 200 response |  -  |


## replayByQuery1

> Object replayByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Create new executions from old ones filter by query parameters. Keep the flow revision

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.replayByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#replayByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | replayByQuery_1 200 response |  -  |


## restart

> Execution restart(executionId, revision)

Restart a new execution from an old one

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        Integer revision = 56; // Integer | The flow revision to use for new execution
        try {
            Execution result = apiInstance.restart(executionId, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restart");
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
| **revision** | **Integer**| The flow revision to use for new execution | [optional] |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | restart 200 response |  -  |


## restart2

> Execution restart2(executionId, tenant, revision)

Restart a new execution from an old one

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | The flow revision to use for new execution
        try {
            Execution result = apiInstance.restart2(executionId, tenant, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restart2");
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
| **revision** | **Integer**| The flow revision to use for new execution | [optional] |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | restart_2 200 response |  -  |


## restartByIds

> BulkResponse restartByIds(requestBody)

Restart a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.restartByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restartByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Restarted with errors |  -  |


## restartByIds1

> BulkResponse restartByIds1(tenant, requestBody)

Restart a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.restartByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restartByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Restarted with errors |  -  |


## restartByQuery

> Object restartByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Restart executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.restartByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restartByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | restartByQuery 200 response |  -  |


## restartByQuery1

> Object restartByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Restart executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.restartByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#restartByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | restartByQuery_1 200 response |  -  |


## resume

> Object resume(executionId)

Resume a paused execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            Object result = apiInstance.resume(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resume");
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

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **409** | if the executions is not paused |  -  |
| **200** | resume 200 response |  -  |


## resume1

> Object resume1(executionId, tenant)

Resume a paused execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            Object result = apiInstance.resume1(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resume1");
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

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **409** | if the executions is not paused |  -  |
| **200** | resume_1 200 response |  -  |


## resumeByIds

> BulkResponse resumeByIds(requestBody)

Resume a list of paused executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.resumeByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resumeByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Resumed with errors |  -  |


## resumeByIds1

> BulkResponse resumeByIds1(tenant, requestBody)

Resume a list of paused executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.resumeByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resumeByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Resumed with errors |  -  |


## resumeByQuery

> Object resumeByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Resume executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.resumeByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resumeByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | resumeByQuery 200 response |  -  |


## resumeByQuery1

> Object resumeByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Resume executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.resumeByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#resumeByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | resumeByQuery_1 200 response |  -  |


## setLabels

> Object setLabels(executionId, label)

Add or update labels of a terminated execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        List<Label> label = Arrays.asList(); // List<Label> | 
        try {
            Object result = apiInstance.setLabels(executionId, label);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabels");
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
| **label** | [**List&lt;Label&gt;**](Label.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | If the execution cannot be found |  -  |
| **400** | If the execution is not terminated |  -  |
| **200** | setLabels 200 response |  -  |


## setLabels1

> Object setLabels1(executionId, tenant, label)

Add or update labels of a terminated execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        List<Label> label = Arrays.asList(); // List<Label> | 
        try {
            Object result = apiInstance.setLabels1(executionId, tenant, label);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabels1");
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
| **label** | [**List&lt;Label&gt;**](Label.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | If the execution cannot be found |  -  |
| **400** | If the execution is not terminated |  -  |
| **200** | setLabels_1 200 response |  -  |


## setLabelsByIds

> BulkResponse setLabelsByIds(executionControllerSetLabelsByIdsRequest)

Set labels on a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        ExecutionControllerSetLabelsByIdsRequest executionControllerSetLabelsByIdsRequest = new ExecutionControllerSetLabelsByIdsRequest(); // ExecutionControllerSetLabelsByIdsRequest | 
        try {
            BulkResponse result = apiInstance.setLabelsByIds(executionControllerSetLabelsByIdsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabelsByIds");
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
| **executionControllerSetLabelsByIdsRequest** | [**ExecutionControllerSetLabelsByIdsRequest**](ExecutionControllerSetLabelsByIdsRequest.md)|  | |

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
| **200** | On success |  -  |
| **422** | Killed with errors |  -  |


## setLabelsByIds1

> BulkResponse setLabelsByIds1(tenant, executionControllerSetLabelsByIdsRequest)

Set labels on a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ExecutionControllerSetLabelsByIdsRequest executionControllerSetLabelsByIdsRequest = new ExecutionControllerSetLabelsByIdsRequest(); // ExecutionControllerSetLabelsByIdsRequest | 
        try {
            BulkResponse result = apiInstance.setLabelsByIds1(tenant, executionControllerSetLabelsByIdsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabelsByIds1");
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
| **executionControllerSetLabelsByIdsRequest** | [**ExecutionControllerSetLabelsByIdsRequest**](ExecutionControllerSetLabelsByIdsRequest.md)|  | |

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
| **200** | On success |  -  |
| **422** | Killed with errors |  -  |


## setLabelsByQuery

> Object setLabelsByQuery(label, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Set label on executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<Label> label = Arrays.asList(); // List<Label> | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.setLabelsByQuery(label, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabelsByQuery");
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
| **label** | [**List&lt;Label&gt;**](Label.md)|  | |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setLabelsByQuery 200 response |  -  |


## setLabelsByQuery1

> Object setLabelsByQuery1(tenant, label, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Set label on executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<Label> label = Arrays.asList(); // List<Label> | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.setLabelsByQuery1(tenant, label, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#setLabelsByQuery1");
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
| **label** | [**List&lt;Label&gt;**](Label.md)|  | |
| **q** | **String**| A string filter | [optional] |
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setLabelsByQuery_1 200 response |  -  |


## trigger

> List&lt;ExecutionControllerExecutionResponse&gt; trigger(namespace, id, wait, labels, revision)

Trigger a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean wait = false; // Boolean | If the server will wait the end of the execution
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        Integer revision = 56; // Integer | The flow revision or latest if null
        try {
            List<ExecutionControllerExecutionResponse> result = apiInstance.trigger(namespace, id, wait, labels, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#trigger");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **wait** | **Boolean**| If the server will wait the end of the execution | [default to false] |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | [optional] |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |

### Return type

[**List&lt;ExecutionControllerExecutionResponse&gt;**](ExecutionControllerExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | trigger 200 response |  -  |


## trigger1

> List&lt;ExecutionControllerExecutionResponse&gt; trigger1(namespace, id, wait, tenant, labels, revision)

Trigger a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        Boolean wait = false; // Boolean | If the server will wait the end of the execution
        String tenant = "tenant_example"; // String | 
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        Integer revision = 56; // Integer | The flow revision or latest if null
        try {
            List<ExecutionControllerExecutionResponse> result = apiInstance.trigger1(namespace, id, wait, tenant, labels, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#trigger1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **wait** | **Boolean**| If the server will wait the end of the execution | [default to false] |
| **tenant** | **String**|  | |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | [optional] |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |

### Return type

[**List&lt;ExecutionControllerExecutionResponse&gt;**](ExecutionControllerExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | trigger_1 200 response |  -  |


## unqueue

> Execution unqueue(executionId)

Unqueue an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            Execution result = apiInstance.unqueue(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueue");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unqueue 200 response |  -  |


## unqueue1

> Execution unqueue1(executionId, tenant)

Unqueue an execution

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.unqueue1(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueue1");
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

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unqueue_1 200 response |  -  |


## unqueueByIds

> BulkResponse unqueueByIds(requestBody)

Unqueue a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.unqueueByIds(requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueueByIds");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Unqueued with errors |  -  |


## unqueueByIds1

> BulkResponse unqueueByIds1(tenant, requestBody)

Unqueue a list of executions

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        List<String> requestBody = Arrays.asList(); // List<String> | 
        try {
            BulkResponse result = apiInstance.unqueueByIds1(tenant, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueueByIds1");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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
| **200** | On success |  -  |
| **422** | Unqueued with errors |  -  |


## unqueueByQuery

> Object unqueueByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Unqueue executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.unqueueByQuery(q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueueByQuery");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | unqueueByQuery 200 response |  -  |


## unqueueByQuery1

> Object unqueueByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter)

Unqueue executions filter by query parameters

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<FlowScope> scope = Arrays.asList(); // List<FlowScope> | The scope of the executions to include
        String namespace = "namespace_example"; // String | A namespace filter prefix
        String flowId = "flowId_example"; // String | A flow id filter
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start datetime
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end datetime
        String timeRange = "PT5M"; // String | A time range filter relative to the current time
        List<StateType> state = Arrays.asList(); // List<StateType> | A state filter
        List<String> labels = Arrays.asList(); // List<String> | A labels filter as a list of 'key:value'
        String triggerExecutionId = "triggerExecutionId_example"; // String | The trigger execution id
        ExecutionRepositoryInterfaceChildFilter childFilter = ExecutionRepositoryInterfaceChildFilter.fromValue("CHILD"); // ExecutionRepositoryInterfaceChildFilter | A execution child filter
        try {
            Object result = apiInstance.unqueueByQuery1(tenant, q, scope, namespace, flowId, startDate, endDate, timeRange, state, labels, triggerExecutionId, childFilter);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#unqueueByQuery1");
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
| **scope** | [**List&lt;FlowScope&gt;**](FlowScope.md)| The scope of the executions to include | [optional] |
| **namespace** | **String**| A namespace filter prefix | [optional] |
| **flowId** | **String**| A flow id filter | [optional] |
| **startDate** | **OffsetDateTime**| The start datetime | [optional] |
| **endDate** | **OffsetDateTime**| The end datetime | [optional] |
| **timeRange** | **String**| A time range filter relative to the current time | [optional] |
| **state** | [**List&lt;StateType&gt;**](StateType.md)| A state filter | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| A labels filter as a list of &#39;key:value&#39; | [optional] |
| **triggerExecutionId** | **String**| The trigger execution id | [optional] |
| **childFilter** | [**ExecutionRepositoryInterfaceChildFilter**](.md)| A execution child filter | [optional] [enum: CHILD, MAIN] |

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
| **200** | unqueueByQuery_1 200 response |  -  |


## validateInputsOnCreate

> List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt; validateInputsOnCreate(namespace, id, labels, revision)

Validate the creation of a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        Integer revision = 56; // Integer | The flow revision or latest if null
        try {
            List<ExecutionControllerApiValidateExecutionInputsResponse> result = apiInstance.validateInputsOnCreate(namespace, id, labels, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#validateInputsOnCreate");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |

### Return type

[**List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt;**](ExecutionControllerApiValidateExecutionInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | validateInputsOnCreate 200 response |  -  |


## validateInputsOnCreate1

> List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt; validateInputsOnCreate1(namespace, id, labels, tenant, revision)

Validate the creation of a new execution for a flow

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        List<String> labels = Arrays.asList(); // List<String> | The labels as a list of 'key:value'
        String tenant = "tenant_example"; // String | 
        Integer revision = 56; // Integer | The flow revision or latest if null
        try {
            List<ExecutionControllerApiValidateExecutionInputsResponse> result = apiInstance.validateInputsOnCreate1(namespace, id, labels, tenant, revision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#validateInputsOnCreate1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels as a list of &#39;key:value&#39; | |
| **tenant** | **String**|  | |
| **revision** | **Integer**| The flow revision or latest if null | [optional] |

### Return type

[**List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt;**](ExecutionControllerApiValidateExecutionInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | if the flow is disabled |  -  |
| **200** | validateInputsOnCreate_1 200 response |  -  |


## validateInputsOnResume

> List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt; validateInputsOnResume(executionId)

Validate inputs to resume a paused execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        try {
            List<ExecutionControllerApiValidateExecutionInputsResponse> result = apiInstance.validateInputsOnResume(executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#validateInputsOnResume");
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

### Return type

[**List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt;**](ExecutionControllerApiValidateExecutionInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **409** | if the executions is not paused |  -  |
| **200** | validateInputsOnResume 200 response |  -  |


## validateInputsOnResume1

> List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt; validateInputsOnResume1(executionId, tenant)

Validate inputs to resume a paused execution.

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String executionId = "executionId_example"; // String | The execution id
        String tenant = "tenant_example"; // String | 
        try {
            List<ExecutionControllerApiValidateExecutionInputsResponse> result = apiInstance.validateInputsOnResume1(executionId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#validateInputsOnResume1");
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

### Return type

[**List&lt;ExecutionControllerApiValidateExecutionInputsResponse&gt;**](ExecutionControllerApiValidateExecutionInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |
| **409** | if the executions is not paused |  -  |
| **200** | validateInputsOnResume_1 200 response |  -  |


## webhookTriggerGet

> Execution webhookTriggerGet(namespace, id, key)

Trigger a new execution by GET webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        try {
            Execution result = apiInstance.webhookTriggerGet(namespace, id, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerGet");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerGet 200 response |  -  |


## webhookTriggerGet1

> Execution webhookTriggerGet1(namespace, id, key, tenant)

Trigger a new execution by GET webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.webhookTriggerGet1(namespace, id, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerGet1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |
| **tenant** | **String**|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerGet_1 200 response |  -  |


## webhookTriggerPost

> Execution webhookTriggerPost(namespace, id, key)

Trigger a new execution by POST webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        try {
            Execution result = apiInstance.webhookTriggerPost(namespace, id, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerPost");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerPost 200 response |  -  |


## webhookTriggerPost1

> Execution webhookTriggerPost1(namespace, id, key, tenant)

Trigger a new execution by POST webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.webhookTriggerPost1(namespace, id, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerPost1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |
| **tenant** | **String**|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerPost_1 200 response |  -  |


## webhookTriggerPut

> Execution webhookTriggerPut(namespace, id, key)

Trigger a new execution by PUT webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        try {
            Execution result = apiInstance.webhookTriggerPut(namespace, id, key);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerPut");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerPut 200 response |  -  |


## webhookTriggerPut1

> Execution webhookTriggerPut1(namespace, id, key, tenant)

Trigger a new execution by PUT webhook trigger

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.ExecutionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        ExecutionsApi apiInstance = new ExecutionsApi(defaultClient);
        String namespace = "namespace_example"; // String | The flow namespace
        String id = "id_example"; // String | The flow id
        String key = "key_example"; // String | The webhook trigger uid
        String tenant = "tenant_example"; // String | 
        try {
            Execution result = apiInstance.webhookTriggerPut1(namespace, id, key, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ExecutionsApi#webhookTriggerPut1");
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
| **namespace** | **String**| The flow namespace | |
| **id** | **String**| The flow id | |
| **key** | **String**| The webhook trigger uid | |
| **tenant** | **String**|  | |

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | webhookTriggerPut_1 200 response |  -  |

