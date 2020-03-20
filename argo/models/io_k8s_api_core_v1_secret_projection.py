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


class kubernetes.client.models.V1SecretProjection(object):
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
        'items': 'list[kubernetes.client.models.V1KeyToPath]',
        'local_object_reference': 'kubernetes.client.models.V1LocalObjectReference',
        'optional': 'bool'
    }

    attribute_map = {
        'items': 'items',
        'local_object_reference': 'localObjectReference',
        'optional': 'optional'
    }

    def __init__(self, items=None, local_object_reference=None, optional=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1SecretProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._local_object_reference = None
        self._optional = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if local_object_reference is not None:
            self.local_object_reference = local_object_reference
        if optional is not None:
            self.optional = optional

    @property
    def items(self):
        """Gets the items of this kubernetes.client.models.V1SecretProjection.  # noqa: E501


        :return: The items of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1KeyToPath]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this kubernetes.client.models.V1SecretProjection.


        :param items: The items of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :type: list[kubernetes.client.models.V1KeyToPath]
        """

        self._items = items

    @property
    def local_object_reference(self):
        """Gets the local_object_reference of this kubernetes.client.models.V1SecretProjection.  # noqa: E501


        :return: The local_object_reference of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :rtype: kubernetes.client.models.V1LocalObjectReference
        """
        return self._local_object_reference

    @local_object_reference.setter
    def local_object_reference(self, local_object_reference):
        """Sets the local_object_reference of this kubernetes.client.models.V1SecretProjection.


        :param local_object_reference: The local_object_reference of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :type: kubernetes.client.models.V1LocalObjectReference
        """

        self._local_object_reference = local_object_reference

    @property
    def optional(self):
        """Gets the optional of this kubernetes.client.models.V1SecretProjection.  # noqa: E501


        :return: The optional of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this kubernetes.client.models.V1SecretProjection.


        :param optional: The optional of this kubernetes.client.models.V1SecretProjection.  # noqa: E501
        :type: bool
        """

        self._optional = optional

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
        if not isinstance(other, kubernetes.client.models.V1SecretProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1SecretProjection):
            return True

        return self.to_dict() != other.to_dict()
