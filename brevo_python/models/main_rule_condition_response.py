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


class MainRuleConditionResponse(object):
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
        '_and': 'list[MainRuleConditionResponse]',
        'lhs': 'object',
        'op': 'str',
        '_or': 'list[MainRuleConditionResponse]',
        'rhs': 'object'
    }

    attribute_map = {
        '_and': 'and',
        'lhs': 'lhs',
        'op': 'op',
        '_or': 'or',
        'rhs': 'rhs'
    }

    def __init__(self, _and=None, lhs=None, op=None, _or=None, rhs=None):  # noqa: E501
        """MainRuleConditionResponse - a model defined in Swagger"""  # noqa: E501

        self.__and = None
        self._lhs = None
        self._op = None
        self.__or = None
        self._rhs = None
        self.discriminator = None

        if _and is not None:
            self._and = _and
        if lhs is not None:
            self.lhs = lhs
        if op is not None:
            self.op = op
        if _or is not None:
            self._or = _or
        if rhs is not None:
            self.rhs = rhs

    @property
    def _and(self):
        """Gets the _and of this MainRuleConditionResponse.  # noqa: E501

        Metric to indicate AND between rules  # noqa: E501

        :return: The _and of this MainRuleConditionResponse.  # noqa: E501
        :rtype: list[MainRuleConditionResponse]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this MainRuleConditionResponse.

        Metric to indicate AND between rules  # noqa: E501

        :param _and: The _and of this MainRuleConditionResponse.  # noqa: E501
        :type: list[MainRuleConditionResponse]
        """

        self.__and = _and

    @property
    def lhs(self):
        """Gets the lhs of this MainRuleConditionResponse.  # noqa: E501

        Conditon of the rule  # noqa: E501

        :return: The lhs of this MainRuleConditionResponse.  # noqa: E501
        :rtype: object
        """
        return self._lhs

    @lhs.setter
    def lhs(self, lhs):
        """Sets the lhs of this MainRuleConditionResponse.

        Conditon of the rule  # noqa: E501

        :param lhs: The lhs of this MainRuleConditionResponse.  # noqa: E501
        :type: object
        """

        self._lhs = lhs

    @property
    def op(self):
        """Gets the op of this MainRuleConditionResponse.  # noqa: E501

        Selected operator for the rule  # noqa: E501

        :return: The op of this MainRuleConditionResponse.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this MainRuleConditionResponse.

        Selected operator for the rule  # noqa: E501

        :param op: The op of this MainRuleConditionResponse.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def _or(self):
        """Gets the _or of this MainRuleConditionResponse.  # noqa: E501

        Metric to indicate OR between rules  # noqa: E501

        :return: The _or of this MainRuleConditionResponse.  # noqa: E501
        :rtype: list[MainRuleConditionResponse]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this MainRuleConditionResponse.

        Metric to indicate OR between rules  # noqa: E501

        :param _or: The _or of this MainRuleConditionResponse.  # noqa: E501
        :type: list[MainRuleConditionResponse]
        """

        self.__or = _or

    @property
    def rhs(self):
        """Gets the rhs of this MainRuleConditionResponse.  # noqa: E501

        Action of the rule  # noqa: E501

        :return: The rhs of this MainRuleConditionResponse.  # noqa: E501
        :rtype: object
        """
        return self._rhs

    @rhs.setter
    def rhs(self, rhs):
        """Sets the rhs of this MainRuleConditionResponse.

        Action of the rule  # noqa: E501

        :param rhs: The rhs of this MainRuleConditionResponse.  # noqa: E501
        :type: object
        """

        self._rhs = rhs

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
        if issubclass(MainRuleConditionResponse, dict):
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
        if not isinstance(other, MainRuleConditionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
