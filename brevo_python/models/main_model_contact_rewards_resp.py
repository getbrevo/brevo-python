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


class MainModelContactRewardsResp(object):
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
        'contact_id': 'int',
        'contact_rewards': 'list[MainModelContactReward]',
        'count': 'int',
        'loyalty_program_id': 'str',
        'loyalty_subscription_id': 'str'
    }

    attribute_map = {
        'contact_id': 'contactId',
        'contact_rewards': 'contactRewards',
        'count': 'count',
        'loyalty_program_id': 'loyaltyProgramId',
        'loyalty_subscription_id': 'loyaltySubscriptionId'
    }

    def __init__(self, contact_id=None, contact_rewards=None, count=None, loyalty_program_id=None, loyalty_subscription_id=None):  # noqa: E501
        """MainModelContactRewardsResp - a model defined in Swagger"""  # noqa: E501

        self._contact_id = None
        self._contact_rewards = None
        self._count = None
        self._loyalty_program_id = None
        self._loyalty_subscription_id = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if contact_rewards is not None:
            self.contact_rewards = contact_rewards
        if count is not None:
            self.count = count
        if loyalty_program_id is not None:
            self.loyalty_program_id = loyalty_program_id
        if loyalty_subscription_id is not None:
            self.loyalty_subscription_id = loyalty_subscription_id

    @property
    def contact_id(self):
        """Gets the contact_id of this MainModelContactRewardsResp.  # noqa: E501

        Contact id associated with the current reward  # noqa: E501

        :return: The contact_id of this MainModelContactRewardsResp.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this MainModelContactRewardsResp.

        Contact id associated with the current reward  # noqa: E501

        :param contact_id: The contact_id of this MainModelContactRewardsResp.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def contact_rewards(self):
        """Gets the contact_rewards of this MainModelContactRewardsResp.  # noqa: E501

        List of all the rewards for current contact  # noqa: E501

        :return: The contact_rewards of this MainModelContactRewardsResp.  # noqa: E501
        :rtype: list[MainModelContactReward]
        """
        return self._contact_rewards

    @contact_rewards.setter
    def contact_rewards(self, contact_rewards):
        """Sets the contact_rewards of this MainModelContactRewardsResp.

        List of all the rewards for current contact  # noqa: E501

        :param contact_rewards: The contact_rewards of this MainModelContactRewardsResp.  # noqa: E501
        :type: list[MainModelContactReward]
        """

        self._contact_rewards = contact_rewards

    @property
    def count(self):
        """Gets the count of this MainModelContactRewardsResp.  # noqa: E501

        Count of the rewards associated with the current contact  # noqa: E501

        :return: The count of this MainModelContactRewardsResp.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MainModelContactRewardsResp.

        Count of the rewards associated with the current contact  # noqa: E501

        :param count: The count of this MainModelContactRewardsResp.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def loyalty_program_id(self):
        """Gets the loyalty_program_id of this MainModelContactRewardsResp.  # noqa: E501

        Loyalty Program Id for the contact  # noqa: E501

        :return: The loyalty_program_id of this MainModelContactRewardsResp.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_program_id

    @loyalty_program_id.setter
    def loyalty_program_id(self, loyalty_program_id):
        """Sets the loyalty_program_id of this MainModelContactRewardsResp.

        Loyalty Program Id for the contact  # noqa: E501

        :param loyalty_program_id: The loyalty_program_id of this MainModelContactRewardsResp.  # noqa: E501
        :type: str
        """

        self._loyalty_program_id = loyalty_program_id

    @property
    def loyalty_subscription_id(self):
        """Gets the loyalty_subscription_id of this MainModelContactRewardsResp.  # noqa: E501

        Loyalty Subscription Id for the contact  # noqa: E501

        :return: The loyalty_subscription_id of this MainModelContactRewardsResp.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_subscription_id

    @loyalty_subscription_id.setter
    def loyalty_subscription_id(self, loyalty_subscription_id):
        """Sets the loyalty_subscription_id of this MainModelContactRewardsResp.

        Loyalty Subscription Id for the contact  # noqa: E501

        :param loyalty_subscription_id: The loyalty_subscription_id of this MainModelContactRewardsResp.  # noqa: E501
        :type: str
        """

        self._loyalty_subscription_id = loyalty_subscription_id

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
        if issubclass(MainModelContactRewardsResp, dict):
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
        if not isinstance(other, MainModelContactRewardsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
