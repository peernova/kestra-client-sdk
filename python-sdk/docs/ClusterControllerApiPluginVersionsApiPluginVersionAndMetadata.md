# ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**metadata** | [**PluginArtifactMetadata**](PluginArtifactMetadata.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_versions_api_plugin_version_and_metadata import ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata from a JSON string
cluster_controller_api_plugin_versions_api_plugin_version_and_metadata_instance = ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata.to_json())

# convert the object into a dict
cluster_controller_api_plugin_versions_api_plugin_version_and_metadata_dict = cluster_controller_api_plugin_versions_api_plugin_version_and_metadata_instance.to_dict()
# create an instance of ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata from a dict
cluster_controller_api_plugin_versions_api_plugin_version_and_metadata_from_dict = ClusterControllerApiPluginVersionsApiPluginVersionAndMetadata.from_dict(cluster_controller_api_plugin_versions_api_plugin_version_and_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


