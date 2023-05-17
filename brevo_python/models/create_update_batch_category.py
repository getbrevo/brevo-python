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


class CreateUpdateBatchCategory(object):
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
        'categories': 'list[CreateUpdateCategories]',
        'update_enabled': 'bool'
    }

    attribute_map = {
        'categories': 'categories',
        'update_enabled': 'updateEnabled'
    }

    def __init__(self, categories=None, update_enabled=None):  # noqa: E501
        """CreateUpdateBatchCategory - a model defined in Swagger"""  # noqa: E501

        self._categories = None
        self._update_enabled = None
        self.discriminator = None

        self.categories = categories
        if update_enabled is not None:
            self.update_enabled = update_enabled

    @property
    def categories(self):
        """Gets the categories of this CreateUpdateBatchCategory.  # noqa: E501

        array of categories objects  # noqa: E501

        :return: The categories of this CreateUpdateBatchCategory.  # noqa: E501
        :rtype: list[CreateUpdateCategories]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CreateUpdateBatchCategory.

        array of categories objects  # noqa: E501

        :param categories: The categories of this CreateUpdateBatchCategory.  # noqa: E501
        :type: list[CreateUpdateCategories]
        """
        if categories is None:
            raise ValueError("Invalid value for `categories`, must not be `None`")  # noqa: E501

        self._categories = categories

    @property
    def update_enabled(self):
        """Gets the update_enabled of this CreateUpdateBatchCategory.  # noqa: E501

        Facilitate to update the existing categories in the same request (updateEnabled = true)  # noqa: E501

        :return: The update_enabled of this CreateUpdateBatchCategory.  # noqa: E501
        :rtype: bool
        """
        return self._update_enabled

    @update_enabled.setter
    def update_enabled(self, update_enabled):
        """Sets the update_enabled of this CreateUpdateBatchCategory.

        Facilitate to update the existing categories in the same request (updateEnabled = true)  # noqa: E501

        :param update_enabled: The update_enabled of this CreateUpdateBatchCategory.  # noqa: E501
        :type: bool
        """

        self._update_enabled = update_enabled

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
        if issubclass(CreateUpdateBatchCategory, dict):
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
        if not isinstance(other, CreateUpdateBatchCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
