# kestrapy.SCIMUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scim_resource_by_id_users**](SCIMUsersApi.md#create_scim_resource_by_id_users) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | 
[**delete_users**](SCIMUsersApi.md#delete_users) | **DELETE** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | 
[**find_users**](SCIMUsersApi.md#find_users) | **POST** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/.search | 
[**get_scim_resource_by_id_users**](SCIMUsersApi.md#get_scim_resource_by_id_users) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | 
[**patch_users**](SCIMUsersApi.md#patch_users) | **PATCH** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | 
[**query_users**](SCIMUsersApi.md#query_users) | **GET** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users | 
[**update_users**](SCIMUsersApi.md#update_users) | **PUT** /api/v1/{tenant}/integrations/{integration}/scim/v2/Users/{id} | 


# **create_scim_resource_by_id_users**
> ScimResource create_scim_resource_by_id_users(integration, tenant, scim_user, attributes=attributes, excluded_attributes=excluded_attributes)

Create

### Example


```python
import kestrapy
from kestrapy.models.scim_resource import ScimResource
from kestrapy.models.scim_user import ScimUser
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    scim_user = kestrapy.ScimUser() # ScimUser | 
    attributes = 'attributes_example' # str |  (optional)
    excluded_attributes = 'excluded_attributes_example' # str |  (optional)

    try:
        api_response = api_instance.create_scim_resource_by_id_users(integration, tenant, scim_user, attributes=attributes, excluded_attributes=excluded_attributes)
        print("The response of SCIMUsersApi->create_scim_resource_by_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->create_scim_resource_by_id_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **scim_user** | [**ScimUser**](ScimUser.md)|  | 
 **attributes** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> delete_users(id, integration, tenant)

Delete from the backing store

### Example


```python
import kestrapy
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    id = 'id_example' # str | 
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 

    try:
        api_instance.delete_users(id, integration, tenant)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->delete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **integration** | **str**|  | 
 **tenant** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_users**
> ScimResource find_users(integration, tenant, search_request)

Search

### Example


```python
import kestrapy
from kestrapy.models.scim_resource import ScimResource
from kestrapy.models.search_request import SearchRequest
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    search_request = kestrapy.SearchRequest() # SearchRequest | 

    try:
        api_response = api_instance.find_users(integration, tenant, search_request)
        print("The response of SCIMUsersApi->find_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->find_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**200** | OK response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scim_resource_by_id_users**
> ScimResource get_scim_resource_by_id_users(id, integration, tenant, attributes=attributes, excluded_attributes=excluded_attributes)

Find by id

### Example


```python
import kestrapy
from kestrapy.models.scim_resource import ScimResource
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    id = 'id_example' # str | 
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    attributes = 'attributes_example' # str |  (optional)
    excluded_attributes = 'excluded_attributes_example' # str |  (optional)

    try:
        api_response = api_instance.get_scim_resource_by_id_users(id, integration, tenant, attributes=attributes, excluded_attributes=excluded_attributes)
        print("The response of SCIMUsersApi->get_scim_resource_by_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->get_scim_resource_by_id_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **attributes** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**200** | OK response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_users**
> patch_users(id, integration, tenant, patch_request, attributes=attributes, excluded_attributes=excluded_attributes)

Patch a portion of the backing store

### Example


```python
import kestrapy
from kestrapy.models.patch_request import PatchRequest
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    id = 'id_example' # str | 
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    patch_request = kestrapy.PatchRequest() # PatchRequest | 
    attributes = 'attributes_example' # str |  (optional)
    excluded_attributes = 'excluded_attributes_example' # str |  (optional)

    try:
        api_instance.patch_users(id, integration, tenant, patch_request, attributes=attributes, excluded_attributes=excluded_attributes)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->patch_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **patch_request** | [**PatchRequest**](PatchRequest.md)|  | 
 **attributes** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_users**
> ScimResource query_users(integration, tenant, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Find by a combination of query parameters

### Example


```python
import kestrapy
from kestrapy.models.scim_resource import ScimResource
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    attributes = 'attributes_example' # str |  (optional)
    excluded_attributes = 'excluded_attributes_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_order = kestrapy.SortOrder() # SortOrder |  (optional)
    start_index = 56 # int |  (optional)
    count = 56 # int |  (optional)

    try:
        api_response = api_instance.query_users(integration, tenant, attributes=attributes, excluded_attributes=excluded_attributes, filter=filter, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
        print("The response of SCIMUsersApi->query_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->query_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **attributes** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | [**SortOrder**](.md)|  | [optional] 
 **start_index** | **int**|  | [optional] 
 **count** | **int**|  | [optional] 

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**200** | OK response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> ScimResource update_users(id, integration, tenant, scim_resource, attributes=attributes, excluded_attributes=excluded_attributes)

Update

### Example


```python
import kestrapy
from kestrapy.models.scim_resource import ScimResource
from kestrapy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kestrapy.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kestrapy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kestrapy.SCIMUsersApi(api_client)
    id = 'id_example' # str | 
    integration = 'integration_example' # str | 
    tenant = 'tenant_example' # str | 
    scim_resource = kestrapy.ScimResource() # ScimResource | 
    attributes = 'attributes_example' # str |  (optional)
    excluded_attributes = 'excluded_attributes_example' # str |  (optional)

    try:
        api_response = api_instance.update_users(id, integration, tenant, scim_resource, attributes=attributes, excluded_attributes=excluded_attributes)
        print("The response of SCIMUsersApi->update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMUsersApi->update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **integration** | **str**|  | 
 **tenant** | **str**|  | 
 **scim_resource** | [**ScimResource**](ScimResource.md)|  | 
 **attributes** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 

### Return type

[**ScimResource**](ScimResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**200** | OK response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

