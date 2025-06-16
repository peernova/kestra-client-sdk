# TestSuiteRunResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**TestSuiteId** | Pointer to **string** |  | [optional] 
**Namespace** | Pointer to **string** |  | [optional] 
**FlowId** | Pointer to **string** |  | [optional] 
**State** | Pointer to [**TestState**](TestState.md) |  | [optional] 
**Results** | Pointer to [**[]UnitTestResult**](UnitTestResult.md) |  | [optional] 

## Methods

### NewTestSuiteRunResult

`func NewTestSuiteRunResult() *TestSuiteRunResult`

NewTestSuiteRunResult instantiates a new TestSuiteRunResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTestSuiteRunResultWithDefaults

`func NewTestSuiteRunResultWithDefaults() *TestSuiteRunResult`

NewTestSuiteRunResultWithDefaults instantiates a new TestSuiteRunResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TestSuiteRunResult) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TestSuiteRunResult) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TestSuiteRunResult) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *TestSuiteRunResult) HasId() bool`

HasId returns a boolean if a field has been set.

### GetTestSuiteId

`func (o *TestSuiteRunResult) GetTestSuiteId() string`

GetTestSuiteId returns the TestSuiteId field if non-nil, zero value otherwise.

### GetTestSuiteIdOk

`func (o *TestSuiteRunResult) GetTestSuiteIdOk() (*string, bool)`

GetTestSuiteIdOk returns a tuple with the TestSuiteId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTestSuiteId

`func (o *TestSuiteRunResult) SetTestSuiteId(v string)`

SetTestSuiteId sets TestSuiteId field to given value.

### HasTestSuiteId

`func (o *TestSuiteRunResult) HasTestSuiteId() bool`

HasTestSuiteId returns a boolean if a field has been set.

### GetNamespace

`func (o *TestSuiteRunResult) GetNamespace() string`

GetNamespace returns the Namespace field if non-nil, zero value otherwise.

### GetNamespaceOk

`func (o *TestSuiteRunResult) GetNamespaceOk() (*string, bool)`

GetNamespaceOk returns a tuple with the Namespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespace

`func (o *TestSuiteRunResult) SetNamespace(v string)`

SetNamespace sets Namespace field to given value.

### HasNamespace

`func (o *TestSuiteRunResult) HasNamespace() bool`

HasNamespace returns a boolean if a field has been set.

### GetFlowId

`func (o *TestSuiteRunResult) GetFlowId() string`

GetFlowId returns the FlowId field if non-nil, zero value otherwise.

### GetFlowIdOk

`func (o *TestSuiteRunResult) GetFlowIdOk() (*string, bool)`

GetFlowIdOk returns a tuple with the FlowId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlowId

`func (o *TestSuiteRunResult) SetFlowId(v string)`

SetFlowId sets FlowId field to given value.

### HasFlowId

`func (o *TestSuiteRunResult) HasFlowId() bool`

HasFlowId returns a boolean if a field has been set.

### GetState

`func (o *TestSuiteRunResult) GetState() TestState`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *TestSuiteRunResult) GetStateOk() (*TestState, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *TestSuiteRunResult) SetState(v TestState)`

SetState sets State field to given value.

### HasState

`func (o *TestSuiteRunResult) HasState() bool`

HasState returns a boolean if a field has been set.

### GetResults

`func (o *TestSuiteRunResult) GetResults() []UnitTestResult`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *TestSuiteRunResult) GetResultsOk() (*[]UnitTestResult, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *TestSuiteRunResult) SetResults(v []UnitTestResult)`

SetResults sets Results field to given value.

### HasResults

`func (o *TestSuiteRunResult) HasResults() bool`

HasResults returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


