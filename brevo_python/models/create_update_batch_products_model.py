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


class CreateUpdateBatchProductsModel(object):
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
        'created_count': 'int',
        'updated_count': 'int'
    }

    attribute_map = {
        'created_count': 'createdCount',
        'updated_count': 'updatedCount'
    }

    def __init__(self, created_count=None, updated_count=None):  # noqa: E501
        """CreateUpdateBatchProductsModel - a model defined in Swagger"""  # noqa: E501

        self._created_count = None
        self._updated_count = None
        self.discriminator = None

        if created_count is not None:
            self.created_count = created_count
        if updated_count is not None:
            self.updated_count = updated_count

    @property
    def created_count(self):
        """Gets the created_count of this CreateUpdateBatchProductsModel.  # noqa: E501

        Number of the new created products  # noqa: E501

        :return: The created_count of this CreateUpdateBatchProductsModel.  # noqa: E501
        :rtype: int
        """
        return self._created_count

    @created_count.setter
    def created_count(self, created_count):
        """Sets the created_count of this CreateUpdateBatchProductsModel.

        Number of the new created products  # noqa: E501

        :param created_count: The created_count of this CreateUpdateBatchProductsModel.  # noqa: E501
        :type: int
        """

        self._created_count = created_count

    @property
    def updated_count(self):
        """Gets the updated_count of this CreateUpdateBatchProductsModel.  # noqa: E501

        Number of the existing products updated  # noqa: E501

        :return: The updated_count of this CreateUpdateBatchProductsModel.  # noqa: E501
        :rtype: int
        """
        return self._updated_count

    @updated_count.setter
    def updated_count(self, updated_count):
        """Sets the updated_count of this CreateUpdateBatchProductsModel.

        Number of the existing products updated  # noqa: E501

        :param updated_count: The updated_count of this CreateUpdateBatchProductsModel.  # noqa: E501
        :type: int
        """

        self._updated_count = updated_count

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
        if issubclass(CreateUpdateBatchProductsModel, dict):
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
        if not isinstance(other, CreateUpdateBatchProductsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other