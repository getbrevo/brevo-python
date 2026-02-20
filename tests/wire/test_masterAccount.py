from .conftest import get_client, verify_request_count


def test_masterAccount_create_a_new_group_of_sub_accounts() -> None:
    """Test createANewGroupOfSubAccounts endpoint with WireMock"""
    test_id = "master_account.create_a_new_group_of_sub_accounts.0"
    client = get_client(test_id)
    client.master_account.create_a_new_group_of_sub_accounts(group_name="My group")
    verify_request_count(test_id, "POST", "/corporate/group", None, 1)


def test_masterAccount_delete_sub_account_from_group() -> None:
    """Test deleteSubAccountFromGroup endpoint with WireMock"""
    test_id = "master_account.delete_sub_account_from_group.0"
    client = get_client(test_id)
    client.master_account.delete_sub_account_from_group(group_id="groupId", sub_account_ids=[423432, 234323, 87678])
    verify_request_count(test_id, "PUT", "/corporate/group/unlink/groupId/subAccounts", None, 1)


def test_masterAccount_get_a_group_details() -> None:
    """Test getAGroupDetails endpoint with WireMock"""
    test_id = "master_account.get_a_group_details.0"
    client = get_client(test_id)
    client.master_account.get_a_group_details(id="id")
    verify_request_count(test_id, "GET", "/corporate/group/id", None, 1)


def test_masterAccount_update_a_group_of_sub_accounts() -> None:
    """Test updateAGroupOfSubAccounts endpoint with WireMock"""
    test_id = "master_account.update_a_group_of_sub_accounts.0"
    client = get_client(test_id)
    client.master_account.update_a_group_of_sub_accounts(id="id")
    verify_request_count(test_id, "PUT", "/corporate/group/id", None, 1)


def test_masterAccount_delete_a_group() -> None:
    """Test deleteAGroup endpoint with WireMock"""
    test_id = "master_account.delete_a_group.0"
    client = get_client(test_id)
    client.master_account.delete_a_group(id="id")
    verify_request_count(test_id, "DELETE", "/corporate/group/id", None, 1)


def test_masterAccount_get_sub_account_groups() -> None:
    """Test getSubAccountGroups endpoint with WireMock"""
    test_id = "master_account.get_sub_account_groups.0"
    client = get_client(test_id)
    client.master_account.get_sub_account_groups()
    verify_request_count(test_id, "GET", "/corporate/groups", None, 1)


def test_masterAccount_get_corporate_invited_users_list() -> None:
    """Test getCorporateInvitedUsersList endpoint with WireMock"""
    test_id = "master_account.get_corporate_invited_users_list.0"
    client = get_client(test_id)
    client.master_account.get_corporate_invited_users_list()
    verify_request_count(test_id, "GET", "/corporate/invited/users", None, 1)


def test_masterAccount_list_of_all_i_ps() -> None:
    """Test listOfAllIPs endpoint with WireMock"""
    test_id = "master_account.list_of_all_i_ps.0"
    client = get_client(test_id)
    client.master_account.list_of_all_i_ps()
    verify_request_count(test_id, "GET", "/corporate/ip", None, 1)


def test_masterAccount_get_the_details_of_requested_master_account() -> None:
    """Test getTheDetailsOfRequestedMasterAccount endpoint with WireMock"""
    test_id = "master_account.get_the_details_of_requested_master_account.0"
    client = get_client(test_id)
    client.master_account.get_the_details_of_requested_master_account()
    verify_request_count(test_id, "GET", "/corporate/masterAccount", None, 1)


def test_masterAccount_generate_sso_token_to_access_admin_account() -> None:
    """Test generateSsoTokenToAccessAdminAccount endpoint with WireMock"""
    test_id = "master_account.generate_sso_token_to_access_admin_account.0"
    client = get_client(test_id)
    client.master_account.generate_sso_token_to_access_admin_account(email="vipin+ent-user@brevo.com")
    verify_request_count(test_id, "POST", "/corporate/ssoToken", None, 1)


