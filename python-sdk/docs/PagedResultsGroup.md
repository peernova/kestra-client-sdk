# PagedResultsGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Group]**](Group.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_group import PagedResultsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsGroup from a JSON string
paged_results_group_instance = PagedResultsGroup.from_json(json)
# print the JSON string representation of the object
print(PagedResultsGroup.to_json())

# convert the object into a dict
paged_results_group_dict = paged_results_group_instance.to_dict()
# create an instance of PagedResultsGroup from a dict
paged_results_group_from_dict = PagedResultsGroup.from_dict(paged_results_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


