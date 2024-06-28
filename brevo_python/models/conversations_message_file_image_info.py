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


class ConversationsMessageFileImageInfo(object):
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
        'width': 'int',
        'height': 'int',
        'preview_url': 'str'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height',
        'preview_url': 'previewUrl'
    }

    def __init__(self, width=None, height=None, preview_url=None):  # noqa: E501
        """ConversationsMessageFileImageInfo - a model defined in Swagger"""  # noqa: E501

        self._width = None
        self._height = None
        self._preview_url = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if preview_url is not None:
            self.preview_url = preview_url

    @property
    def width(self):
        """Gets the width of this ConversationsMessageFileImageInfo.  # noqa: E501

        Width of the image  # noqa: E501

        :return: The width of this ConversationsMessageFileImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ConversationsMessageFileImageInfo.

        Width of the image  # noqa: E501

        :param width: The width of this ConversationsMessageFileImageInfo.  # noqa: E501
        :type: int
        """
        if width is not None and width < 0:  # noqa: E501
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `0`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this ConversationsMessageFileImageInfo.  # noqa: E501

        height of the image  # noqa: E501

        :return: The height of this ConversationsMessageFileImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ConversationsMessageFileImageInfo.

        height of the image  # noqa: E501

        :param height: The height of this ConversationsMessageFileImageInfo.  # noqa: E501
        :type: int
        """
        if height is not None and height < 0:  # noqa: E501
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0`")  # noqa: E501

        self._height = height

    @property
    def preview_url(self):
        """Gets the preview_url of this ConversationsMessageFileImageInfo.  # noqa: E501

        URL of the preview  # noqa: E501

        :return: The preview_url of this ConversationsMessageFileImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        """Sets the preview_url of this ConversationsMessageFileImageInfo.

        URL of the preview  # noqa: E501

        :param preview_url: The preview_url of this ConversationsMessageFileImageInfo.  # noqa: E501
        :type: str
        """

        self._preview_url = preview_url

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
        if issubclass(ConversationsMessageFileImageInfo, dict):
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
        if not isinstance(other, ConversationsMessageFileImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
