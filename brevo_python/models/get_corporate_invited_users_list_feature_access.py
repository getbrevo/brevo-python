# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   | 422  | Error. Unprocessable Entity |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCorporateInvitedUsersListFeatureAccess(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_management': 'list[str]',
        'api_keys': 'list[str]',
        'my_plan': 'list[str]',
        'apps_management': 'list[str]'
    }

    attribute_map = {
        'user_management': 'user_management',
        'api_keys': 'api_keys',
        'my_plan': 'my_plan',
        'apps_management': 'apps_management'
    }

    def __init__(self, user_management=None, api_keys=None, my_plan=None, apps_management=None):  # noqa: E501
        """GetCorporateInvitedUsersListFeatureAccess - a model defined in Swagger"""  # noqa: E501

        self._user_management = None
        self._api_keys = None
        self._my_plan = None
        self._apps_management = None
        self.discriminator = None

        if user_management is not None:
            self.user_management = user_management
        if api_keys is not None:
            self.api_keys = api_keys
        if my_plan is not None:
            self.my_plan = my_plan
        if apps_management is not None:
            self.apps_management = apps_management

    @property
    def user_management(self):
        """Gets the user_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501

        User management accessiblity.  # noqa: E501

        :return: The user_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_management

    @user_management.setter
    def user_management(self, user_management):
        """Sets the user_management of this GetCorporateInvitedUsersListFeatureAccess.

        User management accessiblity.  # noqa: E501

        :param user_management: The user_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :type: list[str]
        """

        self._user_management = user_management

    @property
    def api_keys(self):
        """Gets the api_keys of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501

        Api keys accessiblity.  # noqa: E501

        :return: The api_keys of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this GetCorporateInvitedUsersListFeatureAccess.

        Api keys accessiblity.  # noqa: E501

        :param api_keys: The api_keys of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :type: list[str]
        """

        self._api_keys = api_keys

    @property
    def my_plan(self):
        """Gets the my_plan of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501

        My plan accessiblity.  # noqa: E501

        :return: The my_plan of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._my_plan

    @my_plan.setter
    def my_plan(self, my_plan):
        """Sets the my_plan of this GetCorporateInvitedUsersListFeatureAccess.

        My plan accessiblity.  # noqa: E501

        :param my_plan: The my_plan of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :type: list[str]
        """

        self._my_plan = my_plan

    @property
    def apps_management(self):
        """Gets the apps_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501

        Apps management accessiblity | Not available in ENTv2  # noqa: E501

        :return: The apps_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._apps_management

    @apps_management.setter
    def apps_management(self, apps_management):
        """Sets the apps_management of this GetCorporateInvitedUsersListFeatureAccess.

        Apps management accessiblity | Not available in ENTv2  # noqa: E501

        :param apps_management: The apps_management of this GetCorporateInvitedUsersListFeatureAccess.  # noqa: E501
        :type: list[str]
        """

        self._apps_management = apps_management

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetCorporateInvitedUsersListFeatureAccess, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetCorporateInvitedUsersListFeatureAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other