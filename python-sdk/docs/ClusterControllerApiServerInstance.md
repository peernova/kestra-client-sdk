# ClusterControllerApiServerInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**ServerInstanceType**](ServerInstanceType.md) |  | [optional] 
**version** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_server_instance import ClusterControllerApiServerInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiServerInstance from a JSON string
cluster_controller_api_server_instance_instance = ClusterControllerApiServerInstance.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiServerInstance.to_json())

# convert the object into a dict
cluster_controller_api_server_instance_dict = cluster_controller_api_server_instance_instance.to_dict()
# create an instance of ClusterControllerApiServerInstance from a dict
cluster_controller_api_server_instance_from_dict = ClusterControllerApiServerInstance.from_dict(cluster_controller_api_server_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