def test_masterAccount_get_the_list_of_all_the_sub_accounts_of_the_master_account() -> None:
    """Test getTheListOfAllTheSubAccountsOfTheMasterAccount endpoint with WireMock"""
    test_id = "master_account.get_the_list_of_all_the_sub_accounts_of_the_master_account.0"
    client = get_client(test_id)
    client.master_account.get_the_list_of_all_the_sub_accounts_of_the_master_account(offset=1, limit=1)
    verify_request_count(test_id, "GET", "/corporate/subAccount", {"offset": "1", "limit": "1"}, 1)


def test_masterAccount_create_a_new_sub_account_under_a_master_account() -> None:
    """Test createANewSubAccountUnderAMasterAccount endpoint with WireMock"""
    test_id = "master_account.create_a_new_sub_account_under_a_master_account.0"
    client = get_client(test_id)
    client.master_account.create_a_new_sub_account_under_a_master_account(
        company_name="Test Sub-account",
        email="test-sub@example.com",
        group_ids=["5f8f8c3b5f56a02d4433b3a7", "5f8f8c3b5f56a02d4433b3a8"],
        language="fr",
        timezone="Europe/Paris",
    )
    verify_request_count(test_id, "POST", "/corporate/subAccount", None, 1)


def test_masterAccount_associate_an_ip_to_sub_accounts() -> None:
    """Test associateAnIpToSubAccounts endpoint with WireMock"""
    test_id = "master_account.associate_an_ip_to_sub_accounts.0"
    client = get_client(test_id)
    client.master_account.associate_an_ip_to_sub_accounts(ids=[234322, 325553, 893432], ip="103.11.32.88")
    verify_request_count(test_id, "POST", "/corporate/subAccount/ip/associate", None, 1)


def test_masterAccount_dissociate_an_ip_to_sub_accounts() -> None:
    """Test dissociateAnIpToSubAccounts endpoint with WireMock"""
    test_id = "master_account.dissociate_an_ip_to_sub_accounts.0"
    client = get_client(test_id)
    client.master_account.dissociate_an_ip_to_sub_accounts(ids=[234322, 325553, 893432], ip="103.11.32.88")
    verify_request_count(test_id, "PUT", "/corporate/subAccount/ip/dissociate", None, 1)


def test_masterAccount_create_an_api_key_for_a_sub_account() -> None:
    """Test createAnApiKeyForASubAccount endpoint with WireMock"""
    test_id = "master_account.create_an_api_key_for_a_sub_account.0"
    client = get_client(test_id)
    client.master_account.create_an_api_key_for_a_sub_account(id=3232323, name="My Api Key")
    verify_request_count(test_id, "POST", "/corporate/subAccount/key", None, 1)


def test_masterAccount_generate_sso_token_to_access_sub_account() -> None:
    """Test generateSsoTokenToAccessSubAccount endpoint with WireMock"""
    test_id = "master_account.generate_sso_token_to_access_sub_account.0"
    client = get_client(test_id)
    client.master_account.generate_sso_token_to_access_sub_account(id=3232323)
    verify_request_count(test_id, "POST", "/corporate/subAccount/ssoToken", None, 1)


def test_masterAccount_get_sub_account_details() -> None:
    """Test getSubAccountDetails endpoint with WireMock"""
    test_id = "master_account.get_sub_account_details.0"
    client = get_client(test_id)
    client.master_account.get_sub_account_details(id=1000000)
    verify_request_count(test_id, "GET", "/corporate/subAccount/1000000", None, 1)


def test_masterAccount_delete_a_sub_account() -> None:
    """Test deleteASubAccount endpoint with WireMock"""
    test_id = "master_account.delete_a_sub_account.0"
    client = get_client(test_id)
    client.master_account.delete_a_sub_account(id=1000000)
    verify_request_count(test_id, "DELETE", "/corporate/subAccount/1000000", None, 1)


def test_masterAccount_enable_disable_sub_account_application_s() -> None:
    """Test enableDisableSubAccountApplicationS endpoint with WireMock"""
    test_id = "master_account.enable_disable_sub_account_application_s.0"
    client = get_client(test_id)
    client.master_account.enable_disable_sub_account_application_s(
        id=1000000, landing_pages=True, meetings=True, sms_campaigns=False, web_push=False, whatsapp=True
    )
    verify_request_count(test_id, "PUT", "/corporate/subAccount/1000000/applications/toggle", None, 1)


