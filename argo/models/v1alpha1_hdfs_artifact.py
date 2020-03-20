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


class V1alpha1HDFSArtifact(object):
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
        'force': 'bool',
        'h_dfs_config': 'V1alpha1HDFSConfig',
        'path': 'str'
    }

    attribute_map = {
        'force': 'force',
        'h_dfs_config': 'hDFSConfig',
        'path': 'path'
    }

    def __init__(self, force=None, h_dfs_config=None, path=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1HDFSArtifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._force = None
        self._h_dfs_config = None
        self._path = None
        self.discriminator = None

        if force is not None:
            self.force = force
        if h_dfs_config is not None:
            self.h_dfs_config = h_dfs_config
        if path is not None:
            self.path = path

    @property
    def force(self):
        """Gets the force of this V1alpha1HDFSArtifact.  # noqa: E501


        :return: The force of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this V1alpha1HDFSArtifact.


        :param force: The force of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def h_dfs_config(self):
        """Gets the h_dfs_config of this V1alpha1HDFSArtifact.  # noqa: E501


        :return: The h_dfs_config of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: V1alpha1HDFSConfig
        """
        return self._h_dfs_config

    @h_dfs_config.setter
    def h_dfs_config(self, h_dfs_config):
        """Sets the h_dfs_config of this V1alpha1HDFSArtifact.


        :param h_dfs_config: The h_dfs_config of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: V1alpha1HDFSConfig
        """

        self._h_dfs_config = h_dfs_config

    @property
    def path(self):
        """Gets the path of this V1alpha1HDFSArtifact.  # noqa: E501


        :return: The path of this V1alpha1HDFSArtifact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1HDFSArtifact.


        :param path: The path of this V1alpha1HDFSArtifact.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if not isinstance(other, V1alpha1HDFSArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1HDFSArtifact):
            return True

        return self.to_dict() != other.to_dict()
