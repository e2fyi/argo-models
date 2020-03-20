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


class kubernetes.client.models.V1ServiceAccountTokenProjection(object):
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
        'audience': 'str',
        'expiration_seconds': 'str',
        'path': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'expiration_seconds': 'expirationSeconds',
        'path': 'path'
    }

    def __init__(self, audience=None, expiration_seconds=None, path=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1ServiceAccountTokenProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience = None
        self._expiration_seconds = None
        self._path = None
        self.discriminator = None

        if audience is not None:
            self.audience = audience
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds
        if path is not None:
            self.path = path

    @property
    def audience(self):
        """Gets the audience of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501


        :return: The audience of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this kubernetes.client.models.V1ServiceAccountTokenProjection.


        :param audience: The audience of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501


        :return: The expiration_seconds of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: str
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this kubernetes.client.models.V1ServiceAccountTokenProjection.


        :param expiration_seconds: The expiration_seconds of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
        :type: str
        """

        self._expiration_seconds = expiration_seconds

    @property
    def path(self):
        """Gets the path of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :return: The path of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this kubernetes.client.models.V1ServiceAccountTokenProjection.

        Path is the path relative to the mount point of the file to project the token into.  # noqa: E501

        :param path: The path of this kubernetes.client.models.V1ServiceAccountTokenProjection.  # noqa: E501
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
        if not isinstance(other, kubernetes.client.models.V1ServiceAccountTokenProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1ServiceAccountTokenProjection):
            return True

        return self.to_dict() != other.to_dict()
