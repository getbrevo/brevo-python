# GetCorporateInvitedUsersListFeatureAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_management** | **list[str]** | User management accessiblity. | [optional] 
**api_keys** | **list[str]** | Api keys accessiblity. | [optional] 
**my_plan** | **list[str]** | My plan accessiblity. | [optional] 
**apps_management** | **list[str]** | Apps management accessiblity | Not available in ENTv2 | [optional] 
**sub_organization_groups** | **list[str]** | Group creation, modification or deletion accessibility | [optional] 
**create_sub_organizations** | **list[str]** | Authorization to create sub-organization in the admin account. If the user creating the sub-organization, belongs to a group, the user must choose a group at the sub-organization creation. | [optional] 
**manage_sub_organizations** | **list[str]** | Authorization to manage and access sub-organizations in the admin account. | [optional] 
**analytics** | **list[str]** | Analytics dashboard accessibility | [optional] 
**security** | **list[str]** | Security page accessibility | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


