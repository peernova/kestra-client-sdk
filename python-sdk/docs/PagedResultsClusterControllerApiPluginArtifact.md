# PagedResultsClusterControllerApiPluginArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterControllerApiPluginArtifact]**](ClusterControllerApiPluginArtifact.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_cluster_controller_api_plugin_artifact import PagedResultsClusterControllerApiPluginArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsClusterControllerApiPluginArtifact from a JSON string
paged_results_cluster_controller_api_plugin_artifact_instance = PagedResultsClusterControllerApiPluginArtifact.from_json(json)
# print the JSON string representation of the object
print(PagedResultsClusterControllerApiPluginArtifact.to_json())

# convert the object into a dict
paged_results_cluster_controller_api_plugin_artifact_dict = paged_results_cluster_controller_api_plugin_artifact_instance.to_dict()
# create an instance of PagedResultsClusterControllerApiPluginArtifact from a dict
paged_results_cluster_controller_api_plugin_artifact_from_dict = PagedResultsClusterControllerApiPluginArtifact.from_dict(paged_results_cluster_controller_api_plugin_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


