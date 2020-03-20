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


class kubernetes.client.models.V1LabelSelectorRequirement(object):
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
        'key': 'str',
        'operator': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, key=None, operator=None, values=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1LabelSelectorRequirement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._operator = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501


        :return: The key of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this kubernetes.client.models.V1LabelSelectorRequirement.


        :param key: The key of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def operator(self):
        """Gets the operator of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.  # noqa: E501

        :return: The operator of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this kubernetes.client.models.V1LabelSelectorRequirement.

        operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.  # noqa: E501

        :param operator: The operator of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def values(self):
        """Gets the values of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501


        :return: The values of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this kubernetes.client.models.V1LabelSelectorRequirement.


        :param values: The values of this kubernetes.client.models.V1LabelSelectorRequirement.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if not isinstance(other, kubernetes.client.models.V1LabelSelectorRequirement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1LabelSelectorRequirement):
            return True

        return self.to_dict() != other.to_dict()
