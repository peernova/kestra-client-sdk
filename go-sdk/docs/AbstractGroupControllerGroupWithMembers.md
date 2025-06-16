# AbstractGroupControllerGroupWithMembers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Deleted** | **bool** |  | 
**Provider** | Pointer to [**IdentityProvider**](IdentityProvider.md) |  | [optional] 
**MembersId** | Pointer to **[]string** |  | [optional] 

## Methods

### NewAbstractGroupControllerGroupWithMembers

`func NewAbstractGroupControllerGroupWithMembers(name string, deleted bool, ) *AbstractGroupControllerGroupWithMembers`

NewAbstractGroupControllerGroupWithMembers instantiates a new AbstractGroupControllerGroupWithMembers object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAbstractGroupControllerGroupWithMembersWithDefaults

`func NewAbstractGroupControllerGroupWithMembersWithDefaults() *AbstractGroupControllerGroupWithMembers`

NewAbstractGroupControllerGroupWithMembersWithDefaults instantiates a new AbstractGroupControllerGroupWithMembers object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AbstractGroupControllerGroupWithMembers) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AbstractGroupControllerGroupWithMembers) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AbstractGroupControllerGroupWithMembers) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *AbstractGroupControllerGroupWithMembers) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *AbstractGroupControllerGroupWithMembers) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AbstractGroupControllerGroupWithMembers) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AbstractGroupControllerGroupWithMembers) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *AbstractGroupControllerGroupWithMembers) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AbstractGroupControllerGroupWithMembers) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AbstractGroupControllerGroupWithMembers) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AbstractGroupControllerGroupWithMembers) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetDeleted

`func (o *AbstractGroupControllerGroupWithMembers) GetDeleted() bool`

GetDeleted returns the Deleted field if non-nil, zero value otherwise.

### GetDeletedOk

`func (o *AbstractGroupControllerGroupWithMembers) GetDeletedOk() (*bool, bool)`

GetDeletedOk returns a tuple with the Deleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeleted

`func (o *AbstractGroupControllerGroupWithMembers) SetDeleted(v bool)`

SetDeleted sets Deleted field to given value.


### GetProvider

`func (o *AbstractGroupControllerGroupWithMembers) GetProvider() IdentityProvider`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *AbstractGroupControllerGroupWithMembers) GetProviderOk() (*IdentityProvider, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *AbstractGroupControllerGroupWithMembers) SetProvider(v IdentityProvider)`

SetProvider sets Provider field to given value.

### HasProvider

`func (o *AbstractGroupControllerGroupWithMembers) HasProvider() bool`

HasProvider returns a boolean if a field has been set.

### GetMembersId

`func (o *AbstractGroupControllerGroupWithMembers) GetMembersId() []string`

GetMembersId returns the MembersId field if non-nil, zero value otherwise.

### GetMembersIdOk

`func (o *AbstractGroupControllerGroupWithMembers) GetMembersIdOk() (*[]string, bool)`

GetMembersIdOk returns a tuple with the MembersId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembersId

`func (o *AbstractGroupControllerGroupWithMembers) SetMembersId(v []string)`

SetMembersId sets MembersId field to given value.

### HasMembersId

`func (o *AbstractGroupControllerGroupWithMembers) HasMembersId() bool`

HasMembersId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


