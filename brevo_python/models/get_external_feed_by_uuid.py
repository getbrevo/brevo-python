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


class GetExternalFeedByUUID(object):
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
        'name': 'str',
        'url': 'str',
        'auth_type': 'str',
        'username': 'str',
        'password': 'str',
        'token': 'str',
        'headers': 'list[GetExternalFeedByUUIDHeaders]',
        'max_retries': 'int',
        'cache': 'bool',
        'created_at': 'datetime',
        'modified_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'auth_type': 'authType',
        'username': 'username',
        'password': 'password',
        'token': 'token',
        'headers': 'headers',
        'max_retries': 'maxRetries',
        'cache': 'cache',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, name=None, url=None, auth_type=None, username=None, password=None, token=None, headers=None, max_retries=None, cache=None, created_at=None, modified_at=None):  # noqa: E501
        """GetExternalFeedByUUID - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._url = None
        self._auth_type = None
        self._username = None
        self._password = None
        self._token = None
        self._headers = None
        self._max_retries = None
        self._cache = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.url = url
        self.auth_type = auth_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        self.headers = headers
        self.max_retries = max_retries
        self.cache = cache
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def id(self):
        """Gets the id of this GetExternalFeedByUUID.  # noqa: E501

        ID of the feed  # noqa: E501

        :return: The id of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetExternalFeedByUUID.

        ID of the feed  # noqa: E501

        :param id: The id of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetExternalFeedByUUID.  # noqa: E501

        Name of the feed  # noqa: E501

        :return: The name of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetExternalFeedByUUID.

        Name of the feed  # noqa: E501

        :param name: The name of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this GetExternalFeedByUUID.  # noqa: E501

        URL of the feed  # noqa: E501

        :return: The url of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetExternalFeedByUUID.

        URL of the feed  # noqa: E501

        :param url: The url of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def auth_type(self):
        """Gets the auth_type of this GetExternalFeedByUUID.  # noqa: E501

        Auth type of the feed: * `basic` * `token` * `noAuth`   # noqa: E501

        :return: The auth_type of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this GetExternalFeedByUUID.

        Auth type of the feed: * `basic` * `token` * `noAuth`   # noqa: E501

        :param auth_type: The auth_type of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """
        if auth_type is None:
            raise ValueError("Invalid value for `auth_type`, must not be `None`")  # noqa: E501
        allowed_values = ["basic", "token", "noAuth"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def username(self):
        """Gets the username of this GetExternalFeedByUUID.  # noqa: E501

        Username for authType `basic`  # noqa: E501

        :return: The username of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetExternalFeedByUUID.

        Username for authType `basic`  # noqa: E501

        :param username: The username of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this GetExternalFeedByUUID.  # noqa: E501

        Password for authType `basic`  # noqa: E501

        :return: The password of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GetExternalFeedByUUID.

        Password for authType `basic`  # noqa: E501

        :param password: The password of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this GetExternalFeedByUUID.  # noqa: E501

        Token for authType `token`  # noqa: E501

        :return: The token of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GetExternalFeedByUUID.

        Token for authType `token`  # noqa: E501

        :param token: The token of this GetExternalFeedByUUID.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def headers(self):
        """Gets the headers of this GetExternalFeedByUUID.  # noqa: E501

        Custom headers for the feed  # noqa: E501

        :return: The headers of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: list[GetExternalFeedByUUIDHeaders]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this GetExternalFeedByUUID.

        Custom headers for the feed  # noqa: E501

        :param headers: The headers of this GetExternalFeedByUUID.  # noqa: E501
        :type: list[GetExternalFeedByUUIDHeaders]
        """
        if headers is None:
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def max_retries(self):
        """Gets the max_retries of this GetExternalFeedByUUID.  # noqa: E501

        Maximum number of retries on the feed url  # noqa: E501

        :return: The max_retries of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this GetExternalFeedByUUID.

        Maximum number of retries on the feed url  # noqa: E501

        :param max_retries: The max_retries of this GetExternalFeedByUUID.  # noqa: E501
        :type: int
        """
        if max_retries is None:
            raise ValueError("Invalid value for `max_retries`, must not be `None`")  # noqa: E501
        if max_retries is not None and max_retries > 5:  # noqa: E501
            raise ValueError("Invalid value for `max_retries`, must be a value less than or equal to `5`")  # noqa: E501
        if max_retries is not None and max_retries < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_retries`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_retries = max_retries

    @property
    def cache(self):
        """Gets the cache of this GetExternalFeedByUUID.  # noqa: E501

        Toggle caching of feed url response  # noqa: E501

        :return: The cache of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: bool
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this GetExternalFeedByUUID.

        Toggle caching of feed url response  # noqa: E501

        :param cache: The cache of this GetExternalFeedByUUID.  # noqa: E501
        :type: bool
        """
        if cache is None:
            raise ValueError("Invalid value for `cache`, must not be `None`")  # noqa: E501

        self._cache = cache

    @property
    def created_at(self):
        """Gets the created_at of this GetExternalFeedByUUID.  # noqa: E501

        Datetime on which the feed was created  # noqa: E501

        :return: The created_at of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetExternalFeedByUUID.

        Datetime on which the feed was created  # noqa: E501

        :param created_at: The created_at of this GetExternalFeedByUUID.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this GetExternalFeedByUUID.  # noqa: E501

        Datetime on which the feed was modified  # noqa: E501

        :return: The modified_at of this GetExternalFeedByUUID.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetExternalFeedByUUID.

        Datetime on which the feed was modified  # noqa: E501

        :param modified_at: The modified_at of this GetExternalFeedByUUID.  # noqa: E501
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

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
        if issubclass(GetExternalFeedByUUID, dict):
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
        if not isinstance(other, GetExternalFeedByUUID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
