# CreateBalanceLimitPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_type** | **str** | Defines whether the limit applies to transaction count or amount. | 
**duration_unit** | **str** | Unit of time for which the limit is applicable. | 
**duration_value** | **int** | Number of time units for the balance limit. | 
**sliding_schedule** | **bool** | Determines if the limit resets on a rolling schedule. | [optional] 
**transaction_type** | **str** | Specifies whether the limit applies to credit or debit transactions. | 
**value** | **int** | Maximum allowed value for the specified constraint type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


