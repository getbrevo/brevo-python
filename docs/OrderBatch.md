# OrderBatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**list[Order]**](Order.md) | array of order objects | 
**notify_url** | **str** | Notify Url provided by client to get the status of batch request | [optional] 
**historical** | **bool** | Defines wether you want your orders to be considered as live data or as historical data (import of past data, synchronising data). True: orders will not trigger any automation workflows. False: orders will trigger workflows as usual. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


