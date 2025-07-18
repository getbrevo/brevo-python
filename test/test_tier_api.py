# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   | 422  | Error. Unprocessable Entity |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import brevo_python
from brevo_python.api.tier_api import TierApi  # noqa: E501
from brevo_python.rest import ApiException


class TestTierApi(unittest.TestCase):
    """TierApi unit test stubs"""

    def setUp(self):
        self.api = brevo_python.api.tier_api.TierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_subscription_to_tier(self):
        """Test case for add_subscription_to_tier

        Assign a tier  # noqa: E501
        """
        pass

    def test_create_tier_for_tier_group(self):
        """Test case for create_tier_for_tier_group

        Create a tier  # noqa: E501
        """
        pass

    def test_create_tier_group(self):
        """Test case for create_tier_group

        Create a tier group  # noqa: E501
        """
        pass

    def test_delete_tier(self):
        """Test case for delete_tier

        Delete tier  # noqa: E501
        """
        pass

    def test_delete_tier_group(self):
        """Test case for delete_tier_group

        Delete tier group  # noqa: E501
        """
        pass

    def test_get_list_of_tier_groups(self):
        """Test case for get_list_of_tier_groups

        List tier groups  # noqa: E501
        """
        pass

    def test_get_loyalty_program_tier(self):
        """Test case for get_loyalty_program_tier

        List tiers  # noqa: E501
        """
        pass

    def test_get_tier_group(self):
        """Test case for get_tier_group

        Get tier group  # noqa: E501
        """
        pass

    def test_update_tier(self):
        """Test case for update_tier

        Update tier  # noqa: E501
        """
        pass

    def test_update_tier_group(self):
        """Test case for update_tier_group

        Update tier group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
