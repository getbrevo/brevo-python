# SendWhatsappMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | ID of the template to send | [optional] 
**text** | **str** | Text to be sent as message body (will be overridden if templateId is passed in the same request) | [optional] 
**sender_number** | **str** | WhatsApp Number with country code. Example, 85264318721 | 
**params** | **object** | Pass the set of attributes to customize the template. For example, {\&quot;FNAME\&quot;:\&quot;Joe\&quot;, \&quot;LNAME\&quot;:\&quot;Doe\&quot;}. | [optional] 
**contact_numbers** | **list[str]** | List of phone numbers of the contacts | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


