from .conftest import get_client, verify_request_count


def test_program_get_lp_list() -> None:
    """Test getLPList endpoint with WireMock"""
    test_id = "program.get_lp_list.0"
    client = get_client(test_id)
    client.program.get_lp_list()
    verify_request_count(test_id, "GET", "/loyalty/config/programs", None, 1)


def test_program_create_new_lp() -> None:
    """Test createNewLP endpoint with WireMock"""
    test_id = "program.create_new_lp.0"
    client = get_client(test_id)
    client.program.create_new_lp(name="name")
    verify_request_count(test_id, "POST", "/loyalty/config/programs", None, 1)


def test_program_get_loyalty_program_info() -> None:
    """Test getLoyaltyProgramInfo endpoint with WireMock"""
    test_id = "program.get_loyalty_program_info.0"
    client = get_client(test_id)
    client.program.get_loyalty_program_info(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/config/programs/pid", None, 1)


def test_program_update_loyalty_program() -> None:
    """Test updateLoyaltyProgram endpoint with WireMock"""
    test_id = "program.update_loyalty_program.0"
    client = get_client(test_id)
    client.program.update_loyalty_program(pid="pid", name="name")
    verify_request_count(test_id, "PUT", "/loyalty/config/programs/pid", None, 1)


def test_program_delete_loyalty_program() -> None:
    """Test deleteLoyaltyProgram endpoint with WireMock"""
    test_id = "program.delete_loyalty_program.0"
    client = get_client(test_id)
    client.program.delete_loyalty_program(pid="pid")
    verify_request_count(test_id, "DELETE", "/loyalty/config/programs/pid", None, 1)


def test_program_partially_update_loyalty_program() -> None:
    """Test partiallyUpdateLoyaltyProgram endpoint with WireMock"""
    test_id = "program.partially_update_loyalty_program.0"
    client = get_client(test_id)
    client.program.partially_update_loyalty_program(pid="pid")
    verify_request_count(test_id, "PATCH", "/loyalty/config/programs/pid", None, 1)


def test_program_get_parameter_subscription_info() -> None:
    """Test getParameterSubscriptionInfo endpoint with WireMock"""
    test_id = "program.get_parameter_subscription_info.0"
    client = get_client(test_id)
    client.program.get_parameter_subscription_info(pid="pid")
    verify_request_count(test_id, "GET", "/loyalty/config/programs/pid/account-info", None, 1)


def test_program_publish_loyalty_program() -> None:
    """Test publishLoyaltyProgram endpoint with WireMock"""
    test_id = "program.publish_loyalty_program.0"
    client = get_client(test_id)
    client.program.publish_loyalty_program(pid="pid")
    verify_request_count(test_id, "POST", "/loyalty/config/programs/pid/publish", None, 1)


def test_program_subscribe_member_to_a_subscription() -> None:
    """Test subscribeMemberToASubscription endpoint with WireMock"""
    test_id = "program.subscribe_member_to_a_subscription.0"
    client = get_client(test_id)
    client.program.subscribe_member_to_a_subscription(pid="pid", member_contact_ids=[1])
    verify_request_count(test_id, "POST", "/loyalty/config/programs/pid/subscription-members", None, 1)


def test_program_delete_contact_members() -> None:
    """Test deleteContactMembers endpoint with WireMock"""
    test_id = "program.delete_contact_members.0"
    client = get_client(test_id)
    client.program.delete_contact_members(pid="pid", member_contact_ids="memberContactIds")
    verify_request_count(
        test_id,
        "DELETE",
        "/loyalty/config/programs/pid/subscription-members",
        {"memberContactIds": "memberContactIds"},
        1,
    )


def test_program_subscribe_to_loyalty_program() -> None:
    """Test subscribeToLoyaltyProgram endpoint with WireMock"""
    test_id = "program.subscribe_to_loyalty_program.0"
    client = get_client(test_id)
    client.program.subscribe_to_loyalty_program(pid="pid", contact_id=1)
    verify_request_count(test_id, "POST", "/loyalty/config/programs/pid/subscriptions", None, 1)
