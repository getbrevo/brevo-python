from .conftest import get_client, verify_request_count


def test_smsTemplates_get_sms_templates() -> None:
    """Test getSMSTemplates endpoint with WireMock"""
    test_id = "sms_templates.get_sms_templates.0"
    client = get_client(test_id)
    client.sms_templates.get_sms_templates()
    verify_request_count(test_id, "GET", "/transactionalSMS/templates", None, 1)
