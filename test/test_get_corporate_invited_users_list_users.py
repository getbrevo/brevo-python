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
from brevo_python.models.get_corporate_invited_users_list_users import GetCorporateInvitedUsersListUsers  # noqa: E501
from brevo_python.rest import ApiException


class TestGetCorporateInvitedUsersListUsers(unittest.TestCase):
    """GetCorporateInvitedUsersListUsers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetCorporateInvitedUsersListUsers(self):
        """Test GetCorporateInvitedUsersListUsers"""
        # FIXME: construct object with mandatory attributes with example values
        # model = brevo_python.models.get_corporate_invited_users_list_users.GetCorporateInvitedUsersListUsers()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
