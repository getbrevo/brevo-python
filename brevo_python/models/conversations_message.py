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


class ConversationsMessage(object):
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
        'id': 'str',
        'type': 'str',
        'text': 'str',
        'visitor_id': 'str',
        'agent_id': 'str',
        'agent_name': 'str',
        'created_at': 'int',
        'is_pushed': 'bool',
        'received_from': 'str',
        'file': 'ConversationsMessageFile'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'text': 'text',
        'visitor_id': 'visitorId',
        'agent_id': 'agentId',
        'agent_name': 'agentName',
        'created_at': 'createdAt',
        'is_pushed': 'isPushed',
        'received_from': 'receivedFrom',
        'file': 'file'
    }

    def __init__(self, id=None, type=None, text=None, visitor_id=None, agent_id=None, agent_name=None, created_at=None, is_pushed=None, received_from=None, file=None):  # noqa: E501
        """ConversationsMessage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._text = None
        self._visitor_id = None
        self._agent_id = None
        self._agent_name = None
        self._created_at = None
        self._is_pushed = None
        self._received_from = None
        self._file = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if text is not None:
            self.text = text
        if visitor_id is not None:
            self.visitor_id = visitor_id
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if created_at is not None:
            self.created_at = created_at
        if is_pushed is not None:
            self.is_pushed = is_pushed
        if received_from is not None:
            self.received_from = received_from
        if file is not None:
            self.file = file

    @property
    def id(self):
        """Gets the id of this ConversationsMessage.  # noqa: E501

        Message ID. It can be used for further manipulations with the message.  # noqa: E501

        :return: The id of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversationsMessage.

        Message ID. It can be used for further manipulations with the message.  # noqa: E501

        :param id: The id of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ConversationsMessage.  # noqa: E501

        `\"agent\"` for agents’ messages, `\"visitor\"` for visitors’ messages.  # noqa: E501

        :return: The type of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationsMessage.

        `\"agent\"` for agents’ messages, `\"visitor\"` for visitors’ messages.  # noqa: E501

        :param type: The type of this ConversationsMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["agent", "visitor"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def text(self):
        """Gets the text of this ConversationsMessage.  # noqa: E501

        Message text or name of the attached file  # noqa: E501

        :return: The text of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ConversationsMessage.

        Message text or name of the attached file  # noqa: E501

        :param text: The text of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def visitor_id(self):
        """Gets the visitor_id of this ConversationsMessage.  # noqa: E501

        visitor’s ID  # noqa: E501

        :return: The visitor_id of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        """Sets the visitor_id of this ConversationsMessage.

        visitor’s ID  # noqa: E501

        :param visitor_id: The visitor_id of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._visitor_id = visitor_id

    @property
    def agent_id(self):
        """Gets the agent_id of this ConversationsMessage.  # noqa: E501

        ID of the agent on whose behalf the message was sent (only in messages sent by an agent).  # noqa: E501

        :return: The agent_id of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this ConversationsMessage.

        ID of the agent on whose behalf the message was sent (only in messages sent by an agent).  # noqa: E501

        :param agent_id: The agent_id of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def agent_name(self):
        """Gets the agent_name of this ConversationsMessage.  # noqa: E501

        Agent’s name as displayed to the visitor. Only in the messages sent by an agent.  # noqa: E501

        :return: The agent_name of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this ConversationsMessage.

        Agent’s name as displayed to the visitor. Only in the messages sent by an agent.  # noqa: E501

        :param agent_name: The agent_name of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._agent_name = agent_name

    @property
    def created_at(self):
        """Gets the created_at of this ConversationsMessage.  # noqa: E501

        Timestamp in milliseconds.  # noqa: E501

        :return: The created_at of this ConversationsMessage.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConversationsMessage.

        Timestamp in milliseconds.  # noqa: E501

        :param created_at: The created_at of this ConversationsMessage.  # noqa: E501
        :type: int
        """
        if created_at is not None and created_at < 0:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must be a value greater than or equal to `0`")  # noqa: E501

        self._created_at = created_at

    @property
    def is_pushed(self):
        """Gets the is_pushed of this ConversationsMessage.  # noqa: E501

        `true` for pushed messages  # noqa: E501

        :return: The is_pushed of this ConversationsMessage.  # noqa: E501
        :rtype: bool
        """
        return self._is_pushed

    @is_pushed.setter
    def is_pushed(self, is_pushed):
        """Sets the is_pushed of this ConversationsMessage.

        `true` for pushed messages  # noqa: E501

        :param is_pushed: The is_pushed of this ConversationsMessage.  # noqa: E501
        :type: bool
        """

        self._is_pushed = is_pushed

    @property
    def received_from(self):
        """Gets the received_from of this ConversationsMessage.  # noqa: E501

        In two-way integrations, messages sent via REST API can be marked with receivedFrom property and then filtered out when received in a webhook to avoid infinite loop.  # noqa: E501

        :return: The received_from of this ConversationsMessage.  # noqa: E501
        :rtype: str
        """
        return self._received_from

    @received_from.setter
    def received_from(self, received_from):
        """Sets the received_from of this ConversationsMessage.

        In two-way integrations, messages sent via REST API can be marked with receivedFrom property and then filtered out when received in a webhook to avoid infinite loop.  # noqa: E501

        :param received_from: The received_from of this ConversationsMessage.  # noqa: E501
        :type: str
        """

        self._received_from = received_from

    @property
    def file(self):
        """Gets the file of this ConversationsMessage.  # noqa: E501


        :return: The file of this ConversationsMessage.  # noqa: E501
        :rtype: ConversationsMessageFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ConversationsMessage.


        :param file: The file of this ConversationsMessage.  # noqa: E501
        :type: ConversationsMessageFile
        """

        self._file = file

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
        if issubclass(ConversationsMessage, dict):
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
        if not isinstance(other, ConversationsMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
