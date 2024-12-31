# GroupsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addGroup**](GroupsApi.md#addGroup) | **PUT** /api/v1/groups/{id}/members/{userId} | Add a group for a user |
| [**addGroup1**](GroupsApi.md#addGroup1) | **PUT** /api/v1/tenants/groups/{id}/members/{userId} | Add a group for a user |
| [**addGroup2**](GroupsApi.md#addGroup2) | **PUT** /api/v1/tenants/{ressourceTenant}/groups/{id}/members/{userId} | Add a group for a user |
| [**addGroup3**](GroupsApi.md#addGroup3) | **PUT** /api/v1/{tenant}/groups/{id}/members/{userId} | Add a group for a user |
| [**addGroup4**](GroupsApi.md#addGroup4) | **PUT** /api/v1/{tenant}/tenants/groups/{id}/members/{userId} | Add a group for a user |
| [**addGroup5**](GroupsApi.md#addGroup5) | **PUT** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id}/members/{userId} | Add a group for a user |
| [**autocomplete**](GroupsApi.md#autocomplete) | **POST** /api/v1/groups/autocomplete | List groups for autocomplete |
| [**autocomplete12**](GroupsApi.md#autocomplete12) | **POST** /api/v1/{tenant}/groups/autocomplete | List groups for autocomplete |
| [**autocomplete15**](GroupsApi.md#autocomplete15) | **POST** /api/v1/{tenant}/tenants/groups/autocomplete | List groups for autocomplete |
| [**autocomplete19**](GroupsApi.md#autocomplete19) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/autocomplete | List groups for autocomplete |
| [**autocomplete3**](GroupsApi.md#autocomplete3) | **POST** /api/v1/tenants/groups/autocomplete | List groups for autocomplete |
| [**autocomplete7**](GroupsApi.md#autocomplete7) | **POST** /api/v1/tenants/{ressourceTenant}/groups/autocomplete | List groups for autocomplete |
| [**create16**](GroupsApi.md#create16) | **POST** /api/v1/tenants/groups | Create a group |
| [**create21**](GroupsApi.md#create21) | **POST** /api/v1/tenants/{ressourceTenant}/groups | Create a group |
| [**create31**](GroupsApi.md#create31) | **POST** /api/v1/{tenant}/groups | Create a group |
| [**create41**](GroupsApi.md#create41) | **POST** /api/v1/{tenant}/tenants/groups | Create a group |
| [**create46**](GroupsApi.md#create46) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/groups | Create a group |
| [**create6**](GroupsApi.md#create6) | **POST** /api/v1/groups | Create a group |
| [**delete18**](GroupsApi.md#delete18) | **DELETE** /api/v1/tenants/groups/{id} | Delete a group |
| [**delete24**](GroupsApi.md#delete24) | **DELETE** /api/v1/tenants/{ressourceTenant}/groups/{id} | Delete a group |
| [**delete34**](GroupsApi.md#delete34) | **DELETE** /api/v1/{tenant}/groups/{id} | Delete a group |
| [**delete46**](GroupsApi.md#delete46) | **DELETE** /api/v1/{tenant}/tenants/groups/{id} | Delete a group |
| [**delete52**](GroupsApi.md#delete52) | **DELETE** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id} | Delete a group |
| [**delete6**](GroupsApi.md#delete6) | **DELETE** /api/v1/groups/{id} | Delete a group |
| [**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /api/v1/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteGroup1**](GroupsApi.md#deleteGroup1) | **DELETE** /api/v1/tenants/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteGroup2**](GroupsApi.md#deleteGroup2) | **DELETE** /api/v1/tenants/{ressourceTenant}/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteGroup3**](GroupsApi.md#deleteGroup3) | **DELETE** /api/v1/{tenant}/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteGroup4**](GroupsApi.md#deleteGroup4) | **DELETE** /api/v1/{tenant}/tenants/groups/{id}/members/{userId} | Delete a group for a user |
| [**deleteGroup5**](GroupsApi.md#deleteGroup5) | **DELETE** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id}/members/{userId} | Delete a group for a user |
| [**find15**](GroupsApi.md#find15) | **GET** /api/v1/tenants/groups/search | Search for groups |
| [**find21**](GroupsApi.md#find21) | **GET** /api/v1/tenants/{ressourceTenant}/groups/search | Search for groups |
| [**find32**](GroupsApi.md#find32) | **GET** /api/v1/{tenant}/groups/search | Search for groups |
| [**find41**](GroupsApi.md#find41) | **GET** /api/v1/{tenant}/tenants/groups/search | Search for groups |
| [**find47**](GroupsApi.md#find47) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/search | Search for groups |
| [**find6**](GroupsApi.md#find6) | **GET** /api/v1/groups/search | Search for groups |
| [**ids**](GroupsApi.md#ids) | **POST** /api/v1/groups/ids | List groups by ids |
| [**ids10**](GroupsApi.md#ids10) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/ids | List groups by ids |
| [**ids2**](GroupsApi.md#ids2) | **POST** /api/v1/tenants/groups/ids | List groups by ids |
| [**ids4**](GroupsApi.md#ids4) | **POST** /api/v1/tenants/{ressourceTenant}/groups/ids | List groups by ids |
| [**ids6**](GroupsApi.md#ids6) | **POST** /api/v1/{tenant}/groups/ids | List groups by ids |
| [**ids8**](GroupsApi.md#ids8) | **POST** /api/v1/{tenant}/tenants/groups/ids | List groups by ids |
| [**index11**](GroupsApi.md#index11) | **GET** /api/v1/tenants/groups/{id} | Get a group |
| [**index16**](GroupsApi.md#index16) | **GET** /api/v1/tenants/{ressourceTenant}/groups/{id} | Get a group |
| [**index25**](GroupsApi.md#index25) | **GET** /api/v1/{tenant}/groups/{id} | Get a group |
| [**index32**](GroupsApi.md#index32) | **GET** /api/v1/{tenant}/tenants/groups/{id} | Get a group |
| [**index37**](GroupsApi.md#index37) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id} | Get a group |
| [**index4**](GroupsApi.md#index4) | **GET** /api/v1/groups/{id} | Get a group |
| [**members**](GroupsApi.md#members) | **GET** /api/v1/groups/{id}/members | Search for users in a group |
| [**members1**](GroupsApi.md#members1) | **GET** /api/v1/tenants/groups/{id}/members | Search for users in a group |
| [**members2**](GroupsApi.md#members2) | **GET** /api/v1/tenants/{ressourceTenant}/groups/{id}/members | Search for users in a group |
| [**members3**](GroupsApi.md#members3) | **GET** /api/v1/{tenant}/groups/{id}/members | Search for users in a group |
| [**members4**](GroupsApi.md#members4) | **GET** /api/v1/{tenant}/tenants/groups/{id}/members | Search for users in a group |
| [**members5**](GroupsApi.md#members5) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id}/members | Search for users in a group |
| [**update10**](GroupsApi.md#update10) | **PUT** /api/v1/tenants/groups/{id} | Update a group |
| [**update14**](GroupsApi.md#update14) | **PUT** /api/v1/tenants/{ressourceTenant}/groups/{id} | Update a group |
| [**update22**](GroupsApi.md#update22) | **PUT** /api/v1/{tenant}/groups/{id} | Update a group |
| [**update28**](GroupsApi.md#update28) | **PUT** /api/v1/{tenant}/tenants/groups/{id} | Update a group |
| [**update32**](GroupsApi.md#update32) | **PUT** /api/v1/{tenant}/tenants/{ressourceTenant}/groups/{id} | Update a group |
| [**update4**](GroupsApi.md#update4) | **PUT** /api/v1/groups/{id} | Update a group |



## addGroup

> ApiUser addGroup(id, userId)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.addGroup(id, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup 200 response |  -  |


## addGroup1

> ApiUser addGroup1(id, userId)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.addGroup1(id, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup_1 200 response |  -  |


## addGroup2

> ApiUser addGroup2(id, userId, ressourceTenant)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            ApiUser result = apiInstance.addGroup2(id, userId, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup2");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup_2 200 response |  -  |


## addGroup3

> ApiUser addGroup3(id, userId, tenant)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.addGroup3(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup_3 200 response |  -  |


## addGroup4

> ApiUser addGroup4(id, userId, tenant)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.addGroup4(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup4");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup_4 200 response |  -  |


## addGroup5

> ApiUser addGroup5(id, userId, ressourceTenant, tenant)

Add a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.addGroup5(id, userId, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#addGroup5");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addGroup_5 200 response |  -  |


## autocomplete

> List&lt;Group&gt; autocomplete(apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete 200 response |  -  |


## autocomplete12

> List&lt;Group&gt; autocomplete12(tenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete12(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete12");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_12 200 response |  -  |


## autocomplete15

> List&lt;Group&gt; autocomplete15(tenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete15(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete15");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_15 200 response |  -  |


## autocomplete19

> List&lt;Group&gt; autocomplete19(ressourceTenant, tenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete19(ressourceTenant, tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete19");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_19 200 response |  -  |


## autocomplete3

> List&lt;Group&gt; autocomplete3(apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete3(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete3");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_3 200 response |  -  |


## autocomplete7

> List&lt;Group&gt; autocomplete7(ressourceTenant, apiAutocomplete)

List groups for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Group> result = apiInstance.autocomplete7(ressourceTenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#autocomplete7");
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
| **apiAutocomplete** | [**ApiAutocomplete**](ApiAutocomplete.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_7 200 response |  -  |


## create16

> Group create16(abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create16(abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create16");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_16 200 response |  -  |


## create21

> Group create21(ressourceTenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create21(ressourceTenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create21");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_21 200 response |  -  |


## create31

> Group create31(tenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create31(tenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create31");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_31 200 response |  -  |


## create41

> Group create41(tenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create41(tenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create41");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_41 200 response |  -  |


## create46

> Group create46(ressourceTenant, tenant, abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create46(ressourceTenant, tenant, abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create46");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_46 200 response |  -  |


## create6

> Group create6(abstractGroupControllerGroupWithMembers)

Create a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        AbstractGroupControllerGroupWithMembers abstractGroupControllerGroupWithMembers = new AbstractGroupControllerGroupWithMembers(); // AbstractGroupControllerGroupWithMembers | 
        try {
            Group result = apiInstance.create6(abstractGroupControllerGroupWithMembers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#create6");
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
| **abstractGroupControllerGroupWithMembers** | [**AbstractGroupControllerGroupWithMembers**](AbstractGroupControllerGroupWithMembers.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_6 200 response |  -  |


## delete18

> delete18(id)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            apiInstance.delete18(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete18");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete24

> delete24(id, ressourceTenant)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            apiInstance.delete24(id, ressourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete24");
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
| **204** | On success |  -  |


## delete34

> delete34(id, tenant)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete34(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete34");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete46

> delete46(id, tenant)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete46(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete46");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete52

> delete52(id, ressourceTenant, tenant)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete52(id, ressourceTenant, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete52");
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
| **204** | On success |  -  |


## delete6

> delete6(id)

Delete a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            apiInstance.delete6(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#delete6");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## deleteGroup

> ApiUser deleteGroup(id, userId)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.deleteGroup(id, userId);
            System.out.println(result);
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
| **userId** | **String**| The user id | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup 200 response |  -  |


## deleteGroup1

> ApiUser deleteGroup1(id, userId)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        try {
            ApiUser result = apiInstance.deleteGroup1(id, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup_1 200 response |  -  |


## deleteGroup2

> ApiUser deleteGroup2(id, userId, ressourceTenant)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            ApiUser result = apiInstance.deleteGroup2(id, userId, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup2");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup_2 200 response |  -  |


## deleteGroup3

> ApiUser deleteGroup3(id, userId, tenant)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.deleteGroup3(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup_3 200 response |  -  |


## deleteGroup4

> ApiUser deleteGroup4(id, userId, tenant)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.deleteGroup4(id, userId, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup4");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup_4 200 response |  -  |


## deleteGroup5

> ApiUser deleteGroup5(id, userId, ressourceTenant, tenant)

Delete a group for a user

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String userId = "userId_example"; // String | The user id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            ApiUser result = apiInstance.deleteGroup5(id, userId, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#deleteGroup5");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteGroup_5 200 response |  -  |


## find15

> PagedResultsGroup find15(page, size, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find15(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find15");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_15 200 response |  -  |


## find21

> PagedResultsGroup find21(page, size, ressourceTenant, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find21(page, size, ressourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find21");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_21 200 response |  -  |


## find32

> PagedResultsGroup find32(page, size, tenant, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find32(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find32");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_32 200 response |  -  |


## find41

> PagedResultsGroup find41(page, size, tenant, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find41(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find41");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_41 200 response |  -  |


## find47

> PagedResultsGroup find47(page, size, ressourceTenant, tenant, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find47(page, size, ressourceTenant, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find47");
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
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsGroup**](PagedResultsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_47 200 response |  -  |


## find6

> PagedResultsGroup find6(page, size, q, sort)

Search for groups

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsGroup result = apiInstance.find6(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#find6");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_6 200 response |  -  |


## ids

> List&lt;Group&gt; ids(apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids 200 response |  -  |


## ids10

> List&lt;Group&gt; ids10(ressourceTenant, tenant, apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids10(ressourceTenant, tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids10");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_10 200 response |  -  |


## ids2

> List&lt;Group&gt; ids2(apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids2(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids2");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_2 200 response |  -  |


## ids4

> List&lt;Group&gt; ids4(ressourceTenant, apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids4(ressourceTenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids4");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_4 200 response |  -  |


## ids6

> List&lt;Group&gt; ids6(tenant, apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids6(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids6");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_6 200 response |  -  |


## ids8

> List&lt;Group&gt; ids8(tenant, apiIds)

List groups by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Group> result = apiInstance.ids8(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#ids8");
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
| **apiIds** | [**ApiIds**](ApiIds.md)|  | |

### Return type

[**List&lt;Group&gt;**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_8 200 response |  -  |


## index11

> Group index11(id)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            Group result = apiInstance.index11(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index11");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_11 200 response |  -  |


## index16

> Group index16(id, ressourceTenant)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            Group result = apiInstance.index16(id, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index16");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_16 200 response |  -  |


## index25

> Group index25(id, tenant)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        try {
            Group result = apiInstance.index25(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index25");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_25 200 response |  -  |


## index32

> Group index32(id, tenant)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        try {
            Group result = apiInstance.index32(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index32");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_32 200 response |  -  |


## index37

> Group index37(id, ressourceTenant, tenant)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Group result = apiInstance.index37(id, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index37");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_37 200 response |  -  |


## index4

> Group index4(id)

Get a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        try {
            Group result = apiInstance.index4(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#index4");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_4 200 response |  -  |


## members

> PagedResultsApiUser members(id, page, size, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members(id, page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members 200 response |  -  |


## members1

> PagedResultsApiUser members1(id, page, size, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members1(id, page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members1");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members_1 200 response |  -  |


## members2

> PagedResultsApiUser members2(id, page, size, ressourceTenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members2(id, page, size, ressourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members2");
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
| **ressourceTenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsApiUser**](PagedResultsApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members_2 200 response |  -  |


## members3

> PagedResultsApiUser members3(id, page, size, tenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members3(id, page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members3");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members_3 200 response |  -  |


## members4

> PagedResultsApiUser members4(id, page, size, tenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members4(id, page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members4");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members_4 200 response |  -  |


## members5

> PagedResultsApiUser members5(id, page, size, ressourceTenant, tenant, q, sort)

Search for users in a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsApiUser result = apiInstance.members5(id, page, size, ressourceTenant, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#members5");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **q** | **String**| A string filter | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The sort of current page | [optional] |

### Return type

[**PagedResultsApiUser**](PagedResultsApiUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | members_5 200 response |  -  |


## update10

> Group update10(id, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update10(id, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update10");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_10 200 response |  -  |


## update14

> Group update14(id, ressourceTenant, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update14(id, ressourceTenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update14");
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
| **ressourceTenant** | **String**|  | |
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_14 200 response |  -  |


## update22

> Group update22(id, tenant, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update22(id, tenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update22");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_22 200 response |  -  |


## update28

> Group update28(id, tenant, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String tenant = "tenant_example"; // String | 
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update28(id, tenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update28");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_28 200 response |  -  |


## update32

> Group update32(id, ressourceTenant, tenant, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update32(id, ressourceTenant, tenant, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update32");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_32 200 response |  -  |


## update4

> Group update4(id, group)

Update a group

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.GroupsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        GroupsApi apiInstance = new GroupsApi(defaultClient);
        String id = "id_example"; // String | The group id
        Group group = new Group(); // Group | 
        try {
            Group result = apiInstance.update4(id, group);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GroupsApi#update4");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_4 200 response |  -  |

