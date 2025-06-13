# GlobalFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**namespace** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**filters** | [**List[QueryFilter]**](QueryFilter.md) |  | [optional] 

## Example

```python
from kestra_api_client.models.global_filter import GlobalFilter

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalFilter from a JSON string
global_filter_instance = GlobalFilter.from_json(json)
# print the JSON string representation of the object
print(GlobalFilter.to_json())

# convert the object into a dict
global_filter_dict = global_filter_instance.to_dict()
# create an instance of GlobalFilter from a dict
global_filter_from_dict = GlobalFilter.from_dict(global_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


