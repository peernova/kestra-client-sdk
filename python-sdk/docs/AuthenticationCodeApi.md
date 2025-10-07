# kestrapy.AuthenticationCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_code**](AuthenticationCodeApi.md#request_code) | **GET** /api/v1/request-code/{email} | Request an authentication code for login verification


# **request_code**
> object request_code(email)

Request an authentication code for login verification

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
    api_instance = kestrapy.AuthenticationCodeApi(api_client)
    email = 'email_example' # str | 

    try:
        # Request an authentication code for login verification
        api_response = api_instance.request_code(email)
        print("The response of AuthenticationCodeApi->request_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationCodeApi->request_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | requestCode 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

