# ClusterControllerApiCreateOrUpdateWorkerGroupRequest

ApiCreateWorkerGroupRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the worker group. | 
**description** | **str** | The description of the worker group. | [optional] 
**allowed_tenants** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_create_or_update_worker_group_request import ClusterControllerApiCreateOrUpdateWorkerGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiCreateOrUpdateWorkerGroupRequest from a JSON string
cluster_controller_api_create_or_update_worker_group_request_instance = ClusterControllerApiCreateOrUpdateWorkerGroupRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiCreateOrUpdateWorkerGroupRequest.to_json())

# convert the object into a dict
cluster_controller_api_create_or_update_worker_group_request_dict = cluster_controller_api_create_or_update_worker_group_request_instance.to_dict()
# create an instance of ClusterControllerApiCreateOrUpdateWorkerGroupRequest from a dict
cluster_controller_api_create_or_update_worker_group_request_from_dict = ClusterControllerApiCreateOrUpdateWorkerGroupRequest.from_dict(cluster_controller_api_create_or_update_worker_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


