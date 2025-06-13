# Plugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**manifest** | **Dict[str, str]** |  | [optional] 
**tasks** | **List[str]** |  | [optional] 
**triggers** | **List[str]** |  | [optional] 
**conditions** | **List[str]** |  | [optional] 
**controllers** | **List[str]** |  | [optional] 
**storages** | **List[str]** |  | [optional] 
**secrets** | **List[str]** |  | [optional] 
**task_runners** | **List[str]** |  | [optional] 
**guides** | **List[str]** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**apps** | **List[str]** |  | [optional] 
**app_blocks** | **List[str]** |  | [optional] 
**charts** | **List[str]** |  | [optional] 
**data_filters** | **List[str]** |  | [optional] 
**log_exporters** | **List[str]** |  | [optional] 
**additional_plugins** | **List[str]** |  | [optional] 
**categories** | [**List[PluginSubGroupPluginCategory]**](PluginSubGroupPluginCategory.md) |  | [optional] 
**sub_group** | **str** |  | [optional] 

## Example

```python
from kestra_api_client.models.plugin import Plugin

# TODO update the JSON string below
json = "{}"
# create an instance of Plugin from a JSON string
plugin_instance = Plugin.from_json(json)
# print the JSON string representation of the object
print(Plugin.to_json())

# convert the object into a dict
plugin_dict = plugin_instance.to_dict()
# create an instance of Plugin from a dict
plugin_from_dict = Plugin.from_dict(plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


