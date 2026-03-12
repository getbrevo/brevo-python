from datetime import date

from .conftest import get_client, verify_request_count


def test_externalFeeds_get_all_external_feeds() -> None:
    """Test getAllExternalFeeds endpoint with WireMock"""
    test_id = "external_feeds.get_all_external_feeds.0"
    client = get_client(test_id)
    client.external_feeds.get_all_external_feeds(
        search="product", start_date=date.fromisoformat("2024-01-01"), end_date=date.fromisoformat("2024-01-31")
    )
    verify_request_count(
        test_id, "GET", "/feeds", {"search": "product", "startDate": "2024-01-01", "endDate": "2024-01-31"}, 1
    )


def test_externalFeeds_create_external_feed() -> None:
    """Test createExternalFeed endpoint with WireMock"""
    test_id = "external_feeds.create_external_feed.0"
    client = get_client(test_id)
    client.external_feeds.create_external_feed(
        name="Public API Feed",
        url="https://jsonplaceholder.typicode.com/posts",
        auth_type="noAuth",
        max_retries=3,
        cache=True,
    )
    verify_request_count(test_id, "POST", "/feeds", None, 1)


def test_externalFeeds_get_external_feed_by_uuid() -> None:
    """Test getExternalFeedByUUID endpoint with WireMock"""
    test_id = "external_feeds.get_external_feed_by_uuid.0"
    client = get_client(test_id)
    client.external_feeds.get_external_feed_by_uuid(uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6")
    verify_request_count(test_id, "GET", "/feeds/b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6", None, 1)


def test_externalFeeds_update_external_feed() -> None:
    """Test updateExternalFeed endpoint with WireMock"""
    test_id = "external_feeds.update_external_feed.0"
    client = get_client(test_id)
    client.external_feeds.update_external_feed(
        uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6",
        name="Updated Product Catalog",
        url="https://api.newstore.com/products/v2",
    )
    verify_request_count(test_id, "PUT", "/feeds/b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6", None, 1)


def test_externalFeeds_delete_external_feed() -> None:
    """Test deleteExternalFeed endpoint with WireMock"""
    test_id = "external_feeds.delete_external_feed.0"
    client = get_client(test_id)
    client.external_feeds.delete_external_feed(uuid_="b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6")
    verify_request_count(test_id, "DELETE", "/feeds/b1c2d3e4-f5a6-47b8-89c0-d1e2f3a4b5c6", None, 1)
