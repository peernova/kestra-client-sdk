# InvitationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create17**](InvitationsApi.md#create17) | **POST** /api/v1/tenants/invitations | Create an invitation |
| [**create22**](InvitationsApi.md#create22) | **POST** /api/v1/tenants/{ressourceTenant}/invitations | Create an invitation |
| [**create34**](InvitationsApi.md#create34) | **POST** /api/v1/{tenant}/invitations | Create an invitation |
| [**create42**](InvitationsApi.md#create42) | **POST** /api/v1/{tenant}/tenants/invitations | Create an invitation |
| [**create47**](InvitationsApi.md#create47) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/invitations | Create an invitation |
| [**create9**](InvitationsApi.md#create9) | **POST** /api/v1/invitations | Create an invitation |
| [**delete19**](InvitationsApi.md#delete19) | **DELETE** /api/v1/tenants/invitations/{id} | Delete an invitation |
| [**delete25**](InvitationsApi.md#delete25) | **DELETE** /api/v1/tenants/{ressourceTenant}/invitations/{id} | Delete an invitation |
| [**delete37**](InvitationsApi.md#delete37) | **DELETE** /api/v1/{tenant}/invitations/{id} | Delete an invitation |
| [**delete47**](InvitationsApi.md#delete47) | **DELETE** /api/v1/{tenant}/tenants/invitations/{id} | Delete an invitation |
| [**delete53**](InvitationsApi.md#delete53) | **DELETE** /api/v1/{tenant}/tenants/{ressourceTenant}/invitations/{id} | Delete an invitation |
| [**delete9**](InvitationsApi.md#delete9) | **DELETE** /api/v1/invitations/{id} | Delete an invitation |
| [**find16**](InvitationsApi.md#find16) | **GET** /api/v1/tenants/invitations/search | Search for invitations |
| [**find22**](InvitationsApi.md#find22) | **GET** /api/v1/tenants/{ressourceTenant}/invitations/search | Search for invitations |
| [**find35**](InvitationsApi.md#find35) | **GET** /api/v1/{tenant}/invitations/search | Search for invitations |
| [**find42**](InvitationsApi.md#find42) | **GET** /api/v1/{tenant}/tenants/invitations/search | Search for invitations |
| [**find48**](InvitationsApi.md#find48) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/invitations/search | Search for invitations |
| [**find9**](InvitationsApi.md#find9) | **GET** /api/v1/invitations/search | Search for invitations |
| [**findByEmail**](InvitationsApi.md#findByEmail) | **GET** /api/v1/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmail1**](InvitationsApi.md#findByEmail1) | **GET** /api/v1/tenants/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmail2**](InvitationsApi.md#findByEmail2) | **GET** /api/v1/tenants/{ressourceTenant}/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmail3**](InvitationsApi.md#findByEmail3) | **GET** /api/v1/{tenant}/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmail4**](InvitationsApi.md#findByEmail4) | **GET** /api/v1/{tenant}/tenants/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmail5**](InvitationsApi.md#findByEmail5) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/invitations/email/{email} | Get all invitations for a given email |
| [**findByEmailAllTenant**](InvitationsApi.md#findByEmailAllTenant) | **GET** /api/v1/me/invitations | Get all invitations for a given email |
| [**findByEmailAllTenant1**](InvitationsApi.md#findByEmailAllTenant1) | **GET** /api/v1/{tenant}/me/invitations | Get all invitations for a given email |
| [**get11**](InvitationsApi.md#get11) | **GET** /api/v1/{tenant}/invitations/{id} | Delete an invitation |
| [**get13**](InvitationsApi.md#get13) | **GET** /api/v1/{tenant}/tenants/invitations/{id} | Delete an invitation |
| [**get15**](InvitationsApi.md#get15) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/invitations/{id} | Delete an invitation |
| [**get3**](InvitationsApi.md#get3) | **GET** /api/v1/invitations/{id} | Delete an invitation |
| [**get5**](InvitationsApi.md#get5) | **GET** /api/v1/tenants/invitations/{id} | Delete an invitation |
| [**get7**](InvitationsApi.md#get7) | **GET** /api/v1/tenants/{ressourceTenant}/invitations/{id} | Delete an invitation |



## create17

> Invitation create17(invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create17(invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create17");
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
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_17 200 response |  -  |


## create22

> Invitation create22(ressourceTenant, invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create22(ressourceTenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create22");
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
| **ressourceTenant** | **String**|  | |
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_22 200 response |  -  |


## create34

> Invitation create34(tenant, invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create34(tenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create34");
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
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_34 200 response |  -  |


## create42

> Invitation create42(tenant, invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create42(tenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create42");
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
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_42 200 response |  -  |


## create47

> Invitation create47(ressourceTenant, tenant, invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create47(ressourceTenant, tenant, invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create47");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_47 200 response |  -  |


## create9

> Invitation create9(invitation)

Create an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Invitation invitation = new Invitation(); // Invitation | 
        try {
            Invitation result = apiInstance.create9(invitation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#create9");
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
| **invitation** | [**Invitation**](Invitation.md)|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_9 200 response |  -  |


## delete19

> delete19(id)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            apiInstance.delete19(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete19");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_19 200 response |  -  |


## delete25

> delete25(id, ressourceTenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            apiInstance.delete25(id, ressourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete25");
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
| **ressourceTenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_25 200 response |  -  |


## delete37

> delete37(id, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete37(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete37");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_37 200 response |  -  |


## delete47

> delete47(id, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete47(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete47");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_47 200 response |  -  |


## delete53

> delete53(id, ressourceTenant, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete53(id, ressourceTenant, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete53");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_53 200 response |  -  |


## delete9

> delete9(id)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            apiInstance.delete9(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#delete9");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | delete_9 200 response |  -  |


## find16

> PagedResultsInvitation find16(page, size, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find16(page, size, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find16");
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
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_16 200 response |  -  |


## find22

> PagedResultsInvitation find22(page, size, ressourceTenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find22(page, size, ressourceTenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find22");
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
| **ressourceTenant** | **String**|  | |
| **email** | **String**| The email address of the invited | [optional] |
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_22 200 response |  -  |


## find35

> PagedResultsInvitation find35(page, size, tenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find35(page, size, tenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find35");
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
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_35 200 response |  -  |


## find42

> PagedResultsInvitation find42(page, size, tenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find42(page, size, tenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find42");
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
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_42 200 response |  -  |


## find48

> PagedResultsInvitation find48(page, size, ressourceTenant, tenant, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find48(page, size, ressourceTenant, tenant, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find48");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **email** | **String**| The email address of the invited | [optional] |
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_48 200 response |  -  |


## find9

> PagedResultsInvitation find9(page, size, email, status, sort)

Search for invitations

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String email = "email_example"; // String | The email address of the invited
        InvitationInvitationStatus status = InvitationInvitationStatus.fromValue("PENDING"); // InvitationInvitationStatus | The current status of the invitations
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsInvitation result = apiInstance.find9(page, size, email, status, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#find9");
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
| **status** | [**InvitationInvitationStatus**](.md)| The current status of the invitations | [optional] [enum: PENDING, ACCEPTED] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsInvitation**](PagedResultsInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_9 200 response |  -  |


## findByEmail

> List&lt;Invitation&gt; findByEmail(email)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        try {
            List<Invitation> result = apiInstance.findByEmail(email);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail 200 response |  -  |


## findByEmail1

> List&lt;Invitation&gt; findByEmail1(email)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        try {
            List<Invitation> result = apiInstance.findByEmail1(email);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail_1 200 response |  -  |


## findByEmail2

> List&lt;Invitation&gt; findByEmail2(email, ressourceTenant)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            List<Invitation> result = apiInstance.findByEmail2(email, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail2");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail_2 200 response |  -  |


## findByEmail3

> List&lt;Invitation&gt; findByEmail3(email, tenant)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String tenant = "tenant_example"; // String | 
        try {
            List<Invitation> result = apiInstance.findByEmail3(email, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail_3 200 response |  -  |


## findByEmail4

> List&lt;Invitation&gt; findByEmail4(email, tenant)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String tenant = "tenant_example"; // String | 
        try {
            List<Invitation> result = apiInstance.findByEmail4(email, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail4");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail_4 200 response |  -  |


## findByEmail5

> List&lt;Invitation&gt; findByEmail5(email, ressourceTenant, tenant)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String email = "email_example"; // String | The email address of the invited
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            List<Invitation> result = apiInstance.findByEmail5(email, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmail5");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmail_5 200 response |  -  |


## findByEmailAllTenant

> List&lt;Invitation&gt; findByEmailAllTenant()

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        try {
            List<Invitation> result = apiInstance.findByEmailAllTenant();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmailAllTenant");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List&lt;Invitation&gt;**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmailAllTenant 200 response |  -  |


## findByEmailAllTenant1

> List&lt;Invitation&gt; findByEmailAllTenant1(tenant)

Get all invitations for a given email

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        try {
            List<Invitation> result = apiInstance.findByEmailAllTenant1(tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#findByEmailAllTenant1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | findByEmailAllTenant_1 200 response |  -  |


## get11

> Invitation get11(id, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String | 
        try {
            Invitation result = apiInstance.get11(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get11");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_11 200 response |  -  |


## get13

> Invitation get13(id, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String tenant = "tenant_example"; // String | 
        try {
            Invitation result = apiInstance.get13(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get13");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_13 200 response |  -  |


## get15

> Invitation get15(id, ressourceTenant, tenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Invitation result = apiInstance.get15(id, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get15");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_15 200 response |  -  |


## get3

> Invitation get3(id)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            Invitation result = apiInstance.get3(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_3 200 response |  -  |


## get5

> Invitation get5(id)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        try {
            Invitation result = apiInstance.get5(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get5");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_5 200 response |  -  |


## get7

> Invitation get7(id, ressourceTenant)

Delete an invitation

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.InvitationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        InvitationsApi apiInstance = new InvitationsApi(defaultClient);
        String id = "id_example"; // String | The id of the invitation
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            Invitation result = apiInstance.get7(id, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitationsApi#get7");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**Invitation**](Invitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get_7 200 response |  -  |

