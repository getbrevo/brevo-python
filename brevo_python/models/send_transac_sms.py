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


class SendTransacSms(object):
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
        'sender': 'str',
        'recipient': 'str',
        'content': 'str',
        'type': 'str',
        'tag': 'str',
        'web_url': 'str',
        'unicode_enabled': 'bool',
        'organisation_prefix': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'recipient': 'recipient',
        'content': 'content',
        'type': 'type',
        'tag': 'tag',
        'web_url': 'webUrl',
        'unicode_enabled': 'unicodeEnabled',
        'organisation_prefix': 'organisationPrefix'
    }

    def __init__(self, sender=None, recipient=None, content=None, type='transactional', tag=None, web_url=None, unicode_enabled=False, organisation_prefix=None):  # noqa: E501
        """SendTransacSms - a model defined in Swagger"""  # noqa: E501

        self._sender = None
        self._recipient = None
        self._content = None
        self._type = None
        self._tag = None
        self._web_url = None
        self._unicode_enabled = None
        self._organisation_prefix = None
        self.discriminator = None

        self.sender = sender
        self.recipient = recipient
        self.content = content
        if type is not None:
            self.type = type
        if tag is not None:
            self.tag = tag
        if web_url is not None:
            self.web_url = web_url
        if unicode_enabled is not None:
            self.unicode_enabled = unicode_enabled
        if organisation_prefix is not None:
            self.organisation_prefix = organisation_prefix

    @property
    def sender(self):
        """Gets the sender of this SendTransacSms.  # noqa: E501

        Name of the sender. **The number of characters is limited to 11 for alphanumeric characters and 15 for numeric characters**  # noqa: E501

        :return: The sender of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SendTransacSms.

        Name of the sender. **The number of characters is limited to 11 for alphanumeric characters and 15 for numeric characters**  # noqa: E501

        :param sender: The sender of this SendTransacSms.  # noqa: E501
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501
        if sender is not None and len(sender) > 15:
            raise ValueError("Invalid value for `sender`, length must be less than or equal to `15`")  # noqa: E501

        self._sender = sender

    @property
    def recipient(self):
        """Gets the recipient of this SendTransacSms.  # noqa: E501

        Mobile number to send SMS with the country code  # noqa: E501

        :return: The recipient of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this SendTransacSms.

        Mobile number to send SMS with the country code  # noqa: E501

        :param recipient: The recipient of this SendTransacSms.  # noqa: E501
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def content(self):
        """Gets the content of this SendTransacSms.  # noqa: E501

        Content of the message. If more than 160 characters long, will be sent as multiple text messages  # noqa: E501

        :return: The content of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SendTransacSms.

        Content of the message. If more than 160 characters long, will be sent as multiple text messages  # noqa: E501

        :param content: The content of this SendTransacSms.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def type(self):
        """Gets the type of this SendTransacSms.  # noqa: E501

        Type of the SMS. Marketing SMS messages are those sent typically with marketing content. Transactional SMS messages are sent to individuals and are triggered in response to some action, such as a sign-up, purchase, etc.  # noqa: E501

        :return: The type of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SendTransacSms.

        Type of the SMS. Marketing SMS messages are those sent typically with marketing content. Transactional SMS messages are sent to individuals and are triggered in response to some action, such as a sign-up, purchase, etc.  # noqa: E501

        :param type: The type of this SendTransacSms.  # noqa: E501
        :type: str
        """
        allowed_values = ["transactional", "marketing"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def tag(self):
        """Gets the tag of this SendTransacSms.  # noqa: E501

        Tag of the message  # noqa: E501

        :return: The tag of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SendTransacSms.

        Tag of the message  # noqa: E501

        :param tag: The tag of this SendTransacSms.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def web_url(self):
        """Gets the web_url of this SendTransacSms.  # noqa: E501

        Webhook to call for each event triggered by the message (delivered etc.)  # noqa: E501

        :return: The web_url of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this SendTransacSms.

        Webhook to call for each event triggered by the message (delivered etc.)  # noqa: E501

        :param web_url: The web_url of this SendTransacSms.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def unicode_enabled(self):
        """Gets the unicode_enabled of this SendTransacSms.  # noqa: E501

        Format of the message. It indicates whether the content should be treated as unicode or not.  # noqa: E501

        :return: The unicode_enabled of this SendTransacSms.  # noqa: E501
        :rtype: bool
        """
        return self._unicode_enabled

    @unicode_enabled.setter
    def unicode_enabled(self, unicode_enabled):
        """Sets the unicode_enabled of this SendTransacSms.

        Format of the message. It indicates whether the content should be treated as unicode or not.  # noqa: E501

        :param unicode_enabled: The unicode_enabled of this SendTransacSms.  # noqa: E501
        :type: bool
        """

        self._unicode_enabled = unicode_enabled

    @property
    def organisation_prefix(self):
        """Gets the organisation_prefix of this SendTransacSms.  # noqa: E501

        A recognizable prefix will ensure your audience knows who you are. Recommended by U.S. carriers. This will be added as your Brand Name before the message content. **Prefer verifying maximum length of 160 characters including this prefix in message content to avoid multiple sending of same sms.**  # noqa: E501

        :return: The organisation_prefix of this SendTransacSms.  # noqa: E501
        :rtype: str
        """
        return self._organisation_prefix

    @organisation_prefix.setter
    def organisation_prefix(self, organisation_prefix):
        """Sets the organisation_prefix of this SendTransacSms.

        A recognizable prefix will ensure your audience knows who you are. Recommended by U.S. carriers. This will be added as your Brand Name before the message content. **Prefer verifying maximum length of 160 characters including this prefix in message content to avoid multiple sending of same sms.**  # noqa: E501

        :param organisation_prefix: The organisation_prefix of this SendTransacSms.  # noqa: E501
        :type: str
        """

        self._organisation_prefix = organisation_prefix

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
        if issubclass(SendTransacSms, dict):
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
        if not isinstance(other, SendTransacSms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
