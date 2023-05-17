# coding: utf-8

"""
    Brevo API

    Brevo provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/brevo  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@brevo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetInvitedUsersListFeatureAccess(object):
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
        'marketing': 'object',
        'conversations': 'object',
        'crm': 'object'
    }

    attribute_map = {
        'marketing': 'marketing',
        'conversations': 'conversations',
        'crm': 'crm'
    }

    def __init__(self, marketing=None, conversations=None, crm=None):  # noqa: E501
        """GetInvitedUsersListFeatureAccess - a model defined in Swagger"""  # noqa: E501

        self._marketing = None
        self._conversations = None
        self._crm = None
        self.discriminator = None

        if marketing is not None:
            self.marketing = marketing
        if conversations is not None:
            self.conversations = conversations
        if crm is not None:
            self.crm = crm

    @property
    def marketing(self):
        """Gets the marketing of this GetInvitedUsersListFeatureAccess.  # noqa: E501

        Marketing features accessiblity.  # noqa: E501

        :return: The marketing of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: object
        """
        return self._marketing

    @marketing.setter
    def marketing(self, marketing):
        """Sets the marketing of this GetInvitedUsersListFeatureAccess.

        Marketing features accessiblity.  # noqa: E501

        :param marketing: The marketing of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :type: object
        """

        self._marketing = marketing

    @property
    def conversations(self):
        """Gets the conversations of this GetInvitedUsersListFeatureAccess.  # noqa: E501

        Conversations features accessiblity.  # noqa: E501

        :return: The conversations of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: object
        """
        return self._conversations

    @conversations.setter
    def conversations(self, conversations):
        """Sets the conversations of this GetInvitedUsersListFeatureAccess.

        Conversations features accessiblity.  # noqa: E501

        :param conversations: The conversations of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :type: object
        """

        self._conversations = conversations

    @property
    def crm(self):
        """Gets the crm of this GetInvitedUsersListFeatureAccess.  # noqa: E501

        CRM features accessiblity.  # noqa: E501

        :return: The crm of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :rtype: object
        """
        return self._crm

    @crm.setter
    def crm(self, crm):
        """Sets the crm of this GetInvitedUsersListFeatureAccess.

        CRM features accessiblity.  # noqa: E501

        :param crm: The crm of this GetInvitedUsersListFeatureAccess.  # noqa: E501
        :type: object
        """

        self._crm = crm

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
        if issubclass(GetInvitedUsersListFeatureAccess, dict):
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
        if not isinstance(other, GetInvitedUsersListFeatureAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other