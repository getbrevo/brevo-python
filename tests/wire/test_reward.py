from .conftest import get_client, verify_request_count


def test_reward_get_code_count() -> None:
    """Test getCodeCount endpoint with WireMock"""
    test_id = "reward.get_code_count.0"
    client = get_client(test_id)
    client.reward.get_code_count(pid="pid", cpid="cpid")
    verify_request_count(test_id, "GET", "/loyalty/offer/programs/pid/code-pools/cpid/codes-count", None, 1)


def test_reward_get_reward_page_api() -> None:
    """Test getRewardPageApi endpoint with WireMock"""
    test_id = "reward.get_reward_page_api.0"
    client = get_client(test_id)
    client.reward.get_reward_page_api(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/offer/programs/pid/offers", None, 1)


def test_reward_create_reward() -> None:
    """Test createReward endpoint with WireMock"""
    test_id = "reward.create_reward.0"
    client = get_client(test_id)
    client.reward.create_reward(pid="pid", name="name")
    verify_request_count(test_id, "POST", "/loyalty/offer/programs/pid/offers", None, 1)


def test_reward_create_voucher() -> None:
    """Test createVoucher endpoint with WireMock"""
    test_id = "reward.create_voucher.0"
    client = get_client(test_id)
    client.reward.create_voucher(pid="pid", reward_id="rewardId")
    verify_request_count(test_id, "POST", "/loyalty/offer/programs/pid/rewards/attribute", None, 1)


def test_reward_redeem_voucher() -> None:
    """Test redeemVoucher endpoint with WireMock"""
    test_id = "reward.redeem_voucher.0"
    client = get_client(test_id)
    client.reward.redeem_voucher(pid="pid")
    verify_request_count(test_id, "POST", "/loyalty/offer/programs/pid/rewards/redeem", None, 1)


def test_reward_complete_redeem_transaction() -> None:
    """Test completeRedeemTransaction endpoint with WireMock"""
    test_id = "reward.complete_redeem_transaction.0"
    client = get_client(test_id)
    client.reward.complete_redeem_transaction(pid="pid", tid="tid")
    verify_request_count(test_id, "POST", "/loyalty/offer/programs/pid/rewards/redeem/tid/complete", None, 1)


def test_reward_revoke_vouchers() -> None:
    """Test revokeVouchers endpoint with WireMock"""
    test_id = "reward.revoke_vouchers.0"
    client = get_client(test_id)
    client.reward.revoke_vouchers(pid="pid")
    verify_request_count(test_id, "DELETE", "/loyalty/offer/programs/pid/rewards/revoke", None, 1)


def test_reward_validate_reward() -> None:
    """Test validateReward endpoint with WireMock"""
    test_id = "reward.validate_reward.0"
    client = get_client(test_id)
    client.reward.validate_reward(pid="pid")
    verify_request_count(test_id, "POST", "/loyalty/offer/programs/pid/rewards/validate", None, 1)


def test_reward_get_reward_information() -> None:
    """Test getRewardInformation endpoint with WireMock"""
    test_id = "reward.get_reward_information.0"
    client = get_client(test_id)
    client.reward.get_reward_information(pid="pid", rid="rid")
    verify_request_count(test_id, "GET", "/loyalty/offer/programs/pid/rewards/rid", None, 1)


def test_reward_get_voucher_for_a_contact() -> None:
    """Test getVoucherForAContact endpoint with WireMock"""
    test_id = "reward.get_voucher_for_a_contact.0"
    client = get_client(test_id)
    client.reward.get_voucher_for_a_contact(pid="pid", contact_id=1)
    verify_request_count(test_id, "GET", "/loyalty/offer/programs/pid/vouchers", {"contactId": "1"}, 1)
