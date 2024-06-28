# GetCouponCollection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the collection. | 
**name** | **str** | The name of the collection. | 
**default_coupon** | **str** | The default coupon of the collection. | 
**created_at** | **datetime** | Datetime on which the collection was created. | 
**total_coupons** | **int** | Total number of coupons in the collection. | 
**remaining_coupons** | **int** | Number of coupons that have not been sent yet. | 
**expiration_date** | **datetime** | Expiration date for the coupon collection in RFC3339 format. | [optional] 
**remaining_days_alert** | **int** | If present, an email notification is going to be sent the defined amount of days before the expiration date. | [optional] 
**remaining_coupons_alert** | **int** | If present, an email notification is going to be sent when the total number of available coupons falls below the defined threshold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


