# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class kubernetes.client.models.V1GitRepoVolumeSource(object):
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
        'directory': 'str',
        'repository': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'repository': 'repository',
        'revision': 'revision'
    }

    def __init__(self, directory=None, repository=None, revision=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1GitRepoVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._directory = None
        self._repository = None
        self._revision = None
        self.discriminator = None

        if directory is not None:
            self.directory = directory
        if repository is not None:
            self.repository = repository
        if revision is not None:
            self.revision = revision

    @property
    def directory(self):
        """Gets the directory of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501


        :return: The directory of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this kubernetes.client.models.V1GitRepoVolumeSource.


        :param directory: The directory of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def repository(self):
        """Gets the repository of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501


        :return: The repository of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this kubernetes.client.models.V1GitRepoVolumeSource.


        :param repository: The repository of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def revision(self):
        """Gets the revision of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501


        :return: The revision of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this kubernetes.client.models.V1GitRepoVolumeSource.


        :param revision: The revision of this kubernetes.client.models.V1GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._revision = revision

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
        if not isinstance(other, kubernetes.client.models.V1GitRepoVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1GitRepoVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
