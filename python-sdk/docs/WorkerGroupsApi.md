# kestra_api_client.WorkerGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker_group**](WorkerGroupsApi.md#create_worker_group) | **POST** /api/v1/cluster/workergroups | Create a new worker group.
[**delete_worker_group_by_id**](WorkerGroupsApi.md#delete_worker_group_by_id) | **DELETE** /api/v1/cluster/workergroups/{id} | Delete an existing worker group.
[**get_worker_group_by_id**](WorkerGroupsApi.md#get_worker_group_by_id) | **GET** /api/v1/cluster/workergroups/{id} | Get details about a worker group.
[**list_worker_groups**](WorkerGroupsApi.md#list_worker_groups) | **GET** /api/v1/cluster/workergroups | List all Worker Groups
[**update_worker_group_by_id**](WorkerGroupsApi.md#update_worker_group_by_id) | **PUT** /api/v1/cluster/workergroups/{id} | Update an existing worker group.


# **create_worker_group**
> ClusterControllerApiWorkerGroup create_worker_group(cluster_controller_api_create_or_update_worker_group_request)

Create a new worker group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_create_or_update_worker_group_request import ClusterControllerApiCreateOrUpdateWorkerGroupRequest
from kestra_api_client.models.cluster_controller_api_worker_group import ClusterControllerApiWorkerGroup
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
    api_instance = kestra_api_client.WorkerGroupsApi(api_client)
    cluster_controller_api_create_or_update_worker_group_request = kestra_api_client.ClusterControllerApiCreateOrUpdateWorkerGroupRequest() # ClusterControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition

    try:
        # Create a new worker group.
        api_response = api_instance.create_worker_group(cluster_controller_api_create_or_update_worker_group_request)
        print("The response of WorkerGroupsApi->create_worker_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkerGroupsApi->create_worker_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_controller_api_create_or_update_worker_group_request** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | 

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createWorkerGroup 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_worker_group_by_id**
> object delete_worker_group_by_id(id)

Delete an existing worker group.

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
    api_instance = kestra_api_client.WorkerGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an existing worker group.
        api_response = api_instance.delete_worker_group_by_id(id)
        print("The response of WorkerGroupsApi->delete_worker_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkerGroupsApi->delete_worker_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | deleteWorkerGroupById 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker_group_by_id**
> ClusterControllerApiWorkerGroupDetails get_worker_group_by_id(id)

Get details about a worker group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_worker_group_details import ClusterControllerApiWorkerGroupDetails
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
    api_instance = kestra_api_client.WorkerGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get details about a worker group.
        api_response = api_instance.get_worker_group_by_id(id)
        print("The response of WorkerGroupsApi->get_worker_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkerGroupsApi->get_worker_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusterControllerApiWorkerGroupDetails**](ClusterControllerApiWorkerGroupDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getWorkerGroupById 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_worker_groups**
> ClusterControllerApiWorkerGroupList list_worker_groups()

List all Worker Groups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_worker_group_list import ClusterControllerApiWorkerGroupList
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
    api_instance = kestra_api_client.WorkerGroupsApi(api_client)

    try:
        # List all Worker Groups
        api_response = api_instance.list_worker_groups()
        print("The response of WorkerGroupsApi->list_worker_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkerGroupsApi->list_worker_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterControllerApiWorkerGroupList**](ClusterControllerApiWorkerGroupList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listWorkerGroups 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_worker_group_by_id**
> ClusterControllerApiWorkerGroup update_worker_group_by_id(id, cluster_controller_api_create_or_update_worker_group_request)

Update an existing worker group.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_create_or_update_worker_group_request import ClusterControllerApiCreateOrUpdateWorkerGroupRequest
from kestra_api_client.models.cluster_controller_api_worker_group import ClusterControllerApiWorkerGroup
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
    api_instance = kestra_api_client.WorkerGroupsApi(api_client)
    id = 'id_example' # str | 
    cluster_controller_api_create_or_update_worker_group_request = kestra_api_client.ClusterControllerApiCreateOrUpdateWorkerGroupRequest() # ClusterControllerApiCreateOrUpdateWorkerGroupRequest | The worker group definition

    try:
        # Update an existing worker group.
        api_response = api_instance.update_worker_group_by_id(id, cluster_controller_api_create_or_update_worker_group_request)
        print("The response of WorkerGroupsApi->update_worker_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkerGroupsApi->update_worker_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cluster_controller_api_create_or_update_worker_group_request** | [**ClusterControllerApiCreateOrUpdateWorkerGroupRequest**](ClusterControllerApiCreateOrUpdateWorkerGroupRequest.md)| The worker group definition | 

### Return type

[**ClusterControllerApiWorkerGroup**](ClusterControllerApiWorkerGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateWorkerGroupById 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

