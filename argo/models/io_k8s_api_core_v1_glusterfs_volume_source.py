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


class kubernetes.client.models.V1GlusterfsVolumeSource(object):
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
        'endpoints': 'str',
        'path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'path': 'path',
        'read_only': 'readOnly'
    }

    def __init__(self, endpoints=None, path=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1GlusterfsVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._endpoints = None
        self._path = None
        self._read_only = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if path is not None:
            self.path = path
        if read_only is not None:
            self.read_only = read_only

    @property
    def endpoints(self):
        """Gets the endpoints of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501


        :return: The endpoints of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this kubernetes.client.models.V1GlusterfsVolumeSource.


        :param endpoints: The endpoints of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :type: str
        """

        self._endpoints = endpoints

    @property
    def path(self):
        """Gets the path of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501


        :return: The path of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this kubernetes.client.models.V1GlusterfsVolumeSource.


        :param path: The path of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501


        :return: The read_only of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this kubernetes.client.models.V1GlusterfsVolumeSource.


        :param read_only: The read_only of this kubernetes.client.models.V1GlusterfsVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, kubernetes.client.models.V1GlusterfsVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1GlusterfsVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
