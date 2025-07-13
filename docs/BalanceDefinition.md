# BalanceDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_availability_duration_modifier** | **str** | startOfPeriod depicts the balancy expiry on start of day/week/month/year. endOfPeriod depicts the balancy expiry on end of day/week/month/year | [optional] 
**balance_availability_duration_unit** | **str** | Unit of time for the balance&#39;s availability (e.g., day/week/month/year). | [optional] 
**balance_availability_duration_value** | **int** | Number of days/weeks/month/year for balance expiry | [optional] 
**balance_expiration_date** | **datetime** | Date when the balance expires and can no longer be used, in dd/mm format. The balance will be expired when this date appears next in the calendar and only one of balanceExpirationDate or balance availability fields can be used. | [optional] 
**balance_option_amount_overtaking_strategy** | **str** | Partial enables partial credit of balance if maximum balance limit is reaching. Strict enables rejection of transaction if it will breach the max credit amount limit. | [optional] 
**balance_option_credit_rounding** | **str** | Rounding strategy for credit transactions. | [optional] 
**balance_option_debit_rounding** | **str** | Rounding strategy for debit transactions. | [optional] 
**created_at** | **datetime** | Timestamp of balance definition creation. | [optional] 
**deleted_at** | **str** | Timestamp of balance definition deletion (nullable). | [optional] 
**description** | **str** | Short description of the balance definition. | [optional] 
**id** | **str** | Unique identifier for the balance definition. | [optional] 
**image_ref** | **str** | Optional image reference URL. | [optional] 
**max_amount** | **float** | Maximum allowable balance. | [optional] 
**max_credit_amount_limit** | **float** | Max credit allowed per operation. | [optional] 
**max_debit_amount_limit** | **float** | Max debit allowed per operation. | [optional] 
**meta** | **dict(str, object)** | Additional metadata for the balance definition. | [optional] 
**min_amount** | **float** | Minimum allowable balance. | [optional] 
**name** | **str** | Name of the balance definition. | [optional] 
**unit** | **str** | Unit of balance (e.g., points, currency). | [optional] 
**updated_at** | **str** | Timestamp of the last update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


