# kestra_api_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_users**](UsersApi.md#autocomplete_users) | **POST** /api/v1/{tenant}/users/autocomplete | List users for autocomplete
[**autocomplete_users_with_resource_tenantas_super_admin**](UsersApi.md#autocomplete_users_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/users/autocomplete | List users for autocomplete
[**autocomplete_usersas_super_admin**](UsersApi.md#autocomplete_usersas_super_admin) | **POST** /api/v1/tenants/users/autocomplete | List users for autocomplete
[**create_api_tokens_for_user**](UsersApi.md#create_api_tokens_for_user) | **POST** /api/v1/{tenant}/users/{id}/api-tokens | Create new API Token for a specific user
[**create_api_tokens_for_user_with_resource_tenantas_super_admin**](UsersApi.md#create_api_tokens_for_user_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens | Create new API Token for a specific user
[**create_api_tokens_for_useras_super_admin**](UsersApi.md#create_api_tokens_for_useras_super_admin) | **POST** /api/v1/tenants/users/{id}/api-tokens | Create new API Token for a specific user
[**create_service_account**](UsersApi.md#create_service_account) | **POST** /api/v1/{tenant}/users/service-accounts | Create a user service account
[**create_service_account_with_resource_tenantas_super_admin**](UsersApi.md#create_service_account_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/users/service-accounts | Create a user service account
[**create_service_accountas_super_admin**](UsersApi.md#create_service_accountas_super_admin) | **POST** /api/v1/tenants/users/service-accounts | Create a user service account
[**create_user**](UsersApi.md#create_user) | **POST** /api/v1/{tenant}/users | Create a standard user
[**create_user_basic_auth**](UsersApi.md#create_user_basic_auth) | **PUT** /api/v1/{tenant}/users/{id}/password | Create a basic auth password for a standard user
[**create_user_basic_auth_with_resource_tenantas_super_admin**](UsersApi.md#create_user_basic_auth_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id}/password | Create a basic auth password for a standard user
[**create_user_basic_authas_super_admin**](UsersApi.md#create_user_basic_authas_super_admin) | **PUT** /api/v1/tenants/users/{id}/password | Create a basic auth password for a standard user
[**create_user_with_resource_tenantas_super_admin**](UsersApi.md#create_user_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/users | Create a standard user
[**create_useras_super_admin**](UsersApi.md#create_useras_super_admin) | **POST** /api/v1/tenants/users | Create a standard user
[**delete_api_token**](UsersApi.md#delete_api_token) | **DELETE** /api/v1/{tenant}/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id
[**delete_api_token_with_resource_tenantas_super_admin**](UsersApi.md#delete_api_token_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id
[**delete_api_tokenas_super_admin**](UsersApi.md#delete_api_tokenas_super_admin) | **DELETE** /api/v1/tenants/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id
[**delete_auth**](UsersApi.md#delete_auth) | **DELETE** /api/v1/{tenant}/users/{id}/auths/{uid} | Delete an Auth for a user
[**delete_auth_with_resource_tenantas_super_admin**](UsersApi.md#delete_auth_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/auths/{uid} | Delete an Auth for a user
[**delete_authas_super_admin**](UsersApi.md#delete_authas_super_admin) | **DELETE** /api/v1/tenants/users/{id}/auths/{uid} | Delete an Auth for a user
[**delete_refresh_token**](UsersApi.md#delete_refresh_token) | **DELETE** /api/v1/{tenant}/users/{id}/refresh-token | Delete a user refresh token
[**delete_refresh_token_with_resource_tenantas_super_admin**](UsersApi.md#delete_refresh_token_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/refresh-token | Delete a user refresh token
[**delete_refresh_tokenas_super_admin**](UsersApi.md#delete_refresh_tokenas_super_admin) | **DELETE** /api/v1/tenants/users/{id}/refresh-token | Delete a user refresh token
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/v1/{tenant}/users/{id} | Delete a user
[**delete_user_with_resource_tenantas_super_admin**](UsersApi.md#delete_user_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id} | Delete a user
[**delete_useras_super_admin**](UsersApi.md#delete_useras_super_admin) | **DELETE** /api/v1/tenants/users/{id} | Delete a user
[**find_all_for_all_tenants**](UsersApi.md#find_all_for_all_tenants) | **GET** /api/v1/tenants/users/instance | Get all users in the instance across all tenantd
[**find_all_for_all_tenants_with_resource_tenant**](UsersApi.md#find_all_for_all_tenants_with_resource_tenant) | **GET** /api/v1/tenants/{resourceTenant}/users/instance | Get all users in the instance across all tenantd
[**get_user**](UsersApi.md#get_user) | **GET** /api/v1/{tenant}/users/{id} | Get a user
[**get_user_with_resource_tenantas_super_admin**](UsersApi.md#get_user_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/users/{id} | Get a user
[**get_useras_super_admin**](UsersApi.md#get_useras_super_admin) | **GET** /api/v1/tenants/users/{id} | Get a user
[**impersonate**](UsersApi.md#impersonate) | **POST** /api/v1/tenants/users/{id}/impersonate | Impersonate a user
[**impersonate_with_resource_tenant**](UsersApi.md#impersonate_with_resource_tenant) | **POST** /api/v1/tenants/{resourceTenant}/users/{id}/impersonate | Impersonate a user
[**list_api_tokens**](UsersApi.md#list_api_tokens) | **GET** /api/v1/{tenant}/users/{id}/api-tokens | List all API Tokens for specific user
[**list_api_tokens_with_resource_tenantas_super_admin**](UsersApi.md#list_api_tokens_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens | List all API Tokens for specific user
[**list_api_tokensas_super_admin**](UsersApi.md#list_api_tokensas_super_admin) | **GET** /api/v1/tenants/users/{id}/api-tokens | List all API Tokens for specific user
[**search_users**](UsersApi.md#search_users) | **GET** /api/v1/{tenant}/users/search | Search for users
[**search_users_with_resource_tenantas_super_admin**](UsersApi.md#search_users_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/users/search | Search for users
[**search_usersas_super_admin**](UsersApi.md#search_usersas_super_admin) | **GET** /api/v1/tenants/users/search | Search for users
[**set_super_admin**](UsersApi.md#set_super_admin) | **PUT** /api/v1/tenants/users/{id}/set-superadmin | Update a user service account
[**set_super_admin_with_resource_tenant**](UsersApi.md#set_super_admin_with_resource_tenant) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id}/set-superadmin | Update a user service account
[**update_current_user_password**](UsersApi.md#update_current_user_password) | **PUT** /api/v1/me/password | Update login password for the current user.
[**update_current_user_password_with_tenant**](UsersApi.md#update_current_user_password_with_tenant) | **PUT** /api/v1/{tenant}/me/password | Update login password for the current user.
[**update_service_account**](UsersApi.md#update_service_account) | **PUT** /api/v1/{tenant}/users/service-accounts/{id} | Update a user service account
[**update_service_account_with_resource_tenantas_super_admin**](UsersApi.md#update_service_account_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/users/service-accounts/{id} | Update a user service account
[**update_service_accountas_super_admin**](UsersApi.md#update_service_accountas_super_admin) | **PUT** /api/v1/tenants/users/service-accounts/{id} | Update a user service account
[**update_user**](UsersApi.md#update_user) | **PUT** /api/v1/{tenant}/users/{id} | Update a standard user
[**update_user_with_resource_tenantas_super_admin**](UsersApi.md#update_user_with_resource_tenantas_super_admin) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id} | Update a standard user
[**update_useras_super_admin**](UsersApi.md#update_useras_super_admin) | **PUT** /api/v1/tenants/users/{id} | Update a standard user


# **autocomplete_users**
> List[ApiUser] autocomplete_users(tenant, abstract_user_controller_user_api_autocomplete)

List users for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_user_api_autocomplete import AbstractUserControllerUserApiAutocomplete
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
    api_instance = kestra_api_client.UsersApi(api_client)
    tenant = 'tenant_example' # str | 
    abstract_user_controller_user_api_autocomplete = kestra_api_client.AbstractUserControllerUserApiAutocomplete() # AbstractUserControllerUserApiAutocomplete | Autocomplete request

    try:
        # List users for autocomplete
        api_response = api_instance.autocomplete_users(tenant, abstract_user_controller_user_api_autocomplete)
        print("The response of UsersApi->autocomplete_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->autocomplete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **abstract_user_controller_user_api_autocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[ApiUser]**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteUsers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_users_with_resource_tenantas_super_admin**
> List[ApiUser] autocomplete_users_with_resource_tenantas_super_admin(resource_tenant, abstract_user_controller_user_api_autocomplete)

List users for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_user_api_autocomplete import AbstractUserControllerUserApiAutocomplete
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
    api_instance = kestra_api_client.UsersApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    abstract_user_controller_user_api_autocomplete = kestra_api_client.AbstractUserControllerUserApiAutocomplete() # AbstractUserControllerUserApiAutocomplete | Autocomplete request

    try:
        # List users for autocomplete
        api_response = api_instance.autocomplete_users_with_resource_tenantas_super_admin(resource_tenant, abstract_user_controller_user_api_autocomplete)
        print("The response of UsersApi->autocomplete_users_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->autocomplete_users_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **abstract_user_controller_user_api_autocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[ApiUser]**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteUsersWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_usersas_super_admin**
> List[ApiUser] autocomplete_usersas_super_admin(abstract_user_controller_user_api_autocomplete)

List users for autocomplete

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_user_api_autocomplete import AbstractUserControllerUserApiAutocomplete
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
    api_instance = kestra_api_client.UsersApi(api_client)
    abstract_user_controller_user_api_autocomplete = kestra_api_client.AbstractUserControllerUserApiAutocomplete() # AbstractUserControllerUserApiAutocomplete | Autocomplete request

    try:
        # List users for autocomplete
        api_response = api_instance.autocomplete_usersas_super_admin(abstract_user_controller_user_api_autocomplete)
        print("The response of UsersApi->autocomplete_usersas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->autocomplete_usersas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abstract_user_controller_user_api_autocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | 

### Return type

[**List[ApiUser]**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | autocompleteUsersasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_tokens_for_user**
> object create_api_tokens_for_user(id, tenant, create_api_token_request)

Create new API Token for a specific user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.create_api_token_request import CreateApiTokenRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 
    create_api_token_request = kestra_api_client.CreateApiTokenRequest() # CreateApiTokenRequest | The create api-token request

    try:
        # Create new API Token for a specific user
        api_response = api_instance.create_api_tokens_for_user(id, tenant, create_api_token_request)
        print("The response of UsersApi->create_api_tokens_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_api_tokens_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **tenant** | **str**|  | 
 **create_api_token_request** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createApiTokensForUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_tokens_for_user_with_resource_tenantas_super_admin**
> object create_api_tokens_for_user_with_resource_tenantas_super_admin(id, resource_tenant, create_api_token_request)

Create new API Token for a specific user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.create_api_token_request import CreateApiTokenRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 
    create_api_token_request = kestra_api_client.CreateApiTokenRequest() # CreateApiTokenRequest | The create api-token request

    try:
        # Create new API Token for a specific user
        api_response = api_instance.create_api_tokens_for_user_with_resource_tenantas_super_admin(id, resource_tenant, create_api_token_request)
        print("The response of UsersApi->create_api_tokens_for_user_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_api_tokens_for_user_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 
 **create_api_token_request** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createApiTokensForUserWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_tokens_for_useras_super_admin**
> object create_api_tokens_for_useras_super_admin(id, create_api_token_request)

Create new API Token for a specific user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.create_api_token_request import CreateApiTokenRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    create_api_token_request = kestra_api_client.CreateApiTokenRequest() # CreateApiTokenRequest | The create api-token request

    try:
        # Create new API Token for a specific user
        api_response = api_instance.create_api_tokens_for_useras_super_admin(id, create_api_token_request)
        print("The response of UsersApi->create_api_tokens_for_useras_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_api_tokens_for_useras_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **create_api_token_request** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createApiTokensForUserasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> ApiServiceAccount create_service_account(tenant, api_service_account)

Create a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    tenant = 'tenant_example' # str | 
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The service account

    try:
        # Create a user service account
        api_response = api_instance.create_service_account(tenant, api_service_account)
        print("The response of UsersApi->create_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createServiceAccount 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account_with_resource_tenantas_super_admin**
> ApiServiceAccount create_service_account_with_resource_tenantas_super_admin(resource_tenant, api_service_account)

Create a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The service account

    try:
        # Create a user service account
        api_response = api_instance.create_service_account_with_resource_tenantas_super_admin(resource_tenant, api_service_account)
        print("The response of UsersApi->create_service_account_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_service_account_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createServiceAccountWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_accountas_super_admin**
> ApiServiceAccount create_service_accountas_super_admin(api_service_account)

Create a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The service account

    try:
        # Create a user service account
        api_response = api_instance.create_service_accountas_super_admin(api_service_account)
        print("The response of UsersApi->create_service_accountas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_service_accountas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createServiceAccountasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> ApiUser create_user(tenant, api_user)

Create a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    tenant = 'tenant_example' # str | 
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Create a standard user
        api_response = api_instance.create_user(tenant, api_user)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_basic_auth**
> ApiUser create_user_basic_auth(id, tenant, abstract_user_controller_password_request)

Create a basic auth password for a standard user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_password_request import AbstractUserControllerPasswordRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 
    abstract_user_controller_password_request = kestra_api_client.AbstractUserControllerPasswordRequest() # AbstractUserControllerPasswordRequest | The password

    try:
        # Create a basic auth password for a standard user
        api_response = api_instance.create_user_basic_auth(id, tenant, abstract_user_controller_password_request)
        print("The response of UsersApi->create_user_basic_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_basic_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **tenant** | **str**|  | 
 **abstract_user_controller_password_request** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUserBasicAuth 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_basic_auth_with_resource_tenantas_super_admin**
> ApiUser create_user_basic_auth_with_resource_tenantas_super_admin(id, resource_tenant, abstract_user_controller_password_request)

Create a basic auth password for a standard user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_password_request import AbstractUserControllerPasswordRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 
    abstract_user_controller_password_request = kestra_api_client.AbstractUserControllerPasswordRequest() # AbstractUserControllerPasswordRequest | The password

    try:
        # Create a basic auth password for a standard user
        api_response = api_instance.create_user_basic_auth_with_resource_tenantas_super_admin(id, resource_tenant, abstract_user_controller_password_request)
        print("The response of UsersApi->create_user_basic_auth_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_basic_auth_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 
 **abstract_user_controller_password_request** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUserBasicAuthWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_basic_authas_super_admin**
> ApiUser create_user_basic_authas_super_admin(id, abstract_user_controller_password_request)

Create a basic auth password for a standard user

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.abstract_user_controller_password_request import AbstractUserControllerPasswordRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    abstract_user_controller_password_request = kestra_api_client.AbstractUserControllerPasswordRequest() # AbstractUserControllerPasswordRequest | The password

    try:
        # Create a basic auth password for a standard user
        api_response = api_instance.create_user_basic_authas_super_admin(id, abstract_user_controller_password_request)
        print("The response of UsersApi->create_user_basic_authas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_basic_authas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **abstract_user_controller_password_request** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUserBasicAuthasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_with_resource_tenantas_super_admin**
> ApiUser create_user_with_resource_tenantas_super_admin(resource_tenant, api_user)

Create a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Create a standard user
        api_response = api_instance.create_user_with_resource_tenantas_super_admin(resource_tenant, api_user)
        print("The response of UsersApi->create_user_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUserWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_useras_super_admin**
> ApiUser create_useras_super_admin(api_user)

Create a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Create a standard user
        api_response = api_instance.create_useras_super_admin(api_user)
        print("The response of UsersApi->create_useras_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_useras_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createUserasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token**
> object delete_api_token(id, token_id, tenant)

Delete an API Token for specific user and token id

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    token_id = 'token_id_example' # str | The token id
    tenant = 'tenant_example' # str | 

    try:
        # Delete an API Token for specific user and token id
        api_response = api_instance.delete_api_token(id, token_id, tenant)
        print("The response of UsersApi->delete_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **token_id** | **str**| The token id | 
 **tenant** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteApiToken 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token_with_resource_tenantas_super_admin**
> object delete_api_token_with_resource_tenantas_super_admin(id, token_id, resource_tenant)

Delete an API Token for specific user and token id

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    token_id = 'token_id_example' # str | The token id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete an API Token for specific user and token id
        api_response = api_instance.delete_api_token_with_resource_tenantas_super_admin(id, token_id, resource_tenant)
        print("The response of UsersApi->delete_api_token_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_api_token_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **token_id** | **str**| The token id | 
 **resource_tenant** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteApiTokenWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_tokenas_super_admin**
> object delete_api_tokenas_super_admin(id, token_id)

Delete an API Token for specific user and token id

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    token_id = 'token_id_example' # str | The token id

    try:
        # Delete an API Token for specific user and token id
        api_response = api_instance.delete_api_tokenas_super_admin(id, token_id)
        print("The response of UsersApi->delete_api_tokenas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_api_tokenas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **token_id** | **str**| The token id | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteApiTokenasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth**
> ApiUser delete_auth(id, uid, tenant)

Delete an Auth for a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    uid = 'uid_example' # str | The auth id
    tenant = 'tenant_example' # str | 

    try:
        # Delete an Auth for a user
        api_response = api_instance.delete_auth(id, uid, tenant)
        print("The response of UsersApi->delete_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **uid** | **str**| The auth id | 
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
**404** | On user not found |  -  |
**200** | deleteAuth 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_with_resource_tenantas_super_admin**
> ApiUser delete_auth_with_resource_tenantas_super_admin(id, uid, resource_tenant)

Delete an Auth for a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    uid = 'uid_example' # str | The auth id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete an Auth for a user
        api_response = api_instance.delete_auth_with_resource_tenantas_super_admin(id, uid, resource_tenant)
        print("The response of UsersApi->delete_auth_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_auth_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **uid** | **str**| The auth id | 
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
**404** | On user not found |  -  |
**200** | deleteAuthWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authas_super_admin**
> ApiUser delete_authas_super_admin(id, uid)

Delete an Auth for a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    uid = 'uid_example' # str | The auth id

    try:
        # Delete an Auth for a user
        api_response = api_instance.delete_authas_super_admin(id, uid)
        print("The response of UsersApi->delete_authas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_authas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **uid** | **str**| The auth id | 

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
**404** | On user not found |  -  |
**200** | deleteAuthasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_refresh_token**
> ApiUser delete_refresh_token(id, tenant)

Delete a user refresh token

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # Delete a user refresh token
        api_response = api_instance.delete_refresh_token(id, tenant)
        print("The response of UsersApi->delete_refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**200** | deleteRefreshToken 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_refresh_token_with_resource_tenantas_super_admin**
> ApiUser delete_refresh_token_with_resource_tenantas_super_admin(id, resource_tenant)

Delete a user refresh token

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete a user refresh token
        api_response = api_instance.delete_refresh_token_with_resource_tenantas_super_admin(id, resource_tenant)
        print("The response of UsersApi->delete_refresh_token_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_refresh_token_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**200** | deleteRefreshTokenWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_refresh_tokenas_super_admin**
> ApiUser delete_refresh_tokenas_super_admin(id)

Delete a user refresh token

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id

    try:
        # Delete a user refresh token
        api_response = api_instance.delete_refresh_tokenas_super_admin(id)
        print("The response of UsersApi->delete_refresh_tokenas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_refresh_tokenas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 

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
**200** | deleteRefreshTokenasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id, tenant)

Delete a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # Delete a user
        api_instance.delete_user(id, tenant)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**404** | On user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_with_resource_tenantas_super_admin**
> delete_user_with_resource_tenantas_super_admin(id, resource_tenant)

Delete a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete a user
        api_instance.delete_user_with_resource_tenantas_super_admin(id, resource_tenant)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**404** | On user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_useras_super_admin**
> delete_useras_super_admin(id)

Delete a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id

    try:
        # Delete a user
        api_instance.delete_useras_super_admin(id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_useras_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 

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
**404** | On user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_for_all_tenants**
> PagedResultsApiUser find_all_for_all_tenants(page, size, sort=sort, q=q, type=type)

Get all users in the instance across all tenantd

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
    api_instance = kestra_api_client.UsersApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    q = 'q_example' # str | A string filter (optional)
    type = kestra_api_client.UserType() # UserType | The type of user (optional)

    try:
        # Get all users in the instance across all tenantd
        api_response = api_instance.find_all_for_all_tenants(page, size, sort=sort, q=q, type=type)
        print("The response of UsersApi->find_all_for_all_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_all_for_all_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **q** | **str**| A string filter | [optional] 
 **type** | [**UserType**](.md)| The type of user | [optional] 

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
**200** | findAllForAllTenants 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_for_all_tenants_with_resource_tenant**
> PagedResultsApiUser find_all_for_all_tenants_with_resource_tenant(page, size, resource_tenant, sort=sort, q=q, type=type)

Get all users in the instance across all tenantd

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
    api_instance = kestra_api_client.UsersApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    q = 'q_example' # str | A string filter (optional)
    type = kestra_api_client.UserType() # UserType | The type of user (optional)

    try:
        # Get all users in the instance across all tenantd
        api_response = api_instance.find_all_for_all_tenants_with_resource_tenant(page, size, resource_tenant, sort=sort, q=q, type=type)
        print("The response of UsersApi->find_all_for_all_tenants_with_resource_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->find_all_for_all_tenants_with_resource_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **q** | **str**| A string filter | [optional] 
 **type** | [**UserType**](.md)| The type of user | [optional] 

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
**200** | findAllForAllTenantsWithResourceTenant 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ApiUser get_user(id, tenant)

Get a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # Get a user
        api_response = api_instance.get_user(id, tenant)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**404** | On user not found |  -  |
**200** | getUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_with_resource_tenantas_super_admin**
> ApiUser get_user_with_resource_tenantas_super_admin(id, resource_tenant)

Get a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Get a user
        api_response = api_instance.get_user_with_resource_tenantas_super_admin(id, resource_tenant)
        print("The response of UsersApi->get_user_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
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
**404** | On user not found |  -  |
**200** | getUserWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_useras_super_admin**
> ApiUser get_useras_super_admin(id)

Get a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id

    try:
        # Get a user
        api_response = api_instance.get_useras_super_admin(id)
        print("The response of UsersApi->get_useras_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_useras_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 

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
**404** | On user not found |  -  |
**200** | getUserasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonate**
> object impersonate(id)

Impersonate a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id

    try:
        # Impersonate a user
        api_response = api_instance.impersonate(id)
        print("The response of UsersApi->impersonate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->impersonate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | impersonate 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impersonate_with_resource_tenant**
> object impersonate_with_resource_tenant(resource_tenant, id)

Impersonate a user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    id = 'id_example' # str | The user id

    try:
        # Impersonate a user
        api_response = api_instance.impersonate_with_resource_tenant(resource_tenant, id)
        print("The response of UsersApi->impersonate_with_resource_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->impersonate_with_resource_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **id** | **str**| The user id | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | impersonateWithResourceTenant 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokens**
> object list_api_tokens(id, tenant)

List all API Tokens for specific user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 

    try:
        # List all API Tokens for specific user
        api_response = api_instance.list_api_tokens(id, tenant)
        print("The response of UsersApi->list_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_api_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **tenant** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listApiTokens 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokens_with_resource_tenantas_super_admin**
> object list_api_tokens_with_resource_tenantas_super_admin(id, resource_tenant)

List all API Tokens for specific user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # List all API Tokens for specific user
        api_response = api_instance.list_api_tokens_with_resource_tenantas_super_admin(id, resource_tenant)
        print("The response of UsersApi->list_api_tokens_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_api_tokens_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listApiTokensWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokensas_super_admin**
> object list_api_tokensas_super_admin(id)

List all API Tokens for specific user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id

    try:
        # List all API Tokens for specific user
        api_response = api_instance.list_api_tokensas_super_admin(id)
        print("The response of UsersApi->list_api_tokensas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_api_tokensas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listApiTokensasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> PagedResultsApiUser search_users(page, size, tenant, q=q, sort=sort, type=type)

Search for users

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
    api_instance = kestra_api_client.UsersApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    type = kestra_api_client.UserType() # UserType | The type of user (optional)

    try:
        # Search for users
        api_response = api_instance.search_users(page, size, tenant, q=q, sort=sort, type=type)
        print("The response of UsersApi->search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **type** | [**UserType**](.md)| The type of user | [optional] 

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
**200** | searchUsers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_with_resource_tenantas_super_admin**
> PagedResultsApiUser search_users_with_resource_tenantas_super_admin(page, size, resource_tenant, q=q, sort=sort, type=type)

Search for users

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
    api_instance = kestra_api_client.UsersApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    type = kestra_api_client.UserType() # UserType | The type of user (optional)

    try:
        # Search for users
        api_response = api_instance.search_users_with_resource_tenantas_super_admin(page, size, resource_tenant, q=q, sort=sort, type=type)
        print("The response of UsersApi->search_users_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->search_users_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **type** | [**UserType**](.md)| The type of user | [optional] 

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
**200** | searchUsersWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_usersas_super_admin**
> PagedResultsApiUser search_usersas_super_admin(page, size, q=q, sort=sort, type=type)

Search for users

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
    api_instance = kestra_api_client.UsersApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    q = 'q_example' # str | A string filter (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    type = kestra_api_client.UserType() # UserType | The type of user (optional)

    try:
        # Search for users
        api_response = api_instance.search_usersas_super_admin(page, size, q=q, sort=sort, type=type)
        print("The response of UsersApi->search_usersas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->search_usersas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **q** | **str**| A string filter | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **type** | [**UserType**](.md)| The type of user | [optional] 

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
**200** | searchUsersasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_super_admin**
> ApiUser set_super_admin(id, body)

Update a user service account

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    body = True # bool | 

    try:
        # Update a user service account
        api_response = api_instance.set_super_admin(id, body)
        print("The response of UsersApi->set_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->set_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **body** | **bool**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | setSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_super_admin_with_resource_tenant**
> ApiUser set_super_admin_with_resource_tenant(resource_tenant, id, body)

Update a user service account

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
    api_instance = kestra_api_client.UsersApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    id = 'id_example' # str | The user id
    body = True # bool | 

    try:
        # Update a user service account
        api_response = api_instance.set_super_admin_with_resource_tenant(resource_tenant, id, body)
        print("The response of UsersApi->set_super_admin_with_resource_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->set_super_admin_with_resource_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **id** | **str**| The user id | 
 **body** | **bool**|  | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | setSuperAdminWithResourceTenant 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_password**
> object update_current_user_password(me_controller_update_password_request)

Update login password for the current user.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.me_controller_update_password_request import MeControllerUpdatePasswordRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    me_controller_update_password_request = kestra_api_client.MeControllerUpdatePasswordRequest() # MeControllerUpdatePasswordRequest | 

    try:
        # Update login password for the current user.
        api_response = api_instance.update_current_user_password(me_controller_update_password_request)
        print("The response of UsersApi->update_current_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **me_controller_update_password_request** | [**MeControllerUpdatePasswordRequest**](MeControllerUpdatePasswordRequest.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateCurrentUserPassword 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_password_with_tenant**
> object update_current_user_password_with_tenant(tenant, me_controller_update_password_request)

Update login password for the current user.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.me_controller_update_password_request import MeControllerUpdatePasswordRequest
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
    api_instance = kestra_api_client.UsersApi(api_client)
    tenant = 'tenant_example' # str | 
    me_controller_update_password_request = kestra_api_client.MeControllerUpdatePasswordRequest() # MeControllerUpdatePasswordRequest | 

    try:
        # Update login password for the current user.
        api_response = api_instance.update_current_user_password_with_tenant(tenant, me_controller_update_password_request)
        print("The response of UsersApi->update_current_user_password_with_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_current_user_password_with_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **me_controller_update_password_request** | [**MeControllerUpdatePasswordRequest**](MeControllerUpdatePasswordRequest.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateCurrentUserPasswordWithTenant 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> ApiServiceAccount update_service_account(id, tenant, api_service_account)

Update a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The user

    try:
        # Update a user service account
        api_response = api_instance.update_service_account(id, tenant, api_service_account)
        print("The response of UsersApi->update_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **tenant** | **str**|  | 
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateServiceAccount 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account_with_resource_tenantas_super_admin**
> ApiServiceAccount update_service_account_with_resource_tenantas_super_admin(id, resource_tenant, api_service_account)

Update a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The user

    try:
        # Update a user service account
        api_response = api_instance.update_service_account_with_resource_tenantas_super_admin(id, resource_tenant, api_service_account)
        print("The response of UsersApi->update_service_account_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_service_account_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateServiceAccountWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_accountas_super_admin**
> ApiServiceAccount update_service_accountas_super_admin(id, api_service_account)

Update a user service account

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.api_service_account import ApiServiceAccount
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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    api_service_account = kestra_api_client.ApiServiceAccount() # ApiServiceAccount | The user

    try:
        # Update a user service account
        api_response = api_instance.update_service_accountas_super_admin(id, api_service_account)
        print("The response of UsersApi->update_service_accountas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_service_accountas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **api_service_account** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | 

### Return type

[**ApiServiceAccount**](ApiServiceAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateServiceAccountasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ApiUser update_user(id, tenant, api_user)

Update a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    tenant = 'tenant_example' # str | 
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Update a standard user
        api_response = api_instance.update_user(id, tenant, api_user)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **tenant** | **str**|  | 
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_with_resource_tenantas_super_admin**
> ApiUser update_user_with_resource_tenantas_super_admin(id, resource_tenant, api_user)

Update a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    resource_tenant = 'resource_tenant_example' # str | 
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Update a standard user
        api_response = api_instance.update_user_with_resource_tenantas_super_admin(id, resource_tenant, api_user)
        print("The response of UsersApi->update_user_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **resource_tenant** | **str**|  | 
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateUserWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_useras_super_admin**
> ApiUser update_useras_super_admin(id, api_user)

Update a standard user

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
    api_instance = kestra_api_client.UsersApi(api_client)
    id = 'id_example' # str | The user id
    api_user = kestra_api_client.ApiUser() # ApiUser | The user

    try:
        # Update a standard user
        api_response = api_instance.update_useras_super_admin(id, api_user)
        print("The response of UsersApi->update_useras_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_useras_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id | 
 **api_user** | [**ApiUser**](ApiUser.md)| The user | 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | On user not found |  -  |
**200** | updateUserasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

