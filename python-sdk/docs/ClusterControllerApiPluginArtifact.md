# ClusterControllerApiPluginArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**artifact_id** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_artifact import ClusterControllerApiPluginArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginArtifact from a JSON string
cluster_controller_api_plugin_artifact_instance = ClusterControllerApiPluginArtifact.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginArtifact.to_json())

# convert the object into a dict
cluster_controller_api_plugin_artifact_dict = cluster_controller_api_plugin_artifact_instance.to_dict()
# create an instance of ClusterControllerApiPluginArtifact from a dict
cluster_controller_api_plugin_artifact_from_dict = ClusterControllerApiPluginArtifact.from_dict(cluster_controller_api_plugin_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


