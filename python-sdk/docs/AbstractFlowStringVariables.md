# AbstractFlowStringVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.abstract_flow_string_variables import AbstractFlowStringVariables

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractFlowStringVariables from a JSON string
abstract_flow_string_variables_instance = AbstractFlowStringVariables.from_json(json)
# print the JSON string representation of the object
print(AbstractFlowStringVariables.to_json())

# convert the object into a dict
abstract_flow_string_variables_dict = abstract_flow_string_variables_instance.to_dict()
# create an instance of AbstractFlowStringVariables from a dict
abstract_flow_string_variables_from_dict = AbstractFlowStringVariables.from_dict(abstract_flow_string_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


