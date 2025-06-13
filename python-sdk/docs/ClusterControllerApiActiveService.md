# ClusterControllerApiActiveService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceType**](ServiceType.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_active_service import ClusterControllerApiActiveService

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiActiveService from a JSON string
cluster_controller_api_active_service_instance = ClusterControllerApiActiveService.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiActiveService.to_json())

# convert the object into a dict
cluster_controller_api_active_service_dict = cluster_controller_api_active_service_instance.to_dict()
# create an instance of ClusterControllerApiActiveService from a dict
cluster_controller_api_active_service_from_dict = ClusterControllerApiActiveService.from_dict(cluster_controller_api_active_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


