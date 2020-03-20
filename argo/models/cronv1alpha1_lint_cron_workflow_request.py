# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class Cronv1alpha1LintCronWorkflowRequest(object):
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
        'cron_workflow': 'V1alpha1CronWorkflow',
        'namespace': 'str'
    }

    attribute_map = {
        'cron_workflow': 'cronWorkflow',
        'namespace': 'namespace'
    }

    def __init__(self, cron_workflow=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """Cronv1alpha1LintCronWorkflowRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cron_workflow = None
        self._namespace = None
        self.discriminator = None

        if cron_workflow is not None:
            self.cron_workflow = cron_workflow
        if namespace is not None:
            self.namespace = namespace

    @property
    def cron_workflow(self):
        """Gets the cron_workflow of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501


        :return: The cron_workflow of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501
        :rtype: V1alpha1CronWorkflow
        """
        return self._cron_workflow

    @cron_workflow.setter
    def cron_workflow(self, cron_workflow):
        """Sets the cron_workflow of this Cronv1alpha1LintCronWorkflowRequest.


        :param cron_workflow: The cron_workflow of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501
        :type: V1alpha1CronWorkflow
        """

        self._cron_workflow = cron_workflow

    @property
    def namespace(self):
        """Gets the namespace of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501


        :return: The namespace of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Cronv1alpha1LintCronWorkflowRequest.


        :param namespace: The namespace of this Cronv1alpha1LintCronWorkflowRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, Cronv1alpha1LintCronWorkflowRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cronv1alpha1LintCronWorkflowRequest):
            return True

        return self.to_dict() != other.to_dict()
