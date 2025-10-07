# MeControllerApiMe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**super_admin** | **bool** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**profile** | [**MeControllerApiProfile**](MeControllerApiProfile.md) |  | [optional] 
**auths** | [**List[IAMTenantAccessControllerApiAuthentication]**](IAMTenantAccessControllerApiAuthentication.md) |  | [optional] 
**tenants** | [**List[MeControllerApiTenant]**](MeControllerApiTenant.md) |  | [optional] 

## Example

```python
from kestrapy.models.me_controller_api_me import MeControllerApiMe

# TODO update the JSON string below
json = "{}"
# create an instance of MeControllerApiMe from a JSON string
me_controller_api_me_instance = MeControllerApiMe.from_json(json)
# print the JSON string representation of the object
print(MeControllerApiMe.to_json())

# convert the object into a dict
me_controller_api_me_dict = me_controller_api_me_instance.to_dict()
# create an instance of MeControllerApiMe from a dict
me_controller_api_me_from_dict = MeControllerApiMe.from_dict(me_controller_api_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


