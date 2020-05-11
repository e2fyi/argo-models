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


class V1alpha1WorkflowSpec(object):
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
        'active_deadline_seconds': 'str',
        'affinity': 'kubernetes.client.models.V1Affinity',
        'arguments': 'V1alpha1Arguments',
        'artifact_repository_ref': 'V1alpha1ArtifactRepositoryRef',
        'automount_service_account_token': 'bool',
        'dns_config': 'kubernetes.client.models.V1PodDNSConfig',
        'dns_policy': 'str',
        'entrypoint': 'str',
        'executor': 'V1alpha1ExecutorConfig',
        'host_aliases': 'list[kubernetes.client.models.V1HostAlias]',
        'host_network': 'bool',
        'image_pull_secrets': 'list[kubernetes.client.models.V1LocalObjectReference]',
        'metrics': 'V1alpha1Metrics',
        'node_selector': 'dict(str, str)',
        'on_exit': 'str',
        'parallelism': 'str',
        'pod_disruption_budget': 'kubernetes.client.models.V1PodDisruptionBudgetSpec',
        'pod_gc': 'V1alpha1PodGC',
        'pod_priority': 'int',
        'pod_priority_class_name': 'str',
        'pod_spec_patch': 'str',
        'priority': 'int',
        'scheduler_name': 'str',
        'security_context': 'kubernetes.client.models.V1PodSecurityContext',
        'service_account_name': 'str',
        'shutdown': 'str',
        'suspend': 'bool',
        'templates': 'list[V1alpha1Template]',
        'tolerations': 'list[kubernetes.client.models.V1Toleration]',
        'ttl_seconds_after_finished': 'int',
        'ttl_strategy': 'V1alpha1TTLStrategy',
        'volume_claim_templates': 'list[kubernetes.client.models.V1PersistentVolumeClaim]',
        'volumes': 'list[kubernetes.client.models.V1Volume]'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'affinity': 'affinity',
        'arguments': 'arguments',
        'artifact_repository_ref': 'artifactRepositoryRef',
        'automount_service_account_token': 'automountServiceAccountToken',
        'dns_config': 'dnsConfig',
        'dns_policy': 'dnsPolicy',
        'entrypoint': 'entrypoint',
        'executor': 'executor',
        'host_aliases': 'hostAliases',
        'host_network': 'hostNetwork',
        'image_pull_secrets': 'imagePullSecrets',
        'metrics': 'metrics',
        'node_selector': 'nodeSelector',
        'on_exit': 'onExit',
        'parallelism': 'parallelism',
        'pod_disruption_budget': 'podDisruptionBudget',
        'pod_gc': 'podGC',
        'pod_priority': 'podPriority',
        'pod_priority_class_name': 'podPriorityClassName',
        'pod_spec_patch': 'podSpecPatch',
        'priority': 'priority',
        'scheduler_name': 'schedulerName',
        'security_context': 'securityContext',
        'service_account_name': 'serviceAccountName',
        'shutdown': 'shutdown',
        'suspend': 'suspend',
        'templates': 'templates',
        'tolerations': 'tolerations',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished',
        'ttl_strategy': 'ttlStrategy',
        'volume_claim_templates': 'volumeClaimTemplates',
        'volumes': 'volumes'
    }

    def __init__(self, active_deadline_seconds=None, affinity=None, arguments=None, artifact_repository_ref=None, automount_service_account_token=None, dns_config=None, dns_policy=None, entrypoint=None, executor=None, host_aliases=None, host_network=None, image_pull_secrets=None, metrics=None, node_selector=None, on_exit=None, parallelism=None, pod_disruption_budget=None, pod_gc=None, pod_priority=None, pod_priority_class_name=None, pod_spec_patch=None, priority=None, scheduler_name=None, security_context=None, service_account_name=None, shutdown=None, suspend=None, templates=None, tolerations=None, ttl_seconds_after_finished=None, ttl_strategy=None, volume_claim_templates=None, volumes=None):  # noqa: E501
        """V1alpha1WorkflowSpec - a model defined in OpenAPI"""  # noqa: E501

        self._active_deadline_seconds = None
        self._affinity = None
        self._arguments = None
        self._artifact_repository_ref = None
        self._automount_service_account_token = None
        self._dns_config = None
        self._dns_policy = None
        self._entrypoint = None
        self._executor = None
        self._host_aliases = None
        self._host_network = None
        self._image_pull_secrets = None
        self._metrics = None
        self._node_selector = None
        self._on_exit = None
        self._parallelism = None
        self._pod_disruption_budget = None
        self._pod_gc = None
        self._pod_priority = None
        self._pod_priority_class_name = None
        self._pod_spec_patch = None
        self._priority = None
        self._scheduler_name = None
        self._security_context = None
        self._service_account_name = None
        self._shutdown = None
        self._suspend = None
        self._templates = None
        self._tolerations = None
        self._ttl_seconds_after_finished = None
        self._ttl_strategy = None
        self._volume_claim_templates = None
        self._volumes = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if affinity is not None:
            self.affinity = affinity
        if arguments is not None:
            self.arguments = arguments
        if artifact_repository_ref is not None:
            self.artifact_repository_ref = artifact_repository_ref
        if automount_service_account_token is not None:
            self.automount_service_account_token = automount_service_account_token
        if dns_config is not None:
            self.dns_config = dns_config
        if dns_policy is not None:
            self.dns_policy = dns_policy
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if executor is not None:
            self.executor = executor
        if host_aliases is not None:
            self.host_aliases = host_aliases
        if host_network is not None:
            self.host_network = host_network
        if image_pull_secrets is not None:
            self.image_pull_secrets = image_pull_secrets
        if metrics is not None:
            self.metrics = metrics
        if node_selector is not None:
            self.node_selector = node_selector
        if on_exit is not None:
            self.on_exit = on_exit
        if parallelism is not None:
            self.parallelism = parallelism
        if pod_disruption_budget is not None:
            self.pod_disruption_budget = pod_disruption_budget
        if pod_gc is not None:
            self.pod_gc = pod_gc
        if pod_priority is not None:
            self.pod_priority = pod_priority
        if pod_priority_class_name is not None:
            self.pod_priority_class_name = pod_priority_class_name
        if pod_spec_patch is not None:
            self.pod_spec_patch = pod_spec_patch
        if priority is not None:
            self.priority = priority
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        if security_context is not None:
            self.security_context = security_context
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if shutdown is not None:
            self.shutdown = shutdown
        if suspend is not None:
            self.suspend = suspend
        if templates is not None:
            self.templates = templates
        if tolerations is not None:
            self.tolerations = tolerations
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished
        if ttl_strategy is not None:
            self.ttl_strategy = ttl_strategy
        if volume_claim_templates is not None:
            self.volume_claim_templates = volume_claim_templates
        if volumes is not None:
            self.volumes = volumes

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The active_deadline_seconds of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1alpha1WorkflowSpec.


        :param active_deadline_seconds: The active_deadline_seconds of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def affinity(self):
        """Gets the affinity of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The affinity of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: kubernetes.client.models.V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this V1alpha1WorkflowSpec.


        :param affinity: The affinity of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: kubernetes.client.models.V1Affinity
        """

        self._affinity = affinity

    @property
    def arguments(self):
        """Gets the arguments of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The arguments of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1Arguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this V1alpha1WorkflowSpec.


        :param arguments: The arguments of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1Arguments
        """

        self._arguments = arguments

    @property
    def artifact_repository_ref(self):
        """Gets the artifact_repository_ref of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The artifact_repository_ref of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1ArtifactRepositoryRef
        """
        return self._artifact_repository_ref

    @artifact_repository_ref.setter
    def artifact_repository_ref(self, artifact_repository_ref):
        """Sets the artifact_repository_ref of this V1alpha1WorkflowSpec.


        :param artifact_repository_ref: The artifact_repository_ref of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1ArtifactRepositoryRef
        """

        self._artifact_repository_ref = artifact_repository_ref

    @property
    def automount_service_account_token(self):
        """Gets the automount_service_account_token of this V1alpha1WorkflowSpec.  # noqa: E501

        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.  # noqa: E501

        :return: The automount_service_account_token of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._automount_service_account_token

    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token):
        """Sets the automount_service_account_token of this V1alpha1WorkflowSpec.

        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.  # noqa: E501

        :param automount_service_account_token: The automount_service_account_token of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._automount_service_account_token = automount_service_account_token

    @property
    def dns_config(self):
        """Gets the dns_config of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The dns_config of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: kubernetes.client.models.V1PodDNSConfig
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        """Sets the dns_config of this V1alpha1WorkflowSpec.


        :param dns_config: The dns_config of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: kubernetes.client.models.V1PodDNSConfig
        """

        self._dns_config = dns_config

    @property
    def dns_policy(self):
        """Gets the dns_policy of this V1alpha1WorkflowSpec.  # noqa: E501

        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.  # noqa: E501

        :return: The dns_policy of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """Sets the dns_policy of this V1alpha1WorkflowSpec.

        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.  # noqa: E501

        :param dns_policy: The dns_policy of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._dns_policy = dns_policy

    @property
    def entrypoint(self):
        """Gets the entrypoint of this V1alpha1WorkflowSpec.  # noqa: E501

        Entrypoint is a template reference to the starting point of the v1alpha1.  # noqa: E501

        :return: The entrypoint of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this V1alpha1WorkflowSpec.

        Entrypoint is a template reference to the starting point of the v1alpha1.  # noqa: E501

        :param entrypoint: The entrypoint of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._entrypoint = entrypoint

    @property
    def executor(self):
        """Gets the executor of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The executor of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1ExecutorConfig
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this V1alpha1WorkflowSpec.


        :param executor: The executor of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1ExecutorConfig
        """

        self._executor = executor

    @property
    def host_aliases(self):
        """Gets the host_aliases of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The host_aliases of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1HostAlias]
        """
        return self._host_aliases

    @host_aliases.setter
    def host_aliases(self, host_aliases):
        """Sets the host_aliases of this V1alpha1WorkflowSpec.


        :param host_aliases: The host_aliases of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[kubernetes.client.models.V1HostAlias]
        """

        self._host_aliases = host_aliases

    @property
    def host_network(self):
        """Gets the host_network of this V1alpha1WorkflowSpec.  # noqa: E501

        Host networking requested for this workflow pod. Default to false.  # noqa: E501

        :return: The host_network of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this V1alpha1WorkflowSpec.

        Host networking requested for this workflow pod. Default to false.  # noqa: E501

        :param host_network: The host_network of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._host_network = host_network

    @property
    def image_pull_secrets(self):
        """Gets the image_pull_secrets of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The image_pull_secrets of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """Sets the image_pull_secrets of this V1alpha1WorkflowSpec.


        :param image_pull_secrets: The image_pull_secrets of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[kubernetes.client.models.V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def metrics(self):
        """Gets the metrics of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The metrics of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this V1alpha1WorkflowSpec.


        :param metrics: The metrics of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1Metrics
        """

        self._metrics = metrics

    @property
    def node_selector(self):
        """Gets the node_selector of this V1alpha1WorkflowSpec.  # noqa: E501

        NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.  # noqa: E501

        :return: The node_selector of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this V1alpha1WorkflowSpec.

        NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.  # noqa: E501

        :param node_selector: The node_selector of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def on_exit(self):
        """Gets the on_exit of this V1alpha1WorkflowSpec.  # noqa: E501

        OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary v1alpha1.  # noqa: E501

        :return: The on_exit of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._on_exit

    @on_exit.setter
    def on_exit(self, on_exit):
        """Sets the on_exit of this V1alpha1WorkflowSpec.

        OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary v1alpha1.  # noqa: E501

        :param on_exit: The on_exit of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._on_exit = on_exit

    @property
    def parallelism(self):
        """Gets the parallelism of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The parallelism of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this V1alpha1WorkflowSpec.


        :param parallelism: The parallelism of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._parallelism = parallelism

    @property
    def pod_disruption_budget(self):
        """Gets the pod_disruption_budget of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The pod_disruption_budget of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: kubernetes.client.models.V1PodDisruptionBudgetSpec
        """
        return self._pod_disruption_budget

    @pod_disruption_budget.setter
    def pod_disruption_budget(self, pod_disruption_budget):
        """Sets the pod_disruption_budget of this V1alpha1WorkflowSpec.


        :param pod_disruption_budget: The pod_disruption_budget of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: kubernetes.client.models.V1PodDisruptionBudgetSpec
        """

        self._pod_disruption_budget = pod_disruption_budget

    @property
    def pod_gc(self):
        """Gets the pod_gc of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The pod_gc of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1PodGC
        """
        return self._pod_gc

    @pod_gc.setter
    def pod_gc(self, pod_gc):
        """Sets the pod_gc of this V1alpha1WorkflowSpec.


        :param pod_gc: The pod_gc of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1PodGC
        """

        self._pod_gc = pod_gc

    @property
    def pod_priority(self):
        """Gets the pod_priority of this V1alpha1WorkflowSpec.  # noqa: E501

        Priority to apply to workflow pods.  # noqa: E501

        :return: The pod_priority of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._pod_priority

    @pod_priority.setter
    def pod_priority(self, pod_priority):
        """Sets the pod_priority of this V1alpha1WorkflowSpec.

        Priority to apply to workflow pods.  # noqa: E501

        :param pod_priority: The pod_priority of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._pod_priority = pod_priority

    @property
    def pod_priority_class_name(self):
        """Gets the pod_priority_class_name of this V1alpha1WorkflowSpec.  # noqa: E501

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :return: The pod_priority_class_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_priority_class_name

    @pod_priority_class_name.setter
    def pod_priority_class_name(self, pod_priority_class_name):
        """Sets the pod_priority_class_name of this V1alpha1WorkflowSpec.

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :param pod_priority_class_name: The pod_priority_class_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._pod_priority_class_name = pod_priority_class_name

    @property
    def pod_spec_patch(self):
        """Gets the pod_spec_patch of this V1alpha1WorkflowSpec.  # noqa: E501

        PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).  # noqa: E501

        :return: The pod_spec_patch of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_spec_patch

    @pod_spec_patch.setter
    def pod_spec_patch(self, pod_spec_patch):
        """Sets the pod_spec_patch of this V1alpha1WorkflowSpec.

        PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).  # noqa: E501

        :param pod_spec_patch: The pod_spec_patch of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._pod_spec_patch = pod_spec_patch

    @property
    def priority(self):
        """Gets the priority of this V1alpha1WorkflowSpec.  # noqa: E501

        Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.  # noqa: E501

        :return: The priority of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V1alpha1WorkflowSpec.

        Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.  # noqa: E501

        :param priority: The priority of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def scheduler_name(self):
        """Gets the scheduler_name of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The scheduler_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """Sets the scheduler_name of this V1alpha1WorkflowSpec.


        :param scheduler_name: The scheduler_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def security_context(self):
        """Gets the security_context of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The security_context of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: kubernetes.client.models.V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this V1alpha1WorkflowSpec.


        :param security_context: The security_context of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: kubernetes.client.models.V1PodSecurityContext
        """

        self._security_context = security_context

    @property
    def service_account_name(self):
        """Gets the service_account_name of this V1alpha1WorkflowSpec.  # noqa: E501

        ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.  # noqa: E501

        :return: The service_account_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this V1alpha1WorkflowSpec.

        ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.  # noqa: E501

        :param service_account_name: The service_account_name of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def shutdown(self):
        """Gets the shutdown of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The shutdown of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._shutdown

    @shutdown.setter
    def shutdown(self, shutdown):
        """Sets the shutdown of this V1alpha1WorkflowSpec.


        :param shutdown: The shutdown of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._shutdown = shutdown

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The suspend of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1WorkflowSpec.


        :param suspend: The suspend of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._suspend = suspend

    @property
    def templates(self):
        """Gets the templates of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The templates of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[V1alpha1Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this V1alpha1WorkflowSpec.


        :param templates: The templates of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[V1alpha1Template]
        """

        self._templates = templates

    @property
    def tolerations(self):
        """Gets the tolerations of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The tolerations of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this V1alpha1WorkflowSpec.


        :param tolerations: The tolerations of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[kubernetes.client.models.V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this V1alpha1WorkflowSpec.  # noqa: E501

        TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes. DEPRECATED: Use TTLStrategy.SecondsAfterCompletion instead.  # noqa: E501

        :return: The ttl_seconds_after_finished of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this V1alpha1WorkflowSpec.

        TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes. DEPRECATED: Use TTLStrategy.SecondsAfterCompletion instead.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def ttl_strategy(self):
        """Gets the ttl_strategy of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The ttl_strategy of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: V1alpha1TTLStrategy
        """
        return self._ttl_strategy

    @ttl_strategy.setter
    def ttl_strategy(self, ttl_strategy):
        """Sets the ttl_strategy of this V1alpha1WorkflowSpec.


        :param ttl_strategy: The ttl_strategy of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: V1alpha1TTLStrategy
        """

        self._ttl_strategy = ttl_strategy

    @property
    def volume_claim_templates(self):
        """Gets the volume_claim_templates of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The volume_claim_templates of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1PersistentVolumeClaim]
        """
        return self._volume_claim_templates

    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates):
        """Sets the volume_claim_templates of this V1alpha1WorkflowSpec.


        :param volume_claim_templates: The volume_claim_templates of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[kubernetes.client.models.V1PersistentVolumeClaim]
        """

        self._volume_claim_templates = volume_claim_templates

    @property
    def volumes(self):
        """Gets the volumes of this V1alpha1WorkflowSpec.  # noqa: E501


        :return: The volumes of this V1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1alpha1WorkflowSpec.


        :param volumes: The volumes of this V1alpha1WorkflowSpec.  # noqa: E501
        :type: list[kubernetes.client.models.V1Volume]
        """

        self._volumes = volumes

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
        if not isinstance(other, V1alpha1WorkflowSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
