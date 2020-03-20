# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class V1alpha1CronWorkflowSpec(object):
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
        'concurrency_policy': 'str',
        'failed_jobs_history_limit': 'int',
        'schedule': 'str',
        'starting_deadline_seconds': 'int',
        'successful_jobs_history_limit': 'int',
        'suspend': 'bool',
        'timezone': 'str',
        'workflow_spec': 'V1alpha1WorkflowSpec'
    }

    attribute_map = {
        'concurrency_policy': 'concurrencyPolicy',
        'failed_jobs_history_limit': 'failedJobsHistoryLimit',
        'schedule': 'schedule',
        'starting_deadline_seconds': 'startingDeadlineSeconds',
        'successful_jobs_history_limit': 'successfulJobsHistoryLimit',
        'suspend': 'suspend',
        'timezone': 'timezone',
        'workflow_spec': 'workflowSpec'
    }

    def __init__(self, concurrency_policy=None, failed_jobs_history_limit=None, schedule=None, starting_deadline_seconds=None, successful_jobs_history_limit=None, suspend=None, timezone=None, workflow_spec=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CronWorkflowSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._concurrency_policy = None
        self._failed_jobs_history_limit = None
        self._schedule = None
        self._starting_deadline_seconds = None
        self._successful_jobs_history_limit = None
        self._suspend = None
        self._timezone = None
        self._workflow_spec = None
        self.discriminator = None

        if concurrency_policy is not None:
            self.concurrency_policy = concurrency_policy
        if failed_jobs_history_limit is not None:
            self.failed_jobs_history_limit = failed_jobs_history_limit
        self.schedule = schedule
        if starting_deadline_seconds is not None:
            self.starting_deadline_seconds = starting_deadline_seconds
        if successful_jobs_history_limit is not None:
            self.successful_jobs_history_limit = successful_jobs_history_limit
        if suspend is not None:
            self.suspend = suspend
        if timezone is not None:
            self.timezone = timezone
        self.workflow_spec = workflow_spec

    @property
    def concurrency_policy(self):
        """Gets the concurrency_policy of this V1alpha1CronWorkflowSpec.  # noqa: E501

        ConcurrencyPolicy is the K8s-style concurrency policy that will be used  # noqa: E501

        :return: The concurrency_policy of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_policy

    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy):
        """Sets the concurrency_policy of this V1alpha1CronWorkflowSpec.

        ConcurrencyPolicy is the K8s-style concurrency policy that will be used  # noqa: E501

        :param concurrency_policy: The concurrency_policy of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: str
        """

        self._concurrency_policy = concurrency_policy

    @property
    def failed_jobs_history_limit(self):
        """Gets the failed_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501

        FailedJobsHistoryLimit is the number of successful jobs to be kept at a time  # noqa: E501

        :return: The failed_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._failed_jobs_history_limit

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit):
        """Sets the failed_jobs_history_limit of this V1alpha1CronWorkflowSpec.

        FailedJobsHistoryLimit is the number of successful jobs to be kept at a time  # noqa: E501

        :param failed_jobs_history_limit: The failed_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: int
        """

        self._failed_jobs_history_limit = failed_jobs_history_limit

    @property
    def schedule(self):
        """Gets the schedule of this V1alpha1CronWorkflowSpec.  # noqa: E501

        Schedule is a schedule to run the Workflow in Cron format  # noqa: E501

        :return: The schedule of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this V1alpha1CronWorkflowSpec.

        Schedule is a schedule to run the Workflow in Cron format  # noqa: E501

        :param schedule: The schedule of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def starting_deadline_seconds(self):
        """Gets the starting_deadline_seconds of this V1alpha1CronWorkflowSpec.  # noqa: E501

        StartingDeadlineSeconds is the K8s-style deadline that will limit the time a CronWorkflow will be run after its original scheduled time if it is missed.  # noqa: E501

        :return: The starting_deadline_seconds of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._starting_deadline_seconds

    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds):
        """Sets the starting_deadline_seconds of this V1alpha1CronWorkflowSpec.

        StartingDeadlineSeconds is the K8s-style deadline that will limit the time a CronWorkflow will be run after its original scheduled time if it is missed.  # noqa: E501

        :param starting_deadline_seconds: The starting_deadline_seconds of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: int
        """

        self._starting_deadline_seconds = starting_deadline_seconds

    @property
    def successful_jobs_history_limit(self):
        """Gets the successful_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501

        SuccessfulJobsHistoryLimit is the number of successful jobs to be kept at a time  # noqa: E501

        :return: The successful_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._successful_jobs_history_limit

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit):
        """Sets the successful_jobs_history_limit of this V1alpha1CronWorkflowSpec.

        SuccessfulJobsHistoryLimit is the number of successful jobs to be kept at a time  # noqa: E501

        :param successful_jobs_history_limit: The successful_jobs_history_limit of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: int
        """

        self._successful_jobs_history_limit = successful_jobs_history_limit

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1CronWorkflowSpec.  # noqa: E501

        Suspend is a flag that will stop new CronWorkflows from running if set to true  # noqa: E501

        :return: The suspend of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1CronWorkflowSpec.

        Suspend is a flag that will stop new CronWorkflows from running if set to true  # noqa: E501

        :param suspend: The suspend of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._suspend = suspend

    @property
    def timezone(self):
        """Gets the timezone of this V1alpha1CronWorkflowSpec.  # noqa: E501

        Timezone is the timezone against which the cron schedule will be calculated, e.g. \"Asia/Tokyo\". Default is machine's local time.  # noqa: E501

        :return: The timezone of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this V1alpha1CronWorkflowSpec.

        Timezone is the timezone against which the cron schedule will be calculated, e.g. \"Asia/Tokyo\". Default is machine's local time.  # noqa: E501

        :param timezone: The timezone of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def workflow_spec(self):
        """Gets the workflow_spec of this V1alpha1CronWorkflowSpec.  # noqa: E501


        :return: The workflow_spec of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :rtype: V1alpha1WorkflowSpec
        """
        return self._workflow_spec

    @workflow_spec.setter
    def workflow_spec(self, workflow_spec):
        """Sets the workflow_spec of this V1alpha1CronWorkflowSpec.


        :param workflow_spec: The workflow_spec of this V1alpha1CronWorkflowSpec.  # noqa: E501
        :type: V1alpha1WorkflowSpec
        """
        if self.local_vars_configuration.client_side_validation and workflow_spec is None:  # noqa: E501
            raise ValueError("Invalid value for `workflow_spec`, must not be `None`")  # noqa: E501

        self._workflow_spec = workflow_spec

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
        if not isinstance(other, V1alpha1CronWorkflowSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CronWorkflowSpec):
            return True

        return self.to_dict() != other.to_dict()
