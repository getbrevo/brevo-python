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


class ScheduleSmtpEmail(object):
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
        'message_id': 'str',
        'message_ids': 'list[str]',
        'batch_id': 'str'
    }

    attribute_map = {
        'message_id': 'messageId',
        'message_ids': 'messageIds',
        'batch_id': 'batchId'
    }

    def __init__(self, message_id=None, message_ids=None, batch_id=None):  # noqa: E501
        """ScheduleSmtpEmail - a model defined in Swagger"""  # noqa: E501

        self._message_id = None
        self._message_ids = None
        self._batch_id = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if message_ids is not None:
            self.message_ids = message_ids
        if batch_id is not None:
            self.batch_id = batch_id

    @property
    def message_id(self):
        """Gets the message_id of this ScheduleSmtpEmail.  # noqa: E501

        Message ID of the transactional email scheduled  # noqa: E501

        :return: The message_id of this ScheduleSmtpEmail.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ScheduleSmtpEmail.

        Message ID of the transactional email scheduled  # noqa: E501

        :param message_id: The message_id of this ScheduleSmtpEmail.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def message_ids(self):
        """Gets the message_ids of this ScheduleSmtpEmail.  # noqa: E501


        :return: The message_ids of this ScheduleSmtpEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._message_ids

    @message_ids.setter
    def message_ids(self, message_ids):
        """Sets the message_ids of this ScheduleSmtpEmail.


        :param message_ids: The message_ids of this ScheduleSmtpEmail.  # noqa: E501
        :type: list[str]
        """

        self._message_ids = message_ids

    @property
    def batch_id(self):
        """Gets the batch_id of this ScheduleSmtpEmail.  # noqa: E501

        Batch ID of the batch transactional email scheduled  # noqa: E501

        :return: The batch_id of this ScheduleSmtpEmail.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this ScheduleSmtpEmail.

        Batch ID of the batch transactional email scheduled  # noqa: E501

        :param batch_id: The batch_id of this ScheduleSmtpEmail.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

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
        if issubclass(ScheduleSmtpEmail, dict):
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
        if not isinstance(other, ScheduleSmtpEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
