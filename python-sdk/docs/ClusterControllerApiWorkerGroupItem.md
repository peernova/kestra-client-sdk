# ClusterControllerApiWorkerGroupItem

ApiWorkerGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of worker group. | [optional] 
**key** | **str** | The key of the worker group. | [optional] 
**description** | **str** | The description of the worker group. | [optional] 
**active_workers** | **int** | The number of active workers for the group. | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_worker_group_item import ClusterControllerApiWorkerGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiWorkerGroupItem from a JSON string
cluster_controller_api_worker_group_item_instance = ClusterControllerApiWorkerGroupItem.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiWorkerGroupItem.to_json())

# convert the object into a dict
cluster_controller_api_worker_group_item_dict = cluster_controller_api_worker_group_item_instance.to_dict()
# create an instance of ClusterControllerApiWorkerGroupItem from a dict
cluster_controller_api_worker_group_item_from_dict = ClusterControllerApiWorkerGroupItem.from_dict(cluster_controller_api_worker_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


