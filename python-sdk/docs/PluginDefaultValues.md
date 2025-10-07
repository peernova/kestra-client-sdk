# PluginDefaultValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.plugin_default_values import PluginDefaultValues

# TODO update the JSON string below
json = "{}"
# create an instance of PluginDefaultValues from a JSON string
plugin_default_values_instance = PluginDefaultValues.from_json(json)
# print the JSON string representation of the object
print(PluginDefaultValues.to_json())

# convert the object into a dict
plugin_default_values_dict = plugin_default_values_instance.to_dict()
# create an instance of PluginDefaultValues from a dict
plugin_default_values_from_dict = PluginDefaultValues.from_dict(plugin_default_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


