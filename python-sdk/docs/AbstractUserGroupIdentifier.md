# AbstractUserGroupIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**membership** | [**AbstractUserGroupIdentifierMembership**](AbstractUserGroupIdentifierMembership.md) |  | [optional] 
**managed_externally** | **bool** |  | [optional] 

## Example

```python
from kestra_api_client.models.abstract_user_group_identifier import AbstractUserGroupIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractUserGroupIdentifier from a JSON string
abstract_user_group_identifier_instance = AbstractUserGroupIdentifier.from_json(json)
# print the JSON string representation of the object
print(AbstractUserGroupIdentifier.to_json())

# convert the object into a dict
abstract_user_group_identifier_dict = abstract_user_group_identifier_instance.to_dict()
# create an instance of AbstractUserGroupIdentifier from a dict
abstract_user_group_identifier_from_dict = AbstractUserGroupIdentifier.from_dict(abstract_user_group_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


