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


class V1alpha1ResourceTemplate(object):
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
        'action': 'str',
        'failure_condition': 'str',
        'manifest': 'str',
        'merge_strategy': 'str',
        'set_owner_reference': 'bool',
        'success_condition': 'str'
    }

    attribute_map = {
        'action': 'action',
        'failure_condition': 'failureCondition',
        'manifest': 'manifest',
        'merge_strategy': 'mergeStrategy',
        'set_owner_reference': 'setOwnerReference',
        'success_condition': 'successCondition'
    }

    def __init__(self, action=None, failure_condition=None, manifest=None, merge_strategy=None, set_owner_reference=None, success_condition=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ResourceTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._failure_condition = None
        self._manifest = None
        self._merge_strategy = None
        self._set_owner_reference = None
        self._success_condition = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if failure_condition is not None:
            self.failure_condition = failure_condition
        if manifest is not None:
            self.manifest = manifest
        if merge_strategy is not None:
            self.merge_strategy = merge_strategy
        if set_owner_reference is not None:
            self.set_owner_reference = set_owner_reference
        if success_condition is not None:
            self.success_condition = success_condition

    @property
    def action(self):
        """Gets the action of this V1alpha1ResourceTemplate.  # noqa: E501


        :return: The action of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1alpha1ResourceTemplate.


        :param action: The action of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def failure_condition(self):
        """Gets the failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501


        :return: The failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._failure_condition

    @failure_condition.setter
    def failure_condition(self, failure_condition):
        """Sets the failure_condition of this V1alpha1ResourceTemplate.


        :param failure_condition: The failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._failure_condition = failure_condition

    @property
    def manifest(self):
        """Gets the manifest of this V1alpha1ResourceTemplate.  # noqa: E501


        :return: The manifest of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this V1alpha1ResourceTemplate.


        :param manifest: The manifest of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

    @property
    def merge_strategy(self):
        """Gets the merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501


        :return: The merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._merge_strategy

    @merge_strategy.setter
    def merge_strategy(self, merge_strategy):
        """Sets the merge_strategy of this V1alpha1ResourceTemplate.


        :param merge_strategy: The merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._merge_strategy = merge_strategy

    @property
    def set_owner_reference(self):
        """Gets the set_owner_reference of this V1alpha1ResourceTemplate.  # noqa: E501

        SetOwnerReference sets the reference to the workflow on the OwnerReference of generated resource.  # noqa: E501

        :return: The set_owner_reference of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._set_owner_reference

    @set_owner_reference.setter
    def set_owner_reference(self, set_owner_reference):
        """Sets the set_owner_reference of this V1alpha1ResourceTemplate.

        SetOwnerReference sets the reference to the workflow on the OwnerReference of generated resource.  # noqa: E501

        :param set_owner_reference: The set_owner_reference of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: bool
        """

        self._set_owner_reference = set_owner_reference

    @property
    def success_condition(self):
        """Gets the success_condition of this V1alpha1ResourceTemplate.  # noqa: E501


        :return: The success_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._success_condition

    @success_condition.setter
    def success_condition(self, success_condition):
        """Sets the success_condition of this V1alpha1ResourceTemplate.


        :param success_condition: The success_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._success_condition = success_condition

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
        if not isinstance(other, V1alpha1ResourceTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ResourceTemplate):
            return True

        return self.to_dict() != other.to_dict()
