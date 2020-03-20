# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class kubernetes.client.models.V1PodAffinity(object):
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
        'preferred_during_scheduling_ignored_during_execution': 'list[kubernetes.client.models.V1WeightedPodAffinityTerm]',
        'required_during_scheduling_ignored_during_execution': 'list[kubernetes.client.models.V1PodAffinityTerm]'
    }

    attribute_map = {
        'preferred_during_scheduling_ignored_during_execution': 'preferredDuringSchedulingIgnoredDuringExecution',
        'required_during_scheduling_ignored_during_execution': 'requiredDuringSchedulingIgnoredDuringExecution'
    }

    def __init__(self, preferred_during_scheduling_ignored_during_execution=None, required_during_scheduling_ignored_during_execution=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1PodAffinity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._preferred_during_scheduling_ignored_during_execution = None
        self._required_during_scheduling_ignored_during_execution = None
        self.discriminator = None

        if preferred_during_scheduling_ignored_during_execution is not None:
            self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        """Gets the preferred_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501


        :return: The preferred_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1WeightedPodAffinityTerm]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        """Sets the preferred_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.


        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501
        :type: list[kubernetes.client.models.V1WeightedPodAffinityTerm]
        """

        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @property
    def required_during_scheduling_ignored_during_execution(self):
        """Gets the required_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501


        :return: The required_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1PodAffinityTerm]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        """Sets the required_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.


        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this kubernetes.client.models.V1PodAffinity.  # noqa: E501
        :type: list[kubernetes.client.models.V1PodAffinityTerm]
        """

        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

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
        if not isinstance(other, kubernetes.client.models.V1PodAffinity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1PodAffinity):
            return True

        return self.to_dict() != other.to_dict()
