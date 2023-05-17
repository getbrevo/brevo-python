# GetWhatsappCampaignsCampaigns

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the WhatsApp Campaign | 
**campaign_name** | **str** | Name of the WhatsApp Campaign | 
**template_id** | **str** | Id of the WhatsApp template | 
**campaign_status** | **str** | Status of the WhatsApp Campaign | 
**scheduled_at** | **str** | UTC date-time on which WhatsApp campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format | 
**error_reason** | **str** | Error reason in the campaign creation | [optional] 
**invalidated_contacts** | **int** | Count of invalidated contacts | [optional] 
**read_percentage** | **float** | Read percentage of the the WhatsApp campaign created | [optional] 
**stats** | [**WhatsappCampStats**](WhatsappCampStats.md) |  | [optional] 
**created_at** | **str** | Creation UTC date-time of the WhatsApp campaign (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**modified_at** | **str** | UTC date-time of last modification of the whatsapp template (YYYY-MM-DDTHH:mm:ss.SSSZ) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


