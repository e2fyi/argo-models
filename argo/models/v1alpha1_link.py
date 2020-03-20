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


class V1alpha1Link(object):
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
        'name': 'str',
        'scope': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'scope': 'scope',
        'url': 'url'
    }

    def __init__(self, name=None, scope=None, url=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Link - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._scope = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if scope is not None:
            self.scope = scope
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this V1alpha1Link.  # noqa: E501


        :return: The name of this V1alpha1Link.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Link.


        :param name: The name of this V1alpha1Link.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def scope(self):
        """Gets the scope of this V1alpha1Link.  # noqa: E501


        :return: The scope of this V1alpha1Link.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this V1alpha1Link.


        :param scope: The scope of this V1alpha1Link.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def url(self):
        """Gets the url of this V1alpha1Link.  # noqa: E501

        The URL. May contain \"${metadata.namespace}\" and \"${metadata.name}\".  # noqa: E501

        :return: The url of this V1alpha1Link.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1Link.

        The URL. May contain \"${metadata.namespace}\" and \"${metadata.name}\".  # noqa: E501

        :param url: The url of this V1alpha1Link.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, V1alpha1Link):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Link):
            return True

        return self.to_dict() != other.to_dict()