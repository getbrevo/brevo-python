# AddSubscriptionMemberPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | Required if LoyaltySubscriptionId is not provided, must be greater than 0 | [optional] 
**loyalty_subscription_id** | **str** | Required if ContactId is not provided, max length 64 | [optional] 
**member_contact_ids** | **list[int]** | Required, each item must be greater than or equal to 1 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


