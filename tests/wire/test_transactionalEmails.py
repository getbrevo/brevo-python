from datetime import date

from .conftest import get_client, verify_request_count


def test_transactionalEmails_get_transac_blocked_contacts() -> None:
    """Test getTransacBlockedContacts endpoint with WireMock"""
    test_id = "transactional_emails.get_transac_blocked_contacts.0"
    client = get_client(test_id)
    client.transactional_emails.get_transac_blocked_contacts()
    verify_request_count(test_id, "GET", "/smtp/blockedContacts", None, 1)


def test_transactionalEmails_unblock_or_resubscribe_a_transactional_contact() -> None:
    """Test unblockOrResubscribeATransactionalContact endpoint with WireMock"""
    test_id = "transactional_emails.unblock_or_resubscribe_a_transactional_contact.0"
    client = get_client(test_id)
    client.transactional_emails.unblock_or_resubscribe_a_transactional_contact(email="email")
    verify_request_count(test_id, "DELETE", "/smtp/blockedContacts/email", None, 1)


def test_transactionalEmails_get_blocked_domains() -> None:
    """Test getBlockedDomains endpoint with WireMock"""
    test_id = "transactional_emails.get_blocked_domains.0"
    client = get_client(test_id)
    client.transactional_emails.get_blocked_domains()
    verify_request_count(test_id, "GET", "/smtp/blockedDomains", None, 1)


def test_transactionalEmails_block_new_domain() -> None:
    """Test blockNewDomain endpoint with WireMock"""
    test_id = "transactional_emails.block_new_domain.0"
    client = get_client(test_id)
    client.transactional_emails.block_new_domain(domain="example.com")
    verify_request_count(test_id, "POST", "/smtp/blockedDomains", None, 1)


def test_transactionalEmails_delete_blocked_domain() -> None:
    """Test deleteBlockedDomain endpoint with WireMock"""
    test_id = "transactional_emails.delete_blocked_domain.0"
    client = get_client(test_id)
    client.transactional_emails.delete_blocked_domain(domain="domain")
    verify_request_count(test_id, "DELETE", "/smtp/blockedDomains/domain", None, 1)


def test_transactionalEmails_delete_hardbounces() -> None:
    """Test deleteHardbounces endpoint with WireMock"""
    test_id = "transactional_emails.delete_hardbounces.0"
    client = get_client(test_id)
    client.transactional_emails.delete_hardbounces()
    verify_request_count(test_id, "POST", "/smtp/deleteHardbounces", None, 1)


def test_transactionalEmails_send_transac_email() -> None:
    """Test sendTransacEmail endpoint with WireMock"""
    test_id = "transactional_emails.send_transac_email.0"
    client = get_client(test_id)
    client.transactional_emails.send_transac_email(
        html_content="<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Brevo.</p></body></html>",
        sender={"email": "hello@brevo.com", "name": "Alex from Brevo"},
        subject="Hello from Brevo!",
        to=[{"email": "johndoe@example.com", "name": "John Doe"}],
    )
    verify_request_count(test_id, "POST", "/smtp/email", None, 1)


def test_transactionalEmails_delete_scheduled_email_by_id() -> None:
    """Test deleteScheduledEmailById endpoint with WireMock"""
    test_id = "transactional_emails.delete_scheduled_email_by_id.0"
    client = get_client(test_id)
    client.transactional_emails.delete_scheduled_email_by_id(identifier="4320f270-a4e3-4a2e-b591-edfe30a5e627")
    verify_request_count(test_id, "DELETE", "/smtp/email/4320f270-a4e3-4a2e-b591-edfe30a5e627", None, 1)


