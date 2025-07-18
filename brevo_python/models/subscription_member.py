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


class SubscriptionMember(object):
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
        'created_at': 'str',
        'member_contact_ids': 'list[int]',
        'organization_id': 'int',
        'owner_contact_id': 'int',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'member_contact_ids': 'memberContactIds',
        'organization_id': 'organizationId',
        'owner_contact_id': 'ownerContactId',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, member_contact_ids=None, organization_id=None, owner_contact_id=None, updated_at=None):  # noqa: E501
        """SubscriptionMember - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._member_contact_ids = None
        self._organization_id = None
        self._owner_contact_id = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if member_contact_ids is not None:
            self.member_contact_ids = member_contact_ids
        if organization_id is not None:
            self.organization_id = organization_id
        if owner_contact_id is not None:
            self.owner_contact_id = owner_contact_id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this SubscriptionMember.  # noqa: E501

        Timestamp when the subscription member was created.  # noqa: E501

        :return: The created_at of this SubscriptionMember.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubscriptionMember.

        Timestamp when the subscription member was created.  # noqa: E501

        :param created_at: The created_at of this SubscriptionMember.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def member_contact_ids(self):
        """Gets the member_contact_ids of this SubscriptionMember.  # noqa: E501

        List of unique member contact IDs.  # noqa: E501

        :return: The member_contact_ids of this SubscriptionMember.  # noqa: E501
        :rtype: list[int]
        """
        return self._member_contact_ids

    @member_contact_ids.setter
    def member_contact_ids(self, member_contact_ids):
        """Sets the member_contact_ids of this SubscriptionMember.

        List of unique member contact IDs.  # noqa: E501

        :param member_contact_ids: The member_contact_ids of this SubscriptionMember.  # noqa: E501
        :type: list[int]
        """

        self._member_contact_ids = member_contact_ids

    @property
    def organization_id(self):
        """Gets the organization_id of this SubscriptionMember.  # noqa: E501

        Unique identifier of the organization.  # noqa: E501

        :return: The organization_id of this SubscriptionMember.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this SubscriptionMember.

        Unique identifier of the organization.  # noqa: E501

        :param organization_id: The organization_id of this SubscriptionMember.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def owner_contact_id(self):
        """Gets the owner_contact_id of this SubscriptionMember.  # noqa: E501

        Unique identifier of the subscription owner.  # noqa: E501

        :return: The owner_contact_id of this SubscriptionMember.  # noqa: E501
        :rtype: int
        """
        return self._owner_contact_id

    @owner_contact_id.setter
    def owner_contact_id(self, owner_contact_id):
        """Sets the owner_contact_id of this SubscriptionMember.

        Unique identifier of the subscription owner.  # noqa: E501

        :param owner_contact_id: The owner_contact_id of this SubscriptionMember.  # noqa: E501
        :type: int
        """

        self._owner_contact_id = owner_contact_id

    @property
    def updated_at(self):
        """Gets the updated_at of this SubscriptionMember.  # noqa: E501

        Timestamp when the subscription member was last updated.  # noqa: E501

        :return: The updated_at of this SubscriptionMember.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SubscriptionMember.

        Timestamp when the subscription member was last updated.  # noqa: E501

        :param updated_at: The updated_at of this SubscriptionMember.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(SubscriptionMember, dict):
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
        if not isinstance(other, SubscriptionMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
