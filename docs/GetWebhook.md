# GetWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the webhook | 
**id** | **int** | ID of the webhook | 
**description** | **str** | Description of the webhook | 
**events** | **list[str]** |  | 
**type** | **str** | Type of webhook (marketing or transactional) | 
**created_at** | **str** | Creation UTC date-time of the webhook (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**modified_at** | **str** | Last modification UTC date-time of the webhook (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**batched** | **bool** | To send batched webhooks | [optional] 
**auth** | [**GetWebhookAuth**](GetWebhookAuth.md) |  | [optional] 
**headers** | [**list[GetWebhookHeaders]**](GetWebhookHeaders.md) | Custom headers to be send with webhooks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


