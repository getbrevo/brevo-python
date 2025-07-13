# CreateWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the webhook | 
**description** | **str** | Description of the webhook | [optional] 
**events** | **list[str]** | - Events triggering the webhook. Possible values for **Transactional** type webhook: #### &#x60;sent&#x60; OR &#x60;request&#x60;, &#x60;delivered&#x60;, &#x60;hardBounce&#x60;, &#x60;softBounce&#x60;, &#x60;blocked&#x60;, &#x60;spam&#x60;, &#x60;invalid&#x60;, &#x60;deferred&#x60;, &#x60;click&#x60;, &#x60;opened&#x60;, &#x60;uniqueOpened&#x60; and &#x60;unsubscribed&#x60; - Possible values for **Marketing** type webhook: #### &#x60;spam&#x60;, &#x60;opened&#x60;, &#x60;click&#x60;, &#x60;hardBounce&#x60;, &#x60;softBounce&#x60;, &#x60;unsubscribed&#x60;, &#x60;listAddition&#x60; &amp; &#x60;delivered&#x60; - Possible values for **Inbound** type webhook: #### &#x60;inboundEmailProcessed&#x60; - Possible values for type **Transactional** and channel **SMS** #### &#x60;accepted&#x60;,&#x60;delivered&#x60;,&#x60;softBounce&#x60;,&#x60;hardBounce&#x60;,&#x60;unsubscribe&#x60;,&#x60;reply&#x60;, &#x60;subscribe&#x60;,&#x60;sent&#x60;,&#x60;blacklisted&#x60;,&#x60;skip&#x60; - Possible values for type **Marketing**  channel **SMS** #### &#x60;sent&#x60;,&#x60;delivered&#x60;,&#x60;softBounce&#x60;,&#x60;hardBounce&#x60;,&#x60;unsubscribe&#x60;,&#x60;reply&#x60;, &#x60;subscribe&#x60;,&#x60;skip&#x60;  | 
**type** | **str** | Type of the webhook | [optional] [default to 'transactional']
**channel** | **str** | channel of webhook | [optional] [default to 'email']
**domain** | **str** | Inbound domain of webhook, required in case of event type &#x60;inbound&#x60; | [optional] 
**batched** | **bool** | To send batched webhooks | [optional] 
**auth** | [**GetWebhookAuth**](GetWebhookAuth.md) |  | [optional] 
**headers** | [**list[GetWebhookHeaders]**](GetWebhookHeaders.md) | Custom headers to be send with webhooks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


