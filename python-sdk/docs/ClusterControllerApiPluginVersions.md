# ClusterControllerApiPluginVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**artifact_id** | **str** |  | [optional] 
**versions** | [**List[ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata]**](ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_versions import ClusterControllerApiPluginVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginVersions from a JSON string
cluster_controller_api_plugin_versions_instance = ClusterControllerApiPluginVersions.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginVersions.to_json())

# convert the object into a dict
cluster_controller_api_plugin_versions_dict = cluster_controller_api_plugin_versions_instance.to_dict()
# create an instance of ClusterControllerApiPluginVersions from a dict
cluster_controller_api_plugin_versions_from_dict = ClusterControllerApiPluginVersions.from_dict(cluster_controller_api_plugin_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


