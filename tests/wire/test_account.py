from .conftest import get_client, verify_request_count


def test_account_get_account() -> None:
    """Test getAccount endpoint with WireMock"""
    test_id = "account.get_account.0"
    client = get_client(test_id)
    client.account.get_account()
    verify_request_count(test_id, "GET", "/account", None, 1)


def test_account_get_account_activity() -> None:
    """Test getAccountActivity endpoint with WireMock"""
    test_id = "account.get_account_activity.0"
    client = get_client(test_id)
    client.account.get_account_activity()
    verify_request_count(test_id, "GET", "/organization/activities", None, 1)
