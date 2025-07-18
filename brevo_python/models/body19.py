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


class Body19(object):
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
        'agent_id': 'str',
        'received_from': 'str',
        'agent_email': 'str',
        'agent_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agentId',
        'received_from': 'receivedFrom',
        'agent_email': 'agentEmail',
        'agent_name': 'agentName'
    }

    def __init__(self, agent_id=None, received_from=None, agent_email=None, agent_name=None):  # noqa: E501
        """Body19 - a model defined in Swagger"""  # noqa: E501

        self._agent_id = None
        self._received_from = None
        self._agent_email = None
        self._agent_name = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if received_from is not None:
            self.received_from = received_from
        if agent_email is not None:
            self.agent_email = agent_email
        if agent_name is not None:
            self.agent_name = agent_name

    @property
    def agent_id(self):
        """Gets the agent_id of this Body19.  # noqa: E501

        agent ID. It can be found on agent’s page or received <a href=\"https://developers.brevo.com/docs/conversations-webhooks\">from a webhook</a>. Alternatively, you can use `agentEmail` + `agentName` + `receivedFrom` instead (all 3 fields required).  # noqa: E501

        :return: The agent_id of this Body19.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Body19.

        agent ID. It can be found on agent’s page or received <a href=\"https://developers.brevo.com/docs/conversations-webhooks\">from a webhook</a>. Alternatively, you can use `agentEmail` + `agentName` + `receivedFrom` instead (all 3 fields required).  # noqa: E501

        :param agent_id: The agent_id of this Body19.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def received_from(self):
        """Gets the received_from of this Body19.  # noqa: E501

        mark your messages to distinguish messages created by you from the others.  # noqa: E501

        :return: The received_from of this Body19.  # noqa: E501
        :rtype: str
        """
        return self._received_from

    @received_from.setter
    def received_from(self, received_from):
        """Sets the received_from of this Body19.

        mark your messages to distinguish messages created by you from the others.  # noqa: E501

        :param received_from: The received_from of this Body19.  # noqa: E501
        :type: str
        """

        self._received_from = received_from

    @property
    def agent_email(self):
        """Gets the agent_email of this Body19.  # noqa: E501

        agent email. When sending online pings from a standalone system, it’s hard to maintain a 1-to-1 relationship between the users of both systems. In this case, an agent can be specified by their email address. If there’s no agent with the specified email address in your Brevo organization, a dummy agent will be created automatically.  # noqa: E501

        :return: The agent_email of this Body19.  # noqa: E501
        :rtype: str
        """
        return self._agent_email

    @agent_email.setter
    def agent_email(self, agent_email):
        """Sets the agent_email of this Body19.

        agent email. When sending online pings from a standalone system, it’s hard to maintain a 1-to-1 relationship between the users of both systems. In this case, an agent can be specified by their email address. If there’s no agent with the specified email address in your Brevo organization, a dummy agent will be created automatically.  # noqa: E501

        :param agent_email: The agent_email of this Body19.  # noqa: E501
        :type: str
        """

        self._agent_email = agent_email

    @property
    def agent_name(self):
        """Gets the agent_name of this Body19.  # noqa: E501

        agent name.  # noqa: E501

        :return: The agent_name of this Body19.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this Body19.

        agent name.  # noqa: E501

        :param agent_name: The agent_name of this Body19.  # noqa: E501
        :type: str
        """

        self._agent_name = agent_name

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
        if issubclass(Body19, dict):
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
        if not isinstance(other, Body19):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
