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


class GetChildInfoStatistics(object):
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
        'previous_month_total_sent': 'int',
        'current_month_total_sent': 'int',
        'total_sent': 'int'
    }

    attribute_map = {
        'previous_month_total_sent': 'previousMonthTotalSent',
        'current_month_total_sent': 'currentMonthTotalSent',
        'total_sent': 'totalSent'
    }

    def __init__(self, previous_month_total_sent=None, current_month_total_sent=None, total_sent=None):  # noqa: E501
        """GetChildInfoStatistics - a model defined in Swagger"""  # noqa: E501

        self._previous_month_total_sent = None
        self._current_month_total_sent = None
        self._total_sent = None
        self.discriminator = None

        if previous_month_total_sent is not None:
            self.previous_month_total_sent = previous_month_total_sent
        if current_month_total_sent is not None:
            self.current_month_total_sent = current_month_total_sent
        if total_sent is not None:
            self.total_sent = total_sent

    @property
    def previous_month_total_sent(self):
        """Gets the previous_month_total_sent of this GetChildInfoStatistics.  # noqa: E501

        Overall emails sent for the previous month  # noqa: E501

        :return: The previous_month_total_sent of this GetChildInfoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._previous_month_total_sent

    @previous_month_total_sent.setter
    def previous_month_total_sent(self, previous_month_total_sent):
        """Sets the previous_month_total_sent of this GetChildInfoStatistics.

        Overall emails sent for the previous month  # noqa: E501

        :param previous_month_total_sent: The previous_month_total_sent of this GetChildInfoStatistics.  # noqa: E501
        :type: int
        """

        self._previous_month_total_sent = previous_month_total_sent

    @property
    def current_month_total_sent(self):
        """Gets the current_month_total_sent of this GetChildInfoStatistics.  # noqa: E501

        Overall emails sent for current month  # noqa: E501

        :return: The current_month_total_sent of this GetChildInfoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._current_month_total_sent

    @current_month_total_sent.setter
    def current_month_total_sent(self, current_month_total_sent):
        """Sets the current_month_total_sent of this GetChildInfoStatistics.

        Overall emails sent for current month  # noqa: E501

        :param current_month_total_sent: The current_month_total_sent of this GetChildInfoStatistics.  # noqa: E501
        :type: int
        """

        self._current_month_total_sent = current_month_total_sent

    @property
    def total_sent(self):
        """Gets the total_sent of this GetChildInfoStatistics.  # noqa: E501

        Overall emails sent for since the account exists  # noqa: E501

        :return: The total_sent of this GetChildInfoStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_sent

    @total_sent.setter
    def total_sent(self, total_sent):
        """Sets the total_sent of this GetChildInfoStatistics.

        Overall emails sent for since the account exists  # noqa: E501

        :param total_sent: The total_sent of this GetChildInfoStatistics.  # noqa: E501
        :type: int
        """

        self._total_sent = total_sent

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
        if issubclass(GetChildInfoStatistics, dict):
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
        if not isinstance(other, GetChildInfoStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other