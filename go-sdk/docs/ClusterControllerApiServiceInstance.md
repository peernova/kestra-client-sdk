# ClusterControllerApiServiceInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Type** | Pointer to [**ServiceType**](ServiceType.md) |  | [optional] 
**State** | Pointer to [**ServiceServiceState**](ServiceServiceState.md) |  | [optional] 
**Server** | Pointer to [**ClusterControllerApiServerInstance**](ClusterControllerApiServerInstance.md) |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewClusterControllerApiServiceInstance

`func NewClusterControllerApiServiceInstance() *ClusterControllerApiServiceInstance`

NewClusterControllerApiServiceInstance instantiates a new ClusterControllerApiServiceInstance object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClusterControllerApiServiceInstanceWithDefaults

`func NewClusterControllerApiServiceInstanceWithDefaults() *ClusterControllerApiServiceInstance`

NewClusterControllerApiServiceInstanceWithDefaults instantiates a new ClusterControllerApiServiceInstance object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ClusterControllerApiServiceInstance) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ClusterControllerApiServiceInstance) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ClusterControllerApiServiceInstance) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *ClusterControllerApiServiceInstance) HasId() bool`

HasId returns a boolean if a field has been set.

### GetType

`func (o *ClusterControllerApiServiceInstance) GetType() ServiceType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ClusterControllerApiServiceInstance) GetTypeOk() (*ServiceType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ClusterControllerApiServiceInstance) SetType(v ServiceType)`

SetType sets Type field to given value.

### HasType

`func (o *ClusterControllerApiServiceInstance) HasType() bool`

HasType returns a boolean if a field has been set.

### GetState

`func (o *ClusterControllerApiServiceInstance) GetState() ServiceServiceState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ClusterControllerApiServiceInstance) GetStateOk() (*ServiceServiceState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ClusterControllerApiServiceInstance) SetState(v ServiceServiceState)`

SetState sets State field to given value.

### HasState

`func (o *ClusterControllerApiServiceInstance) HasState() bool`

HasState returns a boolean if a field has been set.

### GetServer

`func (o *ClusterControllerApiServiceInstance) GetServer() ClusterControllerApiServerInstance`

GetServer returns the Server field if non-nil, zero value otherwise.

### GetServerOk

`func (o *ClusterControllerApiServiceInstance) GetServerOk() (*ClusterControllerApiServerInstance, bool)`

GetServerOk returns a tuple with the Server field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServer

`func (o *ClusterControllerApiServiceInstance) SetServer(v ClusterControllerApiServerInstance)`

SetServer sets Server field to given value.

### HasServer

`func (o *ClusterControllerApiServiceInstance) HasServer() bool`

HasServer returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ClusterControllerApiServiceInstance) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ClusterControllerApiServiceInstance) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ClusterControllerApiServiceInstance) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *ClusterControllerApiServiceInstance) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *ClusterControllerApiServiceInstance) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ClusterControllerApiServiceInstance) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ClusterControllerApiServiceInstance) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *ClusterControllerApiServiceInstance) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


