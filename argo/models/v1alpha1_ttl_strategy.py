# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.7.0-rc1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class V1alpha1TTLStrategy(object):
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
        'seconds_after_completion': 'int',
        'seconds_after_failure': 'int',
        'seconds_after_success': 'int'
    }

    attribute_map = {
        'seconds_after_completion': 'secondsAfterCompletion',
        'seconds_after_failure': 'secondsAfterFailure',
        'seconds_after_success': 'secondsAfterSuccess'
    }

    def __init__(self, seconds_after_completion=None, seconds_after_failure=None, seconds_after_success=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1TTLStrategy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._seconds_after_completion = None
        self._seconds_after_failure = None
        self._seconds_after_success = None
        self.discriminator = None

        if seconds_after_completion is not None:
            self.seconds_after_completion = seconds_after_completion
        if seconds_after_failure is not None:
            self.seconds_after_failure = seconds_after_failure
        if seconds_after_success is not None:
            self.seconds_after_success = seconds_after_success

    @property
    def seconds_after_completion(self):
        """Gets the seconds_after_completion of this V1alpha1TTLStrategy.  # noqa: E501


        :return: The seconds_after_completion of this V1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_completion

    @seconds_after_completion.setter
    def seconds_after_completion(self, seconds_after_completion):
        """Sets the seconds_after_completion of this V1alpha1TTLStrategy.


        :param seconds_after_completion: The seconds_after_completion of this V1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_completion = seconds_after_completion

    @property
    def seconds_after_failure(self):
        """Gets the seconds_after_failure of this V1alpha1TTLStrategy.  # noqa: E501


        :return: The seconds_after_failure of this V1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_failure

    @seconds_after_failure.setter
    def seconds_after_failure(self, seconds_after_failure):
        """Sets the seconds_after_failure of this V1alpha1TTLStrategy.


        :param seconds_after_failure: The seconds_after_failure of this V1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_failure = seconds_after_failure

    @property
    def seconds_after_success(self):
        """Gets the seconds_after_success of this V1alpha1TTLStrategy.  # noqa: E501


        :return: The seconds_after_success of this V1alpha1TTLStrategy.  # noqa: E501
        :rtype: int
        """
        return self._seconds_after_success

    @seconds_after_success.setter
    def seconds_after_success(self, seconds_after_success):
        """Sets the seconds_after_success of this V1alpha1TTLStrategy.


        :param seconds_after_success: The seconds_after_success of this V1alpha1TTLStrategy.  # noqa: E501
        :type: int
        """

        self._seconds_after_success = seconds_after_success

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
        if not isinstance(other, V1alpha1TTLStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1TTLStrategy):
            return True

        return self.to_dict() != other.to_dict()
