# ClusterControllerApiServiceInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**ServiceType**](ServiceType.md) |  | [optional] 
**state** | [**ServiceServiceState**](ServiceServiceState.md) |  | [optional] 
**server** | [**ClusterControllerApiServerInstance**](ClusterControllerApiServerInstance.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_service_instance import ClusterControllerApiServiceInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiServiceInstance from a JSON string
cluster_controller_api_service_instance_instance = ClusterControllerApiServiceInstance.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiServiceInstance.to_json())

# convert the object into a dict
cluster_controller_api_service_instance_dict = cluster_controller_api_service_instance_instance.to_dict()
# create an instance of ClusterControllerApiServiceInstance from a dict
cluster_controller_api_service_instance_from_dict = ClusterControllerApiServiceInstance.from_dict(cluster_controller_api_service_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


