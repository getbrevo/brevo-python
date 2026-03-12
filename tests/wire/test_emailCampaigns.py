from .conftest import get_client, verify_request_count


def test_emailCampaigns_get_email_campaigns() -> None:
    """Test getEmailCampaigns endpoint with WireMock"""
    test_id = "email_campaigns.get_email_campaigns.0"
    client = get_client(test_id)
    client.email_campaigns.get_email_campaigns()
    verify_request_count(test_id, "GET", "/emailCampaigns", None, 1)


def test_emailCampaigns_create_email_campaign() -> None:
    """Test createEmailCampaign endpoint with WireMock"""
    test_id = "email_campaigns.create_email_campaign.0"
    client = get_client(test_id)
    client.email_campaigns.create_email_campaign(name="Newsletter - May 2017", sender={})
    verify_request_count(test_id, "POST", "/emailCampaigns", None, 1)


def test_emailCampaigns_upload_image_to_gallery() -> None:
    """Test uploadImageToGallery endpoint with WireMock"""
    test_id = "email_campaigns.upload_image_to_gallery.0"
    client = get_client(test_id)
    client.email_campaigns.upload_image_to_gallery(image_url="https://somedomain.com/image1.jpg")
    verify_request_count(test_id, "POST", "/emailCampaigns/images", None, 1)


def test_emailCampaigns_get_email_campaign() -> None:
    """Test getEmailCampaign endpoint with WireMock"""
    test_id = "email_campaigns.get_email_campaign.0"
    client = get_client(test_id)
    client.email_campaigns.get_email_campaign(campaign_id=1000000)
    verify_request_count(test_id, "GET", "/emailCampaigns/1000000", None, 1)


def test_emailCampaigns_update_email_campaign() -> None:
    """Test updateEmailCampaign endpoint with WireMock"""
    test_id = "email_campaigns.update_email_campaign.0"
    client = get_client(test_id)
    client.email_campaigns.update_email_campaign(campaign_id=1000000)
    verify_request_count(test_id, "PUT", "/emailCampaigns/1000000", None, 1)


def test_emailCampaigns_delete_email_campaign() -> None:
    """Test deleteEmailCampaign endpoint with WireMock"""
    test_id = "email_campaigns.delete_email_campaign.0"
    client = get_client(test_id)
    client.email_campaigns.delete_email_campaign(campaign_id=1000000)
    verify_request_count(test_id, "DELETE", "/emailCampaigns/1000000", None, 1)


def test_emailCampaigns_get_ab_test_campaign_result() -> None:
    """Test getAbTestCampaignResult endpoint with WireMock"""
    test_id = "email_campaigns.get_ab_test_campaign_result.0"
    client = get_client(test_id)
    client.email_campaigns.get_ab_test_campaign_result(campaign_id=1000000)
    verify_request_count(test_id, "GET", "/emailCampaigns/1000000/abTestCampaignResult", None, 1)


def test_emailCampaigns_email_export_recipients() -> None:
    """Test emailExportRecipients endpoint with WireMock"""
    test_id = "email_campaigns.email_export_recipients.0"
    client = get_client(test_id)
    client.email_campaigns.email_export_recipients(campaign_id=1000000, recipients_type="all")
    verify_request_count(test_id, "POST", "/emailCampaigns/1000000/exportRecipients", None, 1)


def test_emailCampaigns_send_email_campaign_now() -> None:
    """Test sendEmailCampaignNow endpoint with WireMock"""
    test_id = "email_campaigns.send_email_campaign_now.0"
    client = get_client(test_id)
    client.email_campaigns.send_email_campaign_now(campaign_id=1000000)
    verify_request_count(test_id, "POST", "/emailCampaigns/1000000/sendNow", None, 1)


def test_emailCampaigns_send_report() -> None:
    """Test sendReport endpoint with WireMock"""
    test_id = "email_campaigns.send_report.0"
    client = get_client(test_id)
    client.email_campaigns.send_report(
        campaign_id=1000000,
        email={"body": "Please find attached the report of our last email campaign.", "to": ["jim.suehan@example.com"]},
    )
    verify_request_count(test_id, "POST", "/emailCampaigns/1000000/sendReport", None, 1)


def test_emailCampaigns_send_test_email() -> None:
    """Test sendTestEmail endpoint with WireMock"""
    test_id = "email_campaigns.send_test_email.0"
    client = get_client(test_id)
    client.email_campaigns.send_test_email(campaign_id=1000000)
    verify_request_count(test_id, "POST", "/emailCampaigns/1000000/sendTest", None, 1)


def test_emailCampaigns_get_shared_template_url() -> None:
    """Test getSharedTemplateUrl endpoint with WireMock"""
    test_id = "email_campaigns.get_shared_template_url.0"
    client = get_client(test_id)
    client.email_campaigns.get_shared_template_url(campaign_id=1000000)
    verify_request_count(test_id, "GET", "/emailCampaigns/1000000/sharedUrl", None, 1)


def test_emailCampaigns_update_campaign_status() -> None:
    """Test updateCampaignStatus endpoint with WireMock"""
    test_id = "email_campaigns.update_campaign_status.0"
    client = get_client(test_id)
    client.email_campaigns.update_campaign_status(campaign_id=1000000)
    verify_request_count(test_id, "PUT", "/emailCampaigns/1000000/status", None, 1)
