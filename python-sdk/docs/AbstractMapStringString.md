# AbstractMapStringString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.abstract_map_string_string import AbstractMapStringString

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractMapStringString from a JSON string
abstract_map_string_string_instance = AbstractMapStringString.from_json(json)
# print the JSON string representation of the object
print(AbstractMapStringString.to_json())

# convert the object into a dict
abstract_map_string_string_dict = abstract_map_string_string_instance.to_dict()
# create an instance of AbstractMapStringString from a dict
abstract_map_string_string_from_dict = AbstractMapStringString.from_dict(abstract_map_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


