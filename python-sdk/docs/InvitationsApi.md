# kestra_api_client.InvitationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /api/v1/{tenant}/invitations | Create an invitation
[**create_invitation_with_resource_tenantas_super_admin**](InvitationsApi.md#create_invitation_with_resource_tenantas_super_admin) | **POST** /api/v1/tenants/{resourceTenant}/invitations | Create an invitation
[**create_invitationas_super_admin**](InvitationsApi.md#create_invitationas_super_admin) | **POST** /api/v1/tenants/invitations | Create an invitation
[**delete_invitation**](InvitationsApi.md#delete_invitation) | **DELETE** /api/v1/{tenant}/invitations/{id} | Delete an invitation
[**delete_invitation_with_resource_tenantas_super_admin**](InvitationsApi.md#delete_invitation_with_resource_tenantas_super_admin) | **DELETE** /api/v1/tenants/{resourceTenant}/invitations/{id} | Delete an invitation
[**delete_invitationas_super_admin**](InvitationsApi.md#delete_invitationas_super_admin) | **DELETE** /api/v1/tenants/invitations/{id} | Delete an invitation
[**find_all_invitations_for_current_user**](InvitationsApi.md#find_all_invitations_for_current_user) | **GET** /api/v1/me/invitations | Get all invitations for a given email
[**find_all_invitations_for_current_user_with_tenant**](InvitationsApi.md#find_all_invitations_for_current_user_with_tenant) | **GET** /api/v1/{tenant}/me/invitations | Get all invitations for a given email
[**get_invitation**](InvitationsApi.md#get_invitation) | **GET** /api/v1/{tenant}/invitations/{id} | Get an invitation
[**get_invitation_with_resource_tenantas_super_admin**](InvitationsApi.md#get_invitation_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/{id} | Get an invitation
[**get_invitationas_super_admin**](InvitationsApi.md#get_invitationas_super_admin) | **GET** /api/v1/tenants/invitations/{id} | Get an invitation
[**list_by_email**](InvitationsApi.md#list_by_email) | **GET** /api/v1/{tenant}/invitations/email/{email} | Get all invitations for a given email
[**list_by_email_with_resource_tenantas_super_admin**](InvitationsApi.md#list_by_email_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/email/{email} | Get all invitations for a given email
[**list_by_emailas_super_admin**](InvitationsApi.md#list_by_emailas_super_admin) | **GET** /api/v1/tenants/invitations/email/{email} | Get all invitations for a given email
[**search_invitations**](InvitationsApi.md#search_invitations) | **GET** /api/v1/{tenant}/invitations/search | Search for invitations
[**search_invitations_with_resource_tenantas_super_admin**](InvitationsApi.md#search_invitations_with_resource_tenantas_super_admin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/search | Search for invitations
[**search_invitationsas_super_admin**](InvitationsApi.md#search_invitationsas_super_admin) | **GET** /api/v1/tenants/invitations/search | Search for invitations


# **create_invitation**
> Invitation create_invitation(tenant, invitation)

Create an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    tenant = 'tenant_example' # str | 
    invitation = kestra_api_client.Invitation() # Invitation | Create a new invitation, send an email if the server-mail is enabled

    try:
        # Create an invitation
        api_response = api_instance.create_invitation(tenant, invitation)
        print("The response of InvitationsApi->create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 
 **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createInvitation 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation_with_resource_tenantas_super_admin**
> Invitation create_invitation_with_resource_tenantas_super_admin(resource_tenant, invitation)

Create an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    resource_tenant = 'resource_tenant_example' # str | 
    invitation = kestra_api_client.Invitation() # Invitation | Create a new invitation, send an email if the server-mail is enabled

    try:
        # Create an invitation
        api_response = api_instance.create_invitation_with_resource_tenantas_super_admin(resource_tenant, invitation)
        print("The response of InvitationsApi->create_invitation_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->create_invitation_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_tenant** | **str**|  | 
 **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createInvitationWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitationas_super_admin**
> Invitation create_invitationas_super_admin(invitation)

Create an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    invitation = kestra_api_client.Invitation() # Invitation | Create a new invitation, send an email if the server-mail is enabled

    try:
        # Create an invitation
        api_response = api_instance.create_invitationas_super_admin(invitation)
        print("The response of InvitationsApi->create_invitationas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->create_invitationas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createInvitationasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation**
> delete_invitation(id, tenant)

Delete an invitation

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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation
    tenant = 'tenant_example' # str | 

    try:
        # Delete an invitation
        api_instance.delete_invitation(id, tenant)
    except Exception as e:
        print("Exception when calling InvitationsApi->delete_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 
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
**200** | deleteInvitation 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation_with_resource_tenantas_super_admin**
> delete_invitation_with_resource_tenantas_super_admin(id, resource_tenant)

Delete an invitation

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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Delete an invitation
        api_instance.delete_invitation_with_resource_tenantas_super_admin(id, resource_tenant)
    except Exception as e:
        print("Exception when calling InvitationsApi->delete_invitation_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 
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
**200** | deleteInvitationWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitationas_super_admin**
> delete_invitationas_super_admin(id)

Delete an invitation

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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation

    try:
        # Delete an invitation
        api_instance.delete_invitationas_super_admin(id)
    except Exception as e:
        print("Exception when calling InvitationsApi->delete_invitationas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 

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
**200** | deleteInvitationasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_invitations_for_current_user**
> List[Invitation] find_all_invitations_for_current_user()

Get all invitations for a given email

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)

    try:
        # Get all invitations for a given email
        api_response = api_instance.find_all_invitations_for_current_user()
        print("The response of InvitationsApi->find_all_invitations_for_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->find_all_invitations_for_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | findAllInvitationsForCurrentUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_invitations_for_current_user_with_tenant**
> List[Invitation] find_all_invitations_for_current_user_with_tenant(tenant)

Get all invitations for a given email

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    tenant = 'tenant_example' # str | 

    try:
        # Get all invitations for a given email
        api_response = api_instance.find_all_invitations_for_current_user_with_tenant(tenant)
        print("The response of InvitationsApi->find_all_invitations_for_current_user_with_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->find_all_invitations_for_current_user_with_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | findAllInvitationsForCurrentUserWithTenant 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation**
> Invitation get_invitation(id, tenant)

Get an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation
    tenant = 'tenant_example' # str | 

    try:
        # Get an invitation
        api_response = api_instance.get_invitation(id, tenant)
        print("The response of InvitationsApi->get_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 
 **tenant** | **str**|  | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getInvitation 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_with_resource_tenantas_super_admin**
> Invitation get_invitation_with_resource_tenantas_super_admin(id, resource_tenant)

Get an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Get an invitation
        api_response = api_instance.get_invitation_with_resource_tenantas_super_admin(id, resource_tenant)
        print("The response of InvitationsApi->get_invitation_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_invitation_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 
 **resource_tenant** | **str**|  | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getInvitationWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitationas_super_admin**
> Invitation get_invitationas_super_admin(id)

Get an invitation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation

    try:
        # Get an invitation
        api_response = api_instance.get_invitationas_super_admin(id)
        print("The response of InvitationsApi->get_invitationas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_invitationas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getInvitationasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_email**
> List[Invitation] list_by_email(email, tenant)

Get all invitations for a given email

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    email = 'email_example' # str | The email address of the invited
    tenant = 'tenant_example' # str | 

    try:
        # Get all invitations for a given email
        api_response = api_instance.list_by_email(email, tenant)
        print("The response of InvitationsApi->list_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->list_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the invited | 
 **tenant** | **str**|  | 

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listByEmail 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_email_with_resource_tenantas_super_admin**
> List[Invitation] list_by_email_with_resource_tenantas_super_admin(email, resource_tenant)

Get all invitations for a given email

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    email = 'email_example' # str | The email address of the invited
    resource_tenant = 'resource_tenant_example' # str | 

    try:
        # Get all invitations for a given email
        api_response = api_instance.list_by_email_with_resource_tenantas_super_admin(email, resource_tenant)
        print("The response of InvitationsApi->list_by_email_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->list_by_email_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the invited | 
 **resource_tenant** | **str**|  | 

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listByEmailWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_emailas_super_admin**
> List[Invitation] list_by_emailas_super_admin(email)

Get all invitations for a given email

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.invitation import Invitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    email = 'email_example' # str | The email address of the invited

    try:
        # Get all invitations for a given email
        api_response = api_instance.list_by_emailas_super_admin(email)
        print("The response of InvitationsApi->list_by_emailas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->list_by_emailas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the invited | 

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listByEmailasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_invitations**
> PagedResultsInvitation search_invitations(page, size, tenant, email=email, status=status, sort=sort)

Search for invitations

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_invitation import PagedResultsInvitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    tenant = 'tenant_example' # str | 
    email = 'email_example' # str | The email address of the invited (optional)
    status = kestra_api_client.InvitationInvitationStatus() # InvitationInvitationStatus | The current status of the invitations (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for invitations
        api_response = api_instance.search_invitations(page, size, tenant, email=email, status=status, sort=sort)
        print("The response of InvitationsApi->search_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->search_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **tenant** | **str**|  | 
 **email** | **str**| The email address of the invited | [optional] 
 **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchInvitations 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_invitations_with_resource_tenantas_super_admin**
> PagedResultsInvitation search_invitations_with_resource_tenantas_super_admin(page, size, resource_tenant, email=email, status=status, sort=sort)

Search for invitations

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_invitation import PagedResultsInvitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    resource_tenant = 'resource_tenant_example' # str | 
    email = 'email_example' # str | The email address of the invited (optional)
    status = kestra_api_client.InvitationInvitationStatus() # InvitationInvitationStatus | The current status of the invitations (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for invitations
        api_response = api_instance.search_invitations_with_resource_tenantas_super_admin(page, size, resource_tenant, email=email, status=status, sort=sort)
        print("The response of InvitationsApi->search_invitations_with_resource_tenantas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->search_invitations_with_resource_tenantas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **resource_tenant** | **str**|  | 
 **email** | **str**| The email address of the invited | [optional] 
 **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchInvitationsWithResourceTenantasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_invitationsas_super_admin**
> PagedResultsInvitation search_invitationsas_super_admin(page, size, email=email, status=status, sort=sort)

Search for invitations

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_invitation import PagedResultsInvitation
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
    api_instance = kestra_api_client.InvitationsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    email = 'email_example' # str | The email address of the invited (optional)
    status = kestra_api_client.InvitationInvitationStatus() # InvitationInvitationStatus | The current status of the invitations (optional)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)

    try:
        # Search for invitations
        api_response = api_instance.search_invitationsas_super_admin(page, size, email=email, status=status, sort=sort)
        print("The response of InvitationsApi->search_invitationsas_super_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->search_invitationsas_super_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **email** | **str**| The email address of the invited | [optional] 
 **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] 
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | searchInvitationsasSuperAdmin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

