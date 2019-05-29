# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v2.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


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
        'success_condition': 'str'
    }

    attribute_map = {
        'action': 'action',
        'failure_condition': 'failureCondition',
        'manifest': 'manifest',
        'merge_strategy': 'mergeStrategy',
        'success_condition': 'successCondition'
    }

    def __init__(self, action=None, failure_condition=None, manifest=None, merge_strategy=None, success_condition=None):  # noqa: E501
        """V1alpha1ResourceTemplate - a model defined in OpenAPI"""  # noqa: E501

        self._action = None
        self._failure_condition = None
        self._manifest = None
        self._merge_strategy = None
        self._success_condition = None
        self.discriminator = None

        self.action = action
        if failure_condition is not None:
            self.failure_condition = failure_condition
        self.manifest = manifest
        if merge_strategy is not None:
            self.merge_strategy = merge_strategy
        if success_condition is not None:
            self.success_condition = success_condition

    @property
    def action(self):
        """Gets the action of this V1alpha1ResourceTemplate.  # noqa: E501

        Action is the action to perform to the resource. Must be one of: get, create, apply, delete, replace  # noqa: E501

        :return: The action of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1alpha1ResourceTemplate.

        Action is the action to perform to the resource. Must be one of: get, create, apply, delete, replace  # noqa: E501

        :param action: The action of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def failure_condition(self):
        """Gets the failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501

        FailureCondition is a label selector expression which describes the conditions of the k8s resource in which the step was considered failed  # noqa: E501

        :return: The failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._failure_condition

    @failure_condition.setter
    def failure_condition(self, failure_condition):
        """Sets the failure_condition of this V1alpha1ResourceTemplate.

        FailureCondition is a label selector expression which describes the conditions of the k8s resource in which the step was considered failed  # noqa: E501

        :param failure_condition: The failure_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._failure_condition = failure_condition

    @property
    def manifest(self):
        """Gets the manifest of this V1alpha1ResourceTemplate.  # noqa: E501

        Manifest contains the kubernetes manifest  # noqa: E501

        :return: The manifest of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this V1alpha1ResourceTemplate.

        Manifest contains the kubernetes manifest  # noqa: E501

        :param manifest: The manifest of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """
        if manifest is None:
            raise ValueError("Invalid value for `manifest`, must not be `None`")  # noqa: E501

        self._manifest = manifest

    @property
    def merge_strategy(self):
        """Gets the merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501

        MergeStrategy is the strategy used to merge a patch. It defaults to \"strategic\" Must be one of: strategic, merge, json  # noqa: E501

        :return: The merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._merge_strategy

    @merge_strategy.setter
    def merge_strategy(self, merge_strategy):
        """Sets the merge_strategy of this V1alpha1ResourceTemplate.

        MergeStrategy is the strategy used to merge a patch. It defaults to \"strategic\" Must be one of: strategic, merge, json  # noqa: E501

        :param merge_strategy: The merge_strategy of this V1alpha1ResourceTemplate.  # noqa: E501
        :type: str
        """

        self._merge_strategy = merge_strategy

    @property
    def success_condition(self):
        """Gets the success_condition of this V1alpha1ResourceTemplate.  # noqa: E501

        SuccessCondition is a label selector expression which describes the conditions of the k8s resource in which it is acceptable to proceed to the following step  # noqa: E501

        :return: The success_condition of this V1alpha1ResourceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._success_condition

    @success_condition.setter
    def success_condition(self, success_condition):
        """Sets the success_condition of this V1alpha1ResourceTemplate.

        SuccessCondition is a label selector expression which describes the conditions of the k8s resource in which it is acceptable to proceed to the following step  # noqa: E501

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
