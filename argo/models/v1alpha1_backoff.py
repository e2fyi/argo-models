# coding: utf-8

"""
    Argo

    Argo  # noqa: E501

    The version of the OpenAPI document: v2.7.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1Backoff(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'duration': 'str',
        'factor': 'int',
        'max_duration': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'factor': 'factor',
        'max_duration': 'maxDuration'
    }

    def __init__(self, duration=None, factor=None, max_duration=None):  # noqa: E501
        """V1alpha1Backoff - a model defined in OpenAPI"""  # noqa: E501

        self._duration = None
        self._factor = None
        self._max_duration = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if factor is not None:
            self.factor = factor
        if max_duration is not None:
            self.max_duration = max_duration

    @property
    def duration(self):
        """Gets the duration of this V1alpha1Backoff.  # noqa: E501


        :return: The duration of this V1alpha1Backoff.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this V1alpha1Backoff.


        :param duration: The duration of this V1alpha1Backoff.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def factor(self):
        """Gets the factor of this V1alpha1Backoff.  # noqa: E501


        :return: The factor of this V1alpha1Backoff.  # noqa: E501
        :rtype: int
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this V1alpha1Backoff.


        :param factor: The factor of this V1alpha1Backoff.  # noqa: E501
        :type: int
        """

        self._factor = factor

    @property
    def max_duration(self):
        """Gets the max_duration of this V1alpha1Backoff.  # noqa: E501


        :return: The max_duration of this V1alpha1Backoff.  # noqa: E501
        :rtype: str
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this V1alpha1Backoff.


        :param max_duration: The max_duration of this V1alpha1Backoff.  # noqa: E501
        :type: str
        """

        self._max_duration = max_duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1Backoff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
