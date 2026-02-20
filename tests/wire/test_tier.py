from .conftest import get_client, verify_request_count


def test_tier_add_subscription_to_tier() -> None:
    """Test addSubscriptionToTier endpoint with WireMock"""
    test_id = "tier.add_subscription_to_tier.0"
    client = get_client(test_id)
    client.tier.add_subscription_to_tier(pid="pid", cid="cid", tid="tid")
    verify_request_count(test_id, "POST", "/loyalty/tier/programs/pid/contacts/cid/tiers/tid", None, 1)


def test_tier_get_list_of_tier_groups() -> None:
    """Test getListOfTierGroups endpoint with WireMock"""
    test_id = "tier.get_list_of_tier_groups.0"
    client = get_client(test_id)
    client.tier.get_list_of_tier_groups(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/tier/programs/pid/tier-groups", None, 1)


def test_tier_create_tier_group() -> None:
    """Test createTierGroup endpoint with WireMock"""
    test_id = "tier.create_tier_group.0"
    client = get_client(test_id)
    client.tier.create_tier_group(pid="pid", name="name")
    verify_request_count(test_id, "POST", "/loyalty/tier/programs/pid/tier-groups", None, 1)


def test_tier_get_tier_group() -> None:
    """Test getTierGroup endpoint with WireMock"""
    test_id = "tier.get_tier_group.0"
    client = get_client(test_id)
    client.tier.get_tier_group(pid="pid", gid="gid")
    verify_request_count(test_id, "GET", "/loyalty/tier/programs/pid/tier-groups/gid", None, 1)


def test_tier_update_tier_group() -> None:
    """Test updateTierGroup endpoint with WireMock"""
    test_id = "tier.update_tier_group.0"
    client = get_client(test_id)
    client.tier.update_tier_group(
        pid="pid",
        gid="gid",
        downgrade_strategy="real_time",
        name="name",
        tier_order=["tierOrder"],
        upgrade_strategy="real_time",
    )
    verify_request_count(test_id, "PUT", "/loyalty/tier/programs/pid/tier-groups/gid", None, 1)


def test_tier_delete_tier_group() -> None:
    """Test deleteTierGroup endpoint with WireMock"""
    test_id = "tier.delete_tier_group.0"
    client = get_client(test_id)
    client.tier.delete_tier_group(pid="pid", gid="gid")
    verify_request_count(test_id, "DELETE", "/loyalty/tier/programs/pid/tier-groups/gid", None, 1)


def test_tier_create_tier_for_tier_group() -> None:
    """Test createTierForTierGroup endpoint with WireMock"""
    test_id = "tier.create_tier_for_tier_group.0"
    client = get_client(test_id)
    client.tier.create_tier_for_tier_group(pid="pid", gid="gid", access_conditions=[{}], name="name")
    verify_request_count(test_id, "POST", "/loyalty/tier/programs/pid/tier-groups/gid/tiers", None, 1)


def test_tier_get_loyalty_program_tier() -> None:
    """Test getLoyaltyProgramTier endpoint with WireMock"""
    test_id = "tier.get_loyalty_program_tier.0"
    client = get_client(test_id)
    client.tier.get_loyalty_program_tier(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/tier/programs/pid/tiers", None, 1)


def test_tier_update_tier() -> None:
    """Test updateTier endpoint with WireMock"""
    test_id = "tier.update_tier.0"
    client = get_client(test_id)
    client.tier.update_tier(pid="pid", tid="tid", access_conditions=[{}], name="name", tier_rewards=[{}])
    verify_request_count(test_id, "PUT", "/loyalty/tier/programs/pid/tiers/tid", None, 1)


def test_tier_delete_tier() -> None:
    """Test deleteTier endpoint with WireMock"""
    test_id = "tier.delete_tier.0"
    client = get_client(test_id)
    client.tier.delete_tier(pid="pid", tid="tid")
    verify_request_count(test_id, "DELETE", "/loyalty/tier/programs/pid/tiers/tid", None, 1)
