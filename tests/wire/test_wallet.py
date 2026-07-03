from .conftest import get_client, verify_request_count


def test_wallet_get_wallet_pass_install_url() -> None:
    """Test getWalletPassInstallUrl endpoint with WireMock"""
    test_id = "wallet.get_wallet_pass_install_url.0"
    client = get_client(test_id)
    client.wallet.get_wallet_pass_install_url(
        pass_id="passId",
        contact_id=1000000,
    )
    verify_request_count(test_id, "GET", "/wallet/passes/passId/installUrl/1000000", None, 1)
