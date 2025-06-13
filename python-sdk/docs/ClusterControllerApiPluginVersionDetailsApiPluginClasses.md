# ClusterControllerApiPluginVersionDetailsApiPluginClasses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**classes** | [**List[ClusterControllerApiPluginVersionDetailsApiPluginClass]**](ClusterControllerApiPluginVersionDetailsApiPluginClass.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_version_details_api_plugin_classes import ClusterControllerApiPluginVersionDetailsApiPluginClasses

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginVersionDetailsApiPluginClasses from a JSON string
cluster_controller_api_plugin_version_details_api_plugin_classes_instance = ClusterControllerApiPluginVersionDetailsApiPluginClasses.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginVersionDetailsApiPluginClasses.to_json())

# convert the object into a dict
cluster_controller_api_plugin_version_details_api_plugin_classes_dict = cluster_controller_api_plugin_version_details_api_plugin_classes_instance.to_dict()
# create an instance of ClusterControllerApiPluginVersionDetailsApiPluginClasses from a dict
cluster_controller_api_plugin_version_details_api_plugin_classes_from_dict = ClusterControllerApiPluginVersionDetailsApiPluginClasses.from_dict(cluster_controller_api_plugin_version_details_api_plugin_classes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


