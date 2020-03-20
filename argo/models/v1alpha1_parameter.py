# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class V1alpha1Parameter(object):
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
        'default': 'str',
        'global_name': 'str',
        'name': 'str',
        'value': 'str',
        'value_from': 'V1alpha1ValueFrom'
    }

    attribute_map = {
        'default': 'default',
        'global_name': 'globalName',
        'name': 'name',
        'value': 'value',
        'value_from': 'valueFrom'
    }

    def __init__(self, default=None, global_name=None, name=None, value=None, value_from=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Parameter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default = None
        self._global_name = None
        self._name = None
        self._value = None
        self._value_from = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if global_name is not None:
            self.global_name = global_name
        self.name = name
        if value is not None:
            self.value = value
        if value_from is not None:
            self.value_from = value_from

    @property
    def default(self):
        """Gets the default of this V1alpha1Parameter.  # noqa: E501

        Default is the default value to use for an input parameter if a value was not supplied  # noqa: E501

        :return: The default of this V1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1alpha1Parameter.

        Default is the default value to use for an input parameter if a value was not supplied  # noqa: E501

        :param default: The default of this V1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def global_name(self):
        """Gets the global_name of this V1alpha1Parameter.  # noqa: E501

        GlobalName exports an output parameter to the global scope, making it available as '{{workflow.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters  # noqa: E501

        :return: The global_name of this V1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._global_name

    @global_name.setter
    def global_name(self, global_name):
        """Sets the global_name of this V1alpha1Parameter.

        GlobalName exports an output parameter to the global scope, making it available as '{{workflow.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters  # noqa: E501

        :param global_name: The global_name of this V1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._global_name = global_name

    @property
    def name(self):
        """Gets the name of this V1alpha1Parameter.  # noqa: E501

        Name is the parameter name  # noqa: E501

        :return: The name of this V1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Parameter.

        Name is the parameter name  # noqa: E501

        :param name: The name of this V1alpha1Parameter.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this V1alpha1Parameter.  # noqa: E501

        Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values  # noqa: E501

        :return: The value of this V1alpha1Parameter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1alpha1Parameter.

        Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values  # noqa: E501

        :param value: The value of this V1alpha1Parameter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_from(self):
        """Gets the value_from of this V1alpha1Parameter.  # noqa: E501


        :return: The value_from of this V1alpha1Parameter.  # noqa: E501
        :rtype: V1alpha1ValueFrom
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this V1alpha1Parameter.


        :param value_from: The value_from of this V1alpha1Parameter.  # noqa: E501
        :type: V1alpha1ValueFrom
        """

        self._value_from = value_from

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
        if not isinstance(other, V1alpha1Parameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Parameter):
            return True

        return self.to_dict() != other.to_dict()
