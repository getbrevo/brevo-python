# MainOrderPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Total amount of the order | [optional] 
**billing** | **object** | Billing information for the order | [optional] 
**contact_id** | **int** | Unique identifier for the contact | [optional] 
**coupons** | **list[str]** | List of coupon codes applied to the order | [optional] 
**created_at** | **datetime** | Timestamp when the order was created | [optional] 
**email** | **str** | Email address associated with the order | [optional] 
**id** | **str** | Unique identifier for the order | [optional] 
**identifiers** | **object** | Additional identifiers for the order | [optional] 
**products** | [**list[MainProductPayload]**](MainProductPayload.md) | List of products in the order | [optional] 
**status** | **str** | Current status of the order | [optional] 
**store_id** | **str** | Identifier for the store where the order was placed | [optional] 
**updated_at** | **datetime** | Timestamp when the order was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


