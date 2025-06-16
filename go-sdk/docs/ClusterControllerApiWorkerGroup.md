# ClusterControllerApiWorkerGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | The ID of worker group. | [optional] 
**Key** | Pointer to **string** | The key of the worker group. | [optional] 
**Description** | Pointer to **string** | The description of the worker group. | [optional] 
**AllowedTenants** | Pointer to **[]string** |  | [optional] 

## Methods

### NewClusterControllerApiWorkerGroup

`func NewClusterControllerApiWorkerGroup() *ClusterControllerApiWorkerGroup`

NewClusterControllerApiWorkerGroup instantiates a new ClusterControllerApiWorkerGroup object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClusterControllerApiWorkerGroupWithDefaults

`func NewClusterControllerApiWorkerGroupWithDefaults() *ClusterControllerApiWorkerGroup`

NewClusterControllerApiWorkerGroupWithDefaults instantiates a new ClusterControllerApiWorkerGroup object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ClusterControllerApiWorkerGroup) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ClusterControllerApiWorkerGroup) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ClusterControllerApiWorkerGroup) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *ClusterControllerApiWorkerGroup) HasId() bool`

HasId returns a boolean if a field has been set.

### GetKey

`func (o *ClusterControllerApiWorkerGroup) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *ClusterControllerApiWorkerGroup) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *ClusterControllerApiWorkerGroup) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *ClusterControllerApiWorkerGroup) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetDescription

`func (o *ClusterControllerApiWorkerGroup) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ClusterControllerApiWorkerGroup) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ClusterControllerApiWorkerGroup) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ClusterControllerApiWorkerGroup) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetAllowedTenants

`func (o *ClusterControllerApiWorkerGroup) GetAllowedTenants() []string`

GetAllowedTenants returns the AllowedTenants field if non-nil, zero value otherwise.

### GetAllowedTenantsOk

`func (o *ClusterControllerApiWorkerGroup) GetAllowedTenantsOk() (*[]string, bool)`

GetAllowedTenantsOk returns a tuple with the AllowedTenants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowedTenants

`func (o *ClusterControllerApiWorkerGroup) SetAllowedTenants(v []string)`

SetAllowedTenants sets AllowedTenants field to given value.

### HasAllowedTenants

`func (o *ClusterControllerApiWorkerGroup) HasAllowedTenants() bool`

HasAllowedTenants returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


