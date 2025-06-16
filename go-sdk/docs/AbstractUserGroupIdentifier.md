# AbstractUserGroupIdentifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TenantId** | Pointer to **NullableString** |  | [optional] 
**GroupId** | Pointer to **string** |  | [optional] 
**Membership** | Pointer to [**AbstractUserGroupIdentifierMembership**](AbstractUserGroupIdentifierMembership.md) |  | [optional] 
**ManagedExternally** | Pointer to **bool** |  | [optional] 

## Methods

### NewAbstractUserGroupIdentifier

`func NewAbstractUserGroupIdentifier() *AbstractUserGroupIdentifier`

NewAbstractUserGroupIdentifier instantiates a new AbstractUserGroupIdentifier object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAbstractUserGroupIdentifierWithDefaults

`func NewAbstractUserGroupIdentifierWithDefaults() *AbstractUserGroupIdentifier`

NewAbstractUserGroupIdentifierWithDefaults instantiates a new AbstractUserGroupIdentifier object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTenantId

`func (o *AbstractUserGroupIdentifier) GetTenantId() string`

GetTenantId returns the TenantId field if non-nil, zero value otherwise.

### GetTenantIdOk

`func (o *AbstractUserGroupIdentifier) GetTenantIdOk() (*string, bool)`

GetTenantIdOk returns a tuple with the TenantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenantId

`func (o *AbstractUserGroupIdentifier) SetTenantId(v string)`

SetTenantId sets TenantId field to given value.

### HasTenantId

`func (o *AbstractUserGroupIdentifier) HasTenantId() bool`

HasTenantId returns a boolean if a field has been set.

### SetTenantIdNil

`func (o *AbstractUserGroupIdentifier) SetTenantIdNil(b bool)`

 SetTenantIdNil sets the value for TenantId to be an explicit nil

### UnsetTenantId
`func (o *AbstractUserGroupIdentifier) UnsetTenantId()`

UnsetTenantId ensures that no value is present for TenantId, not even an explicit nil
### GetGroupId

`func (o *AbstractUserGroupIdentifier) GetGroupId() string`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *AbstractUserGroupIdentifier) GetGroupIdOk() (*string, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *AbstractUserGroupIdentifier) SetGroupId(v string)`

SetGroupId sets GroupId field to given value.

### HasGroupId

`func (o *AbstractUserGroupIdentifier) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### GetMembership

`func (o *AbstractUserGroupIdentifier) GetMembership() AbstractUserGroupIdentifierMembership`

GetMembership returns the Membership field if non-nil, zero value otherwise.

### GetMembershipOk

`func (o *AbstractUserGroupIdentifier) GetMembershipOk() (*AbstractUserGroupIdentifierMembership, bool)`

GetMembershipOk returns a tuple with the Membership field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembership

`func (o *AbstractUserGroupIdentifier) SetMembership(v AbstractUserGroupIdentifierMembership)`

SetMembership sets Membership field to given value.

### HasMembership

`func (o *AbstractUserGroupIdentifier) HasMembership() bool`

HasMembership returns a boolean if a field has been set.

### GetManagedExternally

`func (o *AbstractUserGroupIdentifier) GetManagedExternally() bool`

GetManagedExternally returns the ManagedExternally field if non-nil, zero value otherwise.

### GetManagedExternallyOk

`func (o *AbstractUserGroupIdentifier) GetManagedExternallyOk() (*bool, bool)`

GetManagedExternallyOk returns a tuple with the ManagedExternally field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManagedExternally

`func (o *AbstractUserGroupIdentifier) SetManagedExternally(v bool)`

SetManagedExternally sets ManagedExternally field to given value.

### HasManagedExternally

`func (o *AbstractUserGroupIdentifier) HasManagedExternally() bool`

HasManagedExternally returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


