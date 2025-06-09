# GroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addUserToGroup**](GroupsApi.md#addUserToGroup) | **PUT** /api/v1/{tenant}/groups/{id}/members/{userId} | Add a group for a user |
| [**addUserToGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#addUserToGroupWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id}/members/{userId} | Add a group for a user |
| [**addUserToGroupasSuperAdmin**](GroupsApi.md#addUserToGroupasSuperAdmin) | **PUT** /api/v1/tenants/groups/{id}/members/{userId} | Add a group for a user |
| [**autocompleteGroups**](GroupsApi.md#autocompleteGroups) | **POST** /api/v1/{tenant}/groups/autocomplete | List groups for autocomplete |
| [**autocompleteGroupsWithResourceTenantasSuperAdmin**](GroupsApi.md#autocompleteGroupsWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/groups/autocomplete | List groups for autocomplete |
| [**autocompleteGroupsasSuperAdmin**](GroupsApi.md#autocompleteGroupsasSuperAdmin) | **POST** /api/v1/tenants/groups/autocomplete | List groups for autocomplete |
| [**createGroup**](GroupsApi.md#createGroup) | **POST** /api/v1/{tenant}/groups | Create a group |
| [**createGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#createGroupWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/groups | Create a group |
| [**createGroupasSuperAdmin**](GroupsApi.md#createGroupasSuperAdmin) | **POST** /api/v1/tenants/groups | Create a group |
| [**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /api/v1/{tenant}/groups/{id} | Delete a group |
| [**deleteGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#deleteGroupWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/groups/{id} | Delete a group |
| [**deleteGroupasSuperAdmin**](GroupsApi.md#deleteGroupasSuperAdmin) | **DELETE** /api/v1/tenants/groups/{id} | Delete a group |
| [**deleteUserFromGroup**](GroupsApi.md#deleteUserFromGroup) | **DELETE** /api/v1/{tenant}/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteUserFromGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#deleteUserFromGroupWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteUserFromGroupasSuperAdmin**](GroupsApi.md#deleteUserFromGroupasSuperAdmin) | **DELETE** /api/v1/tenants/groups/{id}/members/{userId} | Delete a group for a user |
| [**getGroup**](GroupsApi.md#getGroup) | **GET** /api/v1/{tenant}/groups/{id} | Get a group |
| [**getGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#getGroupWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/groups/{id} | Get a group |
| [**getGroupasSuperAdmin**](GroupsApi.md#getGroupasSuperAdmin) | **GET** /api/v1/tenants/groups/{id} | Get a group |
| [**listGroupIds**](GroupsApi.md#listGroupIds) | **POST** /api/v1/{tenant}/groups/ids | List groups by ids |
| [**listGroupIdsWithResourceTenantasSuperAdmin**](GroupsApi.md#listGroupIdsWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/groups/ids | List groups by ids |
| [**listGroupIdsasSuperAdmin**](GroupsApi.md#listGroupIdsasSuperAdmin) | **POST** /api/v1/tenants/groups/ids | List groups by ids |
| [**searchGroupMembers**](GroupsApi.md#searchGroupMembers) | **GET** /api/v1/{tenant}/groups/{id}/members | Search for users in a group |
| [**searchGroupMembersWithResourceTenantasSuperAdmin**](GroupsApi.md#searchGroupMembersWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/groups/{id}/members | Search for users in a group |
| [**searchGroupMembersasSuperAdmin**](GroupsApi.md#searchGroupMembersasSuperAdmin) | **GET** /api/v1/tenants/groups/{id}/members | Search for users in a group |
| [**searchGroups**](GroupsApi.md#searchGroups) | **GET** /api/v1/{tenant}/groups/search | Search for groups |
| [**searchGroupsWithResourceTenantasSuperAdmin**](GroupsApi.md#searchGroupsWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/groups/search | Search for groups |
| [**searchGroupsasSuperAdmin**](GroupsApi.md#searchGroupsasSuperAdmin) | **GET** /api/v1/tenants/groups/search | Search for groups |
| [**setUserMembershipForGroup**](GroupsApi.md#setUserMembershipForGroup) | **PUT** /api/v1/{tenant}/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group |
| [**setUserMembershipForGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#setUserMembershipForGroupWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group |
| [**setUserMembershipForGroupasSuperAdmin**](GroupsApi.md#setUserMembershipForGroupasSuperAdmin) | **PUT** /api/v1/tenants/groups/{id}/members/membership/{userId} | Set the membership type of a user in a group |
| [**updateGroup**](GroupsApi.md#updateGroup) | **PUT** /api/v1/{tenant}/groups/{id} | Update a group |
| [**updateGroupWithResourceTenantasSuperAdmin**](GroupsApi.md#updateGroupWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/groups/{id} | Update a group |
| [**updateGroupasSuperAdmin**](GroupsApi.md#updateGroupasSuperAdmin) | **PUT** /api/v1/tenants/groups/{id} | Update a group |



## addUserToGroup

> ApiUser addUserToGroup(id, userId, tenant)

Add a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.addUserToGroup(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addUserToGroup");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **tenant** | **String**|  | |

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
| **200** | addUserToGroup 200 response |  -  |


## addUserToGroupWithResourceTenantasSuperAdmin

> ApiUser addUserToGroupWithResourceTenantasSuperAdmin(id, userId, resourceTenant)

Add a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.addUserToGroupWithResourceTenantasSuperAdmin(id, userId, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addUserToGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **resourceTenant** | **String**|  | |

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
| **200** | addUserToGroupWithResourceTenantasSuperAdmin 200 response |  -  |


## addUserToGroupasSuperAdmin

> ApiUser addUserToGroupasSuperAdmin(id, userId)

Add a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.addUserToGroupasSuperAdmin(id, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addUserToGroupasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |

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
| **200** | addUserToGroupasSuperAdmin 200 response |  -  |


## autocompleteGroups

> List&lt;Group&gt; autocompleteGroups(tenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Group> result = apiInstance.autocompleteGroups(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocompleteGroups");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteGroups 200 response |  -  |


## autocompleteGroupsWithResourceTenantasSuperAdmin

> List&lt;Group&gt; autocompleteGroupsWithResourceTenantasSuperAdmin(resourceTenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Group> result = apiInstance.autocompleteGroupsWithResourceTenantasSuperAdmin(resourceTenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocompleteGroupsWithResourceTenantasSuperAdmin");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteGroupsWithResourceTenantasSuperAdmin 200 response |  -  |


## autocompleteGroupsasSuperAdmin

> List&lt;Group&gt; autocompleteGroupsasSuperAdmin(apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | Autocomplete request
        try {
            List<Group> result = apiInstance.autocompleteGroupsasSuperAdmin(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocompleteGroupsasSuperAdmin");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteGroupsasSuperAdmin 200 response |  -  |


## createGroup

> Group createGroup(tenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | The group
        try {
            Group result = apiInstance.createGroup(tenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#createGroup");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | |

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
| **200** | createGroup 200 response |  -  |


## createGroupWithResourceTenantasSuperAdmin

> Group createGroupWithResourceTenantasSuperAdmin(resourceTenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | The group
        try {
            Group result = apiInstance.createGroupWithResourceTenantasSuperAdmin(resourceTenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#createGroupWithResourceTenantasSuperAdmin");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | |

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
| **200** | createGroupWithResourceTenantasSuperAdmin 200 response |  -  |


## createGroupasSuperAdmin

> Group createGroupasSuperAdmin(abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | The group
        try {
            Group result = apiInstance.createGroupasSuperAdmin(abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#createGroupasSuperAdmin");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)| The group | |

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
| **200** | createGroupasSuperAdmin 200 response |  -  |


## deleteGroup

> deleteGroup(id, tenant)

Delete a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String |
        try {
            apiInstance.deleteGroup(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup");
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
| **id** | **String**| The group id | |
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


## deleteGroupWithResourceTenantasSuperAdmin

> deleteGroupWithResourceTenantasSuperAdmin(id, resourceTenant)

Delete a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            apiInstance.deleteGroupWithResourceTenantasSuperAdmin(id, resourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
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


## deleteGroupasSuperAdmin

> deleteGroupasSuperAdmin(id)

Delete a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            apiInstance.deleteGroupasSuperAdmin(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroupasSuperAdmin");
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
| **id** | **String**| The group id | |

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


## deleteUserFromGroup

> ApiUser deleteUserFromGroup(id, userId, tenant)

Delete a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteUserFromGroup(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteUserFromGroup");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **tenant** | **String**|  | |

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
| **200** | deleteUserFromGroup 200 response |  -  |


## deleteUserFromGroupWithResourceTenantasSuperAdmin

> ApiUser deleteUserFromGroupWithResourceTenantasSuperAdmin(id, userId, resourceTenant)

Delete a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteUserFromGroupWithResourceTenantasSuperAdmin(id, userId, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteUserFromGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **resourceTenant** | **String**|  | |

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
| **200** | deleteUserFromGroupWithResourceTenantasSuperAdmin 200 response |  -  |


## deleteUserFromGroupasSuperAdmin

> ApiUser deleteUserFromGroupasSuperAdmin(id, userId)

Delete a group for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.deleteUserFromGroupasSuperAdmin(id, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteUserFromGroupasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |

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
| **200** | deleteUserFromGroupasSuperAdmin 200 response |  -  |


## getGroup

> Group getGroup(id, tenant)

Get a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String |
        try {
            Group result = apiInstance.getGroup(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#getGroup");
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
| **id** | **String**| The group id | |
| **tenant** | **String**|  | |

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
| **200** | getGroup 200 response |  -  |


## getGroupWithResourceTenantasSuperAdmin

> Group getGroupWithResourceTenantasSuperAdmin(id, resourceTenant)

Get a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            Group result = apiInstance.getGroupWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#getGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **resourceTenant** | **String**|  | |

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
| **200** | getGroupWithResourceTenantasSuperAdmin 200 response |  -  |


## getGroupasSuperAdmin

> Group getGroupasSuperAdmin(id)

Get a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            Group result = apiInstance.getGroupasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#getGroupasSuperAdmin");
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
| **id** | **String**| The group id | |

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
| **200** | getGroupasSuperAdmin 200 response |  -  |


## listGroupIds

> List&lt;Group&gt; listGroupIds(tenant, apiIds)

List groups by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Group> result = apiInstance.listGroupIds(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#listGroupIds");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listGroupIds 200 response |  -  |


## listGroupIdsWithResourceTenantasSuperAdmin

> List&lt;Group&gt; listGroupIdsWithResourceTenantasSuperAdmin(resourceTenant, apiIds)

List groups by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Group> result = apiInstance.listGroupIdsWithResourceTenantasSuperAdmin(resourceTenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#listGroupIdsWithResourceTenantasSuperAdmin");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listGroupIdsWithResourceTenantasSuperAdmin 200 response |  -  |


## listGroupIdsasSuperAdmin

> List&lt;Group&gt; listGroupIdsasSuperAdmin(apiIds)

List groups by ids

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | The ids that must be present on results
        try {
            List<Group> result = apiInstance.listGroupIdsasSuperAdmin(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#listGroupIdsasSuperAdmin");
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

[**List&lt;Group&gt;**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listGroupIdsasSuperAdmin 200 response |  -  |


## searchGroupMembers

> PagedResultsApiUser searchGroupMembers(id, page, size, tenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.searchGroupMembers(id, page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroupMembers");
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
| **id** | **String**| The group id | |
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchGroupMembers 200 response |  -  |


## searchGroupMembersWithResourceTenantasSuperAdmin

> PagedResultsApiUser searchGroupMembersWithResourceTenantasSuperAdmin(id, page, size, resourceTenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.searchGroupMembersWithResourceTenantasSuperAdmin(id, page, size, resourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroupMembersWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **resourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchGroupMembersWithResourceTenantasSuperAdmin 200 response |  -  |


## searchGroupMembersasSuperAdmin

> PagedResultsApiUser searchGroupMembersasSuperAdmin(id, page, size, q, sort)

Search for users in a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.searchGroupMembersasSuperAdmin(id, page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroupMembersasSuperAdmin");
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
| **id** | **String**| The group id | |
| **page** | **Integer**| The current page | [default to 1] |
| **size** | **Integer**| The current page size | [default to 10] |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchGroupMembersasSuperAdmin 200 response |  -  |


## searchGroups

> PagedResultsGroup searchGroups(page, size, tenant, q, sort)

Search for groups

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.searchGroups(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroups");
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

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchGroups 200 response |  -  |


## searchGroupsWithResourceTenantasSuperAdmin

> PagedResultsGroup searchGroupsWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort)

Search for groups

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.searchGroupsWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroupsWithResourceTenantasSuperAdmin");
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

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchGroupsWithResourceTenantasSuperAdmin 200 response |  -  |


## searchGroupsasSuperAdmin

> PagedResultsGroup searchGroupsasSuperAdmin(page, size, q, sort)

Search for groups

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.searchGroupsasSuperAdmin(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#searchGroupsasSuperAdmin");
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

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | searchGroupsasSuperAdmin 200 response |  -  |


## setUserMembershipForGroup

> ApiUser setUserMembershipForGroup(id, userId, membership, tenant)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        AbstractUserGroupIdentifierMembership membership = AbstractUserGroupIdentifierMembership.fromValue("OWNER"); // AbstractUserGroupIdentifierMembership | The membership type
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.setUserMembershipForGroup(id, userId, membership, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#setUserMembershipForGroup");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | [enum: OWNER, MEMBER] |
| **tenant** | **String**|  | |

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
| **200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |


## setUserMembershipForGroupWithResourceTenantasSuperAdmin

> ApiUser setUserMembershipForGroupWithResourceTenantasSuperAdmin(id, userId, membership, resourceTenant)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        AbstractUserGroupIdentifierMembership membership = AbstractUserGroupIdentifierMembership.fromValue("OWNER"); // AbstractUserGroupIdentifierMembership | The membership type
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.setUserMembershipForGroupWithResourceTenantasSuperAdmin(id, userId, membership, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#setUserMembershipForGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | [enum: OWNER, MEMBER] |
| **resourceTenant** | **String**|  | |

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
| **200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |


## setUserMembershipForGroupasSuperAdmin

> ApiUser setUserMembershipForGroupasSuperAdmin(id, userId, membership)

Set the membership type of a user in a group

Sets the membership type of a user in a group. This method allows a group owner or a user with UPDATE permission to modify the membership of a user in a specific group.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        AbstractUserGroupIdentifierMembership membership = AbstractUserGroupIdentifierMembership.fromValue("OWNER"); // AbstractUserGroupIdentifierMembership | The membership type
        try {
            ApiUser result = apiInstance.setUserMembershipForGroupasSuperAdmin(id, userId, membership);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#setUserMembershipForGroupasSuperAdmin");
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
| **id** | **String**| The group id | |
| **userId** | **String**| The user id | |
| **membership** | [**AbstractUserGroupIdentifierMembership**](.md)| The membership type | [enum: OWNER, MEMBER] |

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
| **200** | An HttpResponse containing the ApiUser object with the updated membership information. |  -  |


## updateGroup

> Group updateGroup(id, tenant, group)

Update a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String |
        Group group = new Group(); // Group | The group
        try {
            Group result = apiInstance.updateGroup(id, tenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#updateGroup");
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
| **id** | **String**| The group id | |
| **tenant** | **String**|  | |
| **group** | [**Group**](Group.md)| The group | |

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
| **200** | updateGroup 200 response |  -  |


## updateGroupWithResourceTenantasSuperAdmin

> Group updateGroupWithResourceTenantasSuperAdmin(id, resourceTenant, group)

Update a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String resourceTenant = "resourceTenant_example"; // String |
        Group group = new Group(); // Group | The group
        try {
            Group result = apiInstance.updateGroupWithResourceTenantasSuperAdmin(id, resourceTenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#updateGroupWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The group id | |
| **resourceTenant** | **String**|  | |
| **group** | [**Group**](Group.md)| The group | |

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
| **200** | updateGroupWithResourceTenantasSuperAdmin 200 response |  -  |


## updateGroupasSuperAdmin

> Group updateGroupasSuperAdmin(id, group)

Update a group

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.GroupsApi;

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

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Group group = new Group(); // Group | The group
        try {
            Group result = apiInstance.updateGroupasSuperAdmin(id, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#updateGroupasSuperAdmin");
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
| **id** | **String**| The group id | |
| **group** | [**Group**](Group.md)| The group | |

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
| **200** | updateGroupasSuperAdmin 200 response |  -  |

