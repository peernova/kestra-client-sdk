# HostUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Uuid** | Pointer to **string** |  | [optional] 
**Hardware** | Pointer to [**HostUsageHardware**](HostUsageHardware.md) |  | [optional] 
**Os** | Pointer to [**HostUsageOs**](HostUsageOs.md) |  | [optional] 
**Jvm** | Pointer to [**HostUsageJvm**](HostUsageJvm.md) |  | [optional] 

## Methods

### NewHostUsage

`func NewHostUsage() *HostUsage`

NewHostUsage instantiates a new HostUsage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHostUsageWithDefaults

`func NewHostUsageWithDefaults() *HostUsage`

NewHostUsageWithDefaults instantiates a new HostUsage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUuid

`func (o *HostUsage) GetUuid() string`

GetUuid returns the Uuid field if non-nil, zero value otherwise.

### GetUuidOk

`func (o *HostUsage) GetUuidOk() (*string, bool)`

GetUuidOk returns a tuple with the Uuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUuid

`func (o *HostUsage) SetUuid(v string)`

SetUuid sets Uuid field to given value.

### HasUuid

`func (o *HostUsage) HasUuid() bool`

HasUuid returns a boolean if a field has been set.

### GetHardware

`func (o *HostUsage) GetHardware() HostUsageHardware`

GetHardware returns the Hardware field if non-nil, zero value otherwise.

### GetHardwareOk

`func (o *HostUsage) GetHardwareOk() (*HostUsageHardware, bool)`

GetHardwareOk returns a tuple with the Hardware field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHardware

`func (o *HostUsage) SetHardware(v HostUsageHardware)`

SetHardware sets Hardware field to given value.

### HasHardware

`func (o *HostUsage) HasHardware() bool`

HasHardware returns a boolean if a field has been set.

### GetOs

`func (o *HostUsage) GetOs() HostUsageOs`

GetOs returns the Os field if non-nil, zero value otherwise.

### GetOsOk

`func (o *HostUsage) GetOsOk() (*HostUsageOs, bool)`

GetOsOk returns a tuple with the Os field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOs

`func (o *HostUsage) SetOs(v HostUsageOs)`

SetOs sets Os field to given value.

### HasOs

`func (o *HostUsage) HasOs() bool`

HasOs returns a boolean if a field has been set.

### GetJvm

`func (o *HostUsage) GetJvm() HostUsageJvm`

GetJvm returns the Jvm field if non-nil, zero value otherwise.

### GetJvmOk

`func (o *HostUsage) GetJvmOk() (*HostUsageJvm, bool)`

GetJvmOk returns a tuple with the Jvm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJvm

`func (o *HostUsage) SetJvm(v HostUsageJvm)`

SetJvm sets Jvm field to given value.

### HasJvm

`func (o *HostUsage) HasJvm() bool`

HasJvm returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


