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


class GetContactCampaignStats(object):
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
        'messages_sent': 'list[GetExtendedContactDetailsStatisticsMessagesSent]',
        'hard_bounces': 'list[GetExtendedContactDetailsStatisticsMessagesSent]',
        'soft_bounces': 'list[GetExtendedContactDetailsStatisticsMessagesSent]',
        'complaints': 'list[GetExtendedContactDetailsStatisticsMessagesSent]',
        'unsubscriptions': 'GetContactCampaignStatsUnsubscriptions',
        'opened': 'list[GetContactCampaignStatsOpened]',
        'clicked': 'list[GetContactCampaignStatsClicked]',
        'transac_attributes': 'list[GetContactCampaignStatsTransacAttributes]',
        'delivered': 'list[GetExtendedContactDetailsStatisticsMessagesSent]'
    }

    attribute_map = {
        'messages_sent': 'messagesSent',
        'hard_bounces': 'hardBounces',
        'soft_bounces': 'softBounces',
        'complaints': 'complaints',
        'unsubscriptions': 'unsubscriptions',
        'opened': 'opened',
        'clicked': 'clicked',
        'transac_attributes': 'transacAttributes',
        'delivered': 'delivered'
    }

    def __init__(self, messages_sent=None, hard_bounces=None, soft_bounces=None, complaints=None, unsubscriptions=None, opened=None, clicked=None, transac_attributes=None, delivered=None):  # noqa: E501
        """GetContactCampaignStats - a model defined in Swagger"""  # noqa: E501

        self._messages_sent = None
        self._hard_bounces = None
        self._soft_bounces = None
        self._complaints = None
        self._unsubscriptions = None
        self._opened = None
        self._clicked = None
        self._transac_attributes = None
        self._delivered = None
        self.discriminator = None

        if messages_sent is not None:
            self.messages_sent = messages_sent
        if hard_bounces is not None:
            self.hard_bounces = hard_bounces
        if soft_bounces is not None:
            self.soft_bounces = soft_bounces
        if complaints is not None:
            self.complaints = complaints
        if unsubscriptions is not None:
            self.unsubscriptions = unsubscriptions
        if opened is not None:
            self.opened = opened
        if clicked is not None:
            self.clicked = clicked
        if transac_attributes is not None:
            self.transac_attributes = transac_attributes
        if delivered is not None:
            self.delivered = delivered

    @property
    def messages_sent(self):
        """Gets the messages_sent of this GetContactCampaignStats.  # noqa: E501


        :return: The messages_sent of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """
        return self._messages_sent

    @messages_sent.setter
    def messages_sent(self, messages_sent):
        """Sets the messages_sent of this GetContactCampaignStats.


        :param messages_sent: The messages_sent of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """

        self._messages_sent = messages_sent

    @property
    def hard_bounces(self):
        """Gets the hard_bounces of this GetContactCampaignStats.  # noqa: E501


        :return: The hard_bounces of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """
        return self._hard_bounces

    @hard_bounces.setter
    def hard_bounces(self, hard_bounces):
        """Sets the hard_bounces of this GetContactCampaignStats.


        :param hard_bounces: The hard_bounces of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """

        self._hard_bounces = hard_bounces

    @property
    def soft_bounces(self):
        """Gets the soft_bounces of this GetContactCampaignStats.  # noqa: E501


        :return: The soft_bounces of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """
        return self._soft_bounces

    @soft_bounces.setter
    def soft_bounces(self, soft_bounces):
        """Sets the soft_bounces of this GetContactCampaignStats.


        :param soft_bounces: The soft_bounces of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """

        self._soft_bounces = soft_bounces

    @property
    def complaints(self):
        """Gets the complaints of this GetContactCampaignStats.  # noqa: E501


        :return: The complaints of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """
        return self._complaints

    @complaints.setter
    def complaints(self, complaints):
        """Sets the complaints of this GetContactCampaignStats.


        :param complaints: The complaints of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """

        self._complaints = complaints

    @property
    def unsubscriptions(self):
        """Gets the unsubscriptions of this GetContactCampaignStats.  # noqa: E501


        :return: The unsubscriptions of this GetContactCampaignStats.  # noqa: E501
        :rtype: GetContactCampaignStatsUnsubscriptions
        """
        return self._unsubscriptions

    @unsubscriptions.setter
    def unsubscriptions(self, unsubscriptions):
        """Sets the unsubscriptions of this GetContactCampaignStats.


        :param unsubscriptions: The unsubscriptions of this GetContactCampaignStats.  # noqa: E501
        :type: GetContactCampaignStatsUnsubscriptions
        """

        self._unsubscriptions = unsubscriptions

    @property
    def opened(self):
        """Gets the opened of this GetContactCampaignStats.  # noqa: E501


        :return: The opened of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetContactCampaignStatsOpened]
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        """Sets the opened of this GetContactCampaignStats.


        :param opened: The opened of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetContactCampaignStatsOpened]
        """

        self._opened = opened

    @property
    def clicked(self):
        """Gets the clicked of this GetContactCampaignStats.  # noqa: E501


        :return: The clicked of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetContactCampaignStatsClicked]
        """
        return self._clicked

    @clicked.setter
    def clicked(self, clicked):
        """Sets the clicked of this GetContactCampaignStats.


        :param clicked: The clicked of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetContactCampaignStatsClicked]
        """

        self._clicked = clicked

    @property
    def transac_attributes(self):
        """Gets the transac_attributes of this GetContactCampaignStats.  # noqa: E501


        :return: The transac_attributes of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetContactCampaignStatsTransacAttributes]
        """
        return self._transac_attributes

    @transac_attributes.setter
    def transac_attributes(self, transac_attributes):
        """Sets the transac_attributes of this GetContactCampaignStats.


        :param transac_attributes: The transac_attributes of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetContactCampaignStatsTransacAttributes]
        """

        self._transac_attributes = transac_attributes

    @property
    def delivered(self):
        """Gets the delivered of this GetContactCampaignStats.  # noqa: E501


        :return: The delivered of this GetContactCampaignStats.  # noqa: E501
        :rtype: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this GetContactCampaignStats.


        :param delivered: The delivered of this GetContactCampaignStats.  # noqa: E501
        :type: list[GetExtendedContactDetailsStatisticsMessagesSent]
        """

        self._delivered = delivered

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
        if issubclass(GetContactCampaignStats, dict):
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
        if not isinstance(other, GetContactCampaignStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
