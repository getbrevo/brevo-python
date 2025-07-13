# CreateOrderPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Order amount (must be non-zero). | 
**balance_definition_id** | **str** | Unique identifier (UUID) of the associated balance definition. | 
**contact_id** | **int** | Unique identifier of the contact placing the order (must be ≥ 1). | 
**due_at** | **str** | RFC3339 timestamp specifying when the order is due. | 
**expires_at** | **str** | Optional RFC3339 timestamp defining order expiration. | [optional] 
**meta** | **object** | Optional metadata associated with the order. | [optional] 
**source** | **str** | Specifies the origin of the order (&#x60;engine&#x60; or &#x60;user&#x60;). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


