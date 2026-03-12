from .conftest import get_client, verify_request_count


def test_smsCampaigns_get_sms_campaigns() -> None:
    """Test getSmsCampaigns endpoint with WireMock"""
    test_id = "sms_campaigns.get_sms_campaigns.0"
    client = get_client(test_id)
    client.sms_campaigns.get_sms_campaigns()
    verify_request_count(test_id, "GET", "/smsCampaigns", None, 1)


def test_smsCampaigns_create_sms_campaign() -> None:
    """Test createSmsCampaign endpoint with WireMock"""
    test_id = "sms_campaigns.create_sms_campaign.0"
    client = get_client(test_id)
    client.sms_campaigns.create_sms_campaign(
        content="Get a discount by visiting our NY store and saying : Happy Spring!",
        name="Spring Promo Code",
        sender="MyShop",
    )
    verify_request_count(test_id, "POST", "/smsCampaigns", None, 1)


def test_smsCampaigns_get_sms_campaign() -> None:
    """Test getSmsCampaign endpoint with WireMock"""
    test_id = "sms_campaigns.get_sms_campaign.0"
    client = get_client(test_id)
    client.sms_campaigns.get_sms_campaign(campaign_id=1000000)
    verify_request_count(test_id, "GET", "/smsCampaigns/1000000", None, 1)


def test_smsCampaigns_update_sms_campaign() -> None:
    """Test updateSmsCampaign endpoint with WireMock"""
    test_id = "sms_campaigns.update_sms_campaign.0"
    client = get_client(test_id)
    client.sms_campaigns.update_sms_campaign(campaign_id=1000000)
    verify_request_count(test_id, "PUT", "/smsCampaigns/1000000", None, 1)


def test_smsCampaigns_delete_sms_campaign() -> None:
    """Test deleteSmsCampaign endpoint with WireMock"""
    test_id = "sms_campaigns.delete_sms_campaign.0"
    client = get_client(test_id)
    client.sms_campaigns.delete_sms_campaign(campaign_id=1000000)
    verify_request_count(test_id, "DELETE", "/smsCampaigns/1000000", None, 1)


def test_smsCampaigns_request_sms_recipient_export() -> None:
    """Test requestSmsRecipientExport endpoint with WireMock"""
    test_id = "sms_campaigns.request_sms_recipient_export.0"
    client = get_client(test_id)
    client.sms_campaigns.request_sms_recipient_export(campaign_id=1000000, recipients_type="all")
    verify_request_count(test_id, "POST", "/smsCampaigns/1000000/exportRecipients", None, 1)


def test_smsCampaigns_send_sms_campaign_now() -> None:
    """Test sendSmsCampaignNow endpoint with WireMock"""
    test_id = "sms_campaigns.send_sms_campaign_now.0"
    client = get_client(test_id)
    client.sms_campaigns.send_sms_campaign_now(campaign_id=1000000)
    verify_request_count(test_id, "POST", "/smsCampaigns/1000000/sendNow", None, 1)


def test_smsCampaigns_send_sms_report() -> None:
    """Test sendSmsReport endpoint with WireMock"""
    test_id = "sms_campaigns.send_sms_report.0"
    client = get_client(test_id)
    client.sms_campaigns.send_sms_report(
        campaign_id=1000000,
        email={"body": "Please find attached the report of our last email campaign.", "to": ["jim.suehan@example.com"]},
    )
    verify_request_count(test_id, "POST", "/smsCampaigns/1000000/sendReport", None, 1)


def test_smsCampaigns_send_test_sms() -> None:
    """Test sendTestSms endpoint with WireMock"""
    test_id = "sms_campaigns.send_test_sms.0"
    client = get_client(test_id)
    client.sms_campaigns.send_test_sms(campaign_id=1000000)
    verify_request_count(test_id, "POST", "/smsCampaigns/1000000/sendTest", None, 1)


def test_smsCampaigns_update_sms_campaign_status() -> None:
    """Test updateSmsCampaignStatus endpoint with WireMock"""
    test_id = "sms_campaigns.update_sms_campaign_status.0"
    client = get_client(test_id)
    client.sms_campaigns.update_sms_campaign_status(campaign_id=1000000)
    verify_request_count(test_id, "PUT", "/smsCampaigns/1000000/status", None, 1)
