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


class GetTransacEmailsListTransactionalEmails(object):
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
        'subject': 'str',
        'template_id': 'int',
        'message_id': 'str',
        'uuid': 'str',
        '_date': 'str',
        '_from': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'email': 'email',
        'subject': 'subject',
        'template_id': 'templateId',
        'message_id': 'messageId',
        'uuid': 'uuid',
        '_date': 'date',
        '_from': 'from',
        'tags': 'tags'
    }

    def __init__(self, email=None, subject=None, template_id=None, message_id=None, uuid=None, _date=None, _from=None, tags=None):  # noqa: E501
        """GetTransacEmailsListTransactionalEmails - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._subject = None
        self._template_id = None
        self._message_id = None
        self._uuid = None
        self.__date = None
        self.__from = None
        self._tags = None
        self.discriminator = None

        self.email = email
        self.subject = subject
        if template_id is not None:
            self.template_id = template_id
        self.message_id = message_id
        self.uuid = uuid
        self._date = _date
        if _from is not None:
            self._from = _from
        if tags is not None:
            self.tags = tags

    @property
    def email(self):
        """Gets the email of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Email address to which transactional email has been sent  # noqa: E501

        :return: The email of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetTransacEmailsListTransactionalEmails.

        Email address to which transactional email has been sent  # noqa: E501

        :param email: The email of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def subject(self):
        """Gets the subject of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Subject of the sent email  # noqa: E501

        :return: The subject of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetTransacEmailsListTransactionalEmails.

        Subject of the sent email  # noqa: E501

        :param subject: The subject of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def template_id(self):
        """Gets the template_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Id of the template  # noqa: E501

        :return: The template_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this GetTransacEmailsListTransactionalEmails.

        Id of the template  # noqa: E501

        :param template_id: The template_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def message_id(self):
        """Gets the message_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Message Id of the sent email  # noqa: E501

        :return: The message_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this GetTransacEmailsListTransactionalEmails.

        Message Id of the sent email  # noqa: E501

        :param message_id: The message_id of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def uuid(self):
        """Gets the uuid of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Unique id of the email sent to a particular contact  # noqa: E501

        :return: The uuid of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this GetTransacEmailsListTransactionalEmails.

        Unique id of the email sent to a particular contact  # noqa: E501

        :param uuid: The uuid of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def _date(self):
        """Gets the _date of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Date on which transactional email was sent  # noqa: E501

        :return: The _date of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetTransacEmailsListTransactionalEmails.

        Date on which transactional email was sent  # noqa: E501

        :param _date: The _date of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def _from(self):
        """Gets the _from of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Email address of the sender from which the email was sent  # noqa: E501

        :return: The _from of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this GetTransacEmailsListTransactionalEmails.

        Email address of the sender from which the email was sent  # noqa: E501

        :param _from: The _from of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def tags(self):
        """Gets the tags of this GetTransacEmailsListTransactionalEmails.  # noqa: E501

        Tags used for your email  # noqa: E501

        :return: The tags of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetTransacEmailsListTransactionalEmails.

        Tags used for your email  # noqa: E501

        :param tags: The tags of this GetTransacEmailsListTransactionalEmails.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(GetTransacEmailsListTransactionalEmails, dict):
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
        if not isinstance(other, GetTransacEmailsListTransactionalEmails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
