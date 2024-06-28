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


class DealAttributesInner(object):
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
        'internal_name': 'str',
        'label': 'str',
        'attribute_type_name': 'str',
        'attribute_options': 'list[object]',
        'is_required': 'bool'
    }

    attribute_map = {
        'internal_name': 'internalName',
        'label': 'label',
        'attribute_type_name': 'attributeTypeName',
        'attribute_options': 'attributeOptions',
        'is_required': 'isRequired'
    }

    def __init__(self, internal_name=None, label=None, attribute_type_name=None, attribute_options=None, is_required=None):  # noqa: E501
        """DealAttributesInner - a model defined in Swagger"""  # noqa: E501

        self._internal_name = None
        self._label = None
        self._attribute_type_name = None
        self._attribute_options = None
        self._is_required = None
        self.discriminator = None

        if internal_name is not None:
            self.internal_name = internal_name
        if label is not None:
            self.label = label
        if attribute_type_name is not None:
            self.attribute_type_name = attribute_type_name
        if attribute_options is not None:
            self.attribute_options = attribute_options
        if is_required is not None:
            self.is_required = is_required

    @property
    def internal_name(self):
        """Gets the internal_name of this DealAttributesInner.  # noqa: E501


        :return: The internal_name of this DealAttributesInner.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this DealAttributesInner.


        :param internal_name: The internal_name of this DealAttributesInner.  # noqa: E501
        :type: str
        """

        self._internal_name = internal_name

    @property
    def label(self):
        """Gets the label of this DealAttributesInner.  # noqa: E501


        :return: The label of this DealAttributesInner.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DealAttributesInner.


        :param label: The label of this DealAttributesInner.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def attribute_type_name(self):
        """Gets the attribute_type_name of this DealAttributesInner.  # noqa: E501


        :return: The attribute_type_name of this DealAttributesInner.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type_name

    @attribute_type_name.setter
    def attribute_type_name(self, attribute_type_name):
        """Sets the attribute_type_name of this DealAttributesInner.


        :param attribute_type_name: The attribute_type_name of this DealAttributesInner.  # noqa: E501
        :type: str
        """

        self._attribute_type_name = attribute_type_name

    @property
    def attribute_options(self):
        """Gets the attribute_options of this DealAttributesInner.  # noqa: E501


        :return: The attribute_options of this DealAttributesInner.  # noqa: E501
        :rtype: list[object]
        """
        return self._attribute_options

    @attribute_options.setter
    def attribute_options(self, attribute_options):
        """Sets the attribute_options of this DealAttributesInner.


        :param attribute_options: The attribute_options of this DealAttributesInner.  # noqa: E501
        :type: list[object]
        """

        self._attribute_options = attribute_options

    @property
    def is_required(self):
        """Gets the is_required of this DealAttributesInner.  # noqa: E501


        :return: The is_required of this DealAttributesInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this DealAttributesInner.


        :param is_required: The is_required of this DealAttributesInner.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

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
        if issubclass(DealAttributesInner, dict):
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
        if not isinstance(other, DealAttributesInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
