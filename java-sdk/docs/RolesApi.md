# RolesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocompleteRoles**](RolesApi.md#autocompleteRoles) | **POST** /api/v1/{tenant}/roles/autocomplete | List roles for autocomplete |
| [**autocompleteRolesWithResourceTenantasSuperAdmin**](RolesApi.md#autocompleteRolesWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/roles/autocomplete | List roles for autocomplete |
| [**autocompleteRolesasSuperAdmin**](RolesApi.md#autocompleteRolesasSuperAdmin) | **POST** /api/v1/tenants/roles/autocomplete | List roles for autocomplete |
| [**createRole**](RolesApi.md#createRole) | **POST** /api/v1/{tenant}/roles | Create a role |
| [**createRoleWithResourceTenantasSuperAdmin**](RolesApi.md#createRoleWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/roles | Create a role |
| [**createRoleasSuperAdmin**](RolesApi.md#createRoleasSuperAdmin) | **POST** /api/v1/tenants/roles | Create a role |
| [**deleteRole**](RolesApi.md#deleteRole) | **DELETE** /api/v1/{tenant}/roles/{id} | Delete a role |
| [**deleteRoleWithResourceTenantasSuperAdmin**](RolesApi.md#deleteRoleWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/roles/{id} | Delete a role |
| [**deleteRoleasSuperAdmin**](RolesApi.md#deleteRoleasSuperAdmin) | **DELETE** /api/v1/tenants/roles/{id} | Delete a role |
| [**getRole**](RolesApi.md#getRole) | **GET** /api/v1/{tenant}/roles/{id} | Get a role |
| [**getRoleWithResourceTenantasSuperAdmin**](RolesApi.md#getRoleWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/roles/{id} | Get a role |
| [**getRoleasSuperAdmin**](RolesApi.md#getRoleasSuperAdmin) | **GET** /api/v1/tenants/roles/{id} | Get a role |
| [**listRolesFromGivenIds**](RolesApi.md#listRolesFromGivenIds) | **POST** /api/v1/{tenant}/roles/ids |  |
| [**listRolesFromGivenIdsWithResourceTenantasSuperAdmin**](RolesApi.md#listRolesFromGivenIdsWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/roles/ids |  |
| [**listRolesFromGivenIdsasSuperAdmin**](RolesApi.md#listRolesFromGivenIdsasSuperAdmin) | **POST** /api/v1/tenants/roles/ids |  |
| [**searchRoles**](RolesApi.md#searchRoles) | **GET** /api/v1/{tenant}/roles/search | Search for roles |
| [**searchRolesWithResourceTenantasSuperAdmin**](RolesApi.md#searchRolesWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/roles/search | Search for roles |
| [**searchRolesasSuperAdmin**](RolesApi.md#searchRolesasSuperAdmin) | **GET** /api/v1/tenants/roles/search | Search for roles |
| [**updateRole**](RolesApi.md#updateRole) | **PUT** /api/v1/{tenant}/roles/{id} | Update a role |
| [**updateRoleWithResourceTenantasSuperAdmin**](RolesApi.md#updateRoleWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/roles/{id} | Update a role |
| [**updateRoleasSuperAdmin**](RolesApi.md#updateRoleasSuperAdmin) | **PUT** /api/v1/tenants/roles/{id} | Update a role |



## autocompleteRoles

> List&lt;Role&gt; autocompleteRoles(tenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Role> result = apiInstance.autocompleteRoles(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocompleteRoles");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **String**|  | |
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteRoles 200 response |  -  |


## autocompleteRolesWithResourceTenantasSuperAdmin

> List&lt;Role&gt; autocompleteRolesWithResourceTenantasSuperAdmin(resourceTenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Role> result = apiInstance.autocompleteRolesWithResourceTenantasSuperAdmin(resourceTenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocompleteRolesWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceTenant** | **String**|  | |
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteRolesWithResourceTenantasSuperAdmin 200 response |  -  |


## autocompleteRolesasSuperAdmin

> List&lt;Role&gt; autocompleteRolesasSuperAdmin(apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Role> result = apiInstance.autocompleteRolesasSuperAdmin(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocompleteRolesasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteRolesasSuperAdmin 200 response |  -  |


## createRole

> Role createRole(tenant, role)

Create a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String |
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.createRole(tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#createRole");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createRole 200 response |  -  |


## createRoleWithResourceTenantasSuperAdmin

> Role createRoleWithResourceTenantasSuperAdmin(resourceTenant, role)

Create a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.createRoleWithResourceTenantasSuperAdmin(resourceTenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#createRoleWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceTenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createRoleWithResourceTenantasSuperAdmin 200 response |  -  |


## createRoleasSuperAdmin

> Role createRoleasSuperAdmin(role)

Create a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.createRoleasSuperAdmin(role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#createRoleasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createRoleasSuperAdmin 200 response |  -  |


## deleteRole

> deleteRole(id, tenant)

Delete a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String |
        try {
            apiInstance.deleteRole(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#deleteRole");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **tenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## deleteRoleWithResourceTenantasSuperAdmin

> deleteRoleWithResourceTenantasSuperAdmin(id, resourceTenant)

Delete a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            apiInstance.deleteRoleWithResourceTenantasSuperAdmin(id, resourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#deleteRoleWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **resourceTenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## deleteRoleasSuperAdmin

> deleteRoleasSuperAdmin(id)

Delete a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            apiInstance.deleteRoleasSuperAdmin(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#deleteRoleasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## getRole

> Role getRole(id, tenant)

Get a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String |
        try {
            Role result = apiInstance.getRole(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#getRole");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **tenant** | **String**|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getRole 200 response |  -  |


## getRoleWithResourceTenantasSuperAdmin

> Role getRoleWithResourceTenantasSuperAdmin(id, resourceTenant)

Get a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            Role result = apiInstance.getRoleWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#getRoleWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **resourceTenant** | **String**|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getRoleWithResourceTenantasSuperAdmin 200 response |  -  |


## getRoleasSuperAdmin

> Role getRoleasSuperAdmin(id)

Get a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            Role result = apiInstance.getRoleasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#getRoleasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getRoleasSuperAdmin 200 response |  -  |


## listRolesFromGivenIds

> List&lt;Role&gt; listRolesFromGivenIds(tenant, apiIds)



List roles by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Role> result = apiInstance.listRolesFromGivenIds(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#listRolesFromGivenIds");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant** | **String**|  | |
| **apiIds** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listRolesFromGivenIds 200 response |  -  |


## listRolesFromGivenIdsWithResourceTenantasSuperAdmin

> List&lt;Role&gt; listRolesFromGivenIdsWithResourceTenantasSuperAdmin(resourceTenant, apiIds)



List roles by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Role> result = apiInstance.listRolesFromGivenIdsWithResourceTenantasSuperAdmin(resourceTenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#listRolesFromGivenIdsWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceTenant** | **String**|  | |
| **apiIds** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listRolesFromGivenIdsWithResourceTenantasSuperAdmin 200 response |  -  |


## listRolesFromGivenIdsasSuperAdmin

> List&lt;Role&gt; listRolesFromGivenIdsasSuperAdmin(apiIds)



List roles by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Role> result = apiInstance.listRolesFromGivenIdsasSuperAdmin(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#listRolesFromGivenIdsasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiIds** | [**ApiIds**](ApiIds.md)| The ids that must be present on results | |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listRolesFromGivenIdsasSuperAdmin 200 response |  -  |


## searchRoles

> PagedResultsRole searchRoles(page, size, tenant, q, sort)

Search for roles

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.searchRoles(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#searchRoles");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsRole**](PagedResultsRole.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchRoles 200 response |  -  |


## searchRolesWithResourceTenantasSuperAdmin

> PagedResultsRole searchRolesWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort)

Search for roles

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.searchRolesWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#searchRolesWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **resourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsRole**](PagedResultsRole.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchRolesWithResourceTenantasSuperAdmin 200 response |  -  |


## searchRolesasSuperAdmin

> PagedResultsRole searchRolesasSuperAdmin(page, size, q, sort)

Search for roles

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.searchRolesasSuperAdmin(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#searchRolesasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsRole**](PagedResultsRole.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchRolesasSuperAdmin 200 response |  -  |


## updateRole

> Role updateRole(id, tenant, role)

Update a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String |
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.updateRole(id, tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#updateRole");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **tenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateRole 200 response |  -  |


## updateRoleWithResourceTenantasSuperAdmin

> Role updateRoleWithResourceTenantasSuperAdmin(id, resourceTenant, role)

Update a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String resourceTenant = "resourceTenant_example"; // String |
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.updateRoleWithResourceTenantasSuperAdmin(id, resourceTenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#updateRoleWithResourceTenantasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **resourceTenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateRoleWithResourceTenantasSuperAdmin 200 response |  -  |


## updateRoleasSuperAdmin

> Role updateRoleasSuperAdmin(id, role)

Update a role

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        // Configure HTTP basic authorization: basicAuth
        HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
        basicAuth.setUsername("YOUR USERNAME");
        basicAuth.setPassword("YOUR PASSWORD");

        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        Role role = new Role(); // Role |
        try {
            Role result = apiInstance.updateRoleasSuperAdmin(id, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#updateRoleasSuperAdmin");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The role id | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateRoleasSuperAdmin 200 response |  -  |

