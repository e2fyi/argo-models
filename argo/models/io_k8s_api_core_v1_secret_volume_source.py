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


class kubernetes.client.models.V1SecretVolumeSource(object):
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
        'default_mode': 'int',
        'items': 'list[kubernetes.client.models.V1KeyToPath]',
        'optional': 'bool',
        'secret_name': 'str'
    }

    attribute_map = {
        'default_mode': 'defaultMode',
        'items': 'items',
        'optional': 'optional',
        'secret_name': 'secretName'
    }

    def __init__(self, default_mode=None, items=None, optional=None, secret_name=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1SecretVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_mode = None
        self._items = None
        self._optional = None
        self._secret_name = None
        self.discriminator = None

        if default_mode is not None:
            self.default_mode = default_mode
        if items is not None:
            self.items = items
        if optional is not None:
            self.optional = optional
        if secret_name is not None:
            self.secret_name = secret_name

    @property
    def default_mode(self):
        """Gets the default_mode of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501


        :return: The default_mode of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """Sets the default_mode of this kubernetes.client.models.V1SecretVolumeSource.


        :param default_mode: The default_mode of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :type: int
        """

        self._default_mode = default_mode

    @property
    def items(self):
        """Gets the items of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501


        :return: The items of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1KeyToPath]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this kubernetes.client.models.V1SecretVolumeSource.


        :param items: The items of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :type: list[kubernetes.client.models.V1KeyToPath]
        """

        self._items = items

    @property
    def optional(self):
        """Gets the optional of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501


        :return: The optional of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this kubernetes.client.models.V1SecretVolumeSource.


        :param optional: The optional of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    @property
    def secret_name(self):
        """Gets the secret_name of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501


        :return: The secret_name of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this kubernetes.client.models.V1SecretVolumeSource.


        :param secret_name: The secret_name of this kubernetes.client.models.V1SecretVolumeSource.  # noqa: E501
        :type: str
        """

        self._secret_name = secret_name

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
        if not isinstance(other, kubernetes.client.models.V1SecretVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1SecretVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
