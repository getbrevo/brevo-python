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


class MainAttributeRewardPayload(object):
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
        'value': 'float',
        'code': 'str',
        'contact_id': 'int',
        'expiration_date': 'str',
        'loyalty_subscription_id': 'str',
        'meta': 'dict(str, object)',
        'reward_id': 'str'
    }

    attribute_map = {
        'value': 'value',
        'code': 'code',
        'contact_id': 'contactId',
        'expiration_date': 'expirationDate',
        'loyalty_subscription_id': 'loyaltySubscriptionId',
        'meta': 'meta',
        'reward_id': 'rewardId'
    }

    def __init__(self, value=None, code=None, contact_id=None, expiration_date=None, loyalty_subscription_id=None, meta=None, reward_id=None):  # noqa: E501
        """MainAttributeRewardPayload - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._code = None
        self._contact_id = None
        self._expiration_date = None
        self._loyalty_subscription_id = None
        self._meta = None
        self._reward_id = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if code is not None:
            self.code = code
        if contact_id is not None:
            self.contact_id = contact_id
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if loyalty_subscription_id is not None:
            self.loyalty_subscription_id = loyalty_subscription_id
        if meta is not None:
            self.meta = meta
        self.reward_id = reward_id

    @property
    def value(self):
        """Gets the value of this MainAttributeRewardPayload.  # noqa: E501

        Value of the selected reward config  # noqa: E501

        :return: The value of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MainAttributeRewardPayload.

        Value of the selected reward config  # noqa: E501

        :param value: The value of this MainAttributeRewardPayload.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def code(self):
        """Gets the code of this MainAttributeRewardPayload.  # noqa: E501

        Code generated to attribute reward to a contact  # noqa: E501

        :return: The code of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MainAttributeRewardPayload.

        Code generated to attribute reward to a contact  # noqa: E501

        :param code: The code of this MainAttributeRewardPayload.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 128:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `128`")  # noqa: E501

        self._code = code

    @property
    def contact_id(self):
        """Gets the contact_id of this MainAttributeRewardPayload.  # noqa: E501

        Contact to attribute the reward  # noqa: E501

        :return: The contact_id of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this MainAttributeRewardPayload.

        Contact to attribute the reward  # noqa: E501

        :param contact_id: The contact_id of this MainAttributeRewardPayload.  # noqa: E501
        :type: int
        """
        if contact_id is not None and contact_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `contact_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._contact_id = contact_id

    @property
    def expiration_date(self):
        """Gets the expiration_date of this MainAttributeRewardPayload.  # noqa: E501

        Reward expiration date  # noqa: E501

        :return: The expiration_date of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this MainAttributeRewardPayload.

        Reward expiration date  # noqa: E501

        :param expiration_date: The expiration_date of this MainAttributeRewardPayload.  # noqa: E501
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def loyalty_subscription_id(self):
        """Gets the loyalty_subscription_id of this MainAttributeRewardPayload.  # noqa: E501

        One of contactId or loyaltySubscriptionId is required  # noqa: E501

        :return: The loyalty_subscription_id of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_subscription_id

    @loyalty_subscription_id.setter
    def loyalty_subscription_id(self, loyalty_subscription_id):
        """Sets the loyalty_subscription_id of this MainAttributeRewardPayload.

        One of contactId or loyaltySubscriptionId is required  # noqa: E501

        :param loyalty_subscription_id: The loyalty_subscription_id of this MainAttributeRewardPayload.  # noqa: E501
        :type: str
        """

        self._loyalty_subscription_id = loyalty_subscription_id

    @property
    def meta(self):
        """Gets the meta of this MainAttributeRewardPayload.  # noqa: E501

        Offer meta information (key/value object)  # noqa: E501

        :return: The meta of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this MainAttributeRewardPayload.

        Offer meta information (key/value object)  # noqa: E501

        :param meta: The meta of this MainAttributeRewardPayload.  # noqa: E501
        :type: dict(str, object)
        """

        self._meta = meta

    @property
    def reward_id(self):
        """Gets the reward_id of this MainAttributeRewardPayload.  # noqa: E501

        Reward id  # noqa: E501

        :return: The reward_id of this MainAttributeRewardPayload.  # noqa: E501
        :rtype: str
        """
        return self._reward_id

    @reward_id.setter
    def reward_id(self, reward_id):
        """Sets the reward_id of this MainAttributeRewardPayload.

        Reward id  # noqa: E501

        :param reward_id: The reward_id of this MainAttributeRewardPayload.  # noqa: E501
        :type: str
        """
        if reward_id is None:
            raise ValueError("Invalid value for `reward_id`, must not be `None`")  # noqa: E501

        self._reward_id = reward_id

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
        if issubclass(MainAttributeRewardPayload, dict):
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
        if not isinstance(other, MainAttributeRewardPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
