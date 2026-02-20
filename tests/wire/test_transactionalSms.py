from .conftest import get_client, verify_request_count


def test_transactionalSms_send_async_transactional_sms() -> None:
    """Test sendAsyncTransactionalSms endpoint with WireMock"""
    test_id = "transactional_sms.send_async_transactional_sms.0"
    client = get_client(test_id)
    client.transactional_sms.send_async_transactional_sms(recipient="33689965433", sender="MyShop")
    verify_request_count(test_id, "POST", "/transactionalSMS/send", None, 1)


def test_transactionalSms_send_transac_sms() -> None:
    """Test sendTransacSms endpoint with WireMock"""
    test_id = "transactional_sms.send_transac_sms.0"
    client = get_client(test_id)
    client.transactional_sms.send_transac_sms(recipient="33689965433", sender="MyShop")
    verify_request_count(test_id, "POST", "/transactionalSMS/sms", None, 1)


def test_transactionalSms_get_transac_aggregated_sms_report() -> None:
    """Test getTransacAggregatedSmsReport endpoint with WireMock"""
    test_id = "transactional_sms.get_transac_aggregated_sms_report.0"
    client = get_client(test_id)
    client.transactional_sms.get_transac_aggregated_sms_report()
    verify_request_count(test_id, "GET", "/transactionalSMS/statistics/aggregatedReport", None, 1)


def test_transactionalSms_get_sms_events() -> None:
    """Test getSmsEvents endpoint with WireMock"""
    test_id = "transactional_sms.get_sms_events.0"
    client = get_client(test_id)
    client.transactional_sms.get_sms_events()
    verify_request_count(test_id, "GET", "/transactionalSMS/statistics/events", None, 1)


def test_transactionalSms_get_transac_sms_report() -> None:
    """Test getTransacSmsReport endpoint with WireMock"""
    test_id = "transactional_sms.get_transac_sms_report.0"
    client = get_client(test_id)
    client.transactional_sms.get_transac_sms_report()
    verify_request_count(test_id, "GET", "/transactionalSMS/statistics/reports", None, 1)
