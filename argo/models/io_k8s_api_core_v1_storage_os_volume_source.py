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


class kubernetes.client.models.V1StorageOSVolumeSource(object):
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
        'fs_type': 'str',
        'read_only': 'bool',
        'secret_ref': 'kubernetes.client.models.V1LocalObjectReference',
        'volume_name': 'str',
        'volume_namespace': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'volume_name': 'volumeName',
        'volume_namespace': 'volumeNamespace'
    }

    def __init__(self, fs_type=None, read_only=None, secret_ref=None, volume_name=None, volume_namespace=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1StorageOSVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._read_only = None
        self._secret_ref = None
        self._volume_name = None
        self._volume_namespace = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_namespace is not None:
            self.volume_namespace = volume_namespace

    @property
    def fs_type(self):
        """Gets the fs_type of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501


        :return: The fs_type of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this kubernetes.client.models.V1StorageOSVolumeSource.


        :param fs_type: The fs_type of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def read_only(self):
        """Gets the read_only of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501


        :return: The read_only of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this kubernetes.client.models.V1StorageOSVolumeSource.


        :param read_only: The read_only of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501


        :return: The secret_ref of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :rtype: kubernetes.client.models.V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this kubernetes.client.models.V1StorageOSVolumeSource.


        :param secret_ref: The secret_ref of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :type: kubernetes.client.models.V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def volume_name(self):
        """Gets the volume_name of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501

        VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.  # noqa: E501

        :return: The volume_name of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this kubernetes.client.models.V1StorageOSVolumeSource.

        VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.  # noqa: E501

        :param volume_name: The volume_name of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_namespace(self):
        """Gets the volume_namespace of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501


        :return: The volume_namespace of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_namespace

    @volume_namespace.setter
    def volume_namespace(self, volume_namespace):
        """Sets the volume_namespace of this kubernetes.client.models.V1StorageOSVolumeSource.


        :param volume_namespace: The volume_namespace of this kubernetes.client.models.V1StorageOSVolumeSource.  # noqa: E501
        :type: str
        """

        self._volume_namespace = volume_namespace

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
        if not isinstance(other, kubernetes.client.models.V1StorageOSVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1StorageOSVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
