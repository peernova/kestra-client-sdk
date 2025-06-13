# ClusterControllerApiWorkerGroupDetails

ApiWorkerGroupDetails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of worker group. | [optional] 
**key** | **str** | The key of the worker group. | [optional] 
**description** | **str** | The description of the worker group. | [optional] 
**allowed_tenants** | **List[str]** |  | [optional] 
**workers** | [**List[ServiceInstance]**](ServiceInstance.md) | The list of workers for the group. | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_worker_group_details import ClusterControllerApiWorkerGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiWorkerGroupDetails from a JSON string
cluster_controller_api_worker_group_details_instance = ClusterControllerApiWorkerGroupDetails.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiWorkerGroupDetails.to_json())

# convert the object into a dict
cluster_controller_api_worker_group_details_dict = cluster_controller_api_worker_group_details_instance.to_dict()
# create an instance of ClusterControllerApiWorkerGroupDetails from a dict
cluster_controller_api_worker_group_details_from_dict = ClusterControllerApiWorkerGroupDetails.from_dict(cluster_controller_api_worker_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


