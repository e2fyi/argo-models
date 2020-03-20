# coding: utf-8

# flake8: noqa
"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from argo.models.cronv1alpha1_create_cron_workflow_request import Cronv1alpha1CreateCronWorkflowRequest
from argo.models.cronv1alpha1_lint_cron_workflow_request import Cronv1alpha1LintCronWorkflowRequest
from argo.models.cronv1alpha1_update_cron_workflow_request import Cronv1alpha1UpdateCronWorkflowRequest
from argo.models.google_protobuf_any import GoogleProtobufAny
from argo.models.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from argo.models.io_k8s_api_core_v1_aws_elastic_block_store_volume_source import kubernetes.client.models.V1AWSElasticBlockStoreVolumeSource
from argo.models.io_k8s_api_core_v1_affinity import kubernetes.client.models.V1Affinity
from argo.models.io_k8s_api_core_v1_azure_disk_volume_source import kubernetes.client.models.V1AzureDiskVolumeSource
from argo.models.io_k8s_api_core_v1_azure_file_volume_source import kubernetes.client.models.V1AzureFileVolumeSource
from argo.models.io_k8s_api_core_v1_csi_volume_source import kubernetes.client.models.V1CSIVolumeSource
from argo.models.io_k8s_api_core_v1_capabilities import kubernetes.client.models.V1Capabilities
from argo.models.io_k8s_api_core_v1_ceph_fs_volume_source import kubernetes.client.models.V1CephFSVolumeSource
from argo.models.io_k8s_api_core_v1_cinder_volume_source import kubernetes.client.models.V1CinderVolumeSource
from argo.models.io_k8s_api_core_v1_config_map_env_source import kubernetes.client.models.V1ConfigMapEnvSource
from argo.models.io_k8s_api_core_v1_config_map_key_selector import kubernetes.client.models.V1ConfigMapKeySelector
from argo.models.io_k8s_api_core_v1_config_map_projection import kubernetes.client.models.V1ConfigMapProjection
from argo.models.io_k8s_api_core_v1_config_map_volume_source import kubernetes.client.models.V1ConfigMapVolumeSource
from argo.models.io_k8s_api_core_v1_container import kubernetes.client.models.V1Container
from argo.models.io_k8s_api_core_v1_container_port import kubernetes.client.models.V1ContainerPort
from argo.models.io_k8s_api_core_v1_create_options import kubernetes.client.models.V1CreateOptions
from argo.models.io_k8s_api_core_v1_delete_options import kubernetes.client.models.V1DeleteOptions
from argo.models.io_k8s_api_core_v1_downward_api_projection import kubernetes.client.models.V1DownwardAPIProjection
from argo.models.io_k8s_api_core_v1_downward_api_volume_file import kubernetes.client.models.V1DownwardAPIVolumeFile
from argo.models.io_k8s_api_core_v1_downward_api_volume_source import kubernetes.client.models.V1DownwardAPIVolumeSource
from argo.models.io_k8s_api_core_v1_empty_dir_volume_source import kubernetes.client.models.V1EmptyDirVolumeSource
from argo.models.io_k8s_api_core_v1_env_from_source import kubernetes.client.models.V1EnvFromSource
from argo.models.io_k8s_api_core_v1_env_var import kubernetes.client.models.V1EnvVar
from argo.models.io_k8s_api_core_v1_env_var_source import kubernetes.client.models.V1EnvVarSource
from argo.models.io_k8s_api_core_v1_exec_action import kubernetes.client.models.V1ExecAction
from argo.models.io_k8s_api_core_v1_fc_volume_source import kubernetes.client.models.V1FCVolumeSource
from argo.models.io_k8s_api_core_v1_fields_v1 import kubernetes.client.models.V1FieldsV1
from argo.models.io_k8s_api_core_v1_flex_volume_source import kubernetes.client.models.V1FlexVolumeSource
from argo.models.io_k8s_api_core_v1_flocker_volume_source import kubernetes.client.models.V1FlockerVolumeSource
from argo.models.io_k8s_api_core_v1_gce_persistent_disk_volume_source import kubernetes.client.models.V1GCEPersistentDiskVolumeSource
from argo.models.io_k8s_api_core_v1_get_options import kubernetes.client.models.V1GetOptions
from argo.models.io_k8s_api_core_v1_git_repo_volume_source import kubernetes.client.models.V1GitRepoVolumeSource
from argo.models.io_k8s_api_core_v1_glusterfs_volume_source import kubernetes.client.models.V1GlusterfsVolumeSource
from argo.models.io_k8s_api_core_v1_http_get_action import kubernetes.client.models.V1HTTPGetAction
from argo.models.io_k8s_api_core_v1_http_header import kubernetes.client.models.V1HTTPHeader
from argo.models.io_k8s_api_core_v1_handler import kubernetes.client.models.V1Handler
from argo.models.io_k8s_api_core_v1_host_alias import kubernetes.client.models.V1HostAlias
from argo.models.io_k8s_api_core_v1_host_path_volume_source import kubernetes.client.models.V1HostPathVolumeSource
from argo.models.io_k8s_api_core_v1_iscsi_volume_source import kubernetes.client.models.V1ISCSIVolumeSource
from argo.models.io_k8s_api_core_v1_int_or_string import kubernetes.client.models.V1IntOrString
from argo.models.io_k8s_api_core_v1_key_to_path import kubernetes.client.models.V1KeyToPath
from argo.models.io_k8s_api_core_v1_label_selector import kubernetes.client.models.V1LabelSelector
from argo.models.io_k8s_api_core_v1_label_selector_requirement import kubernetes.client.models.V1LabelSelectorRequirement
from argo.models.io_k8s_api_core_v1_lifecycle import kubernetes.client.models.V1Lifecycle
from argo.models.io_k8s_api_core_v1_list_meta import kubernetes.client.models.V1ListMeta
from argo.models.io_k8s_api_core_v1_list_options import kubernetes.client.models.V1ListOptions
from argo.models.io_k8s_api_core_v1_local_object_reference import kubernetes.client.models.V1LocalObjectReference
from argo.models.io_k8s_api_core_v1_managed_fields_entry import kubernetes.client.models.V1ManagedFieldsEntry
from argo.models.io_k8s_api_core_v1_nfs_volume_source import kubernetes.client.models.V1NFSVolumeSource
from argo.models.io_k8s_api_core_v1_node_affinity import kubernetes.client.models.V1NodeAffinity
from argo.models.io_k8s_api_core_v1_node_selector import kubernetes.client.models.V1NodeSelector
from argo.models.io_k8s_api_core_v1_node_selector_requirement import kubernetes.client.models.V1NodeSelectorRequirement
from argo.models.io_k8s_api_core_v1_node_selector_term import kubernetes.client.models.V1NodeSelectorTerm
from argo.models.io_k8s_api_core_v1_object_field_selector import kubernetes.client.models.V1ObjectFieldSelector
from argo.models.io_k8s_api_core_v1_object_meta import kubernetes.client.models.V1ObjectMeta
from argo.models.io_k8s_api_core_v1_object_reference import kubernetes.client.models.V1ObjectReference
from argo.models.io_k8s_api_core_v1_owner_reference import kubernetes.client.models.V1OwnerReference
from argo.models.io_k8s_api_core_v1_persistent_volume_claim import kubernetes.client.models.V1PersistentVolumeClaim
from argo.models.io_k8s_api_core_v1_persistent_volume_claim_condition import kubernetes.client.models.V1PersistentVolumeClaimCondition
from argo.models.io_k8s_api_core_v1_persistent_volume_claim_spec import kubernetes.client.models.V1PersistentVolumeClaimSpec
from argo.models.io_k8s_api_core_v1_persistent_volume_claim_status import kubernetes.client.models.V1PersistentVolumeClaimStatus
from argo.models.io_k8s_api_core_v1_persistent_volume_claim_volume_source import kubernetes.client.models.V1PersistentVolumeClaimVolumeSource
from argo.models.io_k8s_api_core_v1_photon_persistent_disk_volume_source import kubernetes.client.models.V1PhotonPersistentDiskVolumeSource
from argo.models.io_k8s_api_core_v1_pod_affinity import kubernetes.client.models.V1PodAffinity
from argo.models.io_k8s_api_core_v1_pod_affinity_term import kubernetes.client.models.V1PodAffinityTerm
from argo.models.io_k8s_api_core_v1_pod_anti_affinity import kubernetes.client.models.V1PodAntiAffinity
from argo.models.io_k8s_api_core_v1_pod_dns_config import kubernetes.client.models.V1PodDNSConfig
from argo.models.io_k8s_api_core_v1_pod_dns_config_option import kubernetes.client.models.V1PodDNSConfigOption
from argo.models.io_k8s_api_core_v1_pod_log_options import kubernetes.client.models.V1PodLogOptions
from argo.models.io_k8s_api_core_v1_pod_security_context import kubernetes.client.models.V1PodSecurityContext
from argo.models.io_k8s_api_core_v1_portworx_volume_source import kubernetes.client.models.V1PortworxVolumeSource
from argo.models.io_k8s_api_core_v1_preconditions import kubernetes.client.models.V1Preconditions
from argo.models.io_k8s_api_core_v1_preferred_scheduling_term import kubernetes.client.models.V1PreferredSchedulingTerm
from argo.models.io_k8s_api_core_v1_probe import kubernetes.client.models.V1Probe
from argo.models.io_k8s_api_core_v1_projected_volume_source import kubernetes.client.models.V1ProjectedVolumeSource
from argo.models.io_k8s_api_core_v1_quantity import kubernetes.client.models.V1Quantity
from argo.models.io_k8s_api_core_v1_quobyte_volume_source import kubernetes.client.models.V1QuobyteVolumeSource
from argo.models.io_k8s_api_core_v1_rbd_volume_source import kubernetes.client.models.V1RBDVolumeSource
from argo.models.io_k8s_api_core_v1_resource_field_selector import kubernetes.client.models.V1ResourceFieldSelector
from argo.models.io_k8s_api_core_v1_resource_requirements import kubernetes.client.models.V1ResourceRequirements
from argo.models.io_k8s_api_core_v1_se_linux_options import kubernetes.client.models.V1SELinuxOptions
from argo.models.io_k8s_api_core_v1_scale_io_volume_source import kubernetes.client.models.V1ScaleIOVolumeSource
from argo.models.io_k8s_api_core_v1_secret_env_source import kubernetes.client.models.V1SecretEnvSource
from argo.models.io_k8s_api_core_v1_secret_key_selector import kubernetes.client.models.V1SecretKeySelector
from argo.models.io_k8s_api_core_v1_secret_projection import kubernetes.client.models.V1SecretProjection
from argo.models.io_k8s_api_core_v1_secret_volume_source import kubernetes.client.models.V1SecretVolumeSource
from argo.models.io_k8s_api_core_v1_security_context import kubernetes.client.models.V1SecurityContext
from argo.models.io_k8s_api_core_v1_service_account_token_projection import kubernetes.client.models.V1ServiceAccountTokenProjection
from argo.models.io_k8s_api_core_v1_storage_os_volume_source import kubernetes.client.models.V1StorageOSVolumeSource
from argo.models.io_k8s_api_core_v1_sysctl import kubernetes.client.models.V1Sysctl
from argo.models.io_k8s_api_core_v1_tcp_socket_action import kubernetes.client.models.V1TCPSocketAction
from argo.models.io_k8s_api_core_v1_time import kubernetes.client.models.V1Time
from argo.models.io_k8s_api_core_v1_toleration import kubernetes.client.models.V1Toleration
from argo.models.io_k8s_api_core_v1_typed_local_object_reference import kubernetes.client.models.V1TypedLocalObjectReference
from argo.models.io_k8s_api_core_v1_volume import kubernetes.client.models.V1Volume
from argo.models.io_k8s_api_core_v1_volume_device import kubernetes.client.models.V1VolumeDevice
from argo.models.io_k8s_api_core_v1_volume_mount import kubernetes.client.models.V1VolumeMount
from argo.models.io_k8s_api_core_v1_volume_projection import kubernetes.client.models.V1VolumeProjection
from argo.models.io_k8s_api_core_v1_volume_source import kubernetes.client.models.V1VolumeSource
from argo.models.io_k8s_api_core_v1_vsphere_virtual_disk_volume_source import kubernetes.client.models.V1VsphereVirtualDiskVolumeSource
from argo.models.io_k8s_api_core_v1_weighted_pod_affinity_term import kubernetes.client.models.V1WeightedPodAffinityTerm
from argo.models.io_k8s_api_core_v1_windows_security_context_options import kubernetes.client.models.V1WindowsSecurityContextOptions
from argo.models.v1alpha1_archive_strategy import V1alpha1ArchiveStrategy
from argo.models.v1alpha1_arguments import V1alpha1Arguments
from argo.models.v1alpha1_artifact import V1alpha1Artifact
from argo.models.v1alpha1_artifact_location import V1alpha1ArtifactLocation
from argo.models.v1alpha1_artifact_repository_ref import V1alpha1ArtifactRepositoryRef
from argo.models.v1alpha1_artifactory_artifact import V1alpha1ArtifactoryArtifact
from argo.models.v1alpha1_artifactory_auth import V1alpha1ArtifactoryAuth
from argo.models.v1alpha1_backoff import V1alpha1Backoff
from argo.models.v1alpha1_continue_on import V1alpha1ContinueOn
from argo.models.v1alpha1_cron_workflow import V1alpha1CronWorkflow
from argo.models.v1alpha1_cron_workflow_list import V1alpha1CronWorkflowList
from argo.models.v1alpha1_cron_workflow_spec import V1alpha1CronWorkflowSpec
from argo.models.v1alpha1_cron_workflow_status import V1alpha1CronWorkflowStatus
from argo.models.v1alpha1_dag_task import V1alpha1DAGTask
from argo.models.v1alpha1_dag_template import V1alpha1DAGTemplate
from argo.models.v1alpha1_executor_config import V1alpha1ExecutorConfig
from argo.models.v1alpha1_git_artifact import V1alpha1GitArtifact
from argo.models.v1alpha1_hdfs_artifact import V1alpha1HDFSArtifact
from argo.models.v1alpha1_hdfs_config import V1alpha1HDFSConfig
from argo.models.v1alpha1_hdfs_krb_config import V1alpha1HDFSKrbConfig
from argo.models.v1alpha1_http_artifact import V1alpha1HTTPArtifact
from argo.models.v1alpha1_info_response import V1alpha1InfoResponse
from argo.models.v1alpha1_inputs import V1alpha1Inputs
from argo.models.v1alpha1_item import V1alpha1Item
from argo.models.v1alpha1_item_value import V1alpha1ItemValue
from argo.models.v1alpha1_log_entry import V1alpha1LogEntry
from argo.models.v1alpha1_metadata import V1alpha1Metadata
from argo.models.v1alpha1_node_status import V1alpha1NodeStatus
from argo.models.v1alpha1_outputs import V1alpha1Outputs
from argo.models.v1alpha1_parallel_steps import V1alpha1ParallelSteps
from argo.models.v1alpha1_parameter import V1alpha1Parameter
from argo.models.v1alpha1_pod_gc import V1alpha1PodGC
from argo.models.v1alpha1_raw_artifact import V1alpha1RawArtifact
from argo.models.v1alpha1_resource_template import V1alpha1ResourceTemplate
from argo.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argo.models.v1alpha1_s3_artifact import V1alpha1S3Artifact
from argo.models.v1alpha1_s3_bucket import V1alpha1S3Bucket
from argo.models.v1alpha1_script_template import V1alpha1ScriptTemplate
from argo.models.v1alpha1_sequence import V1alpha1Sequence
from argo.models.v1alpha1_suspend_template import V1alpha1SuspendTemplate
from argo.models.v1alpha1_ttl_strategy import V1alpha1TTLStrategy
from argo.models.v1alpha1_template import V1alpha1Template
from argo.models.v1alpha1_template_ref import V1alpha1TemplateRef
from argo.models.v1alpha1_user_container import V1alpha1UserContainer
from argo.models.v1alpha1_value_from import V1alpha1ValueFrom
from argo.models.v1alpha1_workflow import V1alpha1Workflow
from argo.models.v1alpha1_workflow_create_request import V1alpha1WorkflowCreateRequest
from argo.models.v1alpha1_workflow_lint_request import V1alpha1WorkflowLintRequest
from argo.models.v1alpha1_workflow_list import V1alpha1WorkflowList
from argo.models.v1alpha1_workflow_resubmit_request import V1alpha1WorkflowResubmitRequest
from argo.models.v1alpha1_workflow_resume_request import V1alpha1WorkflowResumeRequest
from argo.models.v1alpha1_workflow_retry_request import V1alpha1WorkflowRetryRequest
from argo.models.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from argo.models.v1alpha1_workflow_status import V1alpha1WorkflowStatus
from argo.models.v1alpha1_workflow_step import V1alpha1WorkflowStep
from argo.models.v1alpha1_workflow_suspend_request import V1alpha1WorkflowSuspendRequest
from argo.models.v1alpha1_workflow_template import V1alpha1WorkflowTemplate
from argo.models.v1alpha1_workflow_template_create_request import V1alpha1WorkflowTemplateCreateRequest
from argo.models.v1alpha1_workflow_template_lint_request import V1alpha1WorkflowTemplateLintRequest
from argo.models.v1alpha1_workflow_template_list import V1alpha1WorkflowTemplateList
from argo.models.v1alpha1_workflow_template_spec import V1alpha1WorkflowTemplateSpec
from argo.models.v1alpha1_workflow_template_update_request import V1alpha1WorkflowTemplateUpdateRequest
from argo.models.v1alpha1_workflow_terminate_request import V1alpha1WorkflowTerminateRequest
from argo.models.v1alpha1_workflow_watch_event import V1alpha1WorkflowWatchEvent
