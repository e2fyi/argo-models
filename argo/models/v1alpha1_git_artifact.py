# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.4.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.configuration import Configuration


class V1alpha1GitArtifact(object):
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
        'depth': 'int',
        'fetch': 'list[str]',
        'insecure_ignore_host_key': 'bool',
        'password_secret': 'kubernetes.client.models.V1SecretKeySelector',
        'repo': 'str',
        'revision': 'str',
        'ssh_private_key_secret': 'kubernetes.client.models.V1SecretKeySelector',
        'username_secret': 'kubernetes.client.models.V1SecretKeySelector'
    }

    attribute_map = {
        'depth': 'depth',
        'fetch': 'fetch',
        'insecure_ignore_host_key': 'insecureIgnoreHostKey',
        'password_secret': 'passwordSecret',
        'repo': 'repo',
        'revision': 'revision',
        'ssh_private_key_secret': 'sshPrivateKeySecret',
        'username_secret': 'usernameSecret'
    }

    def __init__(self, depth=None, fetch=None, insecure_ignore_host_key=None, password_secret=None, repo=None, revision=None, ssh_private_key_secret=None, username_secret=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1GitArtifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._depth = None
        self._fetch = None
        self._insecure_ignore_host_key = None
        self._password_secret = None
        self._repo = None
        self._revision = None
        self._ssh_private_key_secret = None
        self._username_secret = None
        self.discriminator = None

        if depth is not None:
            self.depth = depth
        if fetch is not None:
            self.fetch = fetch
        if insecure_ignore_host_key is not None:
            self.insecure_ignore_host_key = insecure_ignore_host_key
        if password_secret is not None:
            self.password_secret = password_secret
        self.repo = repo
        if revision is not None:
            self.revision = revision
        if ssh_private_key_secret is not None:
            self.ssh_private_key_secret = ssh_private_key_secret
        if username_secret is not None:
            self.username_secret = username_secret

    @property
    def depth(self):
        """Gets the depth of this V1alpha1GitArtifact.  # noqa: E501

        Depth specifies clones/fetches should be shallow and include the given number of commits from the branch tip  # noqa: E501

        :return: The depth of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this V1alpha1GitArtifact.

        Depth specifies clones/fetches should be shallow and include the given number of commits from the branch tip  # noqa: E501

        :param depth: The depth of this V1alpha1GitArtifact.  # noqa: E501
        :type: int
        """

        self._depth = depth

    @property
    def fetch(self):
        """Gets the fetch of this V1alpha1GitArtifact.  # noqa: E501

        Fetch specifies a number of refs that should be fetched before checkout  # noqa: E501

        :return: The fetch of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: list[str]
        """
        return self._fetch

    @fetch.setter
    def fetch(self, fetch):
        """Sets the fetch of this V1alpha1GitArtifact.

        Fetch specifies a number of refs that should be fetched before checkout  # noqa: E501

        :param fetch: The fetch of this V1alpha1GitArtifact.  # noqa: E501
        :type: list[str]
        """

        self._fetch = fetch

    @property
    def insecure_ignore_host_key(self):
        """Gets the insecure_ignore_host_key of this V1alpha1GitArtifact.  # noqa: E501

        InsecureIgnoreHostKey disables SSH strict host key checking during git clone  # noqa: E501

        :return: The insecure_ignore_host_key of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_ignore_host_key

    @insecure_ignore_host_key.setter
    def insecure_ignore_host_key(self, insecure_ignore_host_key):
        """Sets the insecure_ignore_host_key of this V1alpha1GitArtifact.

        InsecureIgnoreHostKey disables SSH strict host key checking during git clone  # noqa: E501

        :param insecure_ignore_host_key: The insecure_ignore_host_key of this V1alpha1GitArtifact.  # noqa: E501
        :type: bool
        """

        self._insecure_ignore_host_key = insecure_ignore_host_key

    @property
    def password_secret(self):
        """Gets the password_secret of this V1alpha1GitArtifact.  # noqa: E501


        :return: The password_secret of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecretKeySelector
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """Sets the password_secret of this V1alpha1GitArtifact.


        :param password_secret: The password_secret of this V1alpha1GitArtifact.  # noqa: E501
        :type: kubernetes.client.models.V1SecretKeySelector
        """

        self._password_secret = password_secret

    @property
    def repo(self):
        """Gets the repo of this V1alpha1GitArtifact.  # noqa: E501

        Repo is the git repository  # noqa: E501

        :return: The repo of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this V1alpha1GitArtifact.

        Repo is the git repository  # noqa: E501

        :param repo: The repo of this V1alpha1GitArtifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repo is None:  # noqa: E501
            raise ValueError("Invalid value for `repo`, must not be `None`")  # noqa: E501

        self._repo = repo

    @property
    def revision(self):
        """Gets the revision of this V1alpha1GitArtifact.  # noqa: E501

        Revision is the git commit, tag, branch to checkout  # noqa: E501

        :return: The revision of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1alpha1GitArtifact.

        Revision is the git commit, tag, branch to checkout  # noqa: E501

        :param revision: The revision of this V1alpha1GitArtifact.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def ssh_private_key_secret(self):
        """Gets the ssh_private_key_secret of this V1alpha1GitArtifact.  # noqa: E501


        :return: The ssh_private_key_secret of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecretKeySelector
        """
        return self._ssh_private_key_secret

    @ssh_private_key_secret.setter
    def ssh_private_key_secret(self, ssh_private_key_secret):
        """Sets the ssh_private_key_secret of this V1alpha1GitArtifact.


        :param ssh_private_key_secret: The ssh_private_key_secret of this V1alpha1GitArtifact.  # noqa: E501
        :type: kubernetes.client.models.V1SecretKeySelector
        """

        self._ssh_private_key_secret = ssh_private_key_secret

    @property
    def username_secret(self):
        """Gets the username_secret of this V1alpha1GitArtifact.  # noqa: E501


        :return: The username_secret of this V1alpha1GitArtifact.  # noqa: E501
        :rtype: kubernetes.client.models.V1SecretKeySelector
        """
        return self._username_secret

    @username_secret.setter
    def username_secret(self, username_secret):
        """Sets the username_secret of this V1alpha1GitArtifact.


        :param username_secret: The username_secret of this V1alpha1GitArtifact.  # noqa: E501
        :type: kubernetes.client.models.V1SecretKeySelector
        """

        self._username_secret = username_secret

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
        if not isinstance(other, V1alpha1GitArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1GitArtifact):
            return True

        return self.to_dict() != other.to_dict()
