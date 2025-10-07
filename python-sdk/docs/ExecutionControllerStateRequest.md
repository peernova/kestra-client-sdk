# ExecutionControllerStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_run_id** | **str** |  | [optional] 
**state** | [**StateType**](StateType.md) |  | [optional] 

## Example

```python
from kestrapy.models.execution_controller_state_request import ExecutionControllerStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionControllerStateRequest from a JSON string
execution_controller_state_request_instance = ExecutionControllerStateRequest.from_json(json)
# print the JSON string representation of the object
print(ExecutionControllerStateRequest.to_json())

# convert the object into a dict
execution_controller_state_request_dict = execution_controller_state_request_instance.to_dict()
# create an instance of ExecutionControllerStateRequest from a dict
execution_controller_state_request_from_dict = ExecutionControllerStateRequest.from_dict(execution_controller_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


