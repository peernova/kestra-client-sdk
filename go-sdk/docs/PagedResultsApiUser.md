# PagedResultsApiUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**[]ApiUser**](ApiUser.md) |  | 
**Total** | **int64** |  | 

## Methods

### NewPagedResultsApiUser

`func NewPagedResultsApiUser(results []ApiUser, total int64, ) *PagedResultsApiUser`

NewPagedResultsApiUser instantiates a new PagedResultsApiUser object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPagedResultsApiUserWithDefaults

`func NewPagedResultsApiUserWithDefaults() *PagedResultsApiUser`

NewPagedResultsApiUserWithDefaults instantiates a new PagedResultsApiUser object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResults

`func (o *PagedResultsApiUser) GetResults() []ApiUser`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *PagedResultsApiUser) GetResultsOk() (*[]ApiUser, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *PagedResultsApiUser) SetResults(v []ApiUser)`

SetResults sets Results field to given value.


### GetTotal

`func (o *PagedResultsApiUser) GetTotal() int64`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *PagedResultsApiUser) GetTotalOk() (*int64, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *PagedResultsApiUser) SetTotal(v int64)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


