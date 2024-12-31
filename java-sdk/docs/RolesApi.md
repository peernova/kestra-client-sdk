# RolesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocomplete14**](RolesApi.md#autocomplete14) | **POST** /api/v1/{tenant}/roles/autocomplete | List roles for autocomplete |
| [**autocomplete17**](RolesApi.md#autocomplete17) | **POST** /api/v1/{tenant}/tenants/roles/autocomplete | List roles for autocomplete |
| [**autocomplete2**](RolesApi.md#autocomplete2) | **POST** /api/v1/roles/autocomplete | List roles for autocomplete |
| [**autocomplete21**](RolesApi.md#autocomplete21) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/autocomplete | List roles for autocomplete |
| [**autocomplete5**](RolesApi.md#autocomplete5) | **POST** /api/v1/tenants/roles/autocomplete | List roles for autocomplete |
| [**autocomplete9**](RolesApi.md#autocomplete9) | **POST** /api/v1/tenants/{ressourceTenant}/roles/autocomplete | List roles for autocomplete |
| [**create11**](RolesApi.md#create11) | **POST** /api/v1/roles | Create a role |
| [**create18**](RolesApi.md#create18) | **POST** /api/v1/tenants/roles | Create a role |
| [**create23**](RolesApi.md#create23) | **POST** /api/v1/tenants/{ressourceTenant}/roles | Create a role |
| [**create36**](RolesApi.md#create36) | **POST** /api/v1/{tenant}/roles | Create a role |
| [**create43**](RolesApi.md#create43) | **POST** /api/v1/{tenant}/tenants/roles | Create a role |
| [**create48**](RolesApi.md#create48) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/roles | Create a role |
| [**delete14**](RolesApi.md#delete14) | **DELETE** /api/v1/roles/{id} | Delete a role |
| [**delete20**](RolesApi.md#delete20) | **DELETE** /api/v1/tenants/roles/{id} | Delete a role |
| [**delete26**](RolesApi.md#delete26) | **DELETE** /api/v1/tenants/{ressourceTenant}/roles/{id} | Delete a role |
| [**delete42**](RolesApi.md#delete42) | **DELETE** /api/v1/{tenant}/roles/{id} | Delete a role |
| [**delete48**](RolesApi.md#delete48) | **DELETE** /api/v1/{tenant}/tenants/roles/{id} | Delete a role |
| [**delete54**](RolesApi.md#delete54) | **DELETE** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/{id} | Delete a role |
| [**find12**](RolesApi.md#find12) | **GET** /api/v1/roles/search | Search for roles |
| [**find17**](RolesApi.md#find17) | **GET** /api/v1/tenants/roles/search | Search for roles |
| [**find23**](RolesApi.md#find23) | **GET** /api/v1/tenants/{ressourceTenant}/roles/search | Search for roles |
| [**find38**](RolesApi.md#find38) | **GET** /api/v1/{tenant}/roles/search | Search for roles |
| [**find43**](RolesApi.md#find43) | **GET** /api/v1/{tenant}/tenants/roles/search | Search for roles |
| [**find49**](RolesApi.md#find49) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/search | Search for roles |
| [**ids1**](RolesApi.md#ids1) | **POST** /api/v1/roles/ids |  |
| [**ids11**](RolesApi.md#ids11) | **POST** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/ids |  |
| [**ids3**](RolesApi.md#ids3) | **POST** /api/v1/tenants/roles/ids |  |
| [**ids5**](RolesApi.md#ids5) | **POST** /api/v1/tenants/{ressourceTenant}/roles/ids |  |
| [**ids7**](RolesApi.md#ids7) | **POST** /api/v1/{tenant}/roles/ids |  |
| [**ids9**](RolesApi.md#ids9) | **POST** /api/v1/{tenant}/tenants/roles/ids |  |
| [**index12**](RolesApi.md#index12) | **GET** /api/v1/tenants/roles/{id} | Get a role |
| [**index17**](RolesApi.md#index17) | **GET** /api/v1/tenants/{ressourceTenant}/roles/{id} | Get a role |
| [**index28**](RolesApi.md#index28) | **GET** /api/v1/{tenant}/roles/{id} | Get a role |
| [**index33**](RolesApi.md#index33) | **GET** /api/v1/{tenant}/tenants/roles/{id} | Get a role |
| [**index38**](RolesApi.md#index38) | **GET** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/{id} | Get a role |
| [**index7**](RolesApi.md#index7) | **GET** /api/v1/roles/{id} | Get a role |
| [**update11**](RolesApi.md#update11) | **PUT** /api/v1/tenants/roles/{id} | Update a role |
| [**update15**](RolesApi.md#update15) | **PUT** /api/v1/tenants/{ressourceTenant}/roles/{id} | Update a role |
| [**update26**](RolesApi.md#update26) | **PUT** /api/v1/{tenant}/roles/{id} | Update a role |
| [**update29**](RolesApi.md#update29) | **PUT** /api/v1/{tenant}/tenants/roles/{id} | Update a role |
| [**update33**](RolesApi.md#update33) | **PUT** /api/v1/{tenant}/tenants/{ressourceTenant}/roles/{id} | Update a role |
| [**update8**](RolesApi.md#update8) | **PUT** /api/v1/roles/{id} | Update a role |



## autocomplete14

> List&lt;Role&gt; autocomplete14(tenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete14(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete14");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_14 200 response |  -  |


## autocomplete17

> List&lt;Role&gt; autocomplete17(tenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete17(tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete17");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_17 200 response |  -  |


## autocomplete2

> List&lt;Role&gt; autocomplete2(apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete2(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete2");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_2 200 response |  -  |


## autocomplete21

> List&lt;Role&gt; autocomplete21(ressourceTenant, tenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete21(ressourceTenant, tenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete21");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_21 200 response |  -  |


## autocomplete5

> List&lt;Role&gt; autocomplete5(apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete5(apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete5");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_5 200 response |  -  |


## autocomplete9

> List&lt;Role&gt; autocomplete9(ressourceTenant, apiAutocomplete)

List roles for autocomplete

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        ApiAutocomplete apiAutocomplete = new ApiAutocomplete(); // ApiAutocomplete | 
        try {
            List<Role> result = apiInstance.autocomplete9(ressourceTenant, apiAutocomplete);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#autocomplete9");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | autocomplete_9 200 response |  -  |


## create11

> Role create11(role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create11(role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create11");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_11 200 response |  -  |


## create18

> Role create18(role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create18(role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create18");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_18 200 response |  -  |


## create23

> Role create23(ressourceTenant, role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create23(ressourceTenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create23");
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
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_23 200 response |  -  |


## create36

> Role create36(tenant, role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create36(tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create36");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_36 200 response |  -  |


## create43

> Role create43(tenant, role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create43(tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create43");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_43 200 response |  -  |


## create48

> Role create48(ressourceTenant, tenant, role)

Create a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.create48(ressourceTenant, tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#create48");
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
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | create_48 200 response |  -  |


## delete14

> delete14(id)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            apiInstance.delete14(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete14");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete20

> delete20(id)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            apiInstance.delete20(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete20");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete26

> delete26(id, ressourceTenant)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            apiInstance.delete26(id, ressourceTenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete26");
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


## delete42

> delete42(id, tenant)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete42(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete42");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete48

> delete48(id, tenant)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete48(id, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete48");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | On success |  -  |


## delete54

> delete54(id, ressourceTenant, tenant)

Delete a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            apiInstance.delete54(id, ressourceTenant, tenant);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#delete54");
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


## find12

> PagedResultsRole find12(page, size, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find12(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find12");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_12 200 response |  -  |


## find17

> PagedResultsRole find17(page, size, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find17(page, size, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find17");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_17 200 response |  -  |


## find23

> PagedResultsRole find23(page, size, ressourceTenant, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find23(page, size, ressourceTenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find23");
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

[**PagedResultsRole**](PagedResultsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_23 200 response |  -  |


## find38

> PagedResultsRole find38(page, size, tenant, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find38(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find38");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_38 200 response |  -  |


## find43

> PagedResultsRole find43(page, size, tenant, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find43(page, size, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find43");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_43 200 response |  -  |


## find49

> PagedResultsRole find49(page, size, ressourceTenant, tenant, q, sort)

Search for roles

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        Integer page = 1; // Integer | The current page
        Integer size = 10; // Integer | The current page size
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        String q = "q_example"; // String | A string filter
        List<String> sort = Arrays.asList(); // List<String> | The sort of current page
        try {
            PagedResultsRole result = apiInstance.find49(page, size, ressourceTenant, tenant, q, sort);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#find49");
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

[**PagedResultsRole**](PagedResultsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | find_49 200 response |  -  |


## ids1

> List&lt;Role&gt; ids1(apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids1(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids1");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_1 200 response |  -  |


## ids11

> List&lt;Role&gt; ids11(ressourceTenant, tenant, apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids11(ressourceTenant, tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids11");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_11 200 response |  -  |


## ids3

> List&lt;Role&gt; ids3(apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids3(apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids3");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_3 200 response |  -  |


## ids5

> List&lt;Role&gt; ids5(ressourceTenant, apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String ressourceTenant = "ressourceTenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids5(ressourceTenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids5");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_5 200 response |  -  |


## ids7

> List&lt;Role&gt; ids7(tenant, apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids7(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids7");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_7 200 response |  -  |


## ids9

> List&lt;Role&gt; ids9(tenant, apiIds)



List roles by ids

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String tenant = "tenant_example"; // String | 
        ApiIds apiIds = new ApiIds(); // ApiIds | 
        try {
            List<Role> result = apiInstance.ids9(tenant, apiIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#ids9");
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

[**List&lt;Role&gt;**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ids_9 200 response |  -  |


## index12

> Role index12(id)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            Role result = apiInstance.index12(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index12");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_12 200 response |  -  |


## index17

> Role index17(id, ressourceTenant)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        try {
            Role result = apiInstance.index17(id, ressourceTenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index17");
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
| **ressourceTenant** | **String**|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_17 200 response |  -  |


## index28

> Role index28(id, tenant)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        try {
            Role result = apiInstance.index28(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index28");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_28 200 response |  -  |


## index33

> Role index33(id, tenant)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        try {
            Role result = apiInstance.index33(id, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index33");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_33 200 response |  -  |


## index38

> Role index38(id, ressourceTenant, tenant)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        try {
            Role result = apiInstance.index38(id, ressourceTenant, tenant);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index38");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_38 200 response |  -  |


## index7

> Role index7(id)

Get a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        try {
            Role result = apiInstance.index7(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#index7");
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | index_7 200 response |  -  |


## update11

> Role update11(id, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update11(id, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update11");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_11 200 response |  -  |


## update15

> Role update15(id, ressourceTenant, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update15(id, ressourceTenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update15");
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
| **ressourceTenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_15 200 response |  -  |


## update26

> Role update26(id, tenant, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update26(id, tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update26");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_26 200 response |  -  |


## update29

> Role update29(id, tenant, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update29(id, tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update29");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_29 200 response |  -  |


## update33

> Role update33(id, ressourceTenant, tenant, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        String ressourceTenant = "ressourceTenant_example"; // String | 
        String tenant = "tenant_example"; // String | 
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update33(id, ressourceTenant, tenant, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update33");
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
| **ressourceTenant** | **String**|  | |
| **tenant** | **String**|  | |
| **role** | [**Role**](Role.md)|  | |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_33 200 response |  -  |


## update8

> Role update8(id, role)

Update a role

### Example

```java
// Import classes:
import io.kestra.api.sdk.internal.ApiClient;
import io.kestra.api.sdk.internal.ApiException;
import io.kestra.api.sdk.internal.Configuration;
import io.kestra.api.sdk.internal.models.*;
import io.kestra.api.sdk.api.RolesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("http://localhost");

        RolesApi apiInstance = new RolesApi(defaultClient);
        String id = "id_example"; // String | The role id
        Role role = new Role(); // Role | 
        try {
            Role result = apiInstance.update8(id, role);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RolesApi#update8");
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | update_8 200 response |  -  |

