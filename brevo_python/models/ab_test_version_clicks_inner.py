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


class AbTestVersionClicksInner(object):
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
        'link': 'str',
        'clicks_count': 'int',
        'click_rate': 'str'
    }

    attribute_map = {
        'link': 'link',
        'clicks_count': 'clicksCount',
        'click_rate': 'clickRate'
    }

    def __init__(self, link=None, clicks_count=None, click_rate=None):  # noqa: E501
        """AbTestVersionClicksInner - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._clicks_count = None
        self._click_rate = None
        self.discriminator = None

        self.link = link
        self.clicks_count = clicks_count
        self.click_rate = click_rate

    @property
    def link(self):
        """Gets the link of this AbTestVersionClicksInner.  # noqa: E501

        URL of the link  # noqa: E501

        :return: The link of this AbTestVersionClicksInner.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AbTestVersionClicksInner.

        URL of the link  # noqa: E501

        :param link: The link of this AbTestVersionClicksInner.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def clicks_count(self):
        """Gets the clicks_count of this AbTestVersionClicksInner.  # noqa: E501

        Number of times a link is clicked  # noqa: E501

        :return: The clicks_count of this AbTestVersionClicksInner.  # noqa: E501
        :rtype: int
        """
        return self._clicks_count

    @clicks_count.setter
    def clicks_count(self, clicks_count):
        """Sets the clicks_count of this AbTestVersionClicksInner.

        Number of times a link is clicked  # noqa: E501

        :param clicks_count: The clicks_count of this AbTestVersionClicksInner.  # noqa: E501
        :type: int
        """
        if clicks_count is None:
            raise ValueError("Invalid value for `clicks_count`, must not be `None`")  # noqa: E501

        self._clicks_count = clicks_count

    @property
    def click_rate(self):
        """Gets the click_rate of this AbTestVersionClicksInner.  # noqa: E501

        Percentage of clicks of link with respect to total clicks  # noqa: E501

        :return: The click_rate of this AbTestVersionClicksInner.  # noqa: E501
        :rtype: str
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this AbTestVersionClicksInner.

        Percentage of clicks of link with respect to total clicks  # noqa: E501

        :param click_rate: The click_rate of this AbTestVersionClicksInner.  # noqa: E501
        :type: str
        """
        if click_rate is None:
            raise ValueError("Invalid value for `click_rate`, must not be `None`")  # noqa: E501

        self._click_rate = click_rate

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
        if issubclass(AbTestVersionClicksInner, dict):
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
        if not isinstance(other, AbTestVersionClicksInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
