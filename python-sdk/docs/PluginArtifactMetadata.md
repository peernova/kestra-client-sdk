# PluginArtifactMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**last_modified_time** | **int** |  | [optional] 
**creation_time** | **int** |  | [optional] 

## Example

```python
from kestrapy.models.plugin_artifact_metadata import PluginArtifactMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PluginArtifactMetadata from a JSON string
plugin_artifact_metadata_instance = PluginArtifactMetadata.from_json(json)
# print the JSON string representation of the object
print(PluginArtifactMetadata.to_json())

# convert the object into a dict
plugin_artifact_metadata_dict = plugin_artifact_metadata_instance.to_dict()
# create an instance of PluginArtifactMetadata from a dict
plugin_artifact_metadata_from_dict = PluginArtifactMetadata.from_dict(plugin_artifact_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


