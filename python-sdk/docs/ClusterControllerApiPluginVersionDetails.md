# ClusterControllerApiPluginVersionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**classes** | [**List[ClusterControllerApiPluginVersionDetailsApiPluginClasses]**](ClusterControllerApiPluginVersionDetailsApiPluginClasses.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_version_details import ClusterControllerApiPluginVersionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginVersionDetails from a JSON string
cluster_controller_api_plugin_version_details_instance = ClusterControllerApiPluginVersionDetails.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginVersionDetails.to_json())

# convert the object into a dict
cluster_controller_api_plugin_version_details_dict = cluster_controller_api_plugin_version_details_instance.to_dict()
# create an instance of ClusterControllerApiPluginVersionDetails from a dict
cluster_controller_api_plugin_version_details_from_dict = ClusterControllerApiPluginVersionDetails.from_dict(cluster_controller_api_plugin_version_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


