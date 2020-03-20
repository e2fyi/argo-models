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


class kubernetes.client.models.V1Quantity(object):
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
        'string': 'str'
    }

    attribute_map = {
        'string': 'string'
    }

    def __init__(self, string=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1Quantity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._string = None
        self.discriminator = None

        if string is not None:
            self.string = string

    @property
    def string(self):
        """Gets the string of this kubernetes.client.models.V1Quantity.  # noqa: E501


        :return: The string of this kubernetes.client.models.V1Quantity.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this kubernetes.client.models.V1Quantity.


        :param string: The string of this kubernetes.client.models.V1Quantity.  # noqa: E501
        :type: str
        """

        self._string = string

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
        if not isinstance(other, kubernetes.client.models.V1Quantity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1Quantity):
            return True

        return self.to_dict() != other.to_dict()
