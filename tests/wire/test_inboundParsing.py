from .conftest import get_client, verify_request_count


def test_inboundParsing_get_inbound_email_events() -> None:
    """Test getInboundEmailEvents endpoint with WireMock"""
    test_id = "inbound_parsing.get_inbound_email_events.0"
    client = get_client(test_id)
    client.inbound_parsing.get_inbound_email_events()
    verify_request_count(test_id, "GET", "/inbound/events", None, 1)


def test_inboundParsing_get_inbound_email_events_by_uuid() -> None:
    """Test getInboundEmailEventsByUuid endpoint with WireMock"""
    test_id = "inbound_parsing.get_inbound_email_events_by_uuid.0"
    client = get_client(test_id)
    client.inbound_parsing.get_inbound_email_events_by_uuid(uuid_="uuid")
    verify_request_count(test_id, "GET", "/inbound/events/uuid", None, 1)


def test_inboundParsing_get_inbound_email_attachment() -> None:
    """Test getInboundEmailAttachment endpoint with WireMock"""
    test_id = "inbound_parsing.get_inbound_email_attachment.0"
    client = get_client(test_id)
    for _ in client.inbound_parsing.get_inbound_email_attachment(download_token="downloadToken"):
        pass
    verify_request_count(test_id, "GET", "/inbound/attachments/downloadToken", None, 1)
