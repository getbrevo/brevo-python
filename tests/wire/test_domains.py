from .conftest import get_client, verify_request_count


def test_domains_get_domains() -> None:
    """Test getDomains endpoint with WireMock"""
    test_id = "domains.get_domains.0"
    client = get_client(test_id)
    client.domains.get_domains()
    verify_request_count(test_id, "GET", "/senders/domains", None, 1)


def test_domains_create_domain() -> None:
    """Test createDomain endpoint with WireMock"""
    test_id = "domains.create_domain.0"
    client = get_client(test_id)
    client.domains.create_domain(name="mycompany.com")
    verify_request_count(test_id, "POST", "/senders/domains", None, 1)


def test_domains_get_domain_configuration() -> None:
    """Test getDomainConfiguration endpoint with WireMock"""
    test_id = "domains.get_domain_configuration.0"
    client = get_client(test_id)
    client.domains.get_domain_configuration(domain_name="domainName")
    verify_request_count(test_id, "GET", "/senders/domains/domainName", None, 1)


def test_domains_delete_domain() -> None:
    """Test deleteDomain endpoint with WireMock"""
    test_id = "domains.delete_domain.0"
    client = get_client(test_id)
    client.domains.delete_domain(domain_name="domainName")
    verify_request_count(test_id, "DELETE", "/senders/domains/domainName", None, 1)


def test_domains_authenticate_domain() -> None:
    """Test authenticateDomain endpoint with WireMock"""
    test_id = "domains.authenticate_domain.0"
    client = get_client(test_id)
    client.domains.authenticate_domain(domain_name="domainName")
    verify_request_count(test_id, "PUT", "/senders/domains/domainName/authenticate", None, 1)
