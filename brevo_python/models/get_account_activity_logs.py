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


class GetAccountActivityLogs(object):
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
        'action': 'str',
        '_date': 'str',
        'user_email': 'str',
        'user_ip': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'action': 'action',
        '_date': 'date',
        'user_email': 'user_email',
        'user_ip': 'user_ip',
        'user_agent': 'user_agent'
    }

    def __init__(self, action=None, _date=None, user_email=None, user_ip=None, user_agent=None):  # noqa: E501
        """GetAccountActivityLogs - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self.__date = None
        self._user_email = None
        self._user_ip = None
        self._user_agent = None
        self.discriminator = None

        self.action = action
        self._date = _date
        self.user_email = user_email
        self.user_ip = user_ip
        self.user_agent = user_agent

    @property
    def action(self):
        """Gets the action of this GetAccountActivityLogs.  # noqa: E501

        Type of activity in the account.  # noqa: E501

        :return: The action of this GetAccountActivityLogs.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GetAccountActivityLogs.

        Type of activity in the account.  # noqa: E501

        :param action: The action of this GetAccountActivityLogs.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def _date(self):
        """Gets the _date of this GetAccountActivityLogs.  # noqa: E501

        Time of the activity.  # noqa: E501

        :return: The _date of this GetAccountActivityLogs.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetAccountActivityLogs.

        Time of the activity.  # noqa: E501

        :param _date: The _date of this GetAccountActivityLogs.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def user_email(self):
        """Gets the user_email of this GetAccountActivityLogs.  # noqa: E501

        Email address of the user who performed activity in the account.  # noqa: E501

        :return: The user_email of this GetAccountActivityLogs.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this GetAccountActivityLogs.

        Email address of the user who performed activity in the account.  # noqa: E501

        :param user_email: The user_email of this GetAccountActivityLogs.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_ip(self):
        """Gets the user_ip of this GetAccountActivityLogs.  # noqa: E501

        IP address of the user who performed activity in the account.  # noqa: E501

        :return: The user_ip of this GetAccountActivityLogs.  # noqa: E501
        :rtype: str
        """
        return self._user_ip

    @user_ip.setter
    def user_ip(self, user_ip):
        """Sets the user_ip of this GetAccountActivityLogs.

        IP address of the user who performed activity in the account.  # noqa: E501

        :param user_ip: The user_ip of this GetAccountActivityLogs.  # noqa: E501
        :type: str
        """
        if user_ip is None:
            raise ValueError("Invalid value for `user_ip`, must not be `None`")  # noqa: E501

        self._user_ip = user_ip

    @property
    def user_agent(self):
        """Gets the user_agent of this GetAccountActivityLogs.  # noqa: E501

        Browser details of the user who performed the activity.  # noqa: E501

        :return: The user_agent of this GetAccountActivityLogs.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this GetAccountActivityLogs.

        Browser details of the user who performed the activity.  # noqa: E501

        :param user_agent: The user_agent of this GetAccountActivityLogs.  # noqa: E501
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")  # noqa: E501

        self._user_agent = user_agent

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
        if issubclass(GetAccountActivityLogs, dict):
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
        if not isinstance(other, GetAccountActivityLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
