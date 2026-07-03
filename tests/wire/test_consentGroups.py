from .conftest import get_client, verify_request_count


def test_consentGroups_get_consent_groups() -> None:
    """Test getConsentGroups endpoint with WireMock"""
    test_id = "consent_groups.get_consent_groups.0"
    client = get_client(test_id)
    client.consent_groups.get_consent_groups()
    verify_request_count(test_id, "GET", "/contacts/consent-groups", None, 1)


def test_consentGroups_create_consent_group() -> None:
    """Test createConsentGroup endpoint with WireMock"""
    test_id = "consent_groups.create_consent_group.0"
    client = get_client(test_id)
    client.consent_groups.create_consent_group(
        name="Newsletter EU",
        signup_mode="manual",
    )
    verify_request_count(test_id, "POST", "/contacts/consent-groups", None, 1)


def test_consentGroups_get_consent_group() -> None:
    """Test getConsentGroup endpoint with WireMock"""
    test_id = "consent_groups.get_consent_group.0"
    client = get_client(test_id)
    client.consent_groups.get_consent_group(
        id=1000000,
    )
    verify_request_count(test_id, "GET", "/contacts/consent-groups/1000000", None, 1)


def test_consentGroups_update_consent_group() -> None:
    """Test updateConsentGroup endpoint with WireMock"""
    test_id = "consent_groups.update_consent_group.0"
    client = get_client(test_id)
    client.consent_groups.update_consent_group(
        id=1000000,
    )
    verify_request_count(test_id, "PUT", "/contacts/consent-groups/1000000", None, 1)


def test_consentGroups_delete_consent_group() -> None:
    """Test deleteConsentGroup endpoint with WireMock"""
    test_id = "consent_groups.delete_consent_group.0"
    client = get_client(test_id)
    client.consent_groups.delete_consent_group(
        id=1000000,
    )
    verify_request_count(test_id, "DELETE", "/contacts/consent-groups/1000000", None, 1)
