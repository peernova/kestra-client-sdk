# MeControllerUpdatePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from kestra_api_client.models.me_controller_update_password_request import MeControllerUpdatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MeControllerUpdatePasswordRequest from a JSON string
me_controller_update_password_request_instance = MeControllerUpdatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(MeControllerUpdatePasswordRequest.to_json())

# convert the object into a dict
me_controller_update_password_request_dict = me_controller_update_password_request_instance.to_dict()
# create an instance of MeControllerUpdatePasswordRequest from a dict
me_controller_update_password_request_from_dict = MeControllerUpdatePasswordRequest.from_dict(me_controller_update_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


