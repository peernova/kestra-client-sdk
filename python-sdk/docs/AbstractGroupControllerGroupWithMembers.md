# AbstractGroupControllerGroupWithMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**deleted** | **bool** |  | 
**provider** | [**IdentityProvider**](IdentityProvider.md) |  | [optional] 
**members_id** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.abstract_group_controller_group_with_members import AbstractGroupControllerGroupWithMembers

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractGroupControllerGroupWithMembers from a JSON string
abstract_group_controller_group_with_members_instance = AbstractGroupControllerGroupWithMembers.from_json(json)
# print the JSON string representation of the object
print(AbstractGroupControllerGroupWithMembers.to_json())

# convert the object into a dict
abstract_group_controller_group_with_members_dict = abstract_group_controller_group_with_members_instance.to_dict()
# create an instance of AbstractGroupControllerGroupWithMembers from a dict
abstract_group_controller_group_with_members_from_dict = AbstractGroupControllerGroupWithMembers.from_dict(abstract_group_controller_group_with_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


