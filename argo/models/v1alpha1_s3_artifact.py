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


class V1alpha1S3Artifact(object):
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
        'key': 'str',
        's3_bucket': 'V1alpha1S3Bucket'
    }

    attribute_map = {
        'key': 'key',
        's3_bucket': 's3Bucket'
    }

    def __init__(self, key=None, s3_bucket=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1S3Artifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._s3_bucket = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if s3_bucket is not None:
            self.s3_bucket = s3_bucket

    @property
    def key(self):
        """Gets the key of this V1alpha1S3Artifact.  # noqa: E501


        :return: The key of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1alpha1S3Artifact.


        :param key: The key of this V1alpha1S3Artifact.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def s3_bucket(self):
        """Gets the s3_bucket of this V1alpha1S3Artifact.  # noqa: E501


        :return: The s3_bucket of this V1alpha1S3Artifact.  # noqa: E501
        :rtype: V1alpha1S3Bucket
        """
        return self._s3_bucket

    @s3_bucket.setter
    def s3_bucket(self, s3_bucket):
        """Sets the s3_bucket of this V1alpha1S3Artifact.


        :param s3_bucket: The s3_bucket of this V1alpha1S3Artifact.  # noqa: E501
        :type: V1alpha1S3Bucket
        """

        self._s3_bucket = s3_bucket

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
        if not isinstance(other, V1alpha1S3Artifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1S3Artifact):
            return True

        return self.to_dict() != other.to_dict()
