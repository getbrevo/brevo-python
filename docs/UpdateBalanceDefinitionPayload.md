# UpdateBalanceDefinitionPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_availability_duration_modifier** | **str** | Defines when the balance expires within the selected duration. | [optional] 
**balance_availability_duration_unit** | **str** | Unit of time for balance validity. | [optional] 
**balance_availability_duration_value** | **int** | Number of time units before the balance expires. | [optional] 
**balance_expiration_date** | **str** | Expiration date (&#x60;dd/mm&#x60; format) or empty if not applicable. | [optional] 
**balance_option_amount_overtaking_strategy** | **str** | Defines whether partial credit is allowed when reaching max balance. | [optional] 
**balance_option_credit_rounding** | **str** | Rounding strategy for credit transactions. | [optional] 
**balance_option_debit_rounding** | **str** | Rounding strategy for debit transactions. | [optional] 
**description** | **str** | Short description of the balance definition. | [optional] 
**image_ref** | **str** | URL of an optional image reference. | [optional] 
**max_amount** | **float** | Maximum allowable balance amount. | [optional] 
**max_credit_amount_limit** | **float** | Maximum credit allowed per operation. | [optional] 
**max_debit_amount_limit** | **float** | Maximum debit allowed per operation. | [optional] 
**meta** | **object** | Optional metadata for the balance definition. | [optional] 
**min_amount** | **float** | Minimum allowable balance amount. | [optional] 
**name** | **str** | Name of the balance definition. | 
**unit** | **str** | Unit of balance measurement. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


