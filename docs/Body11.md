# Body11

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of deal | [optional] 
**attributes** | **object** | Attributes for deal update  To assign owner of a Deal you can send attributes.deal_owner and utilize the account email or ID.  If you wish to update the pipeline of a deal you need to provide the &#x60;pipeline&#x60; and the &#x60;deal_stage&#x60;.  Pipeline and deal_stage are ids you can fetch using this endpoint &#x60;/crm/pipeline/details/{pipelineID}&#x60;  | [optional] 
**linked_contacts_ids** | **list[int]** | Warning - Using PATCH on linkedContactIds replaces the list of linked contacts. Omitted IDs will be removed. | [optional] 
**linked_companies_ids** | **list[str]** | Warning - Using PATCH on linkedCompaniesIds replaces the list of linked contacts. Omitted IDs will be removed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


