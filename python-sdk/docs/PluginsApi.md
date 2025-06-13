# kestra_api_client.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_input_types**](PluginsApi.md#get_all_input_types) | **GET** /api/v1/{tenant}/plugins/inputs | Get all types for an inputs
[**get_plugin_by_subgroups**](PluginsApi.md#get_plugin_by_subgroups) | **GET** /api/v1/{tenant}/plugins/groups/subgroups | Get plugins group by subgroups
[**get_plugin_documentation**](PluginsApi.md#get_plugin_documentation) | **GET** /api/v1/{tenant}/plugins/{cls} | Get plugin documentation
[**get_plugin_documentation_from_version**](PluginsApi.md#get_plugin_documentation_from_version) | **GET** /api/v1/{tenant}/plugins/{cls}/versions/{version} | Get plugin documentation
[**get_plugin_group_icons**](PluginsApi.md#get_plugin_group_icons) | **GET** /api/v1/{tenant}/plugins/icons/groups | Get plugins icons
[**get_plugin_icons**](PluginsApi.md#get_plugin_icons) | **GET** /api/v1/{tenant}/plugins/icons | Get plugins icons
[**get_plugin_versions**](PluginsApi.md#get_plugin_versions) | **GET** /api/v1/{tenant}/plugins/{cls}/versions | Get all versions for a plugin
[**get_schema_from_input_type**](PluginsApi.md#get_schema_from_input_type) | **GET** /api/v1/{tenant}/plugins/inputs/{type} | Get json schemas for an input type
[**get_schemas_from_type**](PluginsApi.md#get_schemas_from_type) | **GET** /api/v1/{tenant}/plugins/schemas/{type} | Get all json schemas for a type
[**get_versioned_plugin_details**](PluginsApi.md#get_versioned_plugin_details) | **GET** /api/v1/cluster/versioned-plugins/{groupId}/{artifactId} | Get details about a Kestra&#39;s plugin artifact.
[**get_versioned_plugin_details_from_version**](PluginsApi.md#get_versioned_plugin_details_from_version) | **GET** /api/v1/cluster/versioned-plugins/{groupId}/{artifactId}/{version} | Get details about a specific Kestra&#39;s plugin artifact version.
[**install_versioned_plugins**](PluginsApi.md#install_versioned_plugins) | **POST** /api/v1/cluster/versioned-plugins/install | Install a specific Kestra&#39;s plugin artifact
[**list_available_versioned_plugins**](PluginsApi.md#list_available_versioned_plugins) | **GET** /api/v1/cluster/versioned-plugins/available | Get the list of available Kestra&#39;s plugin artifact.
[**list_plugins**](PluginsApi.md#list_plugins) | **GET** /api/v1/{tenant}/plugins | Get list of plugins
[**list_versioned_plugin**](PluginsApi.md#list_versioned_plugin) | **GET** /api/v1/cluster/versioned-plugins | Get the list of installed Kestra&#39;s plugin artifact.
[**resolve_versioned_plugins**](PluginsApi.md#resolve_versioned_plugins) | **POST** /api/v1/cluster/versioned-plugins/resolve | Resolve a specific Kestra&#39;s plugin artifact
[**uninstall_versioned_plugins**](PluginsApi.md#uninstall_versioned_plugins) | **DELETE** /api/v1/cluster/versioned-plugins/uninstall | Uninstall Kestra&#39;s plugin artifacts
[**upload_versioned_plugins**](PluginsApi.md#upload_versioned_plugins) | **POST** /api/v1/cluster/versioned-plugins/upload | Upload a Kestra&#39;s plugin artifact


# **get_all_input_types**
> List[InputType] get_all_input_types(tenant)

Get all types for an inputs

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.input_type import InputType
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    tenant = 'tenant_example' # str | 

    try:
        # Get all types for an inputs
        api_response = api_instance.get_all_input_types(tenant)
        print("The response of PluginsApi->get_all_input_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_all_input_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 

### Return type

[**List[InputType]**](InputType.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getAllInputTypes 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_by_subgroups**
> List[Plugin] get_plugin_by_subgroups(include_deprecated, tenant)

Get plugins group by subgroups

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin import Plugin
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    include_deprecated = True # bool | Whether to include deprecated plugins (default to True)
    tenant = 'tenant_example' # str | 

    try:
        # Get plugins group by subgroups
        api_response = api_instance.get_plugin_by_subgroups(include_deprecated, tenant)
        print("The response of PluginsApi->get_plugin_by_subgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_by_subgroups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deprecated** | **bool**| Whether to include deprecated plugins | [default to True]
 **tenant** | **str**|  | 

### Return type

[**List[Plugin]**](Plugin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginBySubgroups 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_documentation**
> DocumentationWithSchema get_plugin_documentation(cls, all, tenant)

Get plugin documentation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.documentation_with_schema import DocumentationWithSchema
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cls = 'cls_example' # str | The plugin full class name
    all = False # bool | Include all the properties (default to False)
    tenant = 'tenant_example' # str | 

    try:
        # Get plugin documentation
        api_response = api_instance.get_plugin_documentation(cls, all, tenant)
        print("The response of PluginsApi->get_plugin_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cls** | **str**| The plugin full class name | 
 **all** | **bool**| Include all the properties | [default to False]
 **tenant** | **str**|  | 

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginDocumentation 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_documentation_from_version**
> DocumentationWithSchema get_plugin_documentation_from_version(cls, version, all, tenant)

Get plugin documentation

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.documentation_with_schema import DocumentationWithSchema
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cls = 'cls_example' # str | The plugin type
    version = 'version_example' # str | The plugin version
    all = False # bool | Include all the properties (default to False)
    tenant = 'tenant_example' # str | 

    try:
        # Get plugin documentation
        api_response = api_instance.get_plugin_documentation_from_version(cls, version, all, tenant)
        print("The response of PluginsApi->get_plugin_documentation_from_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_documentation_from_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cls** | **str**| The plugin type | 
 **version** | **str**| The plugin version | 
 **all** | **bool**| Include all the properties | [default to False]
 **tenant** | **str**|  | 

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginDocumentationFromVersion 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_group_icons**
> Dict[str, PluginIcon] get_plugin_group_icons(tenant)

Get plugins icons

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin_icon import PluginIcon
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    tenant = 'tenant_example' # str | 

    try:
        # Get plugins icons
        api_response = api_instance.get_plugin_group_icons(tenant)
        print("The response of PluginsApi->get_plugin_group_icons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_group_icons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 

### Return type

[**Dict[str, PluginIcon]**](PluginIcon.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginGroupIcons 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_icons**
> Dict[str, PluginIcon] get_plugin_icons(tenant)

Get plugins icons

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin_icon import PluginIcon
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    tenant = 'tenant_example' # str | 

    try:
        # Get plugins icons
        api_response = api_instance.get_plugin_icons(tenant)
        print("The response of PluginsApi->get_plugin_icons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_icons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 

### Return type

[**Dict[str, PluginIcon]**](PluginIcon.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginIcons 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_versions**
> PluginControllerApiPluginVersions get_plugin_versions(cls, tenant)

Get all versions for a plugin

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin_controller_api_plugin_versions import PluginControllerApiPluginVersions
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cls = 'cls_example' # str | The plugin type
    tenant = 'tenant_example' # str | 

    try:
        # Get all versions for a plugin
        api_response = api_instance.get_plugin_versions(cls, tenant)
        print("The response of PluginsApi->get_plugin_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cls** | **str**| The plugin type | 
 **tenant** | **str**|  | 

### Return type

[**PluginControllerApiPluginVersions**](PluginControllerApiPluginVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getPluginVersions 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_from_input_type**
> DocumentationWithSchema get_schema_from_input_type(type, tenant)

Get json schemas for an input type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.documentation_with_schema import DocumentationWithSchema
from kestra_api_client.models.type import Type
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    type = kestra_api_client.Type() # Type | The schema needed
    tenant = 'tenant_example' # str | 

    try:
        # Get json schemas for an input type
        api_response = api_instance.get_schema_from_input_type(type, tenant)
        print("The response of PluginsApi->get_schema_from_input_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_schema_from_input_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type**](.md)| The schema needed | 
 **tenant** | **str**|  | 

### Return type

[**DocumentationWithSchema**](DocumentationWithSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getSchemaFromInputType 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas_from_type**
> Dict[str, object] get_schemas_from_type(type, array_of, tenant)

Get all json schemas for a type

The schema will be output as [http://json-schema.org/draft-07/schema](Json Schema Draft 7)

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.schema_type import SchemaType
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    type = kestra_api_client.SchemaType() # SchemaType | The schema needed
    array_of = False # bool | If schema should be an array of requested type (default to False)
    tenant = 'tenant_example' # str | 

    try:
        # Get all json schemas for a type
        api_response = api_instance.get_schemas_from_type(type, array_of, tenant)
        print("The response of PluginsApi->get_schemas_from_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_schemas_from_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**SchemaType**](.md)| The schema needed | 
 **array_of** | **bool**| If schema should be an array of requested type | [default to False]
 **tenant** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getSchemasFromType 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versioned_plugin_details**
> ClusterControllerApiPluginVersions get_versioned_plugin_details(group_id, artifact_id)

Get details about a Kestra's plugin artifact.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_plugin_versions import ClusterControllerApiPluginVersions
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    group_id = 'group_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get details about a Kestra's plugin artifact.
        api_response = api_instance.get_versioned_plugin_details(group_id, artifact_id)
        print("The response of PluginsApi->get_versioned_plugin_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_versioned_plugin_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **artifact_id** | **str**|  | 

### Return type

[**ClusterControllerApiPluginVersions**](ClusterControllerApiPluginVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getVersionedPluginDetails 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versioned_plugin_details_from_version**
> ClusterControllerApiPluginVersionDetails get_versioned_plugin_details_from_version(group_id, artifact_id, version)

Get details about a specific Kestra's plugin artifact version.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_plugin_version_details import ClusterControllerApiPluginVersionDetails
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    group_id = 'group_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    version = 'version_example' # str | 

    try:
        # Get details about a specific Kestra's plugin artifact version.
        api_response = api_instance.get_versioned_plugin_details_from_version(group_id, artifact_id, version)
        print("The response of PluginsApi->get_versioned_plugin_details_from_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_versioned_plugin_details_from_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ClusterControllerApiPluginVersionDetails**](ClusterControllerApiPluginVersionDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getVersionedPluginDetailsFromVersion 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_versioned_plugins**
> ClusterControllerApiPluginArtifactListPluginArtifact install_versioned_plugins(cluster_controller_api_plugin_list_request)

Install a specific Kestra's plugin artifact

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_plugin_artifact_list_plugin_artifact import ClusterControllerApiPluginArtifactListPluginArtifact
from kestra_api_client.models.cluster_controller_api_plugin_list_request import ClusterControllerApiPluginListRequest
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cluster_controller_api_plugin_list_request = kestra_api_client.ClusterControllerApiPluginListRequest() # ClusterControllerApiPluginListRequest | List of plugins

    try:
        # Install a specific Kestra's plugin artifact
        api_response = api_instance.install_versioned_plugins(cluster_controller_api_plugin_list_request)
        print("The response of PluginsApi->install_versioned_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->install_versioned_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_controller_api_plugin_list_request** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | 

### Return type

[**ClusterControllerApiPluginArtifactListPluginArtifact**](ClusterControllerApiPluginArtifactListPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | installVersionedPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_versioned_plugins**
> object list_available_versioned_plugins()

Get the list of available Kestra's plugin artifact.

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
    api_instance = kestra_api_client.PluginsApi(api_client)

    try:
        # Get the list of available Kestra's plugin artifact.
        api_response = api_instance.list_available_versioned_plugins()
        print("The response of PluginsApi->list_available_versioned_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_available_versioned_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | listAvailableVersionedPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plugins**
> List[Plugin] list_plugins(tenant)

Get list of plugins

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin import Plugin
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    tenant = 'tenant_example' # str | 

    try:
        # Get list of plugins
        api_response = api_instance.list_plugins(tenant)
        print("The response of PluginsApi->list_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | **str**|  | 

### Return type

[**List[Plugin]**](Plugin.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versioned_plugin**
> PagedResultsClusterControllerApiPluginArtifact list_versioned_plugin(page, size, sort=sort, q=q)

Get the list of installed Kestra's plugin artifact.

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.paged_results_cluster_controller_api_plugin_artifact import PagedResultsClusterControllerApiPluginArtifact
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    page = 1 # int | The current page (default to 1)
    size = 10 # int | The current page size (default to 10)
    sort = ['sort_example'] # List[str] | The sort of current page (optional)
    q = 'q_example' # str | The query (optional)

    try:
        # Get the list of installed Kestra's plugin artifact.
        api_response = api_instance.list_versioned_plugin(page, size, sort=sort, q=q)
        print("The response of PluginsApi->list_versioned_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_versioned_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current page | [default to 1]
 **size** | **int**| The current page size | [default to 10]
 **sort** | [**List[str]**](str.md)| The sort of current page | [optional] 
 **q** | **str**| The query | [optional] 

### Return type

[**PagedResultsClusterControllerApiPluginArtifact**](PagedResultsClusterControllerApiPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | listVersionedPlugin 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_versioned_plugins**
> ClusterControllerApiPluginArtifactListPluginResolutionResult resolve_versioned_plugins(cluster_controller_api_plugin_list_request)

Resolve a specific Kestra's plugin artifact

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_plugin_artifact_list_plugin_resolution_result import ClusterControllerApiPluginArtifactListPluginResolutionResult
from kestra_api_client.models.cluster_controller_api_plugin_list_request import ClusterControllerApiPluginListRequest
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cluster_controller_api_plugin_list_request = kestra_api_client.ClusterControllerApiPluginListRequest() # ClusterControllerApiPluginListRequest | List of plugins

    try:
        # Resolve a specific Kestra's plugin artifact
        api_response = api_instance.resolve_versioned_plugins(cluster_controller_api_plugin_list_request)
        print("The response of PluginsApi->resolve_versioned_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->resolve_versioned_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_controller_api_plugin_list_request** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | 

### Return type

[**ClusterControllerApiPluginArtifactListPluginResolutionResult**](ClusterControllerApiPluginArtifactListPluginResolutionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resolveVersionedPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_versioned_plugins**
> ClusterControllerApiPluginArtifactListPluginArtifact uninstall_versioned_plugins(cluster_controller_api_plugin_list_request)

Uninstall Kestra's plugin artifacts

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.cluster_controller_api_plugin_artifact_list_plugin_artifact import ClusterControllerApiPluginArtifactListPluginArtifact
from kestra_api_client.models.cluster_controller_api_plugin_list_request import ClusterControllerApiPluginListRequest
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    cluster_controller_api_plugin_list_request = kestra_api_client.ClusterControllerApiPluginListRequest() # ClusterControllerApiPluginListRequest | List of plugins

    try:
        # Uninstall Kestra's plugin artifacts
        api_response = api_instance.uninstall_versioned_plugins(cluster_controller_api_plugin_list_request)
        print("The response of PluginsApi->uninstall_versioned_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->uninstall_versioned_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_controller_api_plugin_list_request** | [**ClusterControllerApiPluginListRequest**](ClusterControllerApiPluginListRequest.md)| List of plugins | 

### Return type

[**ClusterControllerApiPluginArtifactListPluginArtifact**](ClusterControllerApiPluginArtifactListPluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uninstallVersionedPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_versioned_plugins**
> PluginArtifact upload_versioned_plugins(file=file)

Upload a Kestra's plugin artifact

### Example

* Basic Authentication (basicAuth):
* Bearer (Bearer) Authentication (bearerAuth):

```python
import kestra_api_client
from kestra_api_client.models.plugin_artifact import PluginArtifact
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
    api_instance = kestra_api_client.PluginsApi(api_client)
    file = None # bytearray |  (optional)

    try:
        # Upload a Kestra's plugin artifact
        api_response = api_instance.upload_versioned_plugins(file=file)
        print("The response of PluginsApi->upload_versioned_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upload_versioned_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**PluginArtifact**](PluginArtifact.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uploadVersionedPlugins 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

