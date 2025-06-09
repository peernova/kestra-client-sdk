# InvitationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInvitation**](InvitationsApi.md#createInvitation) | **POST** /api/v1/{tenant}/invitations | Create an invitation |
| [**createInvitationWithResourceTenantasSuperAdmin**](InvitationsApi.md#createInvitationWithResourceTenantasSuperAdmin) | **POST** /api/v1/tenants/{resourceTenant}/invitations | Create an invitation |
| [**createInvitationasSuperAdmin**](InvitationsApi.md#createInvitationasSuperAdmin) | **POST** /api/v1/tenants/invitations | Create an invitation |
| [**deleteInvitation**](InvitationsApi.md#deleteInvitation) | **DELETE** /api/v1/{tenant}/invitations/{id} | Delete an invitation |
| [**deleteInvitationWithResourceTenantasSuperAdmin**](InvitationsApi.md#deleteInvitationWithResourceTenantasSuperAdmin) | **DELETE** /api/v1/tenants/{resourceTenant}/invitations/{id} | Delete an invitation |
| [**deleteInvitationasSuperAdmin**](InvitationsApi.md#deleteInvitationasSuperAdmin) | **DELETE** /api/v1/tenants/invitations/{id} | Delete an invitation |
| [**findAllInvitationsForCurrentUser**](InvitationsApi.md#findAllInvitationsForCurrentUser) | **GET** /api/v1/{tenant}/me/invitations | Get all invitations for a given email |
| [**getInvitation**](InvitationsApi.md#getInvitation) | **GET** /api/v1/{tenant}/invitations/{id} | Get an invitation |
| [**getInvitationWithResourceTenantasSuperAdmin**](InvitationsApi.md#getInvitationWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/{id} | Get an invitation |
| [**getInvitationasSuperAdmin**](InvitationsApi.md#getInvitationasSuperAdmin) | **GET** /api/v1/tenants/invitations/{id} | Get an invitation |
| [**listByEmail**](InvitationsApi.md#listByEmail) | **GET** /api/v1/{tenant}/invitations/email/{email} | Get all invitations for a given email |
| [**listByEmailWithResourceTenantasSuperAdmin**](InvitationsApi.md#listByEmailWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/email/{email} | Get all invitations for a given email |
| [**listByEmailasSuperAdmin**](InvitationsApi.md#listByEmailasSuperAdmin) | **GET** /api/v1/tenants/invitations/email/{email} | Get all invitations for a given email |
| [**searchInvitations**](InvitationsApi.md#searchInvitations) | **GET** /api/v1/{tenant}/invitations/search | Search for invitations |
| [**searchInvitationsWithResourceTenantasSuperAdmin**](InvitationsApi.md#searchInvitationsWithResourceTenantasSuperAdmin) | **GET** /api/v1/tenants/{resourceTenant}/invitations/search | Search for invitations |
| [**searchInvitationsasSuperAdmin**](InvitationsApi.md#searchInvitationsasSuperAdmin) | **GET** /api/v1/tenants/invitations/search | Search for invitations |



## createInvitation

> Invitation createInvitation(tenant, invitation)

Create an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        Invitation invitation = new Invitation(); // Invitation | Create a new invitation, send an email if the server-mail is enabled
        try {
            Invitation result = apiInstance.createInvitation(tenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#createInvitation");
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
| **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | |

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
| **200** | createInvitation 200 response |  -  |


## createInvitationWithResourceTenantasSuperAdmin

> Invitation createInvitationWithResourceTenantasSuperAdmin(resourceTenant, invitation)

Create an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String resourceTenant = "resourceTenant_example"; // String |
        Invitation invitation = new Invitation(); // Invitation | Create a new invitation, send an email if the server-mail is enabled
        try {
            Invitation result = apiInstance.createInvitationWithResourceTenantasSuperAdmin(resourceTenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#createInvitationWithResourceTenantasSuperAdmin");
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
| **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | |

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
| **200** | createInvitationWithResourceTenantasSuperAdmin 200 response |  -  |


## createInvitationasSuperAdmin

> Invitation createInvitationasSuperAdmin(invitation)

Create an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Invitation invitation = new Invitation(); // Invitation | Create a new invitation, send an email if the server-mail is enabled
        try {
            Invitation result = apiInstance.createInvitationasSuperAdmin(invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#createInvitationasSuperAdmin");
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
| **invitation** | [**Invitation**](Invitation.md)| Create a new invitation, send an email if the server-mail is enabled | |

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
| **200** | createInvitationasSuperAdmin 200 response |  -  |


## deleteInvitation

> deleteInvitation(id, tenant)

Delete an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String |
        try {
            apiInstance.deleteInvitation(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#deleteInvitation");
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
| **id** | **String**| The id of the invitation | |
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
| **200** | deleteInvitation 200 response |  -  |


## deleteInvitationWithResourceTenantasSuperAdmin

> deleteInvitationWithResourceTenantasSuperAdmin(id, resourceTenant)

Delete an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            apiInstance.deleteInvitationWithResourceTenantasSuperAdmin(id, resourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#deleteInvitationWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The id of the invitation | |
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
| **200** | deleteInvitationWithResourceTenantasSuperAdmin 200 response |  -  |


## deleteInvitationasSuperAdmin

> deleteInvitationasSuperAdmin(id)

Delete an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            apiInstance.deleteInvitationasSuperAdmin(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#deleteInvitationasSuperAdmin");
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
| **id** | **String**| The id of the invitation | |

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
| **200** | deleteInvitationasSuperAdmin 200 response |  -  |


## findAllInvitationsForCurrentUser

> List&lt;Invitation&gt; findAllInvitationsForCurrentUser(tenant)

Get all invitations for a given email

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String tenant = "tenant_example"; // String |
        try {
            List<Invitation> result = apiInstance.findAllInvitationsForCurrentUser(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findAllInvitationsForCurrentUser");
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

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findAllInvitationsForCurrentUser 200 response |  -  |


## getInvitation

> Invitation getInvitation(id, tenant)

Get an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String |
        try {
            Invitation result = apiInstance.getInvitation(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#getInvitation");
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
| **id** | **String**| The id of the invitation | |
| **tenant** | **String**|  | |

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
| **200** | getInvitation 200 response |  -  |


## getInvitationWithResourceTenantasSuperAdmin

> Invitation getInvitationWithResourceTenantasSuperAdmin(id, resourceTenant)

Get an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            Invitation result = apiInstance.getInvitationWithResourceTenantasSuperAdmin(id, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#getInvitationWithResourceTenantasSuperAdmin");
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
| **id** | **String**| The id of the invitation | |
| **resourceTenant** | **String**|  | |

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
| **200** | getInvitationWithResourceTenantasSuperAdmin 200 response |  -  |


## getInvitationasSuperAdmin

> Invitation getInvitationasSuperAdmin(id)

Get an invitation

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            Invitation result = apiInstance.getInvitationasSuperAdmin(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#getInvitationasSuperAdmin");
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
| **id** | **String**| The id of the invitation | |

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
| **200** | getInvitationasSuperAdmin 200 response |  -  |


## listByEmail

> List&lt;Invitation&gt; listByEmail(email, tenant)

Get all invitations for a given email

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String tenant = "tenant_example"; // String |
        try {
            List<Invitation> result = apiInstance.listByEmail(email, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#listByEmail");
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
| **email** | **String**| The email address of the invited | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listByEmail 200 response |  -  |


## listByEmailWithResourceTenantasSuperAdmin

> List&lt;Invitation&gt; listByEmailWithResourceTenantasSuperAdmin(email, resourceTenant)

Get all invitations for a given email

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String resourceTenant = "resourceTenant_example"; // String |
        try {
            List<Invitation> result = apiInstance.listByEmailWithResourceTenantasSuperAdmin(email, resourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#listByEmailWithResourceTenantasSuperAdmin");
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
| **email** | **String**| The email address of the invited | |
| **resourceTenant** | **String**|  | |

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listByEmailWithResourceTenantasSuperAdmin 200 response |  -  |


## listByEmailasSuperAdmin

> List&lt;Invitation&gt; listByEmailasSuperAdmin(email)

Get all invitations for a given email

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        try {
            List<Invitation> result = apiInstance.listByEmailasSuperAdmin(email);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#listByEmailasSuperAdmin");
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
| **email** | **String**| The email address of the invited | |

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listByEmailasSuperAdmin 200 response |  -  |


## searchInvitations

> PagedResultsInvitation searchInvitations(page, size, tenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String |
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.searchInvitations(page, size, tenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#searchInvitations");
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
| **email** | **String**| The email address of the invited | [optional] |
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED, EXPIRED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchInvitations 200 response |  -  |


## searchInvitationsWithResourceTenantasSuperAdmin

> PagedResultsInvitation searchInvitationsWithResourceTenantasSuperAdmin(page, size, resourceTenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String resourceTenant = "resourceTenant_example"; // String |
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.searchInvitationsWithResourceTenantasSuperAdmin(page, size, resourceTenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#searchInvitationsWithResourceTenantasSuperAdmin");
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
| **email** | **String**| The email address of the invited | [optional] |
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED, EXPIRED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchInvitationsWithResourceTenantasSuperAdmin 200 response |  -  |


## searchInvitationsasSuperAdmin

> PagedResultsInvitation searchInvitationsasSuperAdmin(page, size, email, status, sort)

Search for invitations

### Example

```java
// Import classes:

import internal.sdk.io.kestraClient;
import internal.sdk.io.kestraException;
import internal.sdk.io.kestra.Configuration;
import api.sdk.io.kestra.InvitationsApi;

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

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.searchInvitationsasSuperAdmin(page, size, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#searchInvitationsasSuperAdmin");
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
| **email** | **String**| The email address of the invited | [optional] |
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED, EXPIRED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

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
| **200** | searchInvitationsasSuperAdmin 200 response |  -  |

