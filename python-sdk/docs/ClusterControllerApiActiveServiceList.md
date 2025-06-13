# ClusterControllerApiActiveServiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**services** | [**List[ClusterControllerApiActiveService]**](ClusterControllerApiActiveService.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_active_service_list import ClusterControllerApiActiveServiceList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiActiveServiceList from a JSON string
cluster_controller_api_active_service_list_instance = ClusterControllerApiActiveServiceList.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiActiveServiceList.to_json())

# convert the object into a dict
cluster_controller_api_active_service_list_dict = cluster_controller_api_active_service_list_instance.to_dict()
# create an instance of ClusterControllerApiActiveServiceList from a dict
cluster_controller_api_active_service_list_from_dict = ClusterControllerApiActiveServiceList.from_dict(cluster_controller_api_active_service_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


