# PagedResultsApiUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ApiUser]**](ApiUser.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_api_user import PagedResultsApiUser

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsApiUser from a JSON string
paged_results_api_user_instance = PagedResultsApiUser.from_json(json)
# print the JSON string representation of the object
print(PagedResultsApiUser.to_json())

# convert the object into a dict
paged_results_api_user_dict = paged_results_api_user_instance.to_dict()
# create an instance of PagedResultsApiUser from a dict
paged_results_api_user_from_dict = PagedResultsApiUser.from_dict(paged_results_api_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


