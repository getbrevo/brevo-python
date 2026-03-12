from .conftest import get_client, verify_request_count


def test_whatsAppCampaigns_get_whats_app_campaigns() -> None:
    """Test getWhatsAppCampaigns endpoint with WireMock"""
    test_id = "whats_app_campaigns.get_whats_app_campaigns.0"
    client = get_client(test_id)
    client.whats_app_campaigns.get_whats_app_campaigns()
    verify_request_count(test_id, "GET", "/whatsappCampaigns", None, 1)


def test_whatsAppCampaigns_create_whats_app_campaign() -> None:
    """Test createWhatsAppCampaign endpoint with WireMock"""
    test_id = "whats_app_campaigns.create_whats_app_campaign.0"
    client = get_client(test_id)
    client.whats_app_campaigns.create_whats_app_campaign(
        name="Test Campaign", recipients={}, scheduled_at="2017-06-01T12:30:00+02:00", template_id=19
    )
    verify_request_count(test_id, "POST", "/whatsappCampaigns", None, 1)


def test_whatsAppCampaigns_get_whats_app_config() -> None:
    """Test getWhatsAppConfig endpoint with WireMock"""
    test_id = "whats_app_campaigns.get_whats_app_config.0"
    client = get_client(test_id)
    client.whats_app_campaigns.get_whats_app_config()
    verify_request_count(test_id, "GET", "/whatsappCampaigns/config", None, 1)


def test_whatsAppCampaigns_create_whats_app_template() -> None:
    """Test createWhatsAppTemplate endpoint with WireMock"""
    test_id = "whats_app_campaigns.create_whats_app_template.0"
    client = get_client(test_id)
    client.whats_app_campaigns.create_whats_app_template(
        body_text="making it look like readable English", category="MARKETING", language="en", name="Test template"
    )
    verify_request_count(test_id, "POST", "/whatsappCampaigns/template", None, 1)


def test_whatsAppCampaigns_get_whats_app_templates() -> None:
    """Test getWhatsAppTemplates endpoint with WireMock"""
    test_id = "whats_app_campaigns.get_whats_app_templates.0"
    client = get_client(test_id)
    client.whats_app_campaigns.get_whats_app_templates()
    verify_request_count(test_id, "GET", "/whatsappCampaigns/template-list", None, 1)


def test_whatsAppCampaigns_send_whats_app_template_approval() -> None:
    """Test sendWhatsAppTemplateApproval endpoint with WireMock"""
    test_id = "whats_app_campaigns.send_whats_app_template_approval.0"
    client = get_client(test_id)
    client.whats_app_campaigns.send_whats_app_template_approval(template_id=1000000)
    verify_request_count(test_id, "POST", "/whatsappCampaigns/template/approval/1000000", None, 1)


def test_whatsAppCampaigns_get_whats_app_campaign() -> None:
    """Test getWhatsAppCampaign endpoint with WireMock"""
    test_id = "whats_app_campaigns.get_whats_app_campaign.0"
    client = get_client(test_id)
    client.whats_app_campaigns.get_whats_app_campaign(campaign_id=1000000)
    verify_request_count(test_id, "GET", "/whatsappCampaigns/1000000", None, 1)


def test_whatsAppCampaigns_update_whats_app_campaign() -> None:
    """Test updateWhatsAppCampaign endpoint with WireMock"""
    test_id = "whats_app_campaigns.update_whats_app_campaign.0"
    client = get_client(test_id)
    client.whats_app_campaigns.update_whats_app_campaign(campaign_id=1000000)
    verify_request_count(test_id, "PUT", "/whatsappCampaigns/1000000", None, 1)


def test_whatsAppCampaigns_delete_whats_app_campaign() -> None:
    """Test deleteWhatsAppCampaign endpoint with WireMock"""
    test_id = "whats_app_campaigns.delete_whats_app_campaign.0"
    client = get_client(test_id)
    client.whats_app_campaigns.delete_whats_app_campaign(campaign_id=1000000)
    verify_request_count(test_id, "DELETE", "/whatsappCampaigns/1000000", None, 1)
