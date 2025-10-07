# HashMapStringObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.hash_map_string_object import HashMapStringObject

# TODO update the JSON string below
json = "{}"
# create an instance of HashMapStringObject from a JSON string
hash_map_string_object_instance = HashMapStringObject.from_json(json)
# print the JSON string representation of the object
print(HashMapStringObject.to_json())

# convert the object into a dict
hash_map_string_object_dict = hash_map_string_object_instance.to_dict()
# create an instance of HashMapStringObject from a dict
hash_map_string_object_from_dict = HashMapStringObject.from_dict(hash_map_string_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


