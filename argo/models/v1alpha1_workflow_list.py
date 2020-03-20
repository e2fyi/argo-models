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


class V1alpha1WorkflowList(object):
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
        'items': 'list[V1alpha1Workflow]',
        'metadata': 'kubernetes.client.models.V1ListMeta'
    }

    attribute_map = {
        'items': 'items',
        'metadata': 'metadata'
    }

    def __init__(self, items=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1WorkflowList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._metadata = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if metadata is not None:
            self.metadata = metadata

    @property
    def items(self):
        """Gets the items of this V1alpha1WorkflowList.  # noqa: E501


        :return: The items of this V1alpha1WorkflowList.  # noqa: E501
        :rtype: list[V1alpha1Workflow]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this V1alpha1WorkflowList.


        :param items: The items of this V1alpha1WorkflowList.  # noqa: E501
        :type: list[V1alpha1Workflow]
        """

        self._items = items

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1WorkflowList.  # noqa: E501


        :return: The metadata of this V1alpha1WorkflowList.  # noqa: E501
        :rtype: kubernetes.client.models.V1ListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1WorkflowList.


        :param metadata: The metadata of this V1alpha1WorkflowList.  # noqa: E501
        :type: kubernetes.client.models.V1ListMeta
        """

        self._metadata = metadata

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
        if not isinstance(other, V1alpha1WorkflowList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1WorkflowList):
            return True

        return self.to_dict() != other.to_dict()
