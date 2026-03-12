from .conftest import get_client, verify_request_count


def test_senders_get_senders() -> None:
    """Test getSenders endpoint with WireMock"""
    test_id = "senders.get_senders.0"
    client = get_client(test_id)
    client.senders.get_senders()
    verify_request_count(test_id, "GET", "/senders", None, 1)


def test_senders_create_sender() -> None:
    """Test createSender endpoint with WireMock"""
    test_id = "senders.create_sender.0"
    client = get_client(test_id)
    client.senders.create_sender(email="support@example.com", name="Support Team")
    verify_request_count(test_id, "POST", "/senders", None, 1)


def test_senders_get_ips() -> None:
    """Test getIps endpoint with WireMock"""
    test_id = "senders.get_ips.0"
    client = get_client(test_id)
    client.senders.get_ips()
    verify_request_count(test_id, "GET", "/senders/ips", None, 1)


def test_senders_update_sender() -> None:
    """Test updateSender endpoint with WireMock"""
    test_id = "senders.update_sender.0"
    client = get_client(test_id)
    client.senders.update_sender(sender_id=1000000, name="New Support Team")
    verify_request_count(test_id, "PUT", "/senders/1000000", None, 1)


def test_senders_delete_sender() -> None:
    """Test deleteSender endpoint with WireMock"""
    test_id = "senders.delete_sender.0"
    client = get_client(test_id)
    client.senders.delete_sender(sender_id=1000000)
    verify_request_count(test_id, "DELETE", "/senders/1000000", None, 1)


def test_senders_get_ips_from_sender() -> None:
    """Test getIpsFromSender endpoint with WireMock"""
    test_id = "senders.get_ips_from_sender.0"
    client = get_client(test_id)
    client.senders.get_ips_from_sender(sender_id=1000000)
    verify_request_count(test_id, "GET", "/senders/1000000/ips", None, 1)


def test_senders_validate_sender_by_otp() -> None:
    """Test validateSenderByOTP endpoint with WireMock"""
    test_id = "senders.validate_sender_by_otp.0"
    client = get_client(test_id)
    client.senders.validate_sender_by_otp(sender_id=1000000, otp=123456)
    verify_request_count(test_id, "PUT", "/senders/1000000/validate", None, 1)
