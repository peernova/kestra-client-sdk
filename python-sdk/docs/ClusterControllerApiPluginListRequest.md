# ClusterControllerApiPluginListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.cluster_controller_api_plugin_list_request import ClusterControllerApiPluginListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterControllerApiPluginListRequest from a JSON string
cluster_controller_api_plugin_list_request_instance = ClusterControllerApiPluginListRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterControllerApiPluginListRequest.to_json())

# convert the object into a dict
cluster_controller_api_plugin_list_request_dict = cluster_controller_api_plugin_list_request_instance.to_dict()
# create an instance of ClusterControllerApiPluginListRequest from a dict
cluster_controller_api_plugin_list_request_from_dict = ClusterControllerApiPluginListRequest.from_dict(cluster_controller_api_plugin_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


