# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class kubernetes.client.models.V1ResourceFieldSelector(object):
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
        'container_name': 'str',
        'divisor': 'kubernetes.client.models.V1Quantity',
        'resource': 'str'
    }

    attribute_map = {
        'container_name': 'containerName',
        'divisor': 'divisor',
        'resource': 'resource'
    }

    def __init__(self, container_name=None, divisor=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1ResourceFieldSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_name = None
        self._divisor = None
        self._resource = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if divisor is not None:
            self.divisor = divisor
        if resource is not None:
            self.resource = resource

    @property
    def container_name(self):
        """Gets the container_name of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501


        :return: The container_name of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this kubernetes.client.models.V1ResourceFieldSelector.


        :param container_name: The container_name of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

    @property
    def divisor(self):
        """Gets the divisor of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501


        :return: The divisor of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :rtype: kubernetes.client.models.V1Quantity
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        """Sets the divisor of this kubernetes.client.models.V1ResourceFieldSelector.


        :param divisor: The divisor of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :type: kubernetes.client.models.V1Quantity
        """

        self._divisor = divisor

    @property
    def resource(self):
        """Gets the resource of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501


        :return: The resource of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this kubernetes.client.models.V1ResourceFieldSelector.


        :param resource: The resource of this kubernetes.client.models.V1ResourceFieldSelector.  # noqa: E501
        :type: str
        """

        self._resource = resource

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
        if not isinstance(other, kubernetes.client.models.V1ResourceFieldSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1ResourceFieldSelector):
            return True

        return self.to_dict() != other.to_dict()
