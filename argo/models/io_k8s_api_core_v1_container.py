# coding: utf-8

"""
    Argo

    Workflow Service API performs CRUD actions against application resources  # noqa: E501

    The version of the OpenAPI document: v2.6.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class kubernetes.client.models.V1Container(object):
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
        'args': 'list[str]',
        'command': 'list[str]',
        'env': 'list[kubernetes.client.models.V1EnvVar]',
        'env_from': 'list[kubernetes.client.models.V1EnvFromSource]',
        'image': 'str',
        'image_pull_policy': 'str',
        'lifecycle': 'kubernetes.client.models.V1Lifecycle',
        'liveness_probe': 'kubernetes.client.models.V1Probe',
        'name': 'str',
        'ports': 'list[kubernetes.client.models.V1ContainerPort]',
        'readiness_probe': 'kubernetes.client.models.V1Probe',
        'resources': 'kubernetes.client.models.V1ResourceRequirements',
        'security_context': 'kubernetes.client.models.V1SecurityContext',
        'startup_probe': 'kubernetes.client.models.V1Probe',
        'stdin': 'bool',
        'stdin_once': 'bool',
        'termination_message_path': 'str',
        'termination_message_policy': 'str',
        'tty': 'bool',
        'volume_devices': 'list[kubernetes.client.models.V1VolumeDevice]',
        'volume_mounts': 'list[kubernetes.client.models.V1VolumeMount]',
        'working_dir': 'str'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'env': 'env',
        'env_from': 'envFrom',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'lifecycle': 'lifecycle',
        'liveness_probe': 'livenessProbe',
        'name': 'name',
        'ports': 'ports',
        'readiness_probe': 'readinessProbe',
        'resources': 'resources',
        'security_context': 'securityContext',
        'startup_probe': 'startupProbe',
        'stdin': 'stdin',
        'stdin_once': 'stdinOnce',
        'termination_message_path': 'terminationMessagePath',
        'termination_message_policy': 'terminationMessagePolicy',
        'tty': 'tty',
        'volume_devices': 'volumeDevices',
        'volume_mounts': 'volumeMounts',
        'working_dir': 'workingDir'
    }

    def __init__(self, args=None, command=None, env=None, env_from=None, image=None, image_pull_policy=None, lifecycle=None, liveness_probe=None, name=None, ports=None, readiness_probe=None, resources=None, security_context=None, startup_probe=None, stdin=None, stdin_once=None, termination_message_path=None, termination_message_policy=None, tty=None, volume_devices=None, volume_mounts=None, working_dir=None, local_vars_configuration=None):  # noqa: E501
        """kubernetes.client.models.V1Container - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._command = None
        self._env = None
        self._env_from = None
        self._image = None
        self._image_pull_policy = None
        self._lifecycle = None
        self._liveness_probe = None
        self._name = None
        self._ports = None
        self._readiness_probe = None
        self._resources = None
        self._security_context = None
        self._startup_probe = None
        self._stdin = None
        self._stdin_once = None
        self._termination_message_path = None
        self._termination_message_policy = None
        self._tty = None
        self._volume_devices = None
        self._volume_mounts = None
        self._working_dir = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if env_from is not None:
            self.env_from = env_from
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if name is not None:
            self.name = name
        if ports is not None:
            self.ports = ports
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if resources is not None:
            self.resources = resources
        if security_context is not None:
            self.security_context = security_context
        if startup_probe is not None:
            self.startup_probe = startup_probe
        if stdin is not None:
            self.stdin = stdin
        if stdin_once is not None:
            self.stdin_once = stdin_once
        if termination_message_path is not None:
            self.termination_message_path = termination_message_path
        if termination_message_policy is not None:
            self.termination_message_policy = termination_message_policy
        if tty is not None:
            self.tty = tty
        if volume_devices is not None:
            self.volume_devices = volume_devices
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def args(self):
        """Gets the args of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The args of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this kubernetes.client.models.V1Container.


        :param args: The args of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The command of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this kubernetes.client.models.V1Container.


        :param command: The command of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The env of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this kubernetes.client.models.V1Container.


        :param env: The env of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[kubernetes.client.models.V1EnvVar]
        """

        self._env = env

    @property
    def env_from(self):
        """Gets the env_from of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The env_from of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from):
        """Sets the env_from of this kubernetes.client.models.V1Container.


        :param env_from: The env_from of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[kubernetes.client.models.V1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def image(self):
        """Gets the image of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The image of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this kubernetes.client.models.V1Container.


        :param image: The image of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The image_pull_policy of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this kubernetes.client.models.V1Container.


        :param image_pull_policy: The image_pull_policy of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def lifecycle(self):
        """Gets the lifecycle of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The lifecycle of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1Lifecycle
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this kubernetes.client.models.V1Container.


        :param lifecycle: The lifecycle of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1Lifecycle
        """

        self._lifecycle = lifecycle

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The liveness_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1Probe
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this kubernetes.client.models.V1Container.


        :param liveness_probe: The liveness_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1Probe
        """

        self._liveness_probe = liveness_probe

    @property
    def name(self):
        """Gets the name of this kubernetes.client.models.V1Container.  # noqa: E501

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :return: The name of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this kubernetes.client.models.V1Container.

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :param name: The name of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ports(self):
        """Gets the ports of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The ports of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this kubernetes.client.models.V1Container.


        :param ports: The ports of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[kubernetes.client.models.V1ContainerPort]
        """

        self._ports = ports

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The readiness_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1Probe
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this kubernetes.client.models.V1Container.


        :param readiness_probe: The readiness_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1Probe
        """

        self._readiness_probe = readiness_probe

    @property
    def resources(self):
        """Gets the resources of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The resources of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this kubernetes.client.models.V1Container.


        :param resources: The resources of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1ResourceRequirements
        """

        self._resources = resources

    @property
    def security_context(self):
        """Gets the security_context of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The security_context of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this kubernetes.client.models.V1Container.


        :param security_context: The security_context of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1SecurityContext
        """

        self._security_context = security_context

    @property
    def startup_probe(self):
        """Gets the startup_probe of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The startup_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: kubernetes.client.models.V1Probe
        """
        return self._startup_probe

    @startup_probe.setter
    def startup_probe(self, startup_probe):
        """Sets the startup_probe of this kubernetes.client.models.V1Container.


        :param startup_probe: The startup_probe of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: kubernetes.client.models.V1Probe
        """

        self._startup_probe = startup_probe

    @property
    def stdin(self):
        """Gets the stdin of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The stdin of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """Sets the stdin of this kubernetes.client.models.V1Container.


        :param stdin: The stdin of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: bool
        """

        self._stdin = stdin

    @property
    def stdin_once(self):
        """Gets the stdin_once of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The stdin_once of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: bool
        """
        return self._stdin_once

    @stdin_once.setter
    def stdin_once(self, stdin_once):
        """Sets the stdin_once of this kubernetes.client.models.V1Container.


        :param stdin_once: The stdin_once of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: bool
        """

        self._stdin_once = stdin_once

    @property
    def termination_message_path(self):
        """Gets the termination_message_path of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The termination_message_path of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._termination_message_path

    @termination_message_path.setter
    def termination_message_path(self, termination_message_path):
        """Sets the termination_message_path of this kubernetes.client.models.V1Container.


        :param termination_message_path: The termination_message_path of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._termination_message_path = termination_message_path

    @property
    def termination_message_policy(self):
        """Gets the termination_message_policy of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The termination_message_policy of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._termination_message_policy

    @termination_message_policy.setter
    def termination_message_policy(self, termination_message_policy):
        """Sets the termination_message_policy of this kubernetes.client.models.V1Container.


        :param termination_message_policy: The termination_message_policy of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._termination_message_policy = termination_message_policy

    @property
    def tty(self):
        """Gets the tty of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The tty of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """Sets the tty of this kubernetes.client.models.V1Container.


        :param tty: The tty of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: bool
        """

        self._tty = tty

    @property
    def volume_devices(self):
        """Gets the volume_devices of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The volume_devices of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1VolumeDevice]
        """
        return self._volume_devices

    @volume_devices.setter
    def volume_devices(self, volume_devices):
        """Sets the volume_devices of this kubernetes.client.models.V1Container.


        :param volume_devices: The volume_devices of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[kubernetes.client.models.V1VolumeDevice]
        """

        self._volume_devices = volume_devices

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The volume_mounts of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: list[kubernetes.client.models.V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this kubernetes.client.models.V1Container.


        :param volume_mounts: The volume_mounts of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: list[kubernetes.client.models.V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def working_dir(self):
        """Gets the working_dir of this kubernetes.client.models.V1Container.  # noqa: E501


        :return: The working_dir of this kubernetes.client.models.V1Container.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this kubernetes.client.models.V1Container.


        :param working_dir: The working_dir of this kubernetes.client.models.V1Container.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

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
        if not isinstance(other, kubernetes.client.models.V1Container):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, kubernetes.client.models.V1Container):
            return True

        return self.to_dict() != other.to_dict()
