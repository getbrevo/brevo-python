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


class CreateSubAccount(object):
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
        'company_name': 'str',
        'email': 'str',
        'language': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'email': 'email',
        'language': 'language',
        'timezone': 'timezone'
    }

    def __init__(self, company_name=None, email=None, language=None, timezone=None):  # noqa: E501
        """CreateSubAccount - a model defined in Swagger"""  # noqa: E501

        self._company_name = None
        self._email = None
        self._language = None
        self._timezone = None
        self.discriminator = None

        self.company_name = company_name
        self.email = email
        if language is not None:
            self.language = language
        if timezone is not None:
            self.timezone = timezone

    @property
    def company_name(self):
        """Gets the company_name of this CreateSubAccount.  # noqa: E501

        Set the name of the sub-account company  # noqa: E501

        :return: The company_name of this CreateSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreateSubAccount.

        Set the name of the sub-account company  # noqa: E501

        :param company_name: The company_name of this CreateSubAccount.  # noqa: E501
        :type: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def email(self):
        """Gets the email of this CreateSubAccount.  # noqa: E501

        Email address for the organization  # noqa: E501

        :return: The email of this CreateSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateSubAccount.

        Email address for the organization  # noqa: E501

        :param email: The email of this CreateSubAccount.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def language(self):
        """Gets the language of this CreateSubAccount.  # noqa: E501

        Set the language of the sub-account  # noqa: E501

        :return: The language of this CreateSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateSubAccount.

        Set the language of the sub-account  # noqa: E501

        :param language: The language of this CreateSubAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "fr", "it", "es", "pt", "de"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this CreateSubAccount.  # noqa: E501

        Set the timezone of the sub-account  # noqa: E501

        :return: The timezone of this CreateSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CreateSubAccount.

        Set the timezone of the sub-account  # noqa: E501

        :param timezone: The timezone of this CreateSubAccount.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(CreateSubAccount, dict):
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
        if not isinstance(other, CreateSubAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other