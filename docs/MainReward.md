# MainReward

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_per_consumer** | **int** | Maximum number of times a consumer can be attributed this reward | [optional] 
**balance_definition_id** | **str** | Unique identifier for the balance definition | [optional] 
**code** | **str** | Unique code for the reward | [optional] 
**code_count** | **int** | Total number of codes generated | [optional] 
**code_generator_id** | **str** | Unique identifier for the code generator | [optional] 
**code_pool_id** | **str** | Unique identifier for the code pool | [optional] 
**config** | **str** | Configuration settings for the reward | [optional] 
**created_at** | **datetime** | Timestamp when the reward was created | [optional] 
**disabled_at** | **datetime** | Disabled date of the reward | [optional] 
**end_date** | **datetime** | End date of the reward validity | [optional] 
**expiration_date** | **datetime** | Expiration date of the reward | [optional] 
**expiration_modifier** | **str** | Select startOfPeriod to configure rewards expiry on start of day/week/month/year. Select endOfPeriod to configure reward expiry on end of day/week/month/year, else select noModification | [optional] [default to 'noModification']
**expiration_unit** | **str** | Unit of time for the rewards&#39;s availability (e.g., day/week/month/year). | [optional] 
**expiration_value** | **int** | Number of days/weeks/month/year for reward expiry | [optional] 
**generator** | **object** | object | [optional] 
**id** | **str** | Unique identifier for the reward | [optional] 
**limits** | [**list[MainLimit]**](MainLimit.md) | Attribution / Redeem Limits for the reward | [optional] 
**loyalty_program_id** | **str** | Id of the loyalty program to which the current reward belongs to | [optional] 
**meta** | **dict(str, object)** | Additional data for reward definition | [optional] 
**name** | **str** | Name of the reward | [optional] 
**products** | [**list[MainProduct]**](MainProduct.md) | Selected products for reward definition | [optional] 
**public_description** | **str** | Public description for the reward | [optional] 
**public_image** | **str** | Public Image for the reward | [optional] 
**public_name** | **str** | Public name for the reward | [optional] 
**redeem_per_consumer** | **int** | Defines the redeem limit for the consumer | [optional] 
**redeem_rules** | **list[str]** | Rules defined to redeem a reward | [optional] 
**reward_configs** | **object** | object | [optional] 
**rule** | **object** | Rule to define the reward | [optional] 
**start_date** | **datetime** | Start date of attribution of the reward | [optional] 
**subtract_balance_definition_id** | **str** | Id of the selected balance while redeeming / attributing a reward | [optional] 
**subtract_balance_strategy** | **str** | Strategy of the Balance while redeeming / attributing a reward | [optional] 
**subtract_balance_value** | **int** | Amount of balance to be selected while redeeming / attributing a reward | [optional] 
**subtract_total_balance** | **bool** | Value to indicate to subtract full balance or not | [optional] 
**total_attribution** | **int** | Defines the limit to which a consumer can attribute a reward | [optional] 
**total_redeem** | **int** | Defines the limit to which a consumer can redeem a reward | [optional] 
**trigger_id** | **str** | Id of the Rule to be updated for that reward | [optional] 
**unit** | **str** | Selected unit of the balance | [optional] 
**updated_at** | **str** | Timestamp for when this reward was last updated. | [optional] 
**value** | **float** | Value of metric in selected config for reward definition | [optional] 
**value_type** | **str** | Type of config selected for reward definition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


