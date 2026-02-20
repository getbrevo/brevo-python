from .conftest import get_client, verify_request_count


def test_companies_get_all_companies() -> None:
    """Test getAllCompanies endpoint with WireMock"""
    test_id = "companies.get_all_companies.0"
    client = get_client(test_id)
    client.companies.get_all_companies()
    verify_request_count(test_id, "GET", "/companies", None, 1)


def test_companies_create_a_company() -> None:
    """Test createACompany endpoint with WireMock"""
    test_id = "companies.create_a_company.0"
    client = get_client(test_id)
    client.companies.create_a_company(name="company")
    verify_request_count(test_id, "POST", "/companies", None, 1)


def test_companies_import_companies_creation_and_updation() -> None:
    """Test importCompaniesCreationAndUpdation endpoint with WireMock"""
    test_id = "companies.import_companies_creation_and_updation.0"
    client = get_client(test_id)
    client.companies.import_companies_creation_and_updation(file="example_file")
    verify_request_count(test_id, "POST", "/companies/import", None, 1)


def test_companies_link_and_unlink_company_with_contact_and_deal() -> None:
    """Test linkAndUnlinkCompanyWithContactAndDeal endpoint with WireMock"""
    test_id = "companies.link_and_unlink_company_with_contact_and_deal.0"
    client = get_client(test_id)
    client.companies.link_and_unlink_company_with_contact_and_deal(id="id")
    verify_request_count(test_id, "PATCH", "/companies/link-unlink/id", None, 1)


def test_companies_get_a_company() -> None:
    """Test getACompany endpoint with WireMock"""
    test_id = "companies.get_a_company.0"
    client = get_client(test_id)
    client.companies.get_a_company(id="id")
    verify_request_count(test_id, "GET", "/companies/id", None, 1)


def test_companies_delete_a_company() -> None:
    """Test deleteACompany endpoint with WireMock"""
    test_id = "companies.delete_a_company.0"
    client = get_client(test_id)
    client.companies.delete_a_company(id="id")
    verify_request_count(test_id, "DELETE", "/companies/id", None, 1)


def test_companies_update_a_company() -> None:
    """Test updateACompany endpoint with WireMock"""
    test_id = "companies.update_a_company.0"
    client = get_client(test_id)
    client.companies.update_a_company(id="id")
    verify_request_count(test_id, "PATCH", "/companies/id", None, 1)


def test_companies_create_a_company_deal_attribute() -> None:
    """Test createACompanyDealAttribute endpoint with WireMock"""
    test_id = "companies.create_a_company_deal_attribute.0"
    client = get_client(test_id)
    client.companies.create_a_company_deal_attribute(
        attribute_type="text", label="Attribute Label", object_type="companies"
    )
    verify_request_count(test_id, "POST", "/crm/attributes", None, 1)


def test_companies_get_company_attributes() -> None:
    """Test getCompanyAttributes endpoint with WireMock"""
    test_id = "companies.get_company_attributes.0"
    client = get_client(test_id)
    client.companies.get_company_attributes()
    verify_request_count(test_id, "GET", "/crm/attributes/companies", None, 1)
