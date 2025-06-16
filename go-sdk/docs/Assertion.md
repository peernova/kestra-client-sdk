# Assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Value** | [**PropertyObject**](PropertyObject.md) |  | 
**TaskId** | Pointer to **string** |  | [optional] 
**ErrorMessage** | Pointer to [**PropertyString**](PropertyString.md) |  | [optional] 
**Description** | Pointer to [**PropertyString**](PropertyString.md) |  | [optional] 
**EndsWith** | Pointer to [**PropertyString**](PropertyString.md) |  | [optional] 
**StartsWith** | Pointer to [**PropertyString**](PropertyString.md) |  | [optional] 
**Contains** | Pointer to [**PropertyString**](PropertyString.md) |  | [optional] 
**EqualTo** | Pointer to [**PropertyObject**](PropertyObject.md) |  | [optional] 
**NotEqualTo** | Pointer to [**PropertyObject**](PropertyObject.md) |  | [optional] 
**GreaterThan** | Pointer to [**PropertyDouble**](PropertyDouble.md) |  | [optional] 
**GreaterThanOrEqualTo** | Pointer to [**PropertyDouble**](PropertyDouble.md) |  | [optional] 
**LessThan** | Pointer to [**PropertyDouble**](PropertyDouble.md) |  | [optional] 
**LessThanOrEqualTo** | Pointer to [**PropertyDouble**](PropertyDouble.md) |  | [optional] 
**In** | Pointer to [**PropertyListString**](PropertyListString.md) |  | [optional] 
**NotIn** | Pointer to [**PropertyListString**](PropertyListString.md) |  | [optional] 
**IsNull** | Pointer to [**PropertyBoolean**](PropertyBoolean.md) |  | [optional] 
**IsNotNull** | Pointer to [**PropertyBoolean**](PropertyBoolean.md) |  | [optional] 

## Methods

### NewAssertion

`func NewAssertion(value PropertyObject, ) *Assertion`

NewAssertion instantiates a new Assertion object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAssertionWithDefaults

`func NewAssertionWithDefaults() *Assertion`

NewAssertionWithDefaults instantiates a new Assertion object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetValue

