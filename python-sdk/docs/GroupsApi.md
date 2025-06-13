# kestra_api_client.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_group**](GroupsApi.md#add_user_to_group) | **PUT** /api/v1/{tenant}/groups/{id}/members/{userId} | Add a group for a user
[**add_user_to_group_with_resource_tenantas_super_admin**](GroupsApi.md#add_user_to_group_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id}/members/{userId} | Add a group for a user
[**add_user_to_groupas_super_admin**](GroupsApi.md#add_user_to_groupas_super_admin) | **PUT** /api/v1/tenants/groups/{id}/members/{userId} | Add a group for a user
[**autocomplete_groups**](GroupsApi.md#autocomplete_groups) | **POST** /api/v1/{tenant}/groups/autocomplete | List groups for autocomplete
[**autocomplete_groups_with_resource_tenantas_super_admin**](GroupsApi.md#autocomplete_groups_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/groups/autocomplete | List groups for autocomplete
[**autocomplete_groupsas_super_admin**](GroupsApi.md#autocomplete_groupsas_super_admin) | **POST** /api/v1/tenants/groups/autocomplete | List groups for autocomplete
[**create_group**](GroupsApi.md#create_group) | **POST** /api/v1/{tenant}/groups | Create a group
[**create_group_with_resource_tenantas_super_admin**](GroupsApi.md#create_group_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/groups | Create a group
[**create_groupas_super_admin**](GroupsApi.md#create_groupas_super_admin) | **POST** /api/v1/tenants/groups | Create a group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /api/v1/{tenant}/groups/{id} | Delete a group
[**delete_group_with_resource_tenantas_super_admin**](GroupsApi.md#delete_group_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/groups/{id} | Delete a group
[**delete_groupas_super_admin**](GroupsApi.md#delete_groupas_super_admin) | **DELETE** /api/v1/tenants/groups/{id} | Delete a group
[**delete_user_from_group**](GroupsApi.md#delete_user_from_group) | **DELETE** /api/v1/{tenant}/groups/{id}/members/{userId} | Delete a group for a user
[**delete_user_from_group_with_resource_tenantas_super_admin**](GroupsApi.md#delete_user_from_group_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/groups/{id}/members/{userId} | Delete a group for a user
[**delete_user_from_groupas_super_admin**](GroupsApi.md#delete_user_from_groupas_super_admin) | **DELETE** /api/v1/tenants/groups/{id}/members/{userId} | Delete a group for a user
[**get_group**](GroupsApi.md#get_group) | **GET** /api/v1/{tenant}/groups/{id} | Get a group
[**get_group_with_resource_tenantas_super_admin**](GroupsApi.md#get_group_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/groups/{id} | Get a group
[**get_groupas_super_admin**](GroupsApi.md#get_groupas_super_admin) | **GET** /api/v1/tenants/groups/{id} | Get a group
[**list_group_ids**](GroupsApi.md#list_group_ids) | **POST** /api/v1/{tenant}/groups/ids | List groups by ids
[**list_group_ids_with_resource_tenantas_super_admin**](GroupsApi.md#list_group_ids_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/groups/ids | List groups by ids
[**list_group_idsas_super_admin**](GroupsApi.md#list_group_idsas_super_admin) | **POST** /api/v1/tenants/groups/ids | List groups by ids
[**search_group_members**](GroupsApi.md#search_group_members) | **GET** /api/v1/{tenant}/groups/{id}/members | Search for users in a group
[**search_group_members_with_resource_tenantas_super_admin**](GroupsApi.md#search_group_members_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/groups/{id}/members | Search for users in a group
[**search_group_membersas_super_admin**](GroupsApi.md#search_group_membersas_super_admin) | **GET** /api/v1/tenants/groups/{id}/members | Search for users in a group
[**search_groups**](GroupsApi.md#search_groups) | **GET** /api/v1/{tenant}/groups/search | Search for groups
[**search_groups_with_resource_tenantas_super_admin**](GroupsApi.md#search_groups_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/groups/search | Search for groups
[**search_groupsas_super_admin**](GroupsApi.md#search_groupsas_super_admin) | **GET** /api/v1/tenants/groups/search | Search for groups
[**set_user_membership_for_group**](GroupsApi.md#set_user_membership_for_group) | **PUT** /api/v1/{tenant}/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group
[**set_user_membership_for_group_with_resource_tenantas_super_admin**](GroupsApi.md#set_user_membership_for_group_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group
[**set_user_membership_for_groupas_super_admin**](GroupsApi.md#set_user_membership_for_groupas_super_admin) | **PUT** /api/v1/tenants/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group
[**update_group**](GroupsApi.md#update_group) | **PUT** /api/v1/{tenant}/groups/{id} | Update a group
[**update_group_with_resource_tenantas_super_admin**](GroupsApi.md#update_group_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id} | Update a group
[**update_groupas_super_admin**](GroupsApi.md#update_groupas_super_admin) | **PUT** /api/v1/tenants/groups/{id} | Update a group


# **add_user_to_group**
> ApiUser add_user_to_group(id, user_id, tenant)

Add a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # Add a group for a user
        api_response = api_instance.add_user_to_group(id, user_id, tenant)
        print("The response of GroupsApi->add_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | addUserToGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_group_with_resource_tenantas_super_admin**
> ApiUser add_user_to_group_with_resource_tenantas_super_admin(id, user_id, resource_tenant)

Add a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Add a group for a user
        api_response = api_instance.add_user_to_group_with_resource_tenantas_super_admin(id, user_id, resource_tenant)
        print("The response of GroupsApi->add_user_to_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_user_to_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | addUserToGroupWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_groupas_super_admin**
> ApiUser add_user_to_groupas_super_admin(id, user_id)

Add a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id

    try:
        # Add a group for a user
        api_response = api_instance.add_user_to_groupas_super_admin(id, user_id)
        print("The response of GroupsApi->add_user_to_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_user_to_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | addUserToGroupasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_groups**
> List[Group] autocomplete_groups(tenant, api_autocomplete)

List groups for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_autocomplete import ApiAutocomplete
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    api_autocomplete = kestra_api_client.ApiAutocomplete() # ApiAutocomplete | Autocomplete request

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

[**List[Group]**](Group.md)

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

# **autocomplete_groups_with_resource_tenantas_super_admin**
> List[Group] autocomplete_groups_with_resource_tenantas_super_admin(resource_tenant, api_autocomplete)

List groups for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_autocomplete import ApiAutocomplete
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    api_autocomplete = kestra_api_client.ApiAutocomplete() # ApiAutocomplete | Autocomplete request

    try:
        # List groups for autocomplete
        api_response = api_instance.autocomplete_groups_with_resource_tenantas_super_admin(resource_tenant, api_autocomplete)
        print("The response of GroupsApi->autocomplete_groups_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->autocomplete_groups_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **api_autocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteGroupsWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_groupsas_super_admin**
> List[Group] autocomplete_groupsas_super_admin(api_autocomplete)

List groups for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_autocomplete import ApiAutocomplete
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    api_autocomplete = kestra_api_client.ApiAutocomplete() # ApiAutocomplete | Autocomplete request

    try:
        # List groups for autocomplete
        api_response = api_instance.autocomplete_groupsas_super_admin(api_autocomplete)
        print("The response of GroupsApi->autocomplete_groupsas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->autocomplete_groupsas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_autocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteGroupsasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(tenant, abstract_group_controller_group_with_members)

Create a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_group_controller_group_with_members import AbstractGroupControllerGroupWithMembers
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    abstract_group_controller_group_with_members = kestra_api_client.AbstractGroupControllerGroupWithMembers() # AbstractGroupControllerGroupWithMembers | The group

    try:
        # Create a group
        api_response = api_instance.create_group(tenant, abstract_group_controller_group_with_members)
        print("The response of GroupsApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **abstract_group_controller_group_with_members** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_with_resource_tenantas_super_admin**
> Group create_group_with_resource_tenantas_super_admin(resource_tenant, abstract_group_controller_group_with_members)

Create a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_group_controller_group_with_members import AbstractGroupControllerGroupWithMembers
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    abstract_group_controller_group_with_members = kestra_api_client.AbstractGroupControllerGroupWithMembers() # AbstractGroupControllerGroupWithMembers | The group

    try:
        # Create a group
        api_response = api_instance.create_group_with_resource_tenantas_super_admin(resource_tenant, abstract_group_controller_group_with_members)
        print("The response of GroupsApi->create_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **abstract_group_controller_group_with_members** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createGroupWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_groupas_super_admin**
> Group create_groupas_super_admin(abstract_group_controller_group_with_members)

Create a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_group_controller_group_with_members import AbstractGroupControllerGroupWithMembers
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    abstract_group_controller_group_with_members = kestra_api_client.AbstractGroupControllerGroupWithMembers() # AbstractGroupControllerGroupWithMembers | The group

    try:
        # Create a group
        api_response = api_instance.create_groupas_super_admin(abstract_group_controller_group_with_members)
        print("The response of GroupsApi->create_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abstract_group_controller_group_with_members** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createGroupasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id, tenant)

Delete a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
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
**204** | On success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_with_resource_tenantas_super_admin**
> delete_group_with_resource_tenantas_super_admin(id, resource_tenant)

Delete a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete a group
        api_instance.delete_group_with_resource_tenantas_super_admin(id, resource_tenant)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **resource_tenant** | **str**|  | 

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
**204** | On success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groupas_super_admin**
> delete_groupas_super_admin(id)

Delete a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id

    try:
        # Delete a group
        api_instance.delete_groupas_super_admin(id)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 

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
**204** | On success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_group**
> ApiUser delete_user_from_group(id, user_id, tenant)

Delete a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # Delete a group for a user
        api_response = api_instance.delete_user_from_group(id, user_id, tenant)
        print("The response of GroupsApi->delete_user_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteUserFromGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_group_with_resource_tenantas_super_admin**
> ApiUser delete_user_from_group_with_resource_tenantas_super_admin(id, user_id, resource_tenant)

Delete a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete a group for a user
        api_response = api_instance.delete_user_from_group_with_resource_tenantas_super_admin(id, user_id, resource_tenant)
        print("The response of GroupsApi->delete_user_from_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_user_from_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteUserFromGroupWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_groupas_super_admin**
> ApiUser delete_user_from_groupas_super_admin(id, user_id)

Delete a group for a user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id

    try:
        # Delete a group for a user
        api_response = api_instance.delete_user_from_groupas_super_admin(id, user_id)
        print("The response of GroupsApi->delete_user_from_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_user_from_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteUserFromGroupasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id, tenant)

Get a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    tenant = 'tenant_example' # str | 

    try:
        # Get a group
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

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_with_resource_tenantas_super_admin**
> Group get_group_with_resource_tenantas_super_admin(id, resource_tenant)

Get a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Get a group
        api_response = api_instance.get_group_with_resource_tenantas_super_admin(id, resource_tenant)
        print("The response of GroupsApi->get_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **resource_tenant** | **str**|  | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getGroupWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groupas_super_admin**
> Group get_groupas_super_admin(id)

Get a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id

    try:
        # Get a group
        api_response = api_instance.get_groupas_super_admin(id)
        print("The response of GroupsApi->get_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getGroupasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_ids**
> List[Group] list_group_ids(tenant, api_ids)

List groups by ids

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_ids import ApiIds
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    tenant = 'tenant_example' # str | 
    api_ids = kestra_api_client.ApiIds() # ApiIds | The ids that must be present on results

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

[**List[Group]**](Group.md)

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

# **list_group_ids_with_resource_tenantas_super_admin**
> List[Group] list_group_ids_with_resource_tenantas_super_admin(resource_tenant, api_ids)

List groups by ids

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_ids import ApiIds
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    api_ids = kestra_api_client.ApiIds() # ApiIds | The ids that must be present on results

    try:
        # List groups by ids
        api_response = api_instance.list_group_ids_with_resource_tenantas_super_admin(resource_tenant, api_ids)
        print("The response of GroupsApi->list_group_ids_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->list_group_ids_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **api_ids** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | 

### Return type

[**List[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listGroupIdsWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_idsas_super_admin**
> List[Group] list_group_idsas_super_admin(api_ids)

List groups by ids

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_ids import ApiIds
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    api_ids = kestra_api_client.ApiIds() # ApiIds | The ids that must be present on results

    try:
        # List groups by ids
        api_response = api_instance.list_group_idsas_super_admin(api_ids)
        print("The response of GroupsApi->list_group_idsas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->list_group_idsas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_ids** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | 

### Return type

[**List[Group]**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listGroupIdsasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_group_members**
> PagedResultsApiUser search_group_members(id, page, size, tenant, q=q, sort=sort)

Search for users in a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_api_user import PagedResultsApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
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

[**PagedResultsApiUser**](PagedResultsApiUser.md)

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

# **search_group_members_with_resource_tenantas_super_admin**
> PagedResultsApiUser search_group_members_with_resource_tenantas_super_admin(id, page, size, resource_tenant, q=q, sort=sort)

Search for users in a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_api_user import PagedResultsApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for users in a group
        api_response = api_instance.search_group_members_with_resource_tenantas_super_admin(id, page, size, resource_tenant, q=q, sort=sort)
        print("The response of GroupsApi->search_group_members_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_group_members_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsApiUser**](PagedResultsApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroupMembersWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_group_membersas_super_admin**
> PagedResultsApiUser search_group_membersas_super_admin(id, page, size, q=q, sort=sort)

Search for users in a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_api_user import PagedResultsApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for users in a group
        api_response = api_instance.search_group_membersas_super_admin(id, page, size, q=q, sort=sort)
        print("The response of GroupsApi->search_group_membersas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_group_membersas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsApiUser**](PagedResultsApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroupMembersasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> PagedResultsGroup search_groups(page, size, tenant, q=q, sort=sort)

Search for groups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_group import PagedResultsGroup
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
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

[**PagedResultsGroup**](PagedResultsGroup.md)

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

# **search_groups_with_resource_tenantas_super_admin**
> PagedResultsGroup search_groups_with_resource_tenantas_super_admin(page, size, resource_tenant, q=q, sort=sort)

Search for groups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_group import PagedResultsGroup
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for groups
        api_response = api_instance.search_groups_with_resource_tenantas_super_admin(page, size, resource_tenant, q=q, sort=sort)
        print("The response of GroupsApi->search_groups_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_groups_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroupsWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groupsas_super_admin**
> PagedResultsGroup search_groupsas_super_admin(page, size, q=q, sort=sort)

Search for groups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_group import PagedResultsGroup
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for groups
        api_response = api_instance.search_groupsas_super_admin(page, size, q=q, sort=sort)
        print("The response of GroupsApi->search_groupsas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->search_groupsas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchGroupsasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_membership_for_group**
> ApiUser set_user_membership_for_group(id, user_id, membership, tenant)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_group_identifier_membership import AbstractUserGroupIdentifierMembership
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    membership = kestra_api_client.AbstractUserGroupIdentifierMembership() # AbstractUserGroupIdentifierMembership | The membership type
    tenant = 'tenant_example' # str | 

    try:
        # Set the membership type of a user in a group
        api_response = api_instance.set_user_membership_for_group(id, user_id, membership, tenant)
        print("The response of GroupsApi->set_user_membership_for_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_user_membership_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | 
 **tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_membership_for_group_with_resource_tenantas_super_admin**
> ApiUser set_user_membership_for_group_with_resource_tenantas_super_admin(id, user_id, membership, resource_tenant)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_group_identifier_membership import AbstractUserGroupIdentifierMembership
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    membership = kestra_api_client.AbstractUserGroupIdentifierMembership() # AbstractUserGroupIdentifierMembership | The membership type
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Set the membership type of a user in a group
        api_response = api_instance.set_user_membership_for_group_with_resource_tenantas_super_admin(id, user_id, membership, resource_tenant)
        print("The response of GroupsApi->set_user_membership_for_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_user_membership_for_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | 
 **resource_tenant** | **str**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_membership_for_groupas_super_admin**
> ApiUser set_user_membership_for_groupas_super_admin(id, user_id, membership)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_group_identifier_membership import AbstractUserGroupIdentifierMembership
from kestra_api_client.models.api_user import ApiUser
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    user_id = 'user_id_example' # str | The user id
    membership = kestra_api_client.AbstractUserGroupIdentifierMembership() # AbstractUserGroupIdentifierMembership | The membership type

    try:
        # Set the membership type of a user in a group
        api_response = api_instance.set_user_membership_for_groupas_super_admin(id, user_id, membership)
        print("The response of GroupsApi->set_user_membership_for_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->set_user_membership_for_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **user_id** | **str**| The user id | 
 **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(id, tenant, group)

Update a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    tenant = 'tenant_example' # str | 
    group = kestra_api_client.Group() # Group | The group

    try:
        # Update a group
        api_response = api_instance.update_group(id, tenant, group)
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
 **group** | [**Group**](Group.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_with_resource_tenantas_super_admin**
> Group update_group_with_resource_tenantas_super_admin(id, resource_tenant, group)

Update a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    resource_tenant = 'resource_tenant_example' # str | 
    group = kestra_api_client.Group() # Group | The group

    try:
        # Update a group
        api_response = api_instance.update_group_with_resource_tenantas_super_admin(id, resource_tenant, group)
        print("The response of GroupsApi->update_group_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_group_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **resource_tenant** | **str**|  | 
 **group** | [**Group**](Group.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateGroupWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groupas_super_admin**
> Group update_groupas_super_admin(id, group)

Update a group

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.group import Group
from kestra_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestra_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = kestra_api_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (Bearer): bearerAuth
configuration = kestra_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kestra_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestra_api_client.GroupsApi(api_client)
    id = 'id_example' # str | The group id
    group = kestra_api_client.Group() # Group | The group

    try:
        # Update a group
        api_response = api_instance.update_groupas_super_admin(id, group)
        print("The response of GroupsApi->update_groupas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_groupas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The group id | 
 **group** | [**Group**](Group.md)| The group | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateGroupasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

