# PagedResultsAbstractBindingControllerBindingDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AbstractBindingControllerBindingDetail]**](AbstractBindingControllerBindingDetail.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_abstract_binding_controller_binding_detail import PagedResultsAbstractBindingControllerBindingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsAbstractBindingControllerBindingDetail from a JSON string
paged_results_abstract_binding_controller_binding_detail_instance = PagedResultsAbstractBindingControllerBindingDetail.from_json(json)
# print the JSON string representation of the object
print(PagedResultsAbstractBindingControllerBindingDetail.to_json())

# convert the object into a dict
paged_results_abstract_binding_controller_binding_detail_dict = paged_results_abstract_binding_controller_binding_detail_instance.to_dict()
# create an instance of PagedResultsAbstractBindingControllerBindingDetail from a dict
paged_results_abstract_binding_controller_binding_detail_from_dict = PagedResultsAbstractBindingControllerBindingDetail.from_dict(paged_results_abstract_binding_controller_binding_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


