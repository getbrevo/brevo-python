from .conftest import get_client, verify_request_count


def test_user_get_invited_users_list() -> None:
    """Test getInvitedUsersList endpoint with WireMock"""
    test_id = "user.get_invited_users_list.0"
    client = get_client(test_id)
    client.user.get_invited_users_list()
    verify_request_count(test_id, "GET", "/organization/invited/users", None, 1)


def test_user_put_revoke_user_permission() -> None:
    """Test putRevokeUserPermission endpoint with WireMock"""
    test_id = "user.put_revoke_user_permission.0"
    client = get_client(test_id)
    client.user.put_revoke_user_permission(email="email")
    verify_request_count(test_id, "PUT", "/organization/user/invitation/revoke/email", None, 1)


def test_user_inviteuser() -> None:
    """Test inviteuser endpoint with WireMock"""
    test_id = "user.inviteuser.0"
    client = get_client(test_id)
    client.user.inviteuser(all_features_access=True, email="inviteuser@example.com", privileges=[{}])
    verify_request_count(test_id, "POST", "/organization/user/invitation/send", None, 1)


def test_user_putresendcancelinvitation() -> None:
    """Test putresendcancelinvitation endpoint with WireMock"""
    test_id = "user.putresendcancelinvitation.0"
    client = get_client(test_id)
    client.user.putresendcancelinvitation(action="resend", email="email")
    verify_request_count(test_id, "PUT", "/organization/user/invitation/resend/email", None, 1)


def test_user_edit_user_permission() -> None:
    """Test EditUserPermission endpoint with WireMock"""
    test_id = "user.edit_user_permission.0"
    client = get_client(test_id)
    client.user.edit_user_permission(all_features_access=True, email="inviteuser@example.com", privileges=[{}])
    verify_request_count(test_id, "POST", "/organization/user/update/permissions", None, 1)


def test_user_get_user_permission() -> None:
    """Test getUserPermission endpoint with WireMock"""
    test_id = "user.get_user_permission.0"
    client = get_client(test_id)
    client.user.get_user_permission(email="email")
    verify_request_count(test_id, "GET", "/organization/user/email/permissions", None, 1)
