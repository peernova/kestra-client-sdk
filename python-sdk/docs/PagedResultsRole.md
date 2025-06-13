# PagedResultsRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Role]**](Role.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_role import PagedResultsRole

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsRole from a JSON string
paged_results_role_instance = PagedResultsRole.from_json(json)
# print the JSON string representation of the object
print(PagedResultsRole.to_json())

# convert the object into a dict
paged_results_role_dict = paged_results_role_instance.to_dict()
# create an instance of PagedResultsRole from a dict
paged_results_role_from_dict = PagedResultsRole.from_dict(paged_results_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


