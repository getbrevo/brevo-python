from .conftest import get_client, verify_request_count


def test_event_create_event() -> None:
    """Test createEvent endpoint with WireMock"""
    test_id = "event.create_event.0"
    client = get_client(test_id)
    client.event.create_event(event_name="video_played", identifiers={})
    verify_request_count(test_id, "POST", "/events", None, 1)
