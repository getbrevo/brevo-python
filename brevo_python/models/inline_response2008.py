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


class InlineResponse2008(object):
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
        'id': 'str',
        'name': 'str',
        'default_coupon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default_coupon': 'defaultCoupon'
    }

    def __init__(self, id=None, name=None, default_coupon=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._default_coupon = None
        self.discriminator = None

        self.id = id
        self.name = name
        if default_coupon is not None:
            self.default_coupon = default_coupon

    @property
    def id(self):
        """Gets the id of this InlineResponse2008.  # noqa: E501

        The id of the collection  # noqa: E501

        :return: The id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2008.

        The id of the collection  # noqa: E501

        :param id: The id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2008.  # noqa: E501

        The name of the collection  # noqa: E501

        :return: The name of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2008.

        The name of the collection  # noqa: E501

        :param name: The name of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default_coupon(self):
        """Gets the default_coupon of this InlineResponse2008.  # noqa: E501

        The default coupon of the collection  # noqa: E501

        :return: The default_coupon of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._default_coupon

    @default_coupon.setter
    def default_coupon(self, default_coupon):
        """Sets the default_coupon of this InlineResponse2008.

        The default coupon of the collection  # noqa: E501

        :param default_coupon: The default_coupon of this InlineResponse2008.  # noqa: E501
        :type: str
        """

        self._default_coupon = default_coupon

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
