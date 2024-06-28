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


class GetCorporateUserPermission(object):
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
        'email': 'str',
        'status': 'str',
        'groups': 'list[GetCorporateUserPermissionGroups]',
        'feature_access': 'GetCorporateUserPermissionFeatureAccess'
    }

    attribute_map = {
        'email': 'email',
        'status': 'status',
        'groups': 'groups',
        'feature_access': 'feature_access'
    }

    def __init__(self, email=None, status=None, groups=None, feature_access=None):  # noqa: E501
        """GetCorporateUserPermission - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._status = None
        self._groups = None
        self._feature_access = None
        self.discriminator = None

        self.email = email
        self.status = status
        self.groups = groups
        self.feature_access = feature_access

    @property
    def email(self):
        """Gets the email of this GetCorporateUserPermission.  # noqa: E501

        Email address of the user.  # noqa: E501

        :return: The email of this GetCorporateUserPermission.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetCorporateUserPermission.

        Email address of the user.  # noqa: E501

        :param email: The email of this GetCorporateUserPermission.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def status(self):
        """Gets the status of this GetCorporateUserPermission.  # noqa: E501

        Status of the invited user.  # noqa: E501

        :return: The status of this GetCorporateUserPermission.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetCorporateUserPermission.

        Status of the invited user.  # noqa: E501

        :param status: The status of this GetCorporateUserPermission.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def groups(self):
        """Gets the groups of this GetCorporateUserPermission.  # noqa: E501


        :return: The groups of this GetCorporateUserPermission.  # noqa: E501
        :rtype: list[GetCorporateUserPermissionGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this GetCorporateUserPermission.


        :param groups: The groups of this GetCorporateUserPermission.  # noqa: E501
        :type: list[GetCorporateUserPermissionGroups]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def feature_access(self):
        """Gets the feature_access of this GetCorporateUserPermission.  # noqa: E501


        :return: The feature_access of this GetCorporateUserPermission.  # noqa: E501
        :rtype: GetCorporateUserPermissionFeatureAccess
        """
        return self._feature_access

    @feature_access.setter
    def feature_access(self, feature_access):
        """Sets the feature_access of this GetCorporateUserPermission.


        :param feature_access: The feature_access of this GetCorporateUserPermission.  # noqa: E501
        :type: GetCorporateUserPermissionFeatureAccess
        """
        if feature_access is None:
            raise ValueError("Invalid value for `feature_access`, must not be `None`")  # noqa: E501

        self._feature_access = feature_access

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
        if issubclass(GetCorporateUserPermission, dict):
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
        if not isinstance(other, GetCorporateUserPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
