# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the order. | 
**created_at** | **str** | Event occurrence UTC date-time (YYYY-MM-DDTHH:mm:ssZ), when order is actually created. | 
**updated_at** | **str** | Event updated UTC date-time (YYYY-MM-DDTHH:mm:ssZ), when the status of the order is actually changed/updated. | 
**status** | **str** | State of the order. | 
**amount** | **float** | Total amount of the order, including all shipping expenses, tax and the price of items. | 
**store_id** | **str** | ID of store where the order is placed | [optional] 
**identifiers** | [**OrderIdentifiers**](OrderIdentifiers.md) |  | [optional] 
**products** | [**list[OrderProducts]**](OrderProducts.md) |  | 
**billing** | [**OrderBilling**](OrderBilling.md) |  | [optional] 
**coupons** | **list[str]** | Coupons applied to the order. Stored case insensitive. | [optional] 
**meta_info** | **dict(str, object)** | Meta data of order to store additional detal such as custom message, customer type, source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


