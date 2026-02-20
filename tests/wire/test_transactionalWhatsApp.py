from .conftest import get_client, verify_request_count


def test_transactionalWhatsApp_send_whatsapp_message() -> None:
    """Test sendWhatsappMessage endpoint with WireMock"""
    test_id = "transactional_whats_app.send_whatsapp_message.0"
    client = get_client(test_id)
    client.transactional_whats_app.send_whatsapp_message(
        request={"contact_numbers": ["contactNumbers"], "sender_number": "senderNumber", "template_id": 123}
    )
    verify_request_count(test_id, "POST", "/whatsapp/sendMessage", None, 1)


def test_transactionalWhatsApp_get_whatsapp_event_report() -> None:
    """Test getWhatsappEventReport endpoint with WireMock"""
    test_id = "transactional_whats_app.get_whatsapp_event_report.0"
    client = get_client(test_id)
    client.transactional_whats_app.get_whatsapp_event_report()
    verify_request_count(test_id, "GET", "/whatsapp/statistics/events", None, 1)
