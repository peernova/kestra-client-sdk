# MiscControllerLicenseInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to **string** |  | [optional] 
**Expiry** | Pointer to **time.Time** |  | [optional] 
**Expired** | Pointer to **bool** |  | [optional] 

## Methods

### NewMiscControllerLicenseInfo

`func NewMiscControllerLicenseInfo() *MiscControllerLicenseInfo`

NewMiscControllerLicenseInfo instantiates a new MiscControllerLicenseInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMiscControllerLicenseInfoWithDefaults

`func NewMiscControllerLicenseInfoWithDefaults() *MiscControllerLicenseInfo`

NewMiscControllerLicenseInfoWithDefaults instantiates a new MiscControllerLicenseInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *MiscControllerLicenseInfo) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *MiscControllerLicenseInfo) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *MiscControllerLicenseInfo) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *MiscControllerLicenseInfo) HasType() bool`

HasType returns a boolean if a field has been set.

### GetExpiry

`func (o *MiscControllerLicenseInfo) GetExpiry() time.Time`

GetExpiry returns the Expiry field if non-nil, zero value otherwise.

### GetExpiryOk

`func (o *MiscControllerLicenseInfo) GetExpiryOk() (*time.Time, bool)`

GetExpiryOk returns a tuple with the Expiry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiry

`func (o *MiscControllerLicenseInfo) SetExpiry(v time.Time)`

SetExpiry sets Expiry field to given value.

### HasExpiry

`func (o *MiscControllerLicenseInfo) HasExpiry() bool`

HasExpiry returns a boolean if a field has been set.

### GetExpired

`func (o *MiscControllerLicenseInfo) GetExpired() bool`

GetExpired returns the Expired field if non-nil, zero value otherwise.

### GetExpiredOk

`func (o *MiscControllerLicenseInfo) GetExpiredOk() (*bool, bool)`

GetExpiredOk returns a tuple with the Expired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpired

`func (o *MiscControllerLicenseInfo) SetExpired(v bool)`

SetExpired sets Expired field to given value.

### HasExpired

`func (o *MiscControllerLicenseInfo) HasExpired() bool`

HasExpired returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


