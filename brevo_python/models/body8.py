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


class Body8(object):
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
        'name': 'str',
        'attributes': 'object',
        'linked_contacts_ids': 'list[int]',
        'linked_companies_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'attributes': 'attributes',
        'linked_contacts_ids': 'linkedContactsIds',
        'linked_companies_ids': 'linkedCompaniesIds'
    }

    def __init__(self, name=None, attributes=None, linked_contacts_ids=None, linked_companies_ids=None):  # noqa: E501
        """Body8 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._attributes = None
        self._linked_contacts_ids = None
        self._linked_companies_ids = None
        self.discriminator = None

        self.name = name
        if attributes is not None:
            self.attributes = attributes
        if linked_contacts_ids is not None:
            self.linked_contacts_ids = linked_contacts_ids
        if linked_companies_ids is not None:
            self.linked_companies_ids = linked_companies_ids

    @property
    def name(self):
        """Gets the name of this Body8.  # noqa: E501

        Name of deal  # noqa: E501

        :return: The name of this Body8.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body8.

        Name of deal  # noqa: E501

        :param name: The name of this Body8.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this Body8.  # noqa: E501

        Attributes for deal creation  To assign owner of a Deal you can send attributes.deal_owner and utilize the account email or ID.  If you want to create a deal on a specific pipeline and stage you can use the following attributes `pipeline` and `deal_stage`.  Pipeline and deal_stage are ids you can fetch using this endpoint `/crm/pipeline/details/{pipelineID}`   # noqa: E501

        :return: The attributes of this Body8.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Body8.

        Attributes for deal creation  To assign owner of a Deal you can send attributes.deal_owner and utilize the account email or ID.  If you want to create a deal on a specific pipeline and stage you can use the following attributes `pipeline` and `deal_stage`.  Pipeline and deal_stage are ids you can fetch using this endpoint `/crm/pipeline/details/{pipelineID}`   # noqa: E501

        :param attributes: The attributes of this Body8.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def linked_contacts_ids(self):
        """Gets the linked_contacts_ids of this Body8.  # noqa: E501

        Contact ids to be linked with deal  # noqa: E501

        :return: The linked_contacts_ids of this Body8.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_contacts_ids

    @linked_contacts_ids.setter
    def linked_contacts_ids(self, linked_contacts_ids):
        """Sets the linked_contacts_ids of this Body8.

        Contact ids to be linked with deal  # noqa: E501

        :param linked_contacts_ids: The linked_contacts_ids of this Body8.  # noqa: E501
        :type: list[int]
        """

        self._linked_contacts_ids = linked_contacts_ids

    @property
    def linked_companies_ids(self):
        """Gets the linked_companies_ids of this Body8.  # noqa: E501

        Company ids to be linked with deal  # noqa: E501

        :return: The linked_companies_ids of this Body8.  # noqa: E501
        :rtype: list[str]
        """
        return self._linked_companies_ids

    @linked_companies_ids.setter
    def linked_companies_ids(self, linked_companies_ids):
        """Sets the linked_companies_ids of this Body8.

        Company ids to be linked with deal  # noqa: E501

        :param linked_companies_ids: The linked_companies_ids of this Body8.  # noqa: E501
        :type: list[str]
        """

        self._linked_companies_ids = linked_companies_ids

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
        if issubclass(Body8, dict):
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
        if not isinstance(other, Body8):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
