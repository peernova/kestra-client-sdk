# RolePermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FLOW** | Pointer to **[]string** |  | [optional] 
**BLUEPRINT** | Pointer to **[]string** |  | [optional] 
**TEMPLATE** | Pointer to **[]string** |  | [optional] 
**NAMESPACE** | Pointer to **[]string** |  | [optional] 
**EXECUTION** | Pointer to **[]string** |  | [optional] 
**USER** | Pointer to **[]string** |  | [optional] 
**GROUP** | Pointer to **[]string** |  | [optional] 
**ROLE** | Pointer to **[]string** |  | [optional] 
**BINDING** | Pointer to **[]string** |  | [optional] 
**AUDITLOG** | Pointer to **[]string** |  | [optional] 
**SECRET** | Pointer to **[]string** |  | [optional] 
**KVSTORE** | Pointer to **[]string** |  | [optional] 
**IMPERSONATE** | Pointer to **[]string** |  | [optional] 
**SETTING** | Pointer to **[]string** |  | [optional] 
**INFRASTRUCTURE** | Pointer to **[]string** |  | [optional] 
**APP** | Pointer to **[]string** |  | [optional] 
**APPEXECUTION** | Pointer to **[]string** |  | [optional] 
**TEST** | Pointer to **[]string** |  | [optional] 
**ME** | Pointer to **[]string** |  | [optional] 
**APITOKEN** | Pointer to **[]string** |  | [optional] 
**DASHBOARD** | Pointer to **[]string** |  | [optional] 
**TENANT** | Pointer to **[]string** |  | [optional] 
**UNKNOWN** | Pointer to **[]string** |  | [optional] 

## Methods

### NewRolePermissions

`func NewRolePermissions() *RolePermissions`

NewRolePermissions instantiates a new RolePermissions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRolePermissionsWithDefaults

`func NewRolePermissionsWithDefaults() *RolePermissions`

NewRolePermissionsWithDefaults instantiates a new RolePermissions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFLOW

`func (o *RolePermissions) GetFLOW() []string`

GetFLOW returns the FLOW field if non-nil, zero value otherwise.

### GetFLOWOk

`func (o *RolePermissions) GetFLOWOk() (*[]string, bool)`

GetFLOWOk returns a tuple with the FLOW field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFLOW

`func (o *RolePermissions) SetFLOW(v []string)`

SetFLOW sets FLOW field to given value.

### HasFLOW

`func (o *RolePermissions) HasFLOW() bool`

HasFLOW returns a boolean if a field has been set.

### GetBLUEPRINT

`func (o *RolePermissions) GetBLUEPRINT() []string`

GetBLUEPRINT returns the BLUEPRINT field if non-nil, zero value otherwise.

### GetBLUEPRINTOk

`func (o *RolePermissions) GetBLUEPRINTOk() (*[]string, bool)`

GetBLUEPRINTOk returns a tuple with the BLUEPRINT field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBLUEPRINT

`func (o *RolePermissions) SetBLUEPRINT(v []string)`

SetBLUEPRINT sets BLUEPRINT field to given value.

### HasBLUEPRINT

`func (o *RolePermissions) HasBLUEPRINT() bool`

HasBLUEPRINT returns a boolean if a field has been set.

### GetTEMPLATE

`func (o *RolePermissions) GetTEMPLATE() []string`

GetTEMPLATE returns the TEMPLATE field if non-nil, zero value otherwise.

### GetTEMPLATEOk

`func (o *RolePermissions) GetTEMPLATEOk() (*[]string, bool)`

GetTEMPLATEOk returns a tuple with the TEMPLATE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTEMPLATE

`func (o *RolePermissions) SetTEMPLATE(v []string)`

SetTEMPLATE sets TEMPLATE field to given value.

### HasTEMPLATE

`func (o *RolePermissions) HasTEMPLATE() bool`

HasTEMPLATE returns a boolean if a field has been set.

### GetNAMESPACE

`func (o *RolePermissions) GetNAMESPACE() []string`

GetNAMESPACE returns the NAMESPACE field if non-nil, zero value otherwise.

