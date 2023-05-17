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


class UpdateEmailCampaignRecipients(object):
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
        'exclusion_list_ids': 'list[int]',
        'list_ids': 'list[int]',
        'segment_ids': 'list[int]'
    }

    attribute_map = {
        'exclusion_list_ids': 'exclusionListIds',
        'list_ids': 'listIds',
        'segment_ids': 'segmentIds'
    }

    def __init__(self, exclusion_list_ids=None, list_ids=None, segment_ids=None):  # noqa: E501
        """UpdateEmailCampaignRecipients - a model defined in Swagger"""  # noqa: E501

        self._exclusion_list_ids = None
        self._list_ids = None
        self._segment_ids = None
        self.discriminator = None

        if exclusion_list_ids is not None:
            self.exclusion_list_ids = exclusion_list_ids
        if list_ids is not None:
            self.list_ids = list_ids
        if segment_ids is not None:
            self.segment_ids = segment_ids

    @property
    def exclusion_list_ids(self):
        """Gets the exclusion_list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501

        List ids which have to be excluded from a campaign  # noqa: E501

        :return: The exclusion_list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :rtype: list[int]
        """
        return self._exclusion_list_ids

    @exclusion_list_ids.setter
    def exclusion_list_ids(self, exclusion_list_ids):
        """Sets the exclusion_list_ids of this UpdateEmailCampaignRecipients.

        List ids which have to be excluded from a campaign  # noqa: E501

        :param exclusion_list_ids: The exclusion_list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :type: list[int]
        """

        self._exclusion_list_ids = exclusion_list_ids

    @property
    def list_ids(self):
        """Gets the list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501

        Lists Ids to send the campaign to. Campaign should only be updated with listIds if listIds were used to create it. REQUIRED if already not present in campaign and scheduledAt is not empty  # noqa: E501

        :return: The list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """Sets the list_ids of this UpdateEmailCampaignRecipients.

        Lists Ids to send the campaign to. Campaign should only be updated with listIds if listIds were used to create it. REQUIRED if already not present in campaign and scheduledAt is not empty  # noqa: E501

        :param list_ids: The list_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :type: list[int]
        """

        self._list_ids = list_ids

    @property
    def segment_ids(self):
        """Gets the segment_ids of this UpdateEmailCampaignRecipients.  # noqa: E501

        Mandatory if listIds are not used. Campaign should only be updated with segmentIds if segmentIds were used to create it. Segment ids to send the campaign to.  # noqa: E501

        :return: The segment_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :rtype: list[int]
        """
        return self._segment_ids

    @segment_ids.setter
    def segment_ids(self, segment_ids):
        """Sets the segment_ids of this UpdateEmailCampaignRecipients.

        Mandatory if listIds are not used. Campaign should only be updated with segmentIds if segmentIds were used to create it. Segment ids to send the campaign to.  # noqa: E501

        :param segment_ids: The segment_ids of this UpdateEmailCampaignRecipients.  # noqa: E501
        :type: list[int]
        """

        self._segment_ids = segment_ids

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
        if issubclass(UpdateEmailCampaignRecipients, dict):
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
        if not isinstance(other, UpdateEmailCampaignRecipients):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
