# ExportWebhooksHistory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Number of days in the past including today (positive integer). _Not compatible with &#39;startDate&#39; and &#39;endDate&#39;_ | [optional] 
**start_date** | **str** | Mandatory if endDate is used. Starting date of the history (YYYY-MM-DD). Must be lower than equal to endDate | [optional] 
**end_date** | **str** | Mandatory if startDate is used. Ending date of the report (YYYY-MM-DD). Must be greater than equal to startDate | [optional] 
**sort** | **str** | Sorting order of records (asc or desc) | [optional] 
**type** | **str** | Filter the history based on webhook type | 
**event** | **str** | Filter the history for a specific event type | 
**notify_url** | **str** | Webhook URL to receive CSV file link | 
**webhook_id** | **int** | Filter the history for a specific webhook id | [optional] 
**email** | **str** | Filter the history for a specific email | [optional] 
**message_id** | **int** | Filter the history for a specific message id. Applicable only for transactional webhooks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


