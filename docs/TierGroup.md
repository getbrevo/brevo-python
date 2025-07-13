# TierGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tier group unique identifier | [optional] 
**name** | **str** | Tier group name | [optional] 
**tier_order** | **list[str]** | Order of the tiers in the group in ascending order | [optional] 
**loyalty_program_id** | **str** | Associated loyalty program Id | [optional] 
**upgrade_strategy** | **str** | Select real_time to upgrade tier on real time balance updates. Select membership_anniversary to upgrade tier on subscription anniversary. Select tier_anniversary to upgrade tier on tier anniversary. | [optional] [default to 'real_time']
**downgrade_strategy** | **str** | Select real_time to downgrade tier on real time balance updates. Select membership_anniversary to downgrade tier on subscription anniversary. Select tier_anniversary to downgrade tier on tier anniversary. | [optional] [default to 'real_time']
**created_at** | **datetime** | Timestamp when the tier group was created | [optional] 
**updated_at** | **datetime** | Timestamp when the tier group was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


