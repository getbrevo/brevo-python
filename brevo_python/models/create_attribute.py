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


class CreateAttribute(object):
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
        'value': 'str',
        'is_recurring': 'bool',
        'enumeration': 'list[CreateAttributeEnumeration]',
        'multi_category_options': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'is_recurring': 'isRecurring',
        'enumeration': 'enumeration',
        'multi_category_options': 'multiCategoryOptions',
        'type': 'type'
    }

    def __init__(self, value=None, is_recurring=None, enumeration=None, multi_category_options=None, type=None):  # noqa: E501
        """CreateAttribute - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._is_recurring = None
        self._enumeration = None
        self._multi_category_options = None
        self._type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if is_recurring is not None:
            self.is_recurring = is_recurring
        if enumeration is not None:
            self.enumeration = enumeration
        if multi_category_options is not None:
            self.multi_category_options = multi_category_options
        if type is not None:
            self.type = type

    @property
    def value(self):
        """Gets the value of this CreateAttribute.  # noqa: E501

        Value of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :return: The value of this CreateAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateAttribute.

        Value of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :param value: The value of this CreateAttribute.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def is_recurring(self):
        """Gets the is_recurring of this CreateAttribute.  # noqa: E501

        Type of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :return: The is_recurring of this CreateAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_recurring

    @is_recurring.setter
    def is_recurring(self, is_recurring):
        """Sets the is_recurring of this CreateAttribute.

        Type of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :param is_recurring: The is_recurring of this CreateAttribute.  # noqa: E501
        :type: bool
        """

        self._is_recurring = is_recurring

    @property
    def enumeration(self):
        """Gets the enumeration of this CreateAttribute.  # noqa: E501

        List of values and labels that the attribute can take. Use only if the attribute's category is \"category\". None of the category options can exceed max 200 characters. For example, [{\"value\":1, \"label\":\"male\"}, {\"value\":2, \"label\":\"female\"}]  # noqa: E501

        :return: The enumeration of this CreateAttribute.  # noqa: E501
        :rtype: list[CreateAttributeEnumeration]
        """
        return self._enumeration

    @enumeration.setter
    def enumeration(self, enumeration):
        """Sets the enumeration of this CreateAttribute.

        List of values and labels that the attribute can take. Use only if the attribute's category is \"category\". None of the category options can exceed max 200 characters. For example, [{\"value\":1, \"label\":\"male\"}, {\"value\":2, \"label\":\"female\"}]  # noqa: E501

        :param enumeration: The enumeration of this CreateAttribute.  # noqa: E501
        :type: list[CreateAttributeEnumeration]
        """

        self._enumeration = enumeration

    @property
    def multi_category_options(self):
        """Gets the multi_category_options of this CreateAttribute.  # noqa: E501

        List of options you want to add for multiple-choice attribute. **Use only if the attribute's category is \"normal\" and attribute's type is \"multiple-choice\". None of the multicategory options can exceed max 200 characters.** For example: **[\"USA\",\"INDIA\"]**   # noqa: E501

        :return: The multi_category_options of this CreateAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._multi_category_options

    @multi_category_options.setter
    def multi_category_options(self, multi_category_options):
        """Sets the multi_category_options of this CreateAttribute.

        List of options you want to add for multiple-choice attribute. **Use only if the attribute's category is \"normal\" and attribute's type is \"multiple-choice\". None of the multicategory options can exceed max 200 characters.** For example: **[\"USA\",\"INDIA\"]**   # noqa: E501

        :param multi_category_options: The multi_category_options of this CreateAttribute.  # noqa: E501
        :type: list[str]
        """

        self._multi_category_options = multi_category_options

    @property
    def type(self):
        """Gets the type of this CreateAttribute.  # noqa: E501

        Type of the attribute. Use only if the attribute's category is 'normal', 'category' or 'transactional' ( type 'user' and 'multiple-choice' is only available if the category is 'normal' attribute, type 'id' is only available if the category is 'transactional' attribute & type 'category' is only available if the category is 'category' attribute )  # noqa: E501

        :return: The type of this CreateAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAttribute.

        Type of the attribute. Use only if the attribute's category is 'normal', 'category' or 'transactional' ( type 'user' and 'multiple-choice' is only available if the category is 'normal' attribute, type 'id' is only available if the category is 'transactional' attribute & type 'category' is only available if the category is 'category' attribute )  # noqa: E501

        :param type: The type of this CreateAttribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "date", "float", "boolean", "id", "category", "multiple-choice"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(CreateAttribute, dict):
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
        if not isinstance(other, CreateAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
