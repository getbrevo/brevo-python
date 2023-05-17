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


class Body2(object):
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
        'link_contact_ids': 'list[int]',
        'unlink_contact_ids': 'list[int]',
        'link_deals_ids': 'list[str]',
        'unlink_deals_ids': 'list[str]'
    }

    attribute_map = {
        'link_contact_ids': 'linkContactIds',
        'unlink_contact_ids': 'unlinkContactIds',
        'link_deals_ids': 'linkDealsIds',
        'unlink_deals_ids': 'unlinkDealsIds'
    }

    def __init__(self, link_contact_ids=None, unlink_contact_ids=None, link_deals_ids=None, unlink_deals_ids=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501

        self._link_contact_ids = None
        self._unlink_contact_ids = None
        self._link_deals_ids = None
        self._unlink_deals_ids = None
        self.discriminator = None

        if link_contact_ids is not None:
            self.link_contact_ids = link_contact_ids
        if unlink_contact_ids is not None:
            self.unlink_contact_ids = unlink_contact_ids
        if link_deals_ids is not None:
            self.link_deals_ids = link_deals_ids
        if unlink_deals_ids is not None:
            self.unlink_deals_ids = unlink_deals_ids

    @property
    def link_contact_ids(self):
        """Gets the link_contact_ids of this Body2.  # noqa: E501

        Contact ids for contacts to be linked with company  # noqa: E501

        :return: The link_contact_ids of this Body2.  # noqa: E501
        :rtype: list[int]
        """
        return self._link_contact_ids

    @link_contact_ids.setter
    def link_contact_ids(self, link_contact_ids):
        """Sets the link_contact_ids of this Body2.

        Contact ids for contacts to be linked with company  # noqa: E501

        :param link_contact_ids: The link_contact_ids of this Body2.  # noqa: E501
        :type: list[int]
        """

        self._link_contact_ids = link_contact_ids

    @property
    def unlink_contact_ids(self):
        """Gets the unlink_contact_ids of this Body2.  # noqa: E501

        Contact ids for contacts to be unlinked from company  # noqa: E501

        :return: The unlink_contact_ids of this Body2.  # noqa: E501
        :rtype: list[int]
        """
        return self._unlink_contact_ids

    @unlink_contact_ids.setter
    def unlink_contact_ids(self, unlink_contact_ids):
        """Sets the unlink_contact_ids of this Body2.

        Contact ids for contacts to be unlinked from company  # noqa: E501

        :param unlink_contact_ids: The unlink_contact_ids of this Body2.  # noqa: E501
        :type: list[int]
        """

        self._unlink_contact_ids = unlink_contact_ids

    @property
    def link_deals_ids(self):
        """Gets the link_deals_ids of this Body2.  # noqa: E501

        Deals ids for deals to be linked with company  # noqa: E501

        :return: The link_deals_ids of this Body2.  # noqa: E501
        :rtype: list[str]
        """
        return self._link_deals_ids

    @link_deals_ids.setter
    def link_deals_ids(self, link_deals_ids):
        """Sets the link_deals_ids of this Body2.

        Deals ids for deals to be linked with company  # noqa: E501

        :param link_deals_ids: The link_deals_ids of this Body2.  # noqa: E501
        :type: list[str]
        """

        self._link_deals_ids = link_deals_ids

    @property
    def unlink_deals_ids(self):
        """Gets the unlink_deals_ids of this Body2.  # noqa: E501

        Deals ids for deals to be unlinked from company  # noqa: E501

        :return: The unlink_deals_ids of this Body2.  # noqa: E501
        :rtype: list[str]
        """
        return self._unlink_deals_ids

    @unlink_deals_ids.setter
    def unlink_deals_ids(self, unlink_deals_ids):
        """Sets the unlink_deals_ids of this Body2.

        Deals ids for deals to be unlinked from company  # noqa: E501

        :param unlink_deals_ids: The unlink_deals_ids of this Body2.  # noqa: E501
        :type: list[str]
        """

        self._unlink_deals_ids = unlink_deals_ids

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
        if issubclass(Body2, dict):
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
        if not isinstance(other, Body2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other