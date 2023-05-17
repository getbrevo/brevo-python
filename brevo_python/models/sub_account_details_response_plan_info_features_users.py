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


class SubAccountDetailsResponsePlanInfoFeaturesUsers(object):
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
        'quantity': 'int',
        'remaining': 'int'
    }

    attribute_map = {
        'quantity': 'quantity',
        'remaining': 'remaining'
    }

    def __init__(self, quantity=None, remaining=None):  # noqa: E501
        """SubAccountDetailsResponsePlanInfoFeaturesUsers - a model defined in Swagger"""  # noqa: E501

        self._quantity = None
        self._remaining = None
        self.discriminator = None

        if quantity is not None:
            self.quantity = quantity
        if remaining is not None:
            self.remaining = remaining

    @property
    def quantity(self):
        """Gets the quantity of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501

        Quantity of multi-account's provided  # noqa: E501

        :return: The quantity of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubAccountDetailsResponsePlanInfoFeaturesUsers.

        Quantity of multi-account's provided  # noqa: E501

        :param quantity: The quantity of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def remaining(self):
        """Gets the remaining of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501

        Available multi-accounts for use  # noqa: E501

        :return: The remaining of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this SubAccountDetailsResponsePlanInfoFeaturesUsers.

        Available multi-accounts for use  # noqa: E501

        :param remaining: The remaining of this SubAccountDetailsResponsePlanInfoFeaturesUsers.  # noqa: E501
        :type: int
        """

        self._remaining = remaining

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
        if issubclass(SubAccountDetailsResponsePlanInfoFeaturesUsers, dict):
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
        if not isinstance(other, SubAccountDetailsResponsePlanInfoFeaturesUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
