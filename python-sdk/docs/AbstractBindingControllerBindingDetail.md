# AbstractBindingControllerBindingDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**Binding**](Binding.md) |  | [optional] 
**role** | [**Role**](Role.md) |  | [optional] 
**user** | [**ApiUser**](ApiUser.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.abstract_binding_controller_binding_detail import AbstractBindingControllerBindingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractBindingControllerBindingDetail from a JSON string
abstract_binding_controller_binding_detail_instance = AbstractBindingControllerBindingDetail.from_json(json)
# print the JSON string representation of the object
print(AbstractBindingControllerBindingDetail.to_json())

# convert the object into a dict
abstract_binding_controller_binding_detail_dict = abstract_binding_controller_binding_detail_instance.to_dict()
# create an instance of AbstractBindingControllerBindingDetail from a dict
abstract_binding_controller_binding_detail_from_dict = AbstractBindingControllerBindingDetail.from_dict(abstract_binding_controller_binding_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


