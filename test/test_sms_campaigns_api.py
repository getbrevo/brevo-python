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
from brevo_python.api.sms_campaigns_api import SMSCampaignsApi  # noqa: E501
from brevo_python.rest import ApiException


class TestSMSCampaignsApi(unittest.TestCase):
    """SMSCampaignsApi unit test stubs"""

    def setUp(self):
        self.api = brevo_python.api.sms_campaigns_api.SMSCampaignsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sms_campaign(self):
        """Test case for create_sms_campaign

        Creates an SMS campaign  # noqa: E501
        """
        pass

    def test_delete_sms_campaign(self):
        """Test case for delete_sms_campaign

        Delete an SMS campaign  # noqa: E501
        """
        pass

    def test_get_sms_campaign(self):
        """Test case for get_sms_campaign

        Get an SMS campaign  # noqa: E501
        """
        pass

    def test_get_sms_campaigns(self):
        """Test case for get_sms_campaigns

        Returns the information for all your created SMS campaigns  # noqa: E501
        """
        pass

    def test_request_sms_recipient_export(self):
        """Test case for request_sms_recipient_export

        Export an SMS campaign's recipients  # noqa: E501
        """
        pass

    def test_send_sms_campaign_now(self):
        """Test case for send_sms_campaign_now

        Send your SMS campaign immediately  # noqa: E501
        """
        pass

    def test_send_sms_report(self):
        """Test case for send_sms_report

        Send an SMS campaign's report  # noqa: E501
        """
        pass

    def test_send_test_sms(self):
        """Test case for send_test_sms

        Send a test SMS campaign  # noqa: E501
        """
        pass

    def test_update_sms_campaign(self):
        """Test case for update_sms_campaign

        Update an SMS campaign  # noqa: E501
        """
        pass

    def test_update_sms_campaign_status(self):
        """Test case for update_sms_campaign_status

        Update a campaign's status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()