# AuditLogDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**Cls** | **string** |  | 
**Permission** | [**Permission**](Permission.md) |  | 
**Id** | Pointer to **string** |  | [optional] 

## Methods

### NewAuditLogDetail

`func NewAuditLogDetail(type_ string, cls string, permission Permission, ) *AuditLogDetail`

NewAuditLogDetail instantiates a new AuditLogDetail object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuditLogDetailWithDefaults

`func NewAuditLogDetailWithDefaults() *AuditLogDetail`

NewAuditLogDetailWithDefaults instantiates a new AuditLogDetail object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *AuditLogDetail) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AuditLogDetail) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AuditLogDetail) SetType(v string)`

SetType sets Type field to given value.


### GetCls

`func (o *AuditLogDetail) GetCls() string`

GetCls returns the Cls field if non-nil, zero value otherwise.

### GetClsOk

`func (o *AuditLogDetail) GetClsOk() (*string, bool)`

GetClsOk returns a tuple with the Cls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCls

`func (o *AuditLogDetail) SetCls(v string)`

SetCls sets Cls field to given value.


### GetPermission

`func (o *AuditLogDetail) GetPermission() Permission`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *AuditLogDetail) GetPermissionOk() (*Permission, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *AuditLogDetail) SetPermission(v Permission)`

SetPermission sets Permission field to given value.


### GetId

`func (o *AuditLogDetail) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AuditLogDetail) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AuditLogDetail) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *AuditLogDetail) HasId() bool`

HasId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


