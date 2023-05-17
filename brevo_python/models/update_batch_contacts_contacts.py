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


class UpdateBatchContactsContacts(object):
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
        'sms': 'str',
        'ext_id': 'str',
        'attributes': 'dict(str, object)',
        'email_blacklisted': 'bool',
        'sms_blacklisted': 'bool',
        'list_ids': 'list[int]',
        'unlink_list_ids': 'list[int]',
        'smtp_blacklist_sender': 'list[str]'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'sms': 'sms',
        'ext_id': 'ext_id',
        'attributes': 'attributes',
        'email_blacklisted': 'emailBlacklisted',
        'sms_blacklisted': 'smsBlacklisted',
        'list_ids': 'listIds',
        'unlink_list_ids': 'unlinkListIds',
        'smtp_blacklist_sender': 'smtpBlacklistSender'
    }

    def __init__(self, email=None, id=None, sms=None, ext_id=None, attributes=None, email_blacklisted=None, sms_blacklisted=None, list_ids=None, unlink_list_ids=None, smtp_blacklist_sender=None):  # noqa: E501
        """UpdateBatchContactsContacts - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._sms = None
        self._ext_id = None
        self._attributes = None
        self._email_blacklisted = None
        self._sms_blacklisted = None
        self._list_ids = None
        self._unlink_list_ids = None
        self._smtp_blacklist_sender = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if sms is not None:
            self.sms = sms
        if ext_id is not None:
            self.ext_id = ext_id
        if attributes is not None:
            self.attributes = attributes
        if email_blacklisted is not None:
            self.email_blacklisted = email_blacklisted
        if sms_blacklisted is not None:
            self.sms_blacklisted = sms_blacklisted
        if list_ids is not None:
            self.list_ids = list_ids
        if unlink_list_ids is not None:
            self.unlink_list_ids = unlink_list_ids
        if smtp_blacklist_sender is not None:
            self.smtp_blacklist_sender = smtp_blacklist_sender

    @property
    def email(self):
        """Gets the email of this UpdateBatchContactsContacts.  # noqa: E501

        Email address of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :return: The email of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateBatchContactsContacts.

        Email address of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :param email: The email of this UpdateBatchContactsContacts.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this UpdateBatchContactsContacts.  # noqa: E501

        id of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :return: The id of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateBatchContactsContacts.

        id of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :param id: The id of this UpdateBatchContactsContacts.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def sms(self):
        """Gets the sms of this UpdateBatchContactsContacts.  # noqa: E501

        SMS of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :return: The sms of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this UpdateBatchContactsContacts.

        SMS of the user to be updated (For each operation only pass one of the supported contact identifiers. Email, id or sms)  # noqa: E501

        :param sms: The sms of this UpdateBatchContactsContacts.  # noqa: E501
        :type: str
        """

        self._sms = sms

    @property
    def ext_id(self):
        """Gets the ext_id of this UpdateBatchContactsContacts.  # noqa: E501

        Pass your own Id to update ext_id of a contact.  # noqa: E501

        :return: The ext_id of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: str
        """
        return self._ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        """Sets the ext_id of this UpdateBatchContactsContacts.

        Pass your own Id to update ext_id of a contact.  # noqa: E501

        :param ext_id: The ext_id of this UpdateBatchContactsContacts.  # noqa: E501
        :type: str
        """

        self._ext_id = ext_id

    @property
    def attributes(self):
        """Gets the attributes of this UpdateBatchContactsContacts.  # noqa: E501

        Pass the set of attributes to be updated. **These attributes must be present in your account**. To update existing email address of a contact with the new one please pass EMAIL in attribtes. For example, **{ \"EMAIL\":\"newemail@domain.com\", \"FNAME\":\"Ellie\", \"LNAME\":\"Roger\"}**. Keep in mind transactional attributes can be updated the same way as normal attributes. Mobile Number in **SMS** field should be passed with proper country code. For example: **{\"SMS\":\"+91xxxxxxxxxx\"} or {\"SMS\":\"0091xxxxxxxxxx\"}**   # noqa: E501

        :return: The attributes of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpdateBatchContactsContacts.

        Pass the set of attributes to be updated. **These attributes must be present in your account**. To update existing email address of a contact with the new one please pass EMAIL in attribtes. For example, **{ \"EMAIL\":\"newemail@domain.com\", \"FNAME\":\"Ellie\", \"LNAME\":\"Roger\"}**. Keep in mind transactional attributes can be updated the same way as normal attributes. Mobile Number in **SMS** field should be passed with proper country code. For example: **{\"SMS\":\"+91xxxxxxxxxx\"} or {\"SMS\":\"0091xxxxxxxxxx\"}**   # noqa: E501

        :param attributes: The attributes of this UpdateBatchContactsContacts.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def email_blacklisted(self):
        """Gets the email_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501

        Set/unset this field to blacklist/allow the contact for emails (emailBlacklisted = true)  # noqa: E501

        :return: The email_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: bool
        """
        return self._email_blacklisted

    @email_blacklisted.setter
    def email_blacklisted(self, email_blacklisted):
        """Sets the email_blacklisted of this UpdateBatchContactsContacts.

        Set/unset this field to blacklist/allow the contact for emails (emailBlacklisted = true)  # noqa: E501

        :param email_blacklisted: The email_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501
        :type: bool
        """

        self._email_blacklisted = email_blacklisted

    @property
    def sms_blacklisted(self):
        """Gets the sms_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501

        Set/unset this field to blacklist/allow the contact for SMS (smsBlacklisted = true)  # noqa: E501

        :return: The sms_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: bool
        """
        return self._sms_blacklisted

    @sms_blacklisted.setter
    def sms_blacklisted(self, sms_blacklisted):
        """Sets the sms_blacklisted of this UpdateBatchContactsContacts.

        Set/unset this field to blacklist/allow the contact for SMS (smsBlacklisted = true)  # noqa: E501

        :param sms_blacklisted: The sms_blacklisted of this UpdateBatchContactsContacts.  # noqa: E501
        :type: bool
        """

        self._sms_blacklisted = sms_blacklisted

    @property
    def list_ids(self):
        """Gets the list_ids of this UpdateBatchContactsContacts.  # noqa: E501

        Ids of the lists to add the contact to  # noqa: E501

        :return: The list_ids of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """Sets the list_ids of this UpdateBatchContactsContacts.

        Ids of the lists to add the contact to  # noqa: E501

        :param list_ids: The list_ids of this UpdateBatchContactsContacts.  # noqa: E501
        :type: list[int]
        """

        self._list_ids = list_ids

    @property
    def unlink_list_ids(self):
        """Gets the unlink_list_ids of this UpdateBatchContactsContacts.  # noqa: E501

        Ids of the lists to remove the contact from  # noqa: E501

        :return: The unlink_list_ids of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: list[int]
        """
        return self._unlink_list_ids

    @unlink_list_ids.setter
    def unlink_list_ids(self, unlink_list_ids):
        """Sets the unlink_list_ids of this UpdateBatchContactsContacts.

        Ids of the lists to remove the contact from  # noqa: E501

        :param unlink_list_ids: The unlink_list_ids of this UpdateBatchContactsContacts.  # noqa: E501
        :type: list[int]
        """

        self._unlink_list_ids = unlink_list_ids

    @property
    def smtp_blacklist_sender(self):
        """Gets the smtp_blacklist_sender of this UpdateBatchContactsContacts.  # noqa: E501

        transactional email forbidden sender for contact. Use only for email Contact  # noqa: E501

        :return: The smtp_blacklist_sender of this UpdateBatchContactsContacts.  # noqa: E501
        :rtype: list[str]
        """
        return self._smtp_blacklist_sender

    @smtp_blacklist_sender.setter
    def smtp_blacklist_sender(self, smtp_blacklist_sender):
        """Sets the smtp_blacklist_sender of this UpdateBatchContactsContacts.

        transactional email forbidden sender for contact. Use only for email Contact  # noqa: E501

        :param smtp_blacklist_sender: The smtp_blacklist_sender of this UpdateBatchContactsContacts.  # noqa: E501
        :type: list[str]
        """

        self._smtp_blacklist_sender = smtp_blacklist_sender

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
        if issubclass(UpdateBatchContactsContacts, dict):
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
        if not isinstance(other, UpdateBatchContactsContacts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
