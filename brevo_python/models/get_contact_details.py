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


class GetContactDetails(object):
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
        'email': 'str',
        'id': 'int',
        'email_blacklisted': 'bool',
        'sms_blacklisted': 'bool',
        'created_at': 'str',
        'modified_at': 'str',
        'list_ids': 'list[int]',
        'list_unsubscribed': 'list[int]',
        'attributes': 'object'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'email_blacklisted': 'emailBlacklisted',
        'sms_blacklisted': 'smsBlacklisted',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'list_ids': 'listIds',
        'list_unsubscribed': 'listUnsubscribed',
        'attributes': 'attributes'
    }

    def __init__(self, email=None, id=None, email_blacklisted=None, sms_blacklisted=None, created_at=None, modified_at=None, list_ids=None, list_unsubscribed=None, attributes=None):  # noqa: E501
        """GetContactDetails - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._email_blacklisted = None
        self._sms_blacklisted = None
        self._created_at = None
        self._modified_at = None
        self._list_ids = None
        self._list_unsubscribed = None
        self._attributes = None
        self.discriminator = None

        self.email = email
        self.id = id
        self.email_blacklisted = email_blacklisted
        self.sms_blacklisted = sms_blacklisted
        self.created_at = created_at
        self.modified_at = modified_at
        self.list_ids = list_ids
        if list_unsubscribed is not None:
            self.list_unsubscribed = list_unsubscribed
        self.attributes = attributes

    @property
    def email(self):
        """Gets the email of this GetContactDetails.  # noqa: E501

        Email address of the contact for which you requested the details  # noqa: E501

        :return: The email of this GetContactDetails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetContactDetails.

        Email address of the contact for which you requested the details  # noqa: E501

        :param email: The email of this GetContactDetails.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this GetContactDetails.  # noqa: E501

        ID of the contact for which you requested the details  # noqa: E501

        :return: The id of this GetContactDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetContactDetails.

        ID of the contact for which you requested the details  # noqa: E501

        :param id: The id of this GetContactDetails.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_blacklisted(self):
        """Gets the email_blacklisted of this GetContactDetails.  # noqa: E501

        Blacklist status for email campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501

        :return: The email_blacklisted of this GetContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._email_blacklisted

    @email_blacklisted.setter
    def email_blacklisted(self, email_blacklisted):
        """Sets the email_blacklisted of this GetContactDetails.

        Blacklist status for email campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501

        :param email_blacklisted: The email_blacklisted of this GetContactDetails.  # noqa: E501
        :type: bool
        """
        if email_blacklisted is None:
            raise ValueError("Invalid value for `email_blacklisted`, must not be `None`")  # noqa: E501

        self._email_blacklisted = email_blacklisted

    @property
    def sms_blacklisted(self):
        """Gets the sms_blacklisted of this GetContactDetails.  # noqa: E501

        Blacklist status for SMS campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501

        :return: The sms_blacklisted of this GetContactDetails.  # noqa: E501
        :rtype: bool
        """
        return self._sms_blacklisted

    @sms_blacklisted.setter
    def sms_blacklisted(self, sms_blacklisted):
        """Sets the sms_blacklisted of this GetContactDetails.

        Blacklist status for SMS campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501

        :param sms_blacklisted: The sms_blacklisted of this GetContactDetails.  # noqa: E501
        :type: bool
        """
        if sms_blacklisted is None:
            raise ValueError("Invalid value for `sms_blacklisted`, must not be `None`")  # noqa: E501

        self._sms_blacklisted = sms_blacklisted

    @property
    def created_at(self):
        """Gets the created_at of this GetContactDetails.  # noqa: E501

        Creation UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The created_at of this GetContactDetails.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetContactDetails.

        Creation UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param created_at: The created_at of this GetContactDetails.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this GetContactDetails.  # noqa: E501

        Last modification UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The modified_at of this GetContactDetails.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetContactDetails.

        Last modification UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param modified_at: The modified_at of this GetContactDetails.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def list_ids(self):
        """Gets the list_ids of this GetContactDetails.  # noqa: E501


        :return: The list_ids of this GetContactDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """Sets the list_ids of this GetContactDetails.


        :param list_ids: The list_ids of this GetContactDetails.  # noqa: E501
        :type: list[int]
        """
        if list_ids is None:
            raise ValueError("Invalid value for `list_ids`, must not be `None`")  # noqa: E501

        self._list_ids = list_ids

    @property
    def list_unsubscribed(self):
        """Gets the list_unsubscribed of this GetContactDetails.  # noqa: E501


        :return: The list_unsubscribed of this GetContactDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_unsubscribed

    @list_unsubscribed.setter
    def list_unsubscribed(self, list_unsubscribed):
        """Sets the list_unsubscribed of this GetContactDetails.


        :param list_unsubscribed: The list_unsubscribed of this GetContactDetails.  # noqa: E501
        :type: list[int]
        """

        self._list_unsubscribed = list_unsubscribed

    @property
    def attributes(self):
        """Gets the attributes of this GetContactDetails.  # noqa: E501

        Set of attributes of the contact  # noqa: E501

        :return: The attributes of this GetContactDetails.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GetContactDetails.

        Set of attributes of the contact  # noqa: E501

        :param attributes: The attributes of this GetContactDetails.  # noqa: E501
        :type: object
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

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
        if issubclass(GetContactDetails, dict):
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
        if not isinstance(other, GetContactDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other