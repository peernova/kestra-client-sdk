# AclServiceNamespaceRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role**](Role.md) |  | [optional] 
**namespace_id** | **str** |  | [optional] 

## Example

```python
from kestra_api_client.models.acl_service_namespace_role import AclServiceNamespaceRole

# TODO update the JSON string below
json = "{}"
# create an instance of AclServiceNamespaceRole from a JSON string
acl_service_namespace_role_instance = AclServiceNamespaceRole.from_json(json)
# print the JSON string representation of the object
print(AclServiceNamespaceRole.to_json())

# convert the object into a dict
acl_service_namespace_role_dict = acl_service_namespace_role_instance.to_dict()
# create an instance of AclServiceNamespaceRole from a dict
acl_service_namespace_role_from_dict = AclServiceNamespaceRole.from_dict(acl_service_namespace_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


