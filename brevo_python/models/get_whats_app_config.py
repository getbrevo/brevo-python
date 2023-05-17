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


class GetWhatsAppConfig(object):
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
        'whatsapp_business_account_id': 'str',
        'sending_limit': 'str',
        'phone_number_quality': 'str',
        'whatsapp_business_account_status': 'str',
        'business_status': 'str',
        'phone_number_name_status': 'str'
    }

    attribute_map = {
        'whatsapp_business_account_id': 'whatsappBusinessAccountId',
        'sending_limit': 'sendingLimit',
        'phone_number_quality': 'phoneNumberQuality',
        'whatsapp_business_account_status': 'whatsappBusinessAccountStatus',
        'business_status': 'businessStatus',
        'phone_number_name_status': 'phoneNumberNameStatus'
    }

    def __init__(self, whatsapp_business_account_id=None, sending_limit=None, phone_number_quality=None, whatsapp_business_account_status=None, business_status=None, phone_number_name_status=None):  # noqa: E501
        """GetWhatsAppConfig - a model defined in Swagger"""  # noqa: E501

        self._whatsapp_business_account_id = None
        self._sending_limit = None
        self._phone_number_quality = None
        self._whatsapp_business_account_status = None
        self._business_status = None
        self._phone_number_name_status = None
        self.discriminator = None

        if whatsapp_business_account_id is not None:
            self.whatsapp_business_account_id = whatsapp_business_account_id
        if sending_limit is not None:
            self.sending_limit = sending_limit
        if phone_number_quality is not None:
            self.phone_number_quality = phone_number_quality
        if whatsapp_business_account_status is not None:
            self.whatsapp_business_account_status = whatsapp_business_account_status
        if business_status is not None:
            self.business_status = business_status
        if phone_number_name_status is not None:
            self.phone_number_name_status = phone_number_name_status

    @property
    def whatsapp_business_account_id(self):
        """Gets the whatsapp_business_account_id of this GetWhatsAppConfig.  # noqa: E501

        Id of the WhatsApp business account  # noqa: E501

        :return: The whatsapp_business_account_id of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._whatsapp_business_account_id

    @whatsapp_business_account_id.setter
    def whatsapp_business_account_id(self, whatsapp_business_account_id):
        """Sets the whatsapp_business_account_id of this GetWhatsAppConfig.

        Id of the WhatsApp business account  # noqa: E501

        :param whatsapp_business_account_id: The whatsapp_business_account_id of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """

        self._whatsapp_business_account_id = whatsapp_business_account_id

    @property
    def sending_limit(self):
        """Gets the sending_limit of this GetWhatsAppConfig.  # noqa: E501

        Sending limit Information of the WhatsApp API account  # noqa: E501

        :return: The sending_limit of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._sending_limit

    @sending_limit.setter
    def sending_limit(self, sending_limit):
        """Sets the sending_limit of this GetWhatsAppConfig.

        Sending limit Information of the WhatsApp API account  # noqa: E501

        :param sending_limit: The sending_limit of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """

        self._sending_limit = sending_limit

    @property
    def phone_number_quality(self):
        """Gets the phone_number_quality of this GetWhatsAppConfig.  # noqa: E501

        Quality status of phone number associated with WhatsApp account. There are three quality ratings. example - **High (GREEN) , Medium (YELLOW) and Low(RED)**  # noqa: E501

        :return: The phone_number_quality of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_quality

    @phone_number_quality.setter
    def phone_number_quality(self, phone_number_quality):
        """Sets the phone_number_quality of this GetWhatsAppConfig.

        Quality status of phone number associated with WhatsApp account. There are three quality ratings. example - **High (GREEN) , Medium (YELLOW) and Low(RED)**  # noqa: E501

        :param phone_number_quality: The phone_number_quality of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["GREEN", "YELLOW", "RED"]  # noqa: E501
        if phone_number_quality not in allowed_values:
            raise ValueError(
                "Invalid value for `phone_number_quality` ({0}), must be one of {1}"  # noqa: E501
                .format(phone_number_quality, allowed_values)
            )

        self._phone_number_quality = phone_number_quality

    @property
    def whatsapp_business_account_status(self):
        """Gets the whatsapp_business_account_status of this GetWhatsAppConfig.  # noqa: E501

        Status information related to WhatsApp Api account  # noqa: E501

        :return: The whatsapp_business_account_status of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._whatsapp_business_account_status

    @whatsapp_business_account_status.setter
    def whatsapp_business_account_status(self, whatsapp_business_account_status):
        """Sets the whatsapp_business_account_status of this GetWhatsAppConfig.

        Status information related to WhatsApp Api account  # noqa: E501

        :param whatsapp_business_account_status: The whatsapp_business_account_status of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """

        self._whatsapp_business_account_status = whatsapp_business_account_status

    @property
    def business_status(self):
        """Gets the business_status of this GetWhatsAppConfig.  # noqa: E501

        Verification status information of the Business account  # noqa: E501

        :return: The business_status of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this GetWhatsAppConfig.

        Verification status information of the Business account  # noqa: E501

        :param business_status: The business_status of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def phone_number_name_status(self):
        """Gets the phone_number_name_status of this GetWhatsAppConfig.  # noqa: E501

        Status of the name associated with WhatsApp Phone number  # noqa: E501

        :return: The phone_number_name_status of this GetWhatsAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_name_status

    @phone_number_name_status.setter
    def phone_number_name_status(self, phone_number_name_status):
        """Sets the phone_number_name_status of this GetWhatsAppConfig.

        Status of the name associated with WhatsApp Phone number  # noqa: E501

        :param phone_number_name_status: The phone_number_name_status of this GetWhatsAppConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPROVED", "PENDING", "REJECTED"]  # noqa: E501
        if phone_number_name_status not in allowed_values:
            raise ValueError(
                "Invalid value for `phone_number_name_status` ({0}), must be one of {1}"  # noqa: E501
                .format(phone_number_name_status, allowed_values)
            )

        self._phone_number_name_status = phone_number_name_status

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
        if issubclass(GetWhatsAppConfig, dict):
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
        if not isinstance(other, GetWhatsAppConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
