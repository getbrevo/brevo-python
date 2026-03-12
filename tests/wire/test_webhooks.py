from .conftest import get_client, verify_request_count


def test_webhooks_get_webhooks() -> None:
    """Test getWebhooks endpoint with WireMock"""
    test_id = "webhooks.get_webhooks.0"
    client = get_client(test_id)
    client.webhooks.get_webhooks()
    verify_request_count(test_id, "GET", "/webhooks", None, 1)


def test_webhooks_create_webhook() -> None:
    """Test createWebhook endpoint with WireMock"""
    test_id = "webhooks.create_webhook.0"
    client = get_client(test_id)
    client.webhooks.create_webhook(events=["sent"], url="http://requestb.in/173lyyx1")
    verify_request_count(test_id, "POST", "/webhooks", None, 1)


def test_webhooks_export_webhooks_history() -> None:
    """Test exportWebhooksHistory endpoint with WireMock"""
    test_id = "webhooks.export_webhooks_history.0"
    client = get_client(test_id)
    client.webhooks.export_webhooks_history(
        event="invalid_parameter", notify_url="https://brevo.com", type="transactional"
    )
    verify_request_count(test_id, "POST", "/webhooks/export", None, 1)


def test_webhooks_get_webhook() -> None:
    """Test getWebhook endpoint with WireMock"""
    test_id = "webhooks.get_webhook.0"
    client = get_client(test_id)
    client.webhooks.get_webhook(webhook_id=1000000)
    verify_request_count(test_id, "GET", "/webhooks/1000000", None, 1)


def test_webhooks_update_webhook() -> None:
    """Test updateWebhook endpoint with WireMock"""
    test_id = "webhooks.update_webhook.0"
    client = get_client(test_id)
    client.webhooks.update_webhook(webhook_id=1000000)
    verify_request_count(test_id, "PUT", "/webhooks/1000000", None, 1)


def test_webhooks_delete_webhook() -> None:
    """Test deleteWebhook endpoint with WireMock"""
    test_id = "webhooks.delete_webhook.0"
    client = get_client(test_id)
    client.webhooks.delete_webhook(webhook_id=1000000)
    verify_request_count(test_id, "DELETE", "/webhooks/1000000", None, 1)
