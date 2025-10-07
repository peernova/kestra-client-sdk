# kestrapy.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_group**](GroupsApi.md#add_user_to_group) | **PUT** /api/v1/{tenant}/groups/{id}/members/{userId} | Add a user to a group
[**autocomplete_groups**](GroupsApi.md#autocomplete_groups) | **POST** /api/v1/{tenant}/groups/autocomplete | List groups for autocomplete
[**create_group**](GroupsApi.md#create_group) | **POST** /api/v1/{tenant}/groups | Create a group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /api/v1/{tenant}/groups/{id} | Delete a group
[**delete_user_from_group**](GroupsApi.md#delete_user_from_group) | **DELETE** /api/v1/{tenant}/groups/{id}/members/{userId} | Remove a user from a group
[**get_group**](GroupsApi.md#get_group) | **GET** /api/v1/{tenant}/groups/{id} | Retrieve a group
[**list_group_ids**](GroupsApi.md#list_group_ids) | **POST** /api/v1/{tenant}/groups/ids | List groups by ids
[**search_group_members**](GroupsApi.md#search_group_members) | **GET** /api/v1/{tenant}/groups/{id}/members | Search for users in a group
[**search_groups**](GroupsApi.md#search_groups) | **GET** /api/v1/{tenant}/groups/search | Search for groups
[**set_user_membership_for_group**](GroupsApi.md#set_user_membership_for_group) | **PUT** /api/v1/{tenant}/groups/{id}/members/membership/{userId} | Update a user&#39;s membership type in a group
[**update_group**](GroupsApi.md#update_group) | **PUT** /api/v1/{tenant}/groups/{id} | Update a group


# **add_user_to_group**
> IAMGroupControllerApiGroupMember add_user_to_group(id, user_id, tenant)

Add a user to a group

Adds the specified user to the given group. If the user does not already have access to the tenant, tenant access will be created automatically.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.iam_group_controller_api_group_member import IAMGroupControllerApiGroupMember
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The ID of the group
    user_id = 'user_id_example' # str | The ID of the user to add to the group
    tenant = 'tenant_example' # str | 

    try:
        # Add a user to a group
        api_response = api_instance.add_user_to_group(id, user_id, tenant)
        print("The response of GroupsApi->add_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the group | 
 **user_id** | **str**| The ID of the user to add to the group | 
 **tenant** | **str**|  | 

### Return type

[**IAMGroupControllerApiGroupMember**](IAMGroupControllerApiGroupMember.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User was successfully added to the group |  -  |
**404** | Group or user not found |  -  |
**409** | User is already a member of the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_groups**
> List[ApiGroupSummary] autocomplete_groups(tenant, api_autocomplete)

List groups for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.api_autocomplete import ApiAutocomplete
from kestrapy.models.api_group_summary import ApiGroupSummary
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    api_autocomplete = kestrapy.ApiAutocomplete() # ApiAutocomplete | Autocomplete request

    try:
        # List groups for autocomplete
        api_response = api_instance.autocomplete_groups(tenant, api_autocomplete)
        print("The response of GroupsApi->autocomplete_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->autocomplete_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **api_autocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[ApiGroupSummary]**](ApiGroupSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteGroups 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> IAMGroupControllerApiGroupDetail create_group(tenant, iam_group_controller_api_create_group_request)

Create a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.iam_group_controller_api_create_group_request import IAMGroupControllerApiCreateGroupRequest
from kestrapy.models.iam_group_controller_api_group_detail import IAMGroupControllerApiGroupDetail
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    iam_group_controller_api_create_group_request = kestrapy.IAMGroupControllerApiCreateGroupRequest() # IAMGroupControllerApiCreateGroupRequest | The group

    try:
        # Create a group
        api_response = api_instance.create_group(tenant, iam_group_controller_api_create_group_request)
        print("The response of GroupsApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **iam_group_controller_api_create_group_request** | [**IAMGroupControllerApiCreateGroupRequest**](IAMGroupControllerApiCreateGroupRequest.md)| The group | 

### Return type

[**IAMGroupControllerApiGroupDetail**](IAMGroupControllerApiGroupDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group was created successfully |  -  |
**409** | A group with the given name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id, tenant)

Delete a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    tenant = 'tenant_example' # str | 

    try:
        # Delete a group
        api_instance.delete_group(id, tenant)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **tenant** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group was deleted successfully |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_group**
> IAMGroupControllerApiGroupMember delete_user_from_group(id, user_id, tenant)

Remove a user from a group

Removes the specified user from the given group. If the user has no other group bindings within the tenant, their access to the tenant will also be revoked.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.iam_group_controller_api_group_member import IAMGroupControllerApiGroupMember
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The ID of the group
    user_id = 'user_id_example' # str | The ID of the user to remove from the group
    tenant = 'tenant_example' # str | 

    try:
        # Remove a user from a group
        api_response = api_instance.delete_user_from_group(id, user_id, tenant)
        print("The response of GroupsApi->delete_user_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the group | 
 **user_id** | **str**| The ID of the user to remove from the group | 
 **tenant** | **str**|  | 

### Return type

[**IAMGroupControllerApiGroupMember**](IAMGroupControllerApiGroupMember.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User was successfully removed from the group |  -  |
**404** | Group or user not found |  -  |
**409** | User is not a member of the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> IAMGroupControllerApiGroupDetail get_group(id, tenant)

Retrieve a group

Retrieves details of a specific group by its ID within the current tenant.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.iam_group_controller_api_group_detail import IAMGroupControllerApiGroupDetail
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    tenant = 'tenant_example' # str | 

    try:
        # Retrieve a group
        api_response = api_instance.get_group(id, tenant)
        print("The response of GroupsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **tenant** | **str**|  | 

### Return type

[**IAMGroupControllerApiGroupDetail**](IAMGroupControllerApiGroupDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group details successfully retrieved |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_ids**
> List[ApiGroupSummary] list_group_ids(tenant, api_ids)

List groups by ids

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.api_group_summary import ApiGroupSummary
from kestrapy.models.api_ids import ApiIds
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    api_ids = kestrapy.ApiIds() # ApiIds | The ids that must be present on results

    try:
        # List groups by ids
        api_response = api_instance.list_group_ids(tenant, api_ids)
        print("The response of GroupsApi->list_group_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->list_group_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **api_ids** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | 

### Return type

[**List[ApiGroupSummary]**](ApiGroupSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listGroupIds 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_group_members**
> PagedResultsIAMGroupControllerApiGroupMember search_group_members(id, page, size, tenant, q=q, sort=sort)

Search for users in a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.paged_results_iam_group_controller_api_group_member import PagedResultsIAMGroupControllerApiGroupMember
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for users in a group
        api_response = api_instance.search_group_members(id, page, size, tenant, q=q, sort=sort)
        print("The response of GroupsApi->search_group_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsIAMGroupControllerApiGroupMember**](PagedResultsIAMGroupControllerApiGroupMember.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroupMembers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> PagedResultsApiGroupSummary search_groups(page, size, tenant, q=q, sort=sort)

Search for groups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.paged_results_api_group_summary import PagedResultsApiGroupSummary
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for groups
        api_response = api_instance.search_groups(page, size, tenant, q=q, sort=sort)
        print("The response of GroupsApi->search_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsApiGroupSummary**](PagedResultsApiGroupSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroups 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_membership_for_group**
> IAMGroupControllerApiGroupMember set_user_membership_for_group(id, user_id, membership, tenant)

Update a user's membership type in a group

Allows a group owner or an authorized user to change the role of a user within a group to OWNER or MEMBER.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.group_identifier_membership import GroupIdentifierMembership
from kestrapy.models.iam_group_controller_api_group_member import IAMGroupControllerApiGroupMember
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The ID of the group
    user_id = 'user_id_example' # str | The ID of the user whose membership is being updated
    membership = kestrapy.GroupIdentifierMembership() # GroupIdentifierMembership | The new membership type to assign to the user.
    tenant = 'tenant_example' # str | 

    try:
        # Update a user's membership type in a group
        api_response = api_instance.set_user_membership_for_group(id, user_id, membership, tenant)
        print("The response of GroupsApi->set_user_membership_for_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_user_membership_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the group | 
 **user_id** | **str**| The ID of the user whose membership is being updated | 
 **membership** | [**GroupIdentifierMembership**](.md)| The new membership type to assign to the user. | 
 **tenant** | **str**|  | 

### Return type

[**IAMGroupControllerApiGroupMember**](IAMGroupControllerApiGroupMember.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Membership type successfully updated |  -  |
**404** | User or group not found |  -  |
**409** | User is not a member of the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> IAMGroupControllerApiGroupDetail update_group(id, tenant, iam_group_controller_api_update_group_request)

Update a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestrapy
from kestrapy.models.iam_group_controller_api_group_detail import IAMGroupControllerApiGroupDetail
from kestrapy.models.iam_group_controller_api_update_group_request import IAMGroupControllerApiUpdateGroupRequest
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestrapy.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestrapy.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    tenant = 'tenant_example' # str | 
    iam_group_controller_api_update_group_request = kestrapy.IAMGroupControllerApiUpdateGroupRequest() # IAMGroupControllerApiUpdateGroupRequest | The group

    try:
        # Update a group
        api_response = api_instance.update_group(id, tenant, iam_group_controller_api_update_group_request)
        print("The response of GroupsApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **tenant** | **str**|  | 
 **iam_group_controller_api_update_group_request** | [**IAMGroupControllerApiUpdateGroupRequest**](IAMGroupControllerApiUpdateGroupRequest.md)| The group | 

### Return type

[**IAMGroupControllerApiGroupDetail**](IAMGroupControllerApiGroupDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group was updated successfully |  -  |
**404** | Group not found |  -  |
**409** | A group with the given name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

