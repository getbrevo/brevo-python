from .conftest import get_client, verify_request_count


def test_deals_get_deal_attributes() -> None:
    """Test getDealAttributes endpoint with WireMock"""
    test_id = "deals.get_deal_attributes.0"
    client = get_client(test_id)
    client.deals.get_deal_attributes()
    verify_request_count(test_id, "GET", "/crm/attributes/deals", None, 1)


def test_deals_get_all_deals() -> None:
    """Test getAllDeals endpoint with WireMock"""
    test_id = "deals.get_all_deals.0"
    client = get_client(test_id)
    client.deals.get_all_deals()
    verify_request_count(test_id, "GET", "/crm/deals", None, 1)


def test_deals_create_a_deal() -> None:
    """Test createADeal endpoint with WireMock"""
    test_id = "deals.create_a_deal.0"
    client = get_client(test_id)
    client.deals.create_a_deal(name="Deal: Connect with company")
    verify_request_count(test_id, "POST", "/crm/deals", None, 1)


def test_deals_import_deals_creation_and_updation() -> None:
    """Test importDealsCreationAndUpdation endpoint with WireMock"""
    test_id = "deals.import_deals_creation_and_updation.0"
    client = get_client(test_id)
    client.deals.import_deals_creation_and_updation(file="example_file")
    verify_request_count(test_id, "POST", "/crm/deals/import", None, 1)


def test_deals_link_and_unlink_a_deal_with_contacts_and_companies() -> None:
    """Test linkAndUnlinkADealWithContactsAndCompanies endpoint with WireMock"""
    test_id = "deals.link_and_unlink_a_deal_with_contacts_and_companies.0"
    client = get_client(test_id)
    client.deals.link_and_unlink_a_deal_with_contacts_and_companies(id="id")
    verify_request_count(test_id, "PATCH", "/crm/deals/link-unlink/id", None, 1)


def test_deals_get_a_deal() -> None:
    """Test getADeal endpoint with WireMock"""
    test_id = "deals.get_a_deal.0"
    client = get_client(test_id)
    client.deals.get_a_deal(id="id")
    verify_request_count(test_id, "GET", "/crm/deals/id", None, 1)


def test_deals_delete_a_deal() -> None:
    """Test deleteADeal endpoint with WireMock"""
    test_id = "deals.delete_a_deal.0"
    client = get_client(test_id)
    client.deals.delete_a_deal(id="id")
    verify_request_count(test_id, "DELETE", "/crm/deals/id", None, 1)


def test_deals_update_a_deal() -> None:
    """Test updateADeal endpoint with WireMock"""
    test_id = "deals.update_a_deal.0"
    client = get_client(test_id)
    client.deals.update_a_deal(id="id")
    verify_request_count(test_id, "PATCH", "/crm/deals/id", None, 1)


def test_deals_get_pipeline_stages() -> None:
    """Test getPipelineStages endpoint with WireMock"""
    test_id = "deals.get_pipeline_stages.0"
    client = get_client(test_id)
    client.deals.get_pipeline_stages()
    verify_request_count(test_id, "GET", "/crm/pipeline/details", None, 1)


def test_deals_get_all_pipelines() -> None:
    """Test getAllPipelines endpoint with WireMock"""
    test_id = "deals.get_all_pipelines.0"
    client = get_client(test_id)
    client.deals.get_all_pipelines()
    verify_request_count(test_id, "GET", "/crm/pipeline/details/all", None, 1)


def test_deals_get_a_pipeline() -> None:
    """Test getAPipeline endpoint with WireMock"""
    test_id = "deals.get_a_pipeline.0"
    client = get_client(test_id)
    client.deals.get_a_pipeline(pipeline_id="pipelineID")
    verify_request_count(test_id, "GET", "/crm/pipeline/details/pipelineID", None, 1)
