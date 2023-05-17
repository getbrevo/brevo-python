# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/getbrevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import brevo_python
from brevo_python.api.email_campaigns_api import EmailCampaignsApi  # noqa: E501
from brevo_python.rest import ApiException


class TestEmailCampaignsApi(unittest.TestCase):
    """EmailCampaignsApi unit test stubs"""

    def setUp(self):
        self.api = brevo_python.api.email_campaigns_api.EmailCampaignsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_email_campaign(self):
        """Test case for create_email_campaign

        Create an email campaign  # noqa: E501
        """
        pass

    def test_delete_email_campaign(self):
        """Test case for delete_email_campaign

        Delete an email campaign  # noqa: E501
        """
        pass

    def test_email_export_recipients(self):
        """Test case for email_export_recipients

        Export the recipients of an email campaign  # noqa: E501
        """
        pass

    def test_get_ab_test_campaign_result(self):
        """Test case for get_ab_test_campaign_result

        Get an A/B test email campaign results  # noqa: E501
        """
        pass

    def test_get_email_campaign(self):
        """Test case for get_email_campaign

        Get an email campaign report  # noqa: E501
        """
        pass

    def test_get_email_campaigns(self):
        """Test case for get_email_campaigns

        Return all your created email campaigns  # noqa: E501
        """
        pass

    def test_get_shared_template_url(self):
        """Test case for get_shared_template_url

        Get a shared template url  # noqa: E501
        """
        pass

    def test_send_email_campaign_now(self):
        """Test case for send_email_campaign_now

        Send an email campaign immediately, based on campaignId  # noqa: E501
        """
        pass

    def test_send_report(self):
        """Test case for send_report

        Send the report of a campaign  # noqa: E501
        """
        pass

    def test_send_test_email(self):
        """Test case for send_test_email

        Send an email campaign to your test list  # noqa: E501
        """
        pass

    def test_update_campaign_status(self):
        """Test case for update_campaign_status

        Update an email campaign status  # noqa: E501
        """
        pass

    def test_update_email_campaign(self):
        """Test case for update_email_campaign

        Update an email campaign  # noqa: E501
        """
        pass

    def test_upload_image_to_gallery(self):
        """Test case for upload_image_to_gallery

        Upload an image to your account's image gallery  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
