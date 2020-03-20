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


class V1alpha1OSSBucket(object):
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
        'access_key_secret': 'kubernetes.client.models.V1SecretKeySelector',
        'bucket': 'str',
        'endpoint': 'str',
        'secret_key_secret': 'kubernetes.client.models.V1SecretKeySelector'
    }

    attribute_map = {
        'access_key_secret': 'accessKeySecret',
        'bucket': 'bucket',
        'endpoint': 'endpoint',
        'secret_key_secret': 'secretKeySecret'
    }

    def __init__(self, access_key_secret=None, bucket=None, endpoint=None, secret_key_secret=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1OSSBucket - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_secret = None
        self._bucket = None
        self._endpoint = None
        self._secret_key_secret = None
        self.discriminator = None

        if access_key_secret is not None:
            self.access_key_secret = access_key_secret
        if bucket is not None:
            self.bucket = bucket
        if endpoint is not None:
            self.endpoint = endpoint
        if secret_key_secret is not None:
            self.secret_key_secret = secret_key_secret

    @property
    def access_key_secret(self):
        """Gets the access_key_secret of this V1alpha1OSSBucket.  # noqa: E501


        :return: The access_key_secret of this V1alpha1OSSBucket.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecretKeySelector
        """
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, access_key_secret):
        """Sets the access_key_secret of this V1alpha1OSSBucket.


        :param access_key_secret: The access_key_secret of this V1alpha1OSSBucket.  # noqa: E501
        :type: kubernetes.client.models.V1SecretKeySelector
        """

        self._access_key_secret = access_key_secret

    @property
    def bucket(self):
        """Gets the bucket of this V1alpha1OSSBucket.  # noqa: E501


        :return: The bucket of this V1alpha1OSSBucket.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this V1alpha1OSSBucket.


        :param bucket: The bucket of this V1alpha1OSSBucket.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def endpoint(self):
        """Gets the endpoint of this V1alpha1OSSBucket.  # noqa: E501


        :return: The endpoint of this V1alpha1OSSBucket.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this V1alpha1OSSBucket.


        :param endpoint: The endpoint of this V1alpha1OSSBucket.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def secret_key_secret(self):
        """Gets the secret_key_secret of this V1alpha1OSSBucket.  # noqa: E501


        :return: The secret_key_secret of this V1alpha1OSSBucket.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecretKeySelector
        """
        return self._secret_key_secret

    @secret_key_secret.setter
    def secret_key_secret(self, secret_key_secret):
        """Sets the secret_key_secret of this V1alpha1OSSBucket.


        :param secret_key_secret: The secret_key_secret of this V1alpha1OSSBucket.  # noqa: E501
        :type: kubernetes.client.models.V1SecretKeySelector
        """

        self._secret_key_secret = secret_key_secret

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
        if not isinstance(other, V1alpha1OSSBucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1OSSBucket):
            return True

        return self.to_dict() != other.to_dict()
