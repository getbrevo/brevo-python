from .conftest import get_client, verify_request_count


def test_oAuth_get_o_auth_m2m_token() -> None:
    """Test getOAuthM2MToken endpoint with WireMock"""
    test_id = "o_auth.get_o_auth_m2m_token.0"
    client = get_client(test_id)
    client.o_auth.get_o_auth_m2m_token(
        client_id="client_id",
        client_secret="client_secret",
    )
    verify_request_count(test_id, "POST", "/oauth/token", None, 2)
