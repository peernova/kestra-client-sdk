# PagedResultsInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Invitation]**](Invitation.md) |  | 
**total** | **int** |  | 

## Example

```python
from kestra_api_client.models.paged_results_invitation import PagedResultsInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultsInvitation from a JSON string
paged_results_invitation_instance = PagedResultsInvitation.from_json(json)
# print the JSON string representation of the object
print(PagedResultsInvitation.to_json())

# convert the object into a dict
paged_results_invitation_dict = paged_results_invitation_instance.to_dict()
# create an instance of PagedResultsInvitation from a dict
paged_results_invitation_from_dict = PagedResultsInvitation.from_dict(paged_results_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


