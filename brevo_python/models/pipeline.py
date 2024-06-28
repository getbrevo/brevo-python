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


class Pipeline(object):
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
        'pipeline': 'str',
        'pipeline_name': 'str',
        'stages': 'list[PipelineStage]'
    }

    attribute_map = {
        'pipeline': 'pipeline',
        'pipeline_name': 'pipeline_name',
        'stages': 'stages'
    }

    def __init__(self, pipeline=None, pipeline_name=None, stages=None):  # noqa: E501
        """Pipeline - a model defined in Swagger"""  # noqa: E501

        self._pipeline = None
        self._pipeline_name = None
        self._stages = None
        self.discriminator = None

        if pipeline is not None:
            self.pipeline = pipeline
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if stages is not None:
            self.stages = stages

    @property
    def pipeline(self):
        """Gets the pipeline of this Pipeline.  # noqa: E501

        Pipeline id  # noqa: E501

        :return: The pipeline of this Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this Pipeline.

        Pipeline id  # noqa: E501

        :param pipeline: The pipeline of this Pipeline.  # noqa: E501
        :type: str
        """

        self._pipeline = pipeline

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this Pipeline.  # noqa: E501

        Pipeline Name  # noqa: E501

        :return: The pipeline_name of this Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this Pipeline.

        Pipeline Name  # noqa: E501

        :param pipeline_name: The pipeline_name of this Pipeline.  # noqa: E501
        :type: str
        """

        self._pipeline_name = pipeline_name

    @property
    def stages(self):
        """Gets the stages of this Pipeline.  # noqa: E501

        List of stages  # noqa: E501

        :return: The stages of this Pipeline.  # noqa: E501
        :rtype: list[PipelineStage]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this Pipeline.

        List of stages  # noqa: E501

        :param stages: The stages of this Pipeline.  # noqa: E501
        :type: list[PipelineStage]
        """

        self._stages = stages

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
        if issubclass(Pipeline, dict):
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
        if not isinstance(other, Pipeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
