# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class kubernetes.client.models.V1DownwardAPIVolumeFile(object):
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
        'field_ref': 'kubernetes.client.models.V1ObjectFieldSelector',
        'mode': 'int',
        'path': 'str',
        'resource_field_ref': 'kubernetes.client.models.V1ResourceFieldSelector'
    }

    attribute_map = {
        'field_ref': 'fieldRef',
        'mode': 'mode',
        'path': 'path',
        'resource_field_ref': 'resourceFieldRef'
    }

    def __init__(self, field_ref=None, mode=None, path=None, resource_field_ref=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1DownwardAPIVolumeFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_ref = None
        self._mode = None
        self._path = None
        self._resource_field_ref = None
        self.discriminator = None

        if field_ref is not None:
            self.field_ref = field_ref
        if mode is not None:
            self.mode = mode
        if path is not None:
            self.path = path
        if resource_field_ref is not None:
            self.resource_field_ref = resource_field_ref

    @property
    def field_ref(self):
        """Gets the field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: kubernetes.client.models.V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """Sets the field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.


        :param field_ref: The field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :type: kubernetes.client.models.V1ObjectFieldSelector
        """

        self._field_ref = field_ref

    @property
    def mode(self):
        """Gets the mode of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The mode of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this kubernetes.client.models.V1DownwardAPIVolumeFile.


        :param mode: The mode of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :type: int
        """

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The path of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this kubernetes.client.models.V1DownwardAPIVolumeFile.


        :param path: The path of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def resource_field_ref(self):
        """Gets the resource_field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The resource_field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: kubernetes.client.models.V1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """Sets the resource_field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.


        :param resource_field_ref: The resource_field_ref of this kubernetes.client.models.V1DownwardAPIVolumeFile.  # noqa: E501
        :type: kubernetes.client.models.V1ResourceFieldSelector
        """

        self._resource_field_ref = resource_field_ref

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
        if not isinstance(other, kubernetes.client.models.V1DownwardAPIVolumeFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1DownwardAPIVolumeFile):
            return True

        return self.to_dict() != other.to_dict()