def test_masterAccount_update_sub_account_plan() -> None:
    """Test updateSubAccountPlan endpoint with WireMock"""
    test_id = "master_account.update_sub_account_plan.0"
    client = get_client(test_id)
    client.master_account.update_sub_account_plan(
        id=1000000,
        credits={"email": 5000, "external_feeds": 1, "sms": 2000, "whatsapp": 100, "wp_subscribers": -1},
        features={"inbox": 10, "landing_page": 20, "sales_users": 6, "users": 15},
    )
    verify_request_count(test_id, "PUT", "/corporate/subAccount/1000000/plan", None, 1)


def test_masterAccount_update_sub_accounts_plan() -> None:
    """Test updateSubAccountsPlan endpoint with WireMock"""
    test_id = "master_account.update_sub_accounts_plan.0"
    client = get_client(test_id)
    client.master_account.update_sub_accounts_plan(
        credits={"email": 5000, "external_feeds": 1, "sms": 2000, "whatsapp": 100, "wp_subscribers": -1},
        features={"landing_page": 20, "sales_users": 6, "users": 15},
        sub_account_ids=[4534345, 987893, 876785],
    )
    verify_request_count(test_id, "PUT", "/corporate/subAccounts/plan", None, 1)


def test_masterAccount_invite_admin_user() -> None:
    """Test inviteAdminUser endpoint with WireMock"""
    test_id = "master_account.invite_admin_user.0"
    client = get_client(test_id)
    client.master_account.invite_admin_user(all_features_access=True, email="inviteuser@example.com", privileges=[{}])
    verify_request_count(test_id, "POST", "/corporate/user/invitation/send", None, 1)


def test_masterAccount_resend_cancel_admin_user_invitation() -> None:
    """Test resendCancelAdminUserInvitation endpoint with WireMock"""
    test_id = "master_account.resend_cancel_admin_user_invitation.0"
    client = get_client(test_id)
    client.master_account.resend_cancel_admin_user_invitation(action="resend", email="email")
    verify_request_count(test_id, "PUT", "/corporate/user/invitation/resend/email", None, 1)


def test_masterAccount_revoke_an_admin_user() -> None:
    """Test revokeAnAdminUser endpoint with WireMock"""
    test_id = "master_account.revoke_an_admin_user.0"
    client = get_client(test_id)
    client.master_account.revoke_an_admin_user(email="email")
    verify_request_count(test_id, "DELETE", "/corporate/user/revoke/email", None, 1)


def test_masterAccount_get_corporate_user_permission() -> None:
    """Test getCorporateUserPermission endpoint with WireMock"""
    test_id = "master_account.get_corporate_user_permission.0"
    client = get_client(test_id)
    client.master_account.get_corporate_user_permission(email="email")
    verify_request_count(test_id, "GET", "/corporate/user/email/permissions", None, 1)


def test_masterAccount_change_admin_user_permissions() -> None:
    """Test changeAdminUserPermissions endpoint with WireMock"""
    test_id = "master_account.change_admin_user_permissions.0"
    client = get_client(test_id)
    client.master_account.change_admin_user_permissions(
        email="email",
        all_features_access=False,
        privileges=[
            {"feature": "user_management", "permissions": ["all"]},
            {"feature": "api", "permissions": ["all"]},
            {"feature": "my_plan", "permissions": ["none"]},
            {"feature": "apps_management", "permissions": ["all"]},
            {"feature": "create_sub_organizations", "permissions": ["all"]},
            {"feature": "sub_organization_groups", "permissions": ["create", "edit_delete"]},
            {"feature": "manage_sub_organizations", "permissions": ["all"]},
            {"feature": "security", "permissions": ["none"]},
            {"feature": "analytics", "permissions": ["create_alerts", "download_data", "my_looks", "explore_create"]},
        ],
    )
    verify_request_count(test_id, "PUT", "/corporate/user/email/permissions", None, 1)
