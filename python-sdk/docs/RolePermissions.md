# RolePermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow** | **List[str]** |  | [optional] 
**blueprint** | **List[str]** |  | [optional] 
**template** | **List[str]** |  | [optional] 
**namespace** | **List[str]** |  | [optional] 
**execution** | **List[str]** |  | [optional] 
**user** | **List[str]** |  | [optional] 
**group** | **List[str]** |  | [optional] 
**role** | **List[str]** |  | [optional] 
**binding** | **List[str]** |  | [optional] 
**auditlog** | **List[str]** |  | [optional] 
**secret** | **List[str]** |  | [optional] 
**kvstore** | **List[str]** |  | [optional] 
**impersonate** | **List[str]** |  | [optional] 
**setting** | **List[str]** |  | [optional] 
**infrastructure** | **List[str]** |  | [optional] 
**app** | **List[str]** |  | [optional] 
**appexecution** | **List[str]** |  | [optional] 
**test** | **List[str]** |  | [optional] 
**me** | **List[str]** |  | [optional] 
**apitoken** | **List[str]** |  | [optional] 
**dashboard** | **List[str]** |  | [optional] 
**tenant** | **List[str]** |  | [optional] 
**unknown** | **List[str]** |  | [optional] 

## Example

```python
from kestra_api_client.models.role_permissions import RolePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissions from a JSON string
role_permissions_instance = RolePermissions.from_json(json)
# print the JSON string representation of the object
print(RolePermissions.to_json())

# convert the object into a dict
role_permissions_dict = role_permissions_instance.to_dict()
# create an instance of RolePermissions from a dict
role_permissions_from_dict = RolePermissions.from_dict(role_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