### GetNAMESPACEOk

`func (o *RolePermissions) GetNAMESPACEOk() (*[]string, bool)`

GetNAMESPACEOk returns a tuple with the NAMESPACE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNAMESPACE

`func (o *RolePermissions) SetNAMESPACE(v []string)`

SetNAMESPACE sets NAMESPACE field to given value.

### HasNAMESPACE

`func (o *RolePermissions) HasNAMESPACE() bool`

HasNAMESPACE returns a boolean if a field has been set.

### GetEXECUTION

`func (o *RolePermissions) GetEXECUTION() []string`

GetEXECUTION returns the EXECUTION field if non-nil, zero value otherwise.

### GetEXECUTIONOk

`func (o *RolePermissions) GetEXECUTIONOk() (*[]string, bool)`

GetEXECUTIONOk returns a tuple with the EXECUTION field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEXECUTION

`func (o *RolePermissions) SetEXECUTION(v []string)`

SetEXECUTION sets EXECUTION field to given value.

### HasEXECUTION

`func (o *RolePermissions) HasEXECUTION() bool`

HasEXECUTION returns a boolean if a field has been set.

### GetUSER

`func (o *RolePermissions) GetUSER() []string`

GetUSER returns the USER field if non-nil, zero value otherwise.

### GetUSEROk

`func (o *RolePermissions) GetUSEROk() (*[]string, bool)`

GetUSEROk returns a tuple with the USER field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUSER

`func (o *RolePermissions) SetUSER(v []string)`

SetUSER sets USER field to given value.

### HasUSER

`func (o *RolePermissions) HasUSER() bool`

HasUSER returns a boolean if a field has been set.

### GetGROUP

`func (o *RolePermissions) GetGROUP() []string`

GetGROUP returns the GROUP field if non-nil, zero value otherwise.

### GetGROUPOk

`func (o *RolePermissions) GetGROUPOk() (*[]string, bool)`

GetGROUPOk returns a tuple with the GROUP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGROUP

`func (o *RolePermissions) SetGROUP(v []string)`

SetGROUP sets GROUP field to given value.

### HasGROUP

`func (o *RolePermissions) HasGROUP() bool`

HasGROUP returns a boolean if a field has been set.

### GetROLE

`func (o *RolePermissions) GetROLE() []string`

GetROLE returns the ROLE field if non-nil, zero value otherwise.

### GetROLEOk

`func (o *RolePermissions) GetROLEOk() (*[]string, bool)`

GetROLEOk returns a tuple with the ROLE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetROLE

`func (o *RolePermissions) SetROLE(v []string)`

SetROLE sets ROLE field to given value.

### HasROLE

`func (o *RolePermissions) HasROLE() bool`

HasROLE returns a boolean if a field has been set.

### GetBINDING

`func (o *RolePermissions) GetBINDING() []string`

GetBINDING returns the BINDING field if non-nil, zero value otherwise.

### GetBINDINGOk

`func (o *RolePermissions) GetBINDINGOk() (*[]string, bool)`

GetBINDINGOk returns a tuple with the BINDING field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBINDING

`func (o *RolePermissions) SetBINDING(v []string)`

SetBINDING sets BINDING field to given value.

### HasBINDING

`func (o *RolePermissions) HasBINDING() bool`

HasBINDING returns a boolean if a field has been set.

### GetAUDITLOG

`func (o *RolePermissions) GetAUDITLOG() []string`

GetAUDITLOG returns the AUDITLOG field if non-nil, zero value otherwise.

### GetAUDITLOGOk

`func (o *RolePermissions) GetAUDITLOGOk() (*[]string, bool)`

GetAUDITLOGOk returns a tuple with the AUDITLOG field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAUDITLOG

`func (o *RolePermissions) SetAUDITLOG(v []string)`

SetAUDITLOG sets AUDITLOG field to given value.

### HasAUDITLOG

`func (o *RolePermissions) HasAUDITLOG() bool`

HasAUDITLOG returns a boolean if a field has been set.

### GetSECRET

