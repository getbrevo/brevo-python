# CreateTransactionPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_subscription_id** | **str** | Unique identifier for the loyalty subscription (required unless &#x60;contactId&#x60; is provided). | [optional] 
**amount** | **float** | Transaction amount (must be provided). | 
**auto_complete** | **bool** | Whether the transaction should be automatically completed. | [optional] 
**balance_definition_id** | **str** | Unique identifier (UUID) of the associated balance definition. | 
**balance_expiry_in_minutes** | **int** | Optional expiry time for the balance in minutes (must be greater than 0 if provided). | [optional] 
**contact_id** | **int** | Unique identifier of the contact involved in the transaction (required unless &#x60;LoyaltySubscriptionId&#x60; is provided). | [optional] 
**event_time** | **str** | Optional timestamp specifying when the transaction occurred. | [optional] 
**meta** | **object** | Optional metadata associated with the transaction. | [optional] 
**ttl** | **int** | Optional time-to-live for the transaction (must be greater than 0 if provided). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