def test_transactionalEmails_get_scheduled_email_by_id() -> None:
    """Test getScheduledEmailById endpoint with WireMock"""
    test_id = "transactional_emails.get_scheduled_email_by_id.0"
    client = get_client(test_id)
    client.transactional_emails.get_scheduled_email_by_id(
        identifier="4320f270-a4e3-4a2e-b591-edfe30a5e627",
        start_date=date.fromisoformat("2022-02-02"),
        end_date=date.fromisoformat("2022-03-02"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/smtp/emailStatus/4320f270-a4e3-4a2e-b591-edfe30a5e627",
        {"startDate": "2022-02-02", "endDate": "2022-03-02"},
        1,
    )


def test_transactionalEmails_get_transac_emails_list() -> None:
    """Test getTransacEmailsList endpoint with WireMock"""
    test_id = "transactional_emails.get_transac_emails_list.0"
    client = get_client(test_id)
    client.transactional_emails.get_transac_emails_list()
    verify_request_count(test_id, "GET", "/smtp/emails", None, 1)


def test_transactionalEmails_get_transac_email_content() -> None:
    """Test getTransacEmailContent endpoint with WireMock"""
    test_id = "transactional_emails.get_transac_email_content.0"
    client = get_client(test_id)
    client.transactional_emails.get_transac_email_content(uuid_="uuid")
    verify_request_count(test_id, "GET", "/smtp/emails/uuid", None, 1)


def test_transactionalEmails_delete_an_smtp_transactional_log() -> None:
    """Test deleteAnSmtpTransactionalLog endpoint with WireMock"""
    test_id = "transactional_emails.delete_an_smtp_transactional_log.0"
    client = get_client(test_id)
    client.transactional_emails.delete_an_smtp_transactional_log(identifier="identifier")
    verify_request_count(test_id, "DELETE", "/smtp/log/identifier", None, 1)


def test_transactionalEmails_get_aggregated_smtp_report() -> None:
    """Test getAggregatedSmtpReport endpoint with WireMock"""
    test_id = "transactional_emails.get_aggregated_smtp_report.0"
    client = get_client(test_id)
    client.transactional_emails.get_aggregated_smtp_report()
    verify_request_count(test_id, "GET", "/smtp/statistics/aggregatedReport", None, 1)


def test_transactionalEmails_get_email_event_report() -> None:
    """Test getEmailEventReport endpoint with WireMock"""
    test_id = "transactional_emails.get_email_event_report.0"
    client = get_client(test_id)
    client.transactional_emails.get_email_event_report()
    verify_request_count(test_id, "GET", "/smtp/statistics/events", None, 1)


def test_transactionalEmails_get_smtp_report() -> None:
    """Test getSmtpReport endpoint with WireMock"""
    test_id = "transactional_emails.get_smtp_report.0"
    client = get_client(test_id)
    client.transactional_emails.get_smtp_report()
    verify_request_count(test_id, "GET", "/smtp/statistics/reports", None, 1)


def test_transactionalEmails_post_preview_smtp_email_templates() -> None:
    """Test postPreviewSmtpEmailTemplates endpoint with WireMock"""
    test_id = "transactional_emails.post_preview_smtp_email_templates.0"
    client = get_client(test_id)
    client.transactional_emails.post_preview_smtp_email_templates(
        request={
            "key": "value",
        }
    )
    verify_request_count(test_id, "POST", "/smtp/template/preview", None, 1)


def test_transactionalEmails_get_smtp_templates() -> None:
    """Test getSmtpTemplates endpoint with WireMock"""
    test_id = "transactional_emails.get_smtp_templates.0"
    client = get_client(test_id)
    client.transactional_emails.get_smtp_templates()
    verify_request_count(test_id, "GET", "/smtp/templates", None, 1)


def test_transactionalEmails_create_smtp_template() -> None:
    """Test createSmtpTemplate endpoint with WireMock"""
    test_id = "transactional_emails.create_smtp_template.0"
    client = get_client(test_id)
    client.transactional_emails.create_smtp_template(
        sender={}, subject="Thanks for your purchase !", template_name="Order Confirmation - EN"
    )
    verify_request_count(test_id, "POST", "/smtp/templates", None, 1)


def test_transactionalEmails_get_smtp_template() -> None:
    """Test getSmtpTemplate endpoint with WireMock"""
    test_id = "transactional_emails.get_smtp_template.0"
    client = get_client(test_id)
    client.transactional_emails.get_smtp_template(template_id=1000000)
    verify_request_count(test_id, "GET", "/smtp/templates/1000000", None, 1)


def test_transactionalEmails_update_smtp_template() -> None:
    """Test updateSmtpTemplate endpoint with WireMock"""
    test_id = "transactional_emails.update_smtp_template.0"
    client = get_client(test_id)
    client.transactional_emails.update_smtp_template(template_id=1000000)
    verify_request_count(test_id, "PUT", "/smtp/templates/1000000", None, 1)


def test_transactionalEmails_delete_smtp_template() -> None:
    """Test deleteSmtpTemplate endpoint with WireMock"""
    test_id = "transactional_emails.delete_smtp_template.0"
    client = get_client(test_id)
    client.transactional_emails.delete_smtp_template(template_id=1000000)
    verify_request_count(test_id, "DELETE", "/smtp/templates/1000000", None, 1)


def test_transactionalEmails_send_test_template() -> None:
    """Test sendTestTemplate endpoint with WireMock"""
    test_id = "transactional_emails.send_test_template.0"
    client = get_client(test_id)
    client.transactional_emails.send_test_template(template_id=1000000)
    verify_request_count(test_id, "POST", "/smtp/templates/1000000/sendTest", None, 1)