`func (o *RolePermissions) GetSECRET() []string`

GetSECRET returns the SECRET field if non-nil, zero value otherwise.

### GetSECRETOk

`func (o *RolePermissions) GetSECRETOk() (*[]string, bool)`

GetSECRETOk returns a tuple with the SECRET field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSECRET

`func (o *RolePermissions) SetSECRET(v []string)`

SetSECRET sets SECRET field to given value.

### HasSECRET

`func (o *RolePermissions) HasSECRET() bool`

HasSECRET returns a boolean if a field has been set.

### GetKVSTORE

`func (o *RolePermissions) GetKVSTORE() []string`

GetKVSTORE returns the KVSTORE field if non-nil, zero value otherwise.

### GetKVSTOREOk

`func (o *RolePermissions) GetKVSTOREOk() (*[]string, bool)`

GetKVSTOREOk returns a tuple with the KVSTORE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKVSTORE

`func (o *RolePermissions) SetKVSTORE(v []string)`

SetKVSTORE sets KVSTORE field to given value.

### HasKVSTORE

`func (o *RolePermissions) HasKVSTORE() bool`

HasKVSTORE returns a boolean if a field has been set.

### GetIMPERSONATE

`func (o *RolePermissions) GetIMPERSONATE() []string`

GetIMPERSONATE returns the IMPERSONATE field if non-nil, zero value otherwise.

### GetIMPERSONATEOk

`func (o *RolePermissions) GetIMPERSONATEOk() (*[]string, bool)`

GetIMPERSONATEOk returns a tuple with the IMPERSONATE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIMPERSONATE

`func (o *RolePermissions) SetIMPERSONATE(v []string)`

SetIMPERSONATE sets IMPERSONATE field to given value.

### HasIMPERSONATE

`func (o *RolePermissions) HasIMPERSONATE() bool`

HasIMPERSONATE returns a boolean if a field has been set.

### GetSETTING

`func (o *RolePermissions) GetSETTING() []string`

GetSETTING returns the SETTING field if non-nil, zero value otherwise.

### GetSETTINGOk

`func (o *RolePermissions) GetSETTINGOk() (*[]string, bool)`

GetSETTINGOk returns a tuple with the SETTING field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSETTING

`func (o *RolePermissions) SetSETTING(v []string)`

SetSETTING sets SETTING field to given value.

### HasSETTING

`func (o *RolePermissions) HasSETTING() bool`

HasSETTING returns a boolean if a field has been set.

### GetINFRASTRUCTURE

`func (o *RolePermissions) GetINFRASTRUCTURE() []string`

GetINFRASTRUCTURE returns the INFRASTRUCTURE field if non-nil, zero value otherwise.

### GetINFRASTRUCTUREOk

`func (o *RolePermissions) GetINFRASTRUCTUREOk() (*[]string, bool)`

GetINFRASTRUCTUREOk returns a tuple with the INFRASTRUCTURE field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetINFRASTRUCTURE

`func (o *RolePermissions) SetINFRASTRUCTURE(v []string)`

SetINFRASTRUCTURE sets INFRASTRUCTURE field to given value.

### HasINFRASTRUCTURE

`func (o *RolePermissions) HasINFRASTRUCTURE() bool`

HasINFRASTRUCTURE returns a boolean if a field has been set.

### GetAPP

`func (o *RolePermissions) GetAPP() []string`

GetAPP returns the APP field if non-nil, zero value otherwise.

### GetAPPOk

`func (o *RolePermissions) GetAPPOk() (*[]string, bool)`

GetAPPOk returns a tuple with the APP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAPP

`func (o *RolePermissions) SetAPP(v []string)`

SetAPP sets APP field to given value.

### HasAPP

`func (o *RolePermissions) HasAPP() bool`

HasAPP returns a boolean if a field has been set.

### GetAPPEXECUTION

`func (o *RolePermissions) GetAPPEXECUTION() []string`

GetAPPEXECUTION returns the APPEXECUTION field if non-nil, zero value otherwise.

### GetAPPEXECUTIONOk

