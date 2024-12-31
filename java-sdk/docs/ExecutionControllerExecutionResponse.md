

# ExecutionControllerExecutionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**namespace** | **String** |  |  |
|**flowId** | **String** |  |  |
|**flowRevision** | **Integer** |  |  |
|**taskRunList** | [**List&lt;TaskRun&gt;**](TaskRun.md) |  |  |
|**inputs** | **Map&lt;String, Object&gt;** |  |  |
|**outputs** | **Map&lt;String, Object&gt;** |  |  |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  |
|**variables** | **Map&lt;String, Object&gt;** |  |  |
|**state** | [**State**](State.md) |  |  |
|**parentId** | **String** |  |  |
|**originalId** | **String** |  |  |
|**trigger** | [**ExecutionTrigger**](ExecutionTrigger.md) |  |  |
|**deleted** | **Boolean** |  |  |
|**metadata** | [**ExecutionMetadata**](ExecutionMetadata.md) |  |  |
|**scheduleDate** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



