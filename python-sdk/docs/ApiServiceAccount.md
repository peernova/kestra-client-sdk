# ApiServiceAccount

A User Service Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identifier of this service account. | [optional] 
**name** | **str** | the name of this service account. | 
**description** | **str** | the description of this service account. | [optional] 
**group_list** | [**List[AbstractUserGroupIdentifier]**](AbstractUserGroupIdentifier.md) |  | [optional] 
**is_super_admin** | **bool** |  | [optional] 

## Example

```python
from kestra_api_client.models.api_service_account import ApiServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ApiServiceAccount from a JSON string
api_service_account_instance = ApiServiceAccount.from_json(json)
# print the JSON string representation of the object
print(ApiServiceAccount.to_json())

# convert the object into a dict
api_service_account_dict = api_service_account_instance.to_dict()
# create an instance of ApiServiceAccount from a dict
api_service_account_from_dict = ApiServiceAccount.from_dict(api_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


