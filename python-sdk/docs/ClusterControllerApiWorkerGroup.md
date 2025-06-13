# ClusterControllerApiWorkerGroup

ApiWorkerGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of worker group. | [optional] 
**key** | **str** | The key of the worker group. | [optional] 
**description** | **str** | The description of the worker group. | [optional] 
**allowed_tenants** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_worker_group import ClusterControllerApiWorkerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiWorkerGroup from a JSON string
cluster_controller_api_worker_group_instance = ClusterControllerApiWorkerGroup.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiWorkerGroup.to_json())

# convert the object into a dict
cluster_controller_api_worker_group_dict = cluster_controller_api_worker_group_instance.to_dict()
# create an instance of ClusterControllerApiWorkerGroup from a dict
cluster_controller_api_worker_group_from_dict = ClusterControllerApiWorkerGroup.from_dict(cluster_controller_api_worker_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


