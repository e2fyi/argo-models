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


class kubernetes.client.models.V1IntOrString(object):
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
        'int_val': 'int',
        'str_val': 'str',
        'type': 'str'
    }

    attribute_map = {
        'int_val': 'intVal',
        'str_val': 'strVal',
        'type': 'type'
    }

    def __init__(self, int_val=None, str_val=None, type=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1IntOrString - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._int_val = None
        self._str_val = None
        self._type = None
        self.discriminator = None

        if int_val is not None:
            self.int_val = int_val
        if str_val is not None:
            self.str_val = str_val
        if type is not None:
            self.type = type

    @property
    def int_val(self):
        """Gets the int_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501


        :return: The int_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :rtype: int
        """
        return self._int_val

    @int_val.setter
    def int_val(self, int_val):
        """Sets the int_val of this kubernetes.client.models.V1IntOrString.


        :param int_val: The int_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :type: int
        """

        self._int_val = int_val

    @property
    def str_val(self):
        """Gets the str_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501


        :return: The str_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :rtype: str
        """
        return self._str_val

    @str_val.setter
    def str_val(self, str_val):
        """Sets the str_val of this kubernetes.client.models.V1IntOrString.


        :param str_val: The str_val of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :type: str
        """

        self._str_val = str_val

    @property
    def type(self):
        """Gets the type of this kubernetes.client.models.V1IntOrString.  # noqa: E501


        :return: The type of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this kubernetes.client.models.V1IntOrString.


        :param type: The type of this kubernetes.client.models.V1IntOrString.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, kubernetes.client.models.V1IntOrString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1IntOrString):
            return True

        return self.to_dict() != other.to_dict()
