# coding: utf-8

"""
    Argo

    Argo  # noqa: E501

    The version of the OpenAPI document: v2.7.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1WorkflowStatus(object):
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
        'compressed_nodes': 'str',
        'conditions': 'list[V1alpha1WorkflowCondition]',
        'finished_at': 'kubernetes.client.models.V1Time',
        'message': 'str',
        'nodes': 'dict(str, V1alpha1NodeStatus)',
        'offload_node_status_version': 'str',
        'outputs': 'V1alpha1Outputs',
        'persistent_volume_claims': 'list[kubernetes.client.models.V1Volume]',
        'phase': 'str',
        'resources_duration': 'dict(str, str)',
        'started_at': 'kubernetes.client.models.V1Time',
        'stored_templates': 'dict(str, V1alpha1Template)'
    }

    attribute_map = {
        'compressed_nodes': 'compressedNodes',
        'conditions': 'conditions',
        'finished_at': 'finishedAt',
        'message': 'message',
        'nodes': 'nodes',
        'offload_node_status_version': 'offloadNodeStatusVersion',
        'outputs': 'outputs',
        'persistent_volume_claims': 'persistentVolumeClaims',
        'phase': 'phase',
        'resources_duration': 'resourcesDuration',
        'started_at': 'startedAt',
        'stored_templates': 'storedTemplates'
    }

    def __init__(self, compressed_nodes=None, conditions=None, finished_at=None, message=None, nodes=None, offload_node_status_version=None, outputs=None, persistent_volume_claims=None, phase=None, resources_duration=None, started_at=None, stored_templates=None):  # noqa: E501
        """V1alpha1WorkflowStatus - a model defined in OpenAPI"""  # noqa: E501

        self._compressed_nodes = None
        self._conditions = None
        self._finished_at = None
        self._message = None
        self._nodes = None
        self._offload_node_status_version = None
        self._outputs = None
        self._persistent_volume_claims = None
        self._phase = None
        self._resources_duration = None
        self._started_at = None
        self._stored_templates = None
        self.discriminator = None

        if compressed_nodes is not None:
            self.compressed_nodes = compressed_nodes
        if conditions is not None:
            self.conditions = conditions
        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        if nodes is not None:
            self.nodes = nodes
        if offload_node_status_version is not None:
            self.offload_node_status_version = offload_node_status_version
        if outputs is not None:
            self.outputs = outputs
        if persistent_volume_claims is not None:
            self.persistent_volume_claims = persistent_volume_claims
        if phase is not None:
            self.phase = phase
        if resources_duration is not None:
            self.resources_duration = resources_duration
        if started_at is not None:
            self.started_at = started_at
        if stored_templates is not None:
            self.stored_templates = stored_templates

    @property
    def compressed_nodes(self):
        """Gets the compressed_nodes of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The compressed_nodes of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._compressed_nodes

    @compressed_nodes.setter
    def compressed_nodes(self, compressed_nodes):
        """Sets the compressed_nodes of this V1alpha1WorkflowStatus.


        :param compressed_nodes: The compressed_nodes of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._compressed_nodes = compressed_nodes

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The conditions of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: list[V1alpha1WorkflowCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1WorkflowStatus.


        :param conditions: The conditions of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: list[V1alpha1WorkflowCondition]
        """

        self._conditions = conditions

    @property
    def finished_at(self):
        """Gets the finished_at of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The finished_at of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: kubernetes.client.models.V1Time
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1alpha1WorkflowStatus.


        :param finished_at: The finished_at of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: kubernetes.client.models.V1Time
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this V1alpha1WorkflowStatus.  # noqa: E501

        A human readable message indicating details about why the workflow is in this condition.  # noqa: E501

        :return: The message of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1alpha1WorkflowStatus.

        A human readable message indicating details about why the workflow is in this condition.  # noqa: E501

        :param message: The message of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def nodes(self):
        """Gets the nodes of this V1alpha1WorkflowStatus.  # noqa: E501

        Nodes is a mapping between a node ID and the node's status.  # noqa: E501

        :return: The nodes of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, V1alpha1NodeStatus)
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this V1alpha1WorkflowStatus.

        Nodes is a mapping between a node ID and the node's status.  # noqa: E501

        :param nodes: The nodes of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, V1alpha1NodeStatus)
        """

        self._nodes = nodes

    @property
    def offload_node_status_version(self):
        """Gets the offload_node_status_version of this V1alpha1WorkflowStatus.  # noqa: E501

        Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.  # noqa: E501

        :return: The offload_node_status_version of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._offload_node_status_version

    @offload_node_status_version.setter
    def offload_node_status_version(self, offload_node_status_version):
        """Sets the offload_node_status_version of this V1alpha1WorkflowStatus.

        Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data.  # noqa: E501

        :param offload_node_status_version: The offload_node_status_version of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._offload_node_status_version = offload_node_status_version

    @property
    def outputs(self):
        """Gets the outputs of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The outputs of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: V1alpha1Outputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1alpha1WorkflowStatus.


        :param outputs: The outputs of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: V1alpha1Outputs
        """

        self._outputs = outputs

    @property
    def persistent_volume_claims(self):
        """Gets the persistent_volume_claims of this V1alpha1WorkflowStatus.  # noqa: E501

        PersistentVolumeClaims tracks all PVCs that were created as part of the v1alpha1. The contents of this list are drained at the end of the workflow.  # noqa: E501

        :return: The persistent_volume_claims of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1Volume]
        """
        return self._persistent_volume_claims

    @persistent_volume_claims.setter
    def persistent_volume_claims(self, persistent_volume_claims):
        """Sets the persistent_volume_claims of this V1alpha1WorkflowStatus.

        PersistentVolumeClaims tracks all PVCs that were created as part of the v1alpha1. The contents of this list are drained at the end of the workflow.  # noqa: E501

        :param persistent_volume_claims: The persistent_volume_claims of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: list[kubernetes.client.models.V1Volume]
        """

        self._persistent_volume_claims = persistent_volume_claims

    @property
    def phase(self):
        """Gets the phase of this V1alpha1WorkflowStatus.  # noqa: E501

        Phase a simple, high-level summary of where the workflow is in its lifecycle.  # noqa: E501

        :return: The phase of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1alpha1WorkflowStatus.

        Phase a simple, high-level summary of where the workflow is in its lifecycle.  # noqa: E501

        :param phase: The phase of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def resources_duration(self):
        """Gets the resources_duration of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The resources_duration of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._resources_duration

    @resources_duration.setter
    def resources_duration(self, resources_duration):
        """Sets the resources_duration of this V1alpha1WorkflowStatus.


        :param resources_duration: The resources_duration of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._resources_duration = resources_duration

    @property
    def started_at(self):
        """Gets the started_at of this V1alpha1WorkflowStatus.  # noqa: E501


        :return: The started_at of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: kubernetes.client.models.V1Time
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1alpha1WorkflowStatus.


        :param started_at: The started_at of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: kubernetes.client.models.V1Time
        """

        self._started_at = started_at

    @property
    def stored_templates(self):
        """Gets the stored_templates of this V1alpha1WorkflowStatus.  # noqa: E501

        StoredTemplates is a mapping between a template ref and the node's status.  # noqa: E501

        :return: The stored_templates of this V1alpha1WorkflowStatus.  # noqa: E501
        :rtype: dict(str, V1alpha1Template)
        """
        return self._stored_templates

    @stored_templates.setter
    def stored_templates(self, stored_templates):
        """Sets the stored_templates of this V1alpha1WorkflowStatus.

        StoredTemplates is a mapping between a template ref and the node's status.  # noqa: E501

        :param stored_templates: The stored_templates of this V1alpha1WorkflowStatus.  # noqa: E501
        :type: dict(str, V1alpha1Template)
        """

        self._stored_templates = stored_templates

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
        if not isinstance(other, V1alpha1WorkflowStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