`func (o *Assertion) GetValue() PropertyObject`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Assertion) GetValueOk() (*PropertyObject, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Assertion) SetValue(v PropertyObject)`

SetValue sets Value field to given value.


### GetTaskId

`func (o *Assertion) GetTaskId() string`

GetTaskId returns the TaskId field if non-nil, zero value otherwise.

### GetTaskIdOk

`func (o *Assertion) GetTaskIdOk() (*string, bool)`

GetTaskIdOk returns a tuple with the TaskId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaskId

`func (o *Assertion) SetTaskId(v string)`

SetTaskId sets TaskId field to given value.

### HasTaskId

`func (o *Assertion) HasTaskId() bool`

HasTaskId returns a boolean if a field has been set.

### GetErrorMessage

`func (o *Assertion) GetErrorMessage() PropertyString`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *Assertion) GetErrorMessageOk() (*PropertyString, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *Assertion) SetErrorMessage(v PropertyString)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *Assertion) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### GetDescription

`func (o *Assertion) GetDescription() PropertyString`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Assertion) GetDescriptionOk() (*PropertyString, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Assertion) SetDescription(v PropertyString)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Assertion) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEndsWith

`func (o *Assertion) GetEndsWith() PropertyString`

GetEndsWith returns the EndsWith field if non-nil, zero value otherwise.

### GetEndsWithOk

`func (o *Assertion) GetEndsWithOk() (*PropertyString, bool)`

GetEndsWithOk returns a tuple with the EndsWith field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndsWith

`func (o *Assertion) SetEndsWith(v PropertyString)`

SetEndsWith sets EndsWith field to given value.

### HasEndsWith

`func (o *Assertion) HasEndsWith() bool`

HasEndsWith returns a boolean if a field has been set.

### GetStartsWith

`func (o *Assertion) GetStartsWith() PropertyString`

GetStartsWith returns the StartsWith field if non-nil, zero value otherwise.

### GetStartsWithOk

`func (o *Assertion) GetStartsWithOk() (*PropertyString, bool)`

GetStartsWithOk returns a tuple with the StartsWith field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartsWith

`func (o *Assertion) SetStartsWith(v PropertyString)`

SetStartsWith sets StartsWith field to given value.

### HasStartsWith

`func (o *Assertion) HasStartsWith() bool`

HasStartsWith returns a boolean if a field has been set.

### GetContains

`func (o *Assertion) GetContains() PropertyString`

GetContains returns the Contains field if non-nil, zero value otherwise.

### GetContainsOk

`func (o *Assertion) GetContainsOk() (*PropertyString, bool)`

GetContainsOk returns a tuple with the Contains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContains

`func (o *Assertion) SetContains(v PropertyString)`

SetContains sets Contains field to given value.

### HasContains

`func (o *Assertion) HasContains() bool`

HasContains returns a boolean if a field has been set.

### GetEqualTo

`func (o *Assertion) GetEqualTo() PropertyObject`

GetEqualTo returns the EqualTo field if non-nil, zero value otherwise.

### GetEqualToOk

`func (o *Assertion) GetEqualToOk() (*PropertyObject, bool)`

GetEqualToOk returns a tuple with the EqualTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEqualTo

`func (o *Assertion) SetEqualTo(v PropertyObject)`

SetEqualTo sets EqualTo field to given value.

### HasEqualTo

`func (o *Assertion) HasEqualTo() bool`

HasEqualTo returns a boolean if a field has been set.

### GetNotEqualTo

`func (o *Assertion) GetNotEqualTo() PropertyObject`

GetNotEqualTo returns the NotEqualTo field if non-nil, zero value otherwise.

### GetNotEqualToOk

`func (o *Assertion) GetNotEqualToOk() (*PropertyObject, bool)`

GetNotEqualToOk returns a tuple with the NotEqualTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotEqualTo

`func (o *Assertion) SetNotEqualTo(v PropertyObject)`

SetNotEqualTo sets NotEqualTo field to given value.

### HasNotEqualTo

`func (o *Assertion) HasNotEqualTo() bool`

HasNotEqualTo returns a boolean if a field has been set.

### GetGreaterThan

`func (o *Assertion) GetGreaterThan() PropertyDouble`

GetGreaterThan returns the GreaterThan field if non-nil, zero value otherwise.

### GetGreaterThanOk

`func (o *Assertion) GetGreaterThanOk() (*PropertyDouble, bool)`

GetGreaterThanOk returns a tuple with the GreaterThan field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGreaterThan

`func (o *Assertion) SetGreaterThan(v PropertyDouble)`

SetGreaterThan sets GreaterThan field to given value.

### HasGreaterThan

`func (o *Assertion) HasGreaterThan() bool`

HasGreaterThan returns a boolean if a field has been set.

### GetGreaterThanOrEqualTo

`func (o *Assertion) GetGreaterThanOrEqualTo() PropertyDouble`

GetGreaterThanOrEqualTo returns the GreaterThanOrEqualTo field if non-nil, zero value otherwise.

### GetGreaterThanOrEqualToOk

`func (o *Assertion) GetGreaterThanOrEqualToOk() (*PropertyDouble, bool)`

GetGreaterThanOrEqualToOk returns a tuple with the GreaterThanOrEqualTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGreaterThanOrEqualTo

`func (o *Assertion) SetGreaterThanOrEqualTo(v PropertyDouble)`

SetGreaterThanOrEqualTo sets GreaterThanOrEqualTo field to given value.

### HasGreaterThanOrEqualTo

`func (o *Assertion) HasGreaterThanOrEqualTo() bool`

HasGreaterThanOrEqualTo returns a boolean if a field has been set.

### GetLessThan

`func (o *Assertion) GetLessThan() PropertyDouble`

GetLessThan returns the LessThan field if non-nil, zero value otherwise.

### GetLessThanOk

`func (o *Assertion) GetLessThanOk() (*PropertyDouble, bool)`

GetLessThanOk returns a tuple with the LessThan field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLessThan

`func (o *Assertion) SetLessThan(v PropertyDouble)`

SetLessThan sets LessThan field to given value.

### HasLessThan

`func (o *Assertion) HasLessThan() bool`

HasLessThan returns a boolean if a field has been set.

### GetLessThanOrEqualTo

`func (o *Assertion) GetLessThanOrEqualTo() PropertyDouble`

GetLessThanOrEqualTo returns the LessThanOrEqualTo field if non-nil, zero value otherwise.

### GetLessThanOrEqualToOk

`func (o *Assertion) GetLessThanOrEqualToOk() (*PropertyDouble, bool)`

GetLessThanOrEqualToOk returns a tuple with the LessThanOrEqualTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLessThanOrEqualTo

`func (o *Assertion) SetLessThanOrEqualTo(v PropertyDouble)`

SetLessThanOrEqualTo sets LessThanOrEqualTo field to given value.

### HasLessThanOrEqualTo

`func (o *Assertion) HasLessThanOrEqualTo() bool`

HasLessThanOrEqualTo returns a boolean if a field has been set.

### GetIn

`func (o *Assertion) GetIn() PropertyListString`

GetIn returns the In field if non-nil, zero value otherwise.

### GetInOk

`func (o *Assertion) GetInOk() (*PropertyListString, bool)`

GetInOk returns a tuple with the In field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIn

`func (o *Assertion) SetIn(v PropertyListString)`

SetIn sets In field to given value.

### HasIn

`func (o *Assertion) HasIn() bool`

HasIn returns a boolean if a field has been set.

### GetNotIn

`func (o *Assertion) GetNotIn() PropertyListString`

GetNotIn returns the NotIn field if non-nil, zero value otherwise.

### GetNotInOk

`func (o *Assertion) GetNotInOk() (*PropertyListString, bool)`

GetNotInOk returns a tuple with the NotIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotIn

`func (o *Assertion) SetNotIn(v PropertyListString)`

SetNotIn sets NotIn field to given value.

### HasNotIn

`func (o *Assertion) HasNotIn() bool`

HasNotIn returns a boolean if a field has been set.

### GetIsNull

`func (o *Assertion) GetIsNull() PropertyBoolean`

GetIsNull returns the IsNull field if non-nil, zero value otherwise.

### GetIsNullOk

`func (o *Assertion) GetIsNullOk() (*PropertyBoolean, bool)`

GetIsNullOk returns a tuple with the IsNull field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsNull

`func (o *Assertion) SetIsNull(v PropertyBoolean)`

SetIsNull sets IsNull field to given value.

### HasIsNull

`func (o *Assertion) HasIsNull() bool`

HasIsNull returns a boolean if a field has been set.

### GetIsNotNull

`func (o *Assertion) GetIsNotNull() PropertyBoolean`

GetIsNotNull returns the IsNotNull field if non-nil, zero value otherwise.

### GetIsNotNullOk

`func (o *Assertion) GetIsNotNullOk() (*PropertyBoolean, bool)`

GetIsNotNullOk returns a tuple with the IsNotNull field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsNotNull

`func (o *Assertion) SetIsNotNull(v PropertyBoolean)`

SetIsNotNull sets IsNotNull field to given value.

### HasIsNotNull

`func (o *Assertion) HasIsNotNull() bool`

HasIsNotNull returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


