# ClusterControllerApiWorkerGroupList

ApiWorkerGroupList.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_groups** | [**List[ClusterControllerApiWorkerGroupItem]**](ClusterControllerApiWorkerGroupItem.md) | The list of worker groups. | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_worker_group_list import ClusterControllerApiWorkerGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiWorkerGroupList from a JSON string
cluster_controller_api_worker_group_list_instance = ClusterControllerApiWorkerGroupList.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiWorkerGroupList.to_json())

# convert the object into a dict
cluster_controller_api_worker_group_list_dict = cluster_controller_api_worker_group_list_instance.to_dict()
# create an instance of ClusterControllerApiWorkerGroupList from a dict
cluster_controller_api_worker_group_list_from_dict = ClusterControllerApiWorkerGroupList.from_dict(cluster_controller_api_worker_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


