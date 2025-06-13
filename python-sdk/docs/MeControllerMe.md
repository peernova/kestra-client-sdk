# MeControllerMe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ApiUser**](ApiUser.md) |  | [optional] 
**roles** | [**List[AclServiceNamespaceRole]**](AclServiceNamespaceRole.md) |  | [optional] 
**tenants** | [**List[ApiTenant]**](ApiTenant.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.me_controller_me import MeControllerMe

# TODO update the JSON string below
json = "{}"
# create an instance of MeControllerMe from a JSON string
me_controller_me_instance = MeControllerMe.from_json(json)
# print the JSON string representation of the object
print(MeControllerMe.to_json())

# convert the object into a dict
me_controller_me_dict = me_controller_me_instance.to_dict()
# create an instance of MeControllerMe from a dict
me_controller_me_from_dict = MeControllerMe.from_dict(me_controller_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


