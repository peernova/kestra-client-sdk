# PagedResultsRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**[]Role**](Role.md) |  | 
**Total** | **int64** |  | 

## Methods

### NewPagedResultsRole

`func NewPagedResultsRole(results []Role, total int64, ) *PagedResultsRole`

NewPagedResultsRole instantiates a new PagedResultsRole object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPagedResultsRoleWithDefaults

`func NewPagedResultsRoleWithDefaults() *PagedResultsRole`

NewPagedResultsRoleWithDefaults instantiates a new PagedResultsRole object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResults

`func (o *PagedResultsRole) GetResults() []Role`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *PagedResultsRole) GetResultsOk() (*[]Role, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *PagedResultsRole) SetResults(v []Role)`

SetResults sets Results field to given value.


### GetTotal

`func (o *PagedResultsRole) GetTotal() int64`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *PagedResultsRole) GetTotalOk() (*int64, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *PagedResultsRole) SetTotal(v int64)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


