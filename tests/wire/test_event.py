from .conftest import get_client, verify_request_count

from brevo.event import (
    CreateBatchEventsRequestItem,
    CreateBatchEventsRequestItemIdentifiers,
    CreateEventRequestIdentifiers,
)


def test_event_create_event() -> None:
    """Test createEvent endpoint with WireMock"""
    test_id = "event.create_event.0"
    client = get_client(test_id)
    client.event.create_event(
        event_name="video_played",
        identifiers=CreateEventRequestIdentifiers(),
    )
    verify_request_count(test_id, "POST", "/events", None, 1)


def test_event_create_batch_events() -> None:
    """Test createBatchEvents endpoint with WireMock"""
    test_id = "event.create_batch_events.0"
    client = get_client(test_id)
    client.event.create_batch_events(
        request=[
            CreateBatchEventsRequestItem(
                event_name="order_created",
                identifiers=CreateBatchEventsRequestItemIdentifiers(),
            )
        ],
    )
    verify_request_count(test_id, "POST", "/events/batch", None, 1)
