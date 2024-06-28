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


class TaskReminder(object):
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
        'value': 'int',
        'unit': 'str',
        'types': 'list[str]'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit',
        'types': 'types'
    }

    def __init__(self, value=None, unit=None, types=None):  # noqa: E501
        """TaskReminder - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._unit = None
        self._types = None
        self.discriminator = None

        self.value = value
        self.unit = unit
        self.types = types

    @property
    def value(self):
        """Gets the value of this TaskReminder.  # noqa: E501

        Value of time unit before reminder is to be sent  # noqa: E501

        :return: The value of this TaskReminder.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TaskReminder.

        Value of time unit before reminder is to be sent  # noqa: E501

        :param value: The value of this TaskReminder.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this TaskReminder.  # noqa: E501

        Unit of time before reminder is to be sent  # noqa: E501

        :return: The unit of this TaskReminder.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TaskReminder.

        Unit of time before reminder is to be sent  # noqa: E501

        :param unit: The unit of this TaskReminder.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        allowed_values = ["minutes", "hours", "weeks", "days"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def types(self):
        """Gets the types of this TaskReminder.  # noqa: E501

        Type of task reminder e.g email, push  # noqa: E501

        :return: The types of this TaskReminder.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this TaskReminder.

        Type of task reminder e.g email, push  # noqa: E501

        :param types: The types of this TaskReminder.  # noqa: E501
        :type: list[str]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

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
        if issubclass(TaskReminder, dict):
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
        if not isinstance(other, TaskReminder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
