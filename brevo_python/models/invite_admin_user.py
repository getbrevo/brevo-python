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


class InviteAdminUser(object):
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
        'all_features_access': 'bool',
        'group_ids': 'list[str]',
        'privileges': 'list[InviteAdminUserPrivileges]'
    }

    attribute_map = {
        'email': 'email',
        'all_features_access': 'all_features_access',
        'group_ids': 'groupIds',
        'privileges': 'privileges'
    }

    def __init__(self, email=None, all_features_access=None, group_ids=None, privileges=None):  # noqa: E501
        """InviteAdminUser - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._all_features_access = None
        self._group_ids = None
        self._privileges = None
        self.discriminator = None

        self.email = email
        self.all_features_access = all_features_access
        if group_ids is not None:
            self.group_ids = group_ids
        self.privileges = privileges

    @property
    def email(self):
        """Gets the email of this InviteAdminUser.  # noqa: E501

        Email address for the organization  # noqa: E501

        :return: The email of this InviteAdminUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteAdminUser.

        Email address for the organization  # noqa: E501

        :param email: The email of this InviteAdminUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def all_features_access(self):
        """Gets the all_features_access of this InviteAdminUser.  # noqa: E501

        All access to the features  # noqa: E501

        :return: The all_features_access of this InviteAdminUser.  # noqa: E501
        :rtype: bool
        """
        return self._all_features_access

    @all_features_access.setter
    def all_features_access(self, all_features_access):
        """Sets the all_features_access of this InviteAdminUser.

        All access to the features  # noqa: E501

        :param all_features_access: The all_features_access of this InviteAdminUser.  # noqa: E501
        :type: bool
        """
        if all_features_access is None:
            raise ValueError("Invalid value for `all_features_access`, must not be `None`")  # noqa: E501

        self._all_features_access = all_features_access

    @property
    def group_ids(self):
        """Gets the group_ids of this InviteAdminUser.  # noqa: E501

        Ids of Group  # noqa: E501

        :return: The group_ids of this InviteAdminUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this InviteAdminUser.

        Ids of Group  # noqa: E501

        :param group_ids: The group_ids of this InviteAdminUser.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def privileges(self):
        """Gets the privileges of this InviteAdminUser.  # noqa: E501


        :return: The privileges of this InviteAdminUser.  # noqa: E501
        :rtype: list[InviteAdminUserPrivileges]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this InviteAdminUser.


        :param privileges: The privileges of this InviteAdminUser.  # noqa: E501
        :type: list[InviteAdminUserPrivileges]
        """
        if privileges is None:
            raise ValueError("Invalid value for `privileges`, must not be `None`")  # noqa: E501

        self._privileges = privileges

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
        if issubclass(InviteAdminUser, dict):
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
        if not isinstance(other, InviteAdminUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
