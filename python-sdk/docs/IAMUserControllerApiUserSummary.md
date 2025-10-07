# IAMUserControllerApiUserSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**tenants** | [**List[ApiTenantSummary]**](ApiTenantSummary.md) |  | [optional] 
**auths** | [**List[IAMUserControllerApiUserAuth]**](IAMUserControllerApiUserAuth.md) |  | [optional] 
**super_admin** | **bool** |  | [optional] 

## Example

```python
from kestrapy.models.iam_user_controller_api_user_summary import IAMUserControllerApiUserSummary

# TODO update the JSON string below
json = "{}"
# create an instance of IAMUserControllerApiUserSummary from a JSON string
iam_user_controller_api_user_summary_instance = IAMUserControllerApiUserSummary.from_json(json)
# print the JSON string representation of the object
print(IAMUserControllerApiUserSummary.to_json())

# convert the object into a dict
iam_user_controller_api_user_summary_dict = iam_user_controller_api_user_summary_instance.to_dict()
# create an instance of IAMUserControllerApiUserSummary from a dict
iam_user_controller_api_user_summary_from_dict = IAMUserControllerApiUserSummary.from_dict(iam_user_controller_api_user_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


