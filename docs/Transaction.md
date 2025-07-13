# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The transaction amount. | [optional] 
**balance_definition_id** | **str** | Unique identifier (UUID) of the associated balance definition. | [optional] 
**cancelled_at** | **str** | Timestamp when the transaction was canceled (nullable). | [optional] 
**completed_at** | **str** | Timestamp when the transaction was completed (nullable). | [optional] 
**contact_id** | **int** | Unique identifier of the contact associated with the transaction. | [optional] 
**created_at** | **str** | Timestamp when the transaction was created. | [optional] 
**event_time** | **str** | Optional timestamp indicating when the transaction event occurred. | [optional] 
**expiration_date** | **str** | Expiry date of the transaction (nullable). | [optional] 
**id** | **str** | Unique identifier (UUID) of the transaction. | [optional] 
**loyalty_program_id** | **str** | Unique identifier (UUID) of the associated loyalty program. | [optional] 
**meta** | **object** | Optional metadata associated with the transaction. | [optional] 
**reject_reason** | **str** | Reason for rejection if the transaction was declined (nullable). | [optional] 
**rejected_at** | **str** | Timestamp when the transaction was rejected (nullable). | [optional] 
**status** | **str** | The current status of the transaction (e.g., pending, completed, rejected). | [optional] 
**updated_at** | **str** | Timestamp when the transaction was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


