# AbstractMapStringObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.abstract_map_string_object import AbstractMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractMapStringObject from a JSON string
abstract_map_string_object_instance = AbstractMapStringObject.from_json(json)
# print the JSON string representation of the object
print(AbstractMapStringObject.to_json())

# convert the object into a dict
abstract_map_string_object_dict = abstract_map_string_object_instance.to_dict()
# create an instance of AbstractMapStringObject from a dict
abstract_map_string_object_from_dict = AbstractMapStringObject.from_dict(abstract_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


