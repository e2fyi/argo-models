# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1WorkflowTemplateSpec(object):
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
        'arguments': 'V1alpha1Arguments',
        'templates': 'list[V1alpha1Template]'
    }

    attribute_map = {
        'arguments': 'arguments',
        'templates': 'templates'
    }

    def __init__(self, arguments=None, templates=None):  # noqa: E501
        """V1alpha1WorkflowTemplateSpec - a model defined in OpenAPI"""  # noqa: E501

        self._arguments = None
        self._templates = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        self.templates = templates

    @property
    def arguments(self):
        """Gets the arguments of this V1alpha1WorkflowTemplateSpec.  # noqa: E501


        :return: The arguments of this V1alpha1WorkflowTemplateSpec.  # noqa: E501
        :rtype: V1alpha1Arguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this V1alpha1WorkflowTemplateSpec.


        :param arguments: The arguments of this V1alpha1WorkflowTemplateSpec.  # noqa: E501
        :type: V1alpha1Arguments
        """

        self._arguments = arguments

    @property
    def templates(self):
        """Gets the templates of this V1alpha1WorkflowTemplateSpec.  # noqa: E501

        Templates is a list of workflow templates.  # noqa: E501

        :return: The templates of this V1alpha1WorkflowTemplateSpec.  # noqa: E501
        :rtype: list[V1alpha1Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this V1alpha1WorkflowTemplateSpec.

        Templates is a list of workflow templates.  # noqa: E501

        :param templates: The templates of this V1alpha1WorkflowTemplateSpec.  # noqa: E501
        :type: list[V1alpha1Template]
        """
        if templates is None:
            raise ValueError("Invalid value for `templates`, must not be `None`")  # noqa: E501

        self._templates = templates

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
        if not isinstance(other, V1alpha1WorkflowTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
