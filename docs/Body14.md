# Body14

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of task | [optional] 
**duration** | **int** | Duration of task in milliseconds [1 minute &#x3D; 60000 ms] | [optional] 
**task_type_id** | **str** | Id for type of task e.g Call / Email / Meeting etc. | [optional] 
**_date** | **datetime** | Task date/time | [optional] 
**notes** | **str** | Notes added to a task | [optional] 
**done** | **bool** | Task marked as done | [optional] 
**assign_to_id** | **str** | To assign a task to a user you can use either the account email or ID. | [optional] 
**contacts_ids** | **list[int]** | Contact ids for contacts linked to this task | [optional] 
**deals_ids** | **list[str]** | Deal ids for deals a task is linked to | [optional] 
**companies_ids** | **list[str]** | Companies ids for companies a task is linked to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


