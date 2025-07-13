# BalanceOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Order amount (must not be zero). | 
**balance_definition_id** | **str** | Optional unique identifier (UUID) of the associated balance definition. | [optional] 
**contact_id** | **int** | Unique identifier of the contact placing the order (must be ≥ 1). | 
**created_at** | **str** | RFC3339 timestamp indicating when the order was created. | 
**due_at** | **str** | RFC3339 timestamp specifying when the order is due in the future. | 
**expires_at** | **str** | Optional RFC3339 timestamp defining order expiration in the future. | [optional] 
**id** | **str** | Unique identifier for the balance order. | [optional] 
**loyalty_program_id** | **str** | Unique identifier of the loyalty program associated with the order. | 
**meta** | **object** | Optional metadata associated with the order. | [optional] 
**processed_at** | **str** | Optional RFC3339 timestamp indicating when the order was processed. | [optional] 
**transactionid** | **str** | Optional reference to the associated transaction ID. | [optional] 
**updated_at** | **str** | RFC3339 timestamp indicating the last update to the order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


