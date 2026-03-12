from .conftest import get_client, verify_request_count


def test_payments_create_payment_request() -> None:
    """Test createPaymentRequest endpoint with WireMock"""
    test_id = "payments.create_payment_request.0"
    client = get_client(test_id)
    client.payments.create_payment_request(
        cart={"currency": "EUR", "specific_amount": 1200}, contact_id=43, reference="Invoice #INV0001"
    )
    verify_request_count(test_id, "POST", "/payments/requests", None, 1)


def test_payments_get_payment_request() -> None:
    """Test getPaymentRequest endpoint with WireMock"""
    test_id = "payments.get_payment_request.0"
    client = get_client(test_id)
    client.payments.get_payment_request(id="050db7b0-9bb7-4c1e-9c68-5a8dace8c1dc")
    verify_request_count(test_id, "GET", "/payments/requests/050db7b0-9bb7-4c1e-9c68-5a8dace8c1dc", None, 1)


def test_payments_delete_payment_request() -> None:
    """Test deletePaymentRequest endpoint with WireMock"""
    test_id = "payments.delete_payment_request.0"
    client = get_client(test_id)
    client.payments.delete_payment_request(id="9ae7d68a-565c-4695-9381-d8fb3e3a14cc")
    verify_request_count(test_id, "DELETE", "/payments/requests/9ae7d68a-565c-4695-9381-d8fb3e3a14cc", None, 1)
