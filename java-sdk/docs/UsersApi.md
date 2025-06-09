# UsersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocompleteUsers**](UsersApi.md#autocompleteUsers) | **POST** /api/v1/{tenant}/users/autocomplete | List users for autocomplete |
| [**autocompleteUsersWithResourceTenantasSuperAdmin**](UsersApi.md#autocompleteUsersWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/users/autocomplete | List users for autocomplete |
| [**autocompleteUsersasSuperAdmin**](UsersApi.md#autocompleteUsersasSuperAdmin) | **POST** /api/v1/tenants/users/autocomplete | List users for autocomplete |
| [**createApiTokensForUser**](UsersApi.md#createApiTokensForUser) | **POST** /api/v1/{tenant}/users/{id}/api-tokens | Create new API Token for a specific user |
| [**createApiTokensForUserWithResourceTenantasSuperAdmin**](UsersApi.md#createApiTokensForUserWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens | Create new API Token for a specific user |
| [**createApiTokensForUserasSuperAdmin**](UsersApi.md#createApiTokensForUserasSuperAdmin) | **POST** /api/v1/tenants/users/{id}/api-tokens | Create new API Token for a specific user |
| [**createServiceAccount**](UsersApi.md#createServiceAccount) | **POST** /api/v1/{tenant}/users/service-accounts | Create a user service account |
| [**createServiceAccountWithResourceTenantasSuperAdmin**](UsersApi.md#createServiceAccountWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/users/service-accounts | Create a user service account |
| [**createServiceAccountasSuperAdmin**](UsersApi.md#createServiceAccountasSuperAdmin) | **POST** /api/v1/tenants/users/service-accounts | Create a user service account |
| [**createUser**](UsersApi.md#createUser) | **POST** /api/v1/{tenant}/users | Create a standard user |
| [**createUserBasicAuth**](UsersApi.md#createUserBasicAuth) | **PUT** /api/v1/{tenant}/users/{id}/password | Create a basic auth password for a standard user |
| [**createUserBasicAuthWithResourceTenantasSuperAdmin**](UsersApi.md#createUserBasicAuthWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id}/password | Create a basic auth password for a standard user |
| [**createUserBasicAuthasSuperAdmin**](UsersApi.md#createUserBasicAuthasSuperAdmin) | **PUT** /api/v1/tenants/users/{id}/password | Create a basic auth password for a standard user |
| [**createUserWithResourceTenantasSuperAdmin**](UsersApi.md#createUserWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/users | Create a standard user |
| [**createUserasSuperAdmin**](UsersApi.md#createUserasSuperAdmin) | **POST** /api/v1/tenants/users | Create a standard user |
| [**deleteApiToken**](UsersApi.md#deleteApiToken) | **DELETE** /api/v1/{tenant}/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id |
| [**deleteApiTokenWithResourceTenantasSuperAdmin**](UsersApi.md#deleteApiTokenWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id |
| [**deleteApiTokenasSuperAdmin**](UsersApi.md#deleteApiTokenasSuperAdmin) | **DELETE** /api/v1/tenants/users/{id}/api-tokens/{tokenId} | Delete an API Token for specific user and token id |
| [**deleteAuth**](UsersApi.md#deleteAuth) | **DELETE** /api/v1/{tenant}/users/{id}/auths/{uid} | Delete an Auth for a user |
| [**deleteAuthWithResourceTenantasSuperAdmin**](UsersApi.md#deleteAuthWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/auths/{uid} | Delete an Auth for a user |
| [**deleteAuthasSuperAdmin**](UsersApi.md#deleteAuthasSuperAdmin) | **DELETE** /api/v1/tenants/users/{id}/auths/{uid} | Delete an Auth for a user |
| [**deleteRefreshToken**](UsersApi.md#deleteRefreshToken) | **DELETE** /api/v1/{tenant}/users/{id}/refresh-token | Delete a user refresh token |
| [**deleteRefreshTokenWithResourceTenantasSuperAdmin**](UsersApi.md#deleteRefreshTokenWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id}/refresh-token | Delete a user refresh token |
| [**deleteRefreshTokenasSuperAdmin**](UsersApi.md#deleteRefreshTokenasSuperAdmin) | **DELETE** /api/v1/tenants/users/{id}/refresh-token | Delete a user refresh token |
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /api/v1/{tenant}/users/{id} | Delete a user |
| [**deleteUserWithResourceTenantasSuperAdmin**](UsersApi.md#deleteUserWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/users/{id} | Delete a user |
| [**deleteUserasSuperAdmin**](UsersApi.md#deleteUserasSuperAdmin) | **DELETE** /api/v1/tenants/users/{id} | Delete a user |
| [**findAllForAllTenants**](UsersApi.md#findAllForAllTenants) | **GET** /api/v1/tenants/users/instance | Get all users in the instance across all tenantd |
| [**findAllForAllTenantsWithResourceTenant**](UsersApi.md#findAllForAllTenantsWithResourceTenant) | **GET** /api/v1/tenants/{resourceTenant}/users/instance | Get all users in the instance across all tenantd |
| [**getUser**](UsersApi.md#getUser) | **GET** /api/v1/{tenant}/users/{id} | Get a user |
| [**getUserWithResourceTenantasSuperAdmin**](UsersApi.md#getUserWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/users/{id} | Get a user |
| [**getUserasSuperAdmin**](UsersApi.md#getUserasSuperAdmin) | **GET** /api/v1/tenants/users/{id} | Get a user |
| [**impersonate**](UsersApi.md#impersonate) | **POST** /api/v1/tenants/users/{id}/impersonate | Impersonate a user |
| [**impersonateWithResourceTenant**](UsersApi.md#impersonateWithResourceTenant) | **POST** /api/v1/tenants/{resourceTenant}/users/{id}/impersonate | Impersonate a user |
| [**listApiTokens**](UsersApi.md#listApiTokens) | **GET** /api/v1/{tenant}/users/{id}/api-tokens | List all API Tokens for specific user |
| [**listApiTokensWithResourceTenantasSuperAdmin**](UsersApi.md#listApiTokensWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/users/{id}/api-tokens | List all API Tokens for specific user |
| [**listApiTokensasSuperAdmin**](UsersApi.md#listApiTokensasSuperAdmin) | **GET** /api/v1/tenants/users/{id}/api-tokens | List all API Tokens for specific user |
| [**searchUsers**](UsersApi.md#searchUsers) | **GET** /api/v1/{tenant}/users/search | Search for users |
| [**searchUsersWithResourceTenantasSuperAdmin**](UsersApi.md#searchUsersWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/users/search | Search for users |
| [**searchUsersasSuperAdmin**](UsersApi.md#searchUsersasSuperAdmin) | **GET** /api/v1/tenants/users/search | Search for users |
| [**setSuperAdmin**](UsersApi.md#setSuperAdmin) | **PUT** /api/v1/tenants/users/{id}/set-superadmin | Update a user service account |
| [**setSuperAdminWithResourceTenant**](UsersApi.md#setSuperAdminWithResourceTenant) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id}/set-superadmin | Update a user service account |
| [**updateCurrentUserPassword**](UsersApi.md#updateCurrentUserPassword) | **PUT** /api/v1/{tenant}/me/password | Update login password for the current user. |
| [**updateServiceAccount**](UsersApi.md#updateServiceAccount) | **PUT** /api/v1/{tenant}/users/service-accounts/{id} | Update a user service account |
| [**updateServiceAccountWithResourceTenantasSuperAdmin**](UsersApi.md#updateServiceAccountWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/users/service-accounts/{id} | Update a user service account |
| [**updateServiceAccountasSuperAdmin**](UsersApi.md#updateServiceAccountasSuperAdmin) | **PUT** /api/v1/tenants/users/service-accounts/{id} | Update a user service account |
| [**updateUser**](UsersApi.md#updateUser) | **PUT** /api/v1/{tenant}/users/{id} | Update a standard user |
| [**updateUserWithResourceTenantasSuperAdmin**](UsersApi.md#updateUserWithResourceTenantasSuperAdmin) | **PUT** /api/v1/tenants/{resourceTenant}/users/{id} | Update a standard user |
| [**updateUserasSuperAdmin**](UsersApi.md#updateUserasSuperAdmin) | **PUT** /api/v1/tenants/users/{id} | Update a standard user |



## autocompleteUsers

> List&lt;ApiUser&gt; autocompleteUsers(tenant, abstractUserControllerUserApiAutocomplete)

List users for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String tenant = "tenant_example"; // String |
        AbstractUserControllerUserApiAutocomplete abstractUserControllerUserApiAutocomplete = new AbstractUserControllerUserApiAutocomplete(); // AbstractUserControllerUserApiAutocomplete | Autocomplete request
        try {
            List<ApiUser> result = apiInstance.autocompleteUsers(tenant, abstractUserControllerUserApiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#autocompleteUsers");
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
| **abstractUserControllerUserApiAutocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;ApiUser&gt;**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteUsers 200 response |  -  |


## autocompleteUsersWithResourceTenantasSuperAdmin

> List&lt;ApiUser&gt; autocompleteUsersWithResourceTenantasSuperAdmin(resourceTenant, abstractUserControllerUserApiAutocomplete)

List users for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        AbstractUserControllerUserApiAutocomplete abstractUserControllerUserApiAutocomplete = new AbstractUserControllerUserApiAutocomplete(); // AbstractUserControllerUserApiAutocomplete | Autocomplete request
        try {
            List<ApiUser> result = apiInstance.autocompleteUsersWithResourceTenantasSuperAdmin(resourceTenant, abstractUserControllerUserApiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#autocompleteUsersWithResourceTenantasSuperAdmin");
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
| **abstractUserControllerUserApiAutocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;ApiUser&gt;**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteUsersWithResourceTenantasSuperAdmin 200 response |  -  |


## autocompleteUsersasSuperAdmin

> List&lt;ApiUser&gt; autocompleteUsersasSuperAdmin(abstractUserControllerUserApiAutocomplete)

List users for autocomplete

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        AbstractUserControllerUserApiAutocomplete abstractUserControllerUserApiAutocomplete = new AbstractUserControllerUserApiAutocomplete(); // AbstractUserControllerUserApiAutocomplete | Autocomplete request
        try {
            List<ApiUser> result = apiInstance.autocompleteUsersasSuperAdmin(abstractUserControllerUserApiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#autocompleteUsersasSuperAdmin");
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
| **abstractUserControllerUserApiAutocomplete** | [**AbstractUserControllerUserApiAutocomplete**](AbstractUserControllerUserApiAutocomplete.md)| Autocomplete request | |

### Return type

[**List&lt;ApiUser&gt;**](ApiUser.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocompleteUsersasSuperAdmin 200 response |  -  |


## createApiTokensForUser

> Object createApiTokensForUser(id, tenant, createApiTokenRequest)

Create new API Token for a specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        CreateApiTokenRequest createApiTokenRequest = new CreateApiTokenRequest(); // CreateApiTokenRequest | The create api-token request
        try {
            Object result = apiInstance.createApiTokensForUser(id, tenant, createApiTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createApiTokensForUser");
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
| **id** | **String**| The user id | |
| **tenant** | **String**|  | |
| **createApiTokenRequest** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createApiTokensForUser 200 response |  -  |


## createApiTokensForUserWithResourceTenantasSuperAdmin

> Object createApiTokensForUserWithResourceTenantasSuperAdmin(id, resourceTenant, createApiTokenRequest)

Create new API Token for a specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        CreateApiTokenRequest createApiTokenRequest = new CreateApiTokenRequest(); // CreateApiTokenRequest | The create api-token request
        try {
            Object result = apiInstance.createApiTokensForUserWithResourceTenantasSuperAdmin(id, resourceTenant, createApiTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createApiTokensForUserWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **resourceTenant** | **String**|  | |
| **createApiTokenRequest** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createApiTokensForUserWithResourceTenantasSuperAdmin 200 response |  -  |


## createApiTokensForUserasSuperAdmin

> Object createApiTokensForUserasSuperAdmin(id, createApiTokenRequest)

Create new API Token for a specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        CreateApiTokenRequest createApiTokenRequest = new CreateApiTokenRequest(); // CreateApiTokenRequest | The create api-token request
        try {
            Object result = apiInstance.createApiTokensForUserasSuperAdmin(id, createApiTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createApiTokensForUserasSuperAdmin");
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
| **id** | **String**| The user id | |
| **createApiTokenRequest** | [**CreateApiTokenRequest**](CreateApiTokenRequest.md)| The create api-token request | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createApiTokensForUserasSuperAdmin 200 response |  -  |


## createServiceAccount

> ApiServiceAccount createServiceAccount(tenant, apiServiceAccount)

Create a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The service account
        try {
            ApiServiceAccount result = apiInstance.createServiceAccount(tenant, apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createServiceAccount");
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
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | |

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
| **200** | createServiceAccount 200 response |  -  |


## createServiceAccountWithResourceTenantasSuperAdmin

> ApiServiceAccount createServiceAccountWithResourceTenantasSuperAdmin(resourceTenant, apiServiceAccount)

Create a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The service account
        try {
            ApiServiceAccount result = apiInstance.createServiceAccountWithResourceTenantasSuperAdmin(resourceTenant, apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createServiceAccountWithResourceTenantasSuperAdmin");
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
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | |

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
| **200** | createServiceAccountWithResourceTenantasSuperAdmin 200 response |  -  |


## createServiceAccountasSuperAdmin

> ApiServiceAccount createServiceAccountasSuperAdmin(apiServiceAccount)

Create a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The service account
        try {
            ApiServiceAccount result = apiInstance.createServiceAccountasSuperAdmin(apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createServiceAccountasSuperAdmin");
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
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The service account | |

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
| **200** | createServiceAccountasSuperAdmin 200 response |  -  |


## createUser

> ApiUser createUser(tenant, apiUser)

Create a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String tenant = "tenant_example"; // String |
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.createUser(tenant, apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUser");
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
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **200** | createUser 200 response |  -  |


## createUserBasicAuth

> ApiUser createUserBasicAuth(id, tenant, abstractUserControllerPasswordRequest)

Create a basic auth password for a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        AbstractUserControllerPasswordRequest abstractUserControllerPasswordRequest = new AbstractUserControllerPasswordRequest(); // AbstractUserControllerPasswordRequest | The password
        try {
            ApiUser result = apiInstance.createUserBasicAuth(id, tenant, abstractUserControllerPasswordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUserBasicAuth");
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
| **id** | **String**| The user id | |
| **tenant** | **String**|  | |
| **abstractUserControllerPasswordRequest** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | |

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
| **200** | createUserBasicAuth 200 response |  -  |


## createUserBasicAuthWithResourceTenantasSuperAdmin

> ApiUser createUserBasicAuthWithResourceTenantasSuperAdmin(id, resourceTenant, abstractUserControllerPasswordRequest)

Create a basic auth password for a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        AbstractUserControllerPasswordRequest abstractUserControllerPasswordRequest = new AbstractUserControllerPasswordRequest(); // AbstractUserControllerPasswordRequest | The password
        try {
            ApiUser result = apiInstance.createUserBasicAuthWithResourceTenantasSuperAdmin(id, resourceTenant, abstractUserControllerPasswordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUserBasicAuthWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **resourceTenant** | **String**|  | |
| **abstractUserControllerPasswordRequest** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | |

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
| **200** | createUserBasicAuthWithResourceTenantasSuperAdmin 200 response |  -  |


## createUserBasicAuthasSuperAdmin

> ApiUser createUserBasicAuthasSuperAdmin(id, abstractUserControllerPasswordRequest)

Create a basic auth password for a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        AbstractUserControllerPasswordRequest abstractUserControllerPasswordRequest = new AbstractUserControllerPasswordRequest(); // AbstractUserControllerPasswordRequest | The password
        try {
            ApiUser result = apiInstance.createUserBasicAuthasSuperAdmin(id, abstractUserControllerPasswordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUserBasicAuthasSuperAdmin");
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
| **id** | **String**| The user id | |
| **abstractUserControllerPasswordRequest** | [**AbstractUserControllerPasswordRequest**](AbstractUserControllerPasswordRequest.md)| The password | |

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
| **200** | createUserBasicAuthasSuperAdmin 200 response |  -  |


## createUserWithResourceTenantasSuperAdmin

> ApiUser createUserWithResourceTenantasSuperAdmin(resourceTenant, apiUser)

Create a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.createUserWithResourceTenantasSuperAdmin(resourceTenant, apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUserWithResourceTenantasSuperAdmin");
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
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **200** | createUserWithResourceTenantasSuperAdmin 200 response |  -  |


## createUserasSuperAdmin

> ApiUser createUserasSuperAdmin(apiUser)

Create a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.createUserasSuperAdmin(apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#createUserasSuperAdmin");
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
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **200** | createUserasSuperAdmin 200 response |  -  |


## deleteApiToken

> Object deleteApiToken(id, tokenId, tenant)

Delete an API Token for specific user and token id

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tokenId = "tokenId_example"; // String | The token id
        String tenant = "tenant_example"; // String |
        try {
            Object result = apiInstance.deleteApiToken(id, tokenId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteApiToken");
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
| **id** | **String**| The user id | |
| **tokenId** | **String**| The token id | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApiToken 200 response |  -  |


## deleteApiTokenWithResourceTenantasSuperAdmin

> Object deleteApiTokenWithResourceTenantasSuperAdmin(id, tokenId, resourceTenant)

Delete an API Token for specific user and token id

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tokenId = "tokenId_example"; // String | The token id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            Object result = apiInstance.deleteApiTokenWithResourceTenantasSuperAdmin(id, tokenId, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteApiTokenWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **tokenId** | **String**| The token id | |
| **resourceTenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApiTokenWithResourceTenantasSuperAdmin 200 response |  -  |


## deleteApiTokenasSuperAdmin

> Object deleteApiTokenasSuperAdmin(id, tokenId)

Delete an API Token for specific user and token id

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tokenId = "tokenId_example"; // String | The token id
        try {
            Object result = apiInstance.deleteApiTokenasSuperAdmin(id, tokenId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteApiTokenasSuperAdmin");
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
| **id** | **String**| The user id | |
| **tokenId** | **String**| The token id | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApiTokenasSuperAdmin 200 response |  -  |


## deleteAuth

> ApiUser deleteAuth(id, uid, tenant)

Delete an Auth for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String uid = "uid_example"; // String | The auth id
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteAuth(id, uid, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteAuth");
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
| **id** | **String**| The user id | |
| **uid** | **String**| The auth id | |
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
| **404** | On user not found |  -  |
| **200** | deleteAuth 200 response |  -  |


## deleteAuthWithResourceTenantasSuperAdmin

> ApiUser deleteAuthWithResourceTenantasSuperAdmin(id, uid, resourceTenant)

Delete an Auth for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String uid = "uid_example"; // String | The auth id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteAuthWithResourceTenantasSuperAdmin(id, uid, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteAuthWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **uid** | **String**| The auth id | |
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
| **404** | On user not found |  -  |
| **200** | deleteAuthWithResourceTenantasSuperAdmin 200 response |  -  |


## deleteAuthasSuperAdmin

> ApiUser deleteAuthasSuperAdmin(id, uid)

Delete an Auth for a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String uid = "uid_example"; // String | The auth id
        try {
            ApiUser result = apiInstance.deleteAuthasSuperAdmin(id, uid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteAuthasSuperAdmin");
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
| **id** | **String**| The user id | |
| **uid** | **String**| The auth id | |

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
| **404** | On user not found |  -  |
| **200** | deleteAuthasSuperAdmin 200 response |  -  |


## deleteRefreshToken

> ApiUser deleteRefreshToken(id, tenant)

Delete a user refresh token

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteRefreshToken(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteRefreshToken");
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
| **id** | **String**| The user id | |
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
| **200** | deleteRefreshToken 200 response |  -  |


## deleteRefreshTokenWithResourceTenantasSuperAdmin

> ApiUser deleteRefreshTokenWithResourceTenantasSuperAdmin(id, resourceTenant)

Delete a user refresh token

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.deleteRefreshTokenWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteRefreshTokenWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
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
| **200** | deleteRefreshTokenWithResourceTenantasSuperAdmin 200 response |  -  |


## deleteRefreshTokenasSuperAdmin

> ApiUser deleteRefreshTokenasSuperAdmin(id)

Delete a user refresh token

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        try {
            ApiUser result = apiInstance.deleteRefreshTokenasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteRefreshTokenasSuperAdmin");
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
| **id** | **String**| The user id | |

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
| **200** | deleteRefreshTokenasSuperAdmin 200 response |  -  |


## deleteUser

> deleteUser(id, tenant)

Delete a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            apiInstance.deleteUser(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteUser");
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
| **id** | **String**| The user id | |
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
| **404** | On user not found |  -  |


## deleteUserWithResourceTenantasSuperAdmin

> deleteUserWithResourceTenantasSuperAdmin(id, resourceTenant)

Delete a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            apiInstance.deleteUserWithResourceTenantasSuperAdmin(id, resourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteUserWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
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
| **404** | On user not found |  -  |


## deleteUserasSuperAdmin

> deleteUserasSuperAdmin(id)

Delete a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        try {
            apiInstance.deleteUserasSuperAdmin(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#deleteUserasSuperAdmin");
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
| **id** | **String**| The user id | |

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
| **404** | On user not found |  -  |


## findAllForAllTenants

> PagedResultsApiUser findAllForAllTenants(page, size, q, type, sort)

Get all users in the instance across all tenantd

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        UserType type = UserType.fromValue("STANDARD"); // UserType | The type of user
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.findAllForAllTenants(page, size, q, type, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#findAllForAllTenants");
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
| **type** | [**UserType**](.md)| The type of user | [optional] [enum: STANDARD, SERVICE_ACCOUNT, SUPER_ADMIN] |
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
| **200** | findAllForAllTenants 200 response |  -  |


## findAllForAllTenantsWithResourceTenant

> PagedResultsApiUser findAllForAllTenantsWithResourceTenant(page, resourceTenant, size, q, type, sort)

Get all users in the instance across all tenantd

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        String resourceTenant = "resourceTenant_example"; // String |
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        UserType type = UserType.fromValue("STANDARD"); // UserType | The type of user
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.findAllForAllTenantsWithResourceTenant(page, resourceTenant, size, q, type, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#findAllForAllTenantsWithResourceTenant");
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
| **resourceTenant** | **String**|  | |
| **size** | **Integer**| The current page size | [default to 10] |
| **q** | **String**| A string filter | [optional] |
| **type** | [**UserType**](.md)| The type of user | [optional] [enum: STANDARD, SERVICE_ACCOUNT, SUPER_ADMIN] |
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
| **200** | findAllForAllTenantsWithResourceTenant 200 response |  -  |


## getUser

> ApiUser getUser(id, tenant)

Get a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            ApiUser result = apiInstance.getUser(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getUser");
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
| **id** | **String**| The user id | |
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
| **404** | On user not found |  -  |
| **200** | getUser 200 response |  -  |


## getUserWithResourceTenantasSuperAdmin

> ApiUser getUserWithResourceTenantasSuperAdmin(id, resourceTenant)

Get a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            ApiUser result = apiInstance.getUserWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getUserWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
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
| **404** | On user not found |  -  |
| **200** | getUserWithResourceTenantasSuperAdmin 200 response |  -  |


## getUserasSuperAdmin

> ApiUser getUserasSuperAdmin(id)

Get a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        try {
            ApiUser result = apiInstance.getUserasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getUserasSuperAdmin");
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
| **id** | **String**| The user id | |

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
| **404** | On user not found |  -  |
| **200** | getUserasSuperAdmin 200 response |  -  |


## impersonate

> Object impersonate(id)

Impersonate a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        try {
            Object result = apiInstance.impersonate(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#impersonate");
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
| **id** | **String**| The user id | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | impersonate 200 response |  -  |


## impersonateWithResourceTenant

> Object impersonateWithResourceTenant(resourceTenant, id)

Impersonate a user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        String id = "id_example"; // String | The user id
        try {
            Object result = apiInstance.impersonateWithResourceTenant(resourceTenant, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#impersonateWithResourceTenant");
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
| **id** | **String**| The user id | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | impersonateWithResourceTenant 200 response |  -  |


## listApiTokens

> Object listApiTokens(id, tenant)

List all API Tokens for specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        try {
            Object result = apiInstance.listApiTokens(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#listApiTokens");
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
| **id** | **String**| The user id | |
| **tenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listApiTokens 200 response |  -  |


## listApiTokensWithResourceTenantasSuperAdmin

> Object listApiTokensWithResourceTenantasSuperAdmin(id, resourceTenant)

List all API Tokens for specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            Object result = apiInstance.listApiTokensWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#listApiTokensWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **resourceTenant** | **String**|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listApiTokensWithResourceTenantasSuperAdmin 200 response |  -  |


## listApiTokensasSuperAdmin

> Object listApiTokensasSuperAdmin(id)

List all API Tokens for specific user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        try {
            Object result = apiInstance.listApiTokensasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#listApiTokensasSuperAdmin");
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
| **id** | **String**| The user id | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listApiTokensasSuperAdmin 200 response |  -  |


## searchUsers

> PagedResultsApiUser searchUsers(page, size, tenant, q, sort, type)

Search for users

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        UserType type = UserType.fromValue("STANDARD"); // UserType | The type of user
        try {
            PagedResultsApiUser result = apiInstance.searchUsers(page, size, tenant, q, sort, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#searchUsers");
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
| **type** | [**UserType**](.md)| The type of user | [optional] [enum: STANDARD, SERVICE_ACCOUNT, SUPER_ADMIN] |

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
| **200** | searchUsers 200 response |  -  |


## searchUsersWithResourceTenantasSuperAdmin

> PagedResultsApiUser searchUsersWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort, type)

Search for users

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String |
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        UserType type = UserType.fromValue("STANDARD"); // UserType | The type of user
        try {
            PagedResultsApiUser result = apiInstance.searchUsersWithResourceTenantasSuperAdmin(page, size, resourceTenant, q, sort, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#searchUsersWithResourceTenantasSuperAdmin");
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
| **type** | [**UserType**](.md)| The type of user | [optional] [enum: STANDARD, SERVICE_ACCOUNT, SUPER_ADMIN] |

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
| **200** | searchUsersWithResourceTenantasSuperAdmin 200 response |  -  |


## searchUsersasSuperAdmin

> PagedResultsApiUser searchUsersasSuperAdmin(page, size, q, sort, type)

Search for users

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        UserType type = UserType.fromValue("STANDARD"); // UserType | The type of user
        try {
            PagedResultsApiUser result = apiInstance.searchUsersasSuperAdmin(page, size, q, sort, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#searchUsersasSuperAdmin");
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
| **type** | [**UserType**](.md)| The type of user | [optional] [enum: STANDARD, SERVICE_ACCOUNT, SUPER_ADMIN] |

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
| **200** | searchUsersasSuperAdmin 200 response |  -  |


## setSuperAdmin

> ApiUser setSuperAdmin(id, body)

Update a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        Boolean body = true; // Boolean |
        try {
            ApiUser result = apiInstance.setSuperAdmin(id, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#setSuperAdmin");
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
| **id** | **String**| The user id | |
| **body** | **Boolean**|  | |

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
| **404** | On user not found |  -  |
| **200** | setSuperAdmin 200 response |  -  |


## setSuperAdminWithResourceTenant

> ApiUser setSuperAdminWithResourceTenant(resourceTenant, id, body)

Update a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        String id = "id_example"; // String | The user id
        Boolean body = true; // Boolean |
        try {
            ApiUser result = apiInstance.setSuperAdminWithResourceTenant(resourceTenant, id, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#setSuperAdminWithResourceTenant");
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
| **id** | **String**| The user id | |
| **body** | **Boolean**|  | |

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
| **404** | On user not found |  -  |
| **200** | setSuperAdminWithResourceTenant 200 response |  -  |


## updateCurrentUserPassword

> Object updateCurrentUserPassword(tenant, meControllerUpdatePasswordRequest)

Update login password for the current user.

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String tenant = "tenant_example"; // String |
        MeControllerUpdatePasswordRequest meControllerUpdatePasswordRequest = new MeControllerUpdatePasswordRequest(); // MeControllerUpdatePasswordRequest |
        try {
            Object result = apiInstance.updateCurrentUserPassword(tenant, meControllerUpdatePasswordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateCurrentUserPassword");
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
| **meControllerUpdatePasswordRequest** | [**MeControllerUpdatePasswordRequest**](MeControllerUpdatePasswordRequest.md)|  | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateCurrentUserPassword 200 response |  -  |


## updateServiceAccount

> ApiServiceAccount updateServiceAccount(id, tenant, apiServiceAccount)

Update a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The user
        try {
            ApiServiceAccount result = apiInstance.updateServiceAccount(id, tenant, apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateServiceAccount");
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
| **id** | **String**| The user id | |
| **tenant** | **String**|  | |
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateServiceAccount 200 response |  -  |


## updateServiceAccountWithResourceTenantasSuperAdmin

> ApiServiceAccount updateServiceAccountWithResourceTenantasSuperAdmin(id, resourceTenant, apiServiceAccount)

Update a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The user
        try {
            ApiServiceAccount result = apiInstance.updateServiceAccountWithResourceTenantasSuperAdmin(id, resourceTenant, apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateServiceAccountWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **resourceTenant** | **String**|  | |
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateServiceAccountWithResourceTenantasSuperAdmin 200 response |  -  |


## updateServiceAccountasSuperAdmin

> ApiServiceAccount updateServiceAccountasSuperAdmin(id, apiServiceAccount)

Update a user service account

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        ApiServiceAccount apiServiceAccount = new ApiServiceAccount(); // ApiServiceAccount | The user
        try {
            ApiServiceAccount result = apiInstance.updateServiceAccountasSuperAdmin(id, apiServiceAccount);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateServiceAccountasSuperAdmin");
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
| **id** | **String**| The user id | |
| **apiServiceAccount** | [**ApiServiceAccount**](ApiServiceAccount.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateServiceAccountasSuperAdmin 200 response |  -  |


## updateUser

> ApiUser updateUser(id, tenant, apiUser)

Update a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String tenant = "tenant_example"; // String |
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.updateUser(id, tenant, apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateUser");
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
| **id** | **String**| The user id | |
| **tenant** | **String**|  | |
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateUser 200 response |  -  |


## updateUserWithResourceTenantasSuperAdmin

> ApiUser updateUserWithResourceTenantasSuperAdmin(id, resourceTenant, apiUser)

Update a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        String resourceTenant = "resourceTenant_example"; // String |
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.updateUserWithResourceTenantasSuperAdmin(id, resourceTenant, apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateUserWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The user id | |
| **resourceTenant** | **String**|  | |
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateUserWithResourceTenantasSuperAdmin 200 response |  -  |


## updateUserasSuperAdmin

> ApiUser updateUserasSuperAdmin(id, apiUser)

Update a standard user

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.UsersApi;

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

        UsersApi apiInstance = new UsersApi(defaultClient);
        String id = "id_example"; // String | The user id
        ApiUser apiUser = new ApiUser(); // ApiUser | The user
        try {
            ApiUser result = apiInstance.updateUserasSuperAdmin(id, apiUser);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#updateUserasSuperAdmin");
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
| **id** | **String**| The user id | |
| **apiUser** | [**ApiUser**](ApiUser.md)| The user | |

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
| **404** | On user not found |  -  |
| **200** | updateUserasSuperAdmin 200 response |  -  |

