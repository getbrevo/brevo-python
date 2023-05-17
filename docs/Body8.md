# Body8

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visitor_id** | **str** | visitor’s ID received &lt;a href&#x3D;\&quot;https://developers.brevo.com/docs/conversations-webhooks\&quot;&gt;from a webhook&lt;/a&gt; or generated by you to &lt;a href&#x3D;\&quot;https://developers.brevo.com/docs/customize-the-widget#identifying-existing-users\&quot;&gt;bind existing user account to Conversations&lt;/a&gt; | 
**text** | **str** | message text | 
**agent_id** | **str** | agent ID. It can be found on agent’s page or received &lt;a href&#x3D;\&quot;https://developers.brevo.com/docs/conversations-webhooks\&quot;&gt;from a webhook&lt;/a&gt;. Alternatively, you can use &#x60;agentEmail&#x60; + &#x60;agentName&#x60; + &#x60;receivedFrom&#x60; instead (all 3 fields required). | [optional] 
**received_from** | **str** | mark your messages to distinguish messages created by you from the others. | [optional] 
**agent_email** | **str** | agent email. When sending messages from a standalone system, it’s hard to maintain a 1-to-1 relationship between the users of both systems. In this case, an agent can be specified by their email address. | [optional] 
**agent_name** | **str** | agent name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