`func (o *RolePermissions) GetAPPEXECUTIONOk() (*[]string, bool)`

GetAPPEXECUTIONOk returns a tuple with the APPEXECUTION field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAPPEXECUTION

`func (o *RolePermissions) SetAPPEXECUTION(v []string)`

SetAPPEXECUTION sets APPEXECUTION field to given value.

### HasAPPEXECUTION

`func (o *RolePermissions) HasAPPEXECUTION() bool`

HasAPPEXECUTION returns a boolean if a field has been set.

### GetTEST

`func (o *RolePermissions) GetTEST() []string`

GetTEST returns the TEST field if non-nil, zero value otherwise.

### GetTESTOk

`func (o *RolePermissions) GetTESTOk() (*[]string, bool)`

GetTESTOk returns a tuple with the TEST field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTEST

`func (o *RolePermissions) SetTEST(v []string)`

SetTEST sets TEST field to given value.

### HasTEST

`func (o *RolePermissions) HasTEST() bool`

HasTEST returns a boolean if a field has been set.

### GetME

`func (o *RolePermissions) GetME() []string`

GetME returns the ME field if non-nil, zero value otherwise.

### GetMEOk

`func (o *RolePermissions) GetMEOk() (*[]string, bool)`

GetMEOk returns a tuple with the ME field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetME

`func (o *RolePermissions) SetME(v []string)`

SetME sets ME field to given value.

### HasME

`func (o *RolePermissions) HasME() bool`

HasME returns a boolean if a field has been set.

### GetAPITOKEN

`func (o *RolePermissions) GetAPITOKEN() []string`

GetAPITOKEN returns the APITOKEN field if non-nil, zero value otherwise.

### GetAPITOKENOk

`func (o *RolePermissions) GetAPITOKENOk() (*[]string, bool)`

GetAPITOKENOk returns a tuple with the APITOKEN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAPITOKEN

`func (o *RolePermissions) SetAPITOKEN(v []string)`

SetAPITOKEN sets APITOKEN field to given value.

### HasAPITOKEN

`func (o *RolePermissions) HasAPITOKEN() bool`

HasAPITOKEN returns a boolean if a field has been set.

### GetDASHBOARD

`func (o *RolePermissions) GetDASHBOARD() []string`

GetDASHBOARD returns the DASHBOARD field if non-nil, zero value otherwise.

### GetDASHBOARDOk

`func (o *RolePermissions) GetDASHBOARDOk() (*[]string, bool)`

GetDASHBOARDOk returns a tuple with the DASHBOARD field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDASHBOARD

`func (o *RolePermissions) SetDASHBOARD(v []string)`

SetDASHBOARD sets DASHBOARD field to given value.

### HasDASHBOARD

`func (o *RolePermissions) HasDASHBOARD() bool`

HasDASHBOARD returns a boolean if a field has been set.

### GetTENANT

`func (o *RolePermissions) GetTENANT() []string`

GetTENANT returns the TENANT field if non-nil, zero value otherwise.

### GetTENANTOk

`func (o *RolePermissions) GetTENANTOk() (*[]string, bool)`

GetTENANTOk returns a tuple with the TENANT field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTENANT

`func (o *RolePermissions) SetTENANT(v []string)`

SetTENANT sets TENANT field to given value.

### HasTENANT

`func (o *RolePermissions) HasTENANT() bool`

HasTENANT returns a boolean if a field has been set.

### GetUNKNOWN

`func (o *RolePermissions) GetUNKNOWN() []string`

GetUNKNOWN returns the UNKNOWN field if non-nil, zero value otherwise.

### GetUNKNOWNOk

`func (o *RolePermissions) GetUNKNOWNOk() (*[]string, bool)`

GetUNKNOWNOk returns a tuple with the UNKNOWN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUNKNOWN

`func (o *RolePermissions) SetUNKNOWN(v []string)`

SetUNKNOWN sets UNKNOWN field to given value.

### HasUNKNOWN

`func (o *RolePermissions) HasUNKNOWN() bool`

HasUNKNOWN returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


