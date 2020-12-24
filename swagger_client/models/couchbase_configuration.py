# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CouchbaseConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'config_id': 'str',
        'user_name': 'str',
        'user_password': 'str',
        'servers': 'list[str]',
        'default_bucket': 'str',
        'buckets': 'list[str]',
        'password_encryption_method': 'str',
        'operation_tracing_enabled': 'bool',
        'mutation_tokens_enabled': 'bool',
        'connect_timeout': 'int',
        'computation_pool_size': 'int',
        'use_ssl': 'bool',
        'ssl_trust_store_file': 'str',
        'ssl_trust_store_pin': 'str',
        'ssl_trust_store_format': 'str',
        'binary_attributes': 'list[str]',
        'certificate_attributes': 'list[str]'
    }

    attribute_map = {
        'config_id': 'configId',
        'user_name': 'userName',
        'user_password': 'userPassword',
        'servers': 'servers',
        'default_bucket': 'defaultBucket',
        'buckets': 'buckets',
        'password_encryption_method': 'passwordEncryptionMethod',
        'operation_tracing_enabled': 'operationTracingEnabled',
        'mutation_tokens_enabled': 'mutationTokensEnabled',
        'connect_timeout': 'connectTimeout',
        'computation_pool_size': 'computationPoolSize',
        'use_ssl': 'useSSL',
        'ssl_trust_store_file': 'sslTrustStoreFile',
        'ssl_trust_store_pin': 'sslTrustStorePin',
        'ssl_trust_store_format': 'sslTrustStoreFormat',
        'binary_attributes': 'binaryAttributes',
        'certificate_attributes': 'certificateAttributes'
    }

    def __init__(self, config_id=None, user_name=None, user_password=None, servers=None, default_bucket=None, buckets=None, password_encryption_method=None, operation_tracing_enabled=False, mutation_tokens_enabled=False, connect_timeout=None, computation_pool_size=None, use_ssl=None, ssl_trust_store_file=None, ssl_trust_store_pin=None, ssl_trust_store_format=None, binary_attributes=None, certificate_attributes=None):  # noqa: E501
        """CouchbaseConfiguration - a model defined in Swagger"""  # noqa: E501
        self._config_id = None
        self._user_name = None
        self._user_password = None
        self._servers = None
        self._default_bucket = None
        self._buckets = None
        self._password_encryption_method = None
        self._operation_tracing_enabled = None
        self._mutation_tokens_enabled = None
        self._connect_timeout = None
        self._computation_pool_size = None
        self._use_ssl = None
        self._ssl_trust_store_file = None
        self._ssl_trust_store_pin = None
        self._ssl_trust_store_format = None
        self._binary_attributes = None
        self._certificate_attributes = None
        self.discriminator = None
        if config_id is not None:
            self.config_id = config_id
        if user_name is not None:
            self.user_name = user_name
        if user_password is not None:
            self.user_password = user_password
        if servers is not None:
            self.servers = servers
        if default_bucket is not None:
            self.default_bucket = default_bucket
        if buckets is not None:
            self.buckets = buckets
        if password_encryption_method is not None:
            self.password_encryption_method = password_encryption_method
        if operation_tracing_enabled is not None:
            self.operation_tracing_enabled = operation_tracing_enabled
        if mutation_tokens_enabled is not None:
            self.mutation_tokens_enabled = mutation_tokens_enabled
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if computation_pool_size is not None:
            self.computation_pool_size = computation_pool_size
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if ssl_trust_store_file is not None:
            self.ssl_trust_store_file = ssl_trust_store_file
        if ssl_trust_store_pin is not None:
            self.ssl_trust_store_pin = ssl_trust_store_pin
        if ssl_trust_store_format is not None:
            self.ssl_trust_store_format = ssl_trust_store_format
        if binary_attributes is not None:
            self.binary_attributes = binary_attributes
        if certificate_attributes is not None:
            self.certificate_attributes = certificate_attributes

    @property
    def config_id(self):
        """Gets the config_id of this CouchbaseConfiguration.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The config_id of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this CouchbaseConfiguration.

        Unique identifier  # noqa: E501

        :param config_id: The config_id of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._config_id = config_id

    @property
    def user_name(self):
        """Gets the user_name of this CouchbaseConfiguration.  # noqa: E501

        Couchbase server user.  # noqa: E501

        :return: The user_name of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CouchbaseConfiguration.

        Couchbase server user.  # noqa: E501

        :param user_name: The user_name of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_password(self):
        """Gets the user_password of this CouchbaseConfiguration.  # noqa: E501

        Encoded Couchbase server user password.  # noqa: E501

        :return: The user_password of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this CouchbaseConfiguration.

        Encoded Couchbase server user password.  # noqa: E501

        :param user_password: The user_password of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._user_password = user_password

    @property
    def servers(self):
        """Gets the servers of this CouchbaseConfiguration.  # noqa: E501

        Couchbase server host and port.  # noqa: E501

        :return: The servers of this CouchbaseConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this CouchbaseConfiguration.

        Couchbase server host and port.  # noqa: E501

        :param servers: The servers of this CouchbaseConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._servers = servers

    @property
    def default_bucket(self):
        """Gets the default_bucket of this CouchbaseConfiguration.  # noqa: E501

        Main bucket that application should use if other mapping rules were not applied.  # noqa: E501

        :return: The default_bucket of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._default_bucket

    @default_bucket.setter
    def default_bucket(self, default_bucket):
        """Sets the default_bucket of this CouchbaseConfiguration.

        Main bucket that application should use if other mapping rules were not applied.  # noqa: E501

        :param default_bucket: The default_bucket of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._default_bucket = default_bucket

    @property
    def buckets(self):
        """Gets the buckets of this CouchbaseConfiguration.  # noqa: E501

        List of buckets defining mapping rules.  # noqa: E501

        :return: The buckets of this CouchbaseConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this CouchbaseConfiguration.

        List of buckets defining mapping rules.  # noqa: E501

        :param buckets: The buckets of this CouchbaseConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._buckets = buckets

    @property
    def password_encryption_method(self):
        """Gets the password_encryption_method of this CouchbaseConfiguration.  # noqa: E501


        :return: The password_encryption_method of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password_encryption_method

    @password_encryption_method.setter
    def password_encryption_method(self, password_encryption_method):
        """Sets the password_encryption_method of this CouchbaseConfiguration.


        :param password_encryption_method: The password_encryption_method of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["SHA", "SSHA", "SHA-256", "SSHA-256", "SHA-384", "SSHA-384", "SHA-512", "SSHA-512", "MD5", "SMD5", "CRYPT", "CRYPT-MD5", "CRYPT-SHA-256", "CRYPT-SHA-512", "CRYPT-BCRYPT", "CRYPT-BCRYPT", "PKCS5S2"]  # noqa: E501
        if password_encryption_method not in allowed_values:
            raise ValueError(
                "Invalid value for `password_encryption_method` ({0}), must be one of {1}"  # noqa: E501
                .format(password_encryption_method, allowed_values)
            )

        self._password_encryption_method = password_encryption_method

    @property
    def operation_tracing_enabled(self):
        """Gets the operation_tracing_enabled of this CouchbaseConfiguration.  # noqa: E501


        :return: The operation_tracing_enabled of this CouchbaseConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._operation_tracing_enabled

    @operation_tracing_enabled.setter
    def operation_tracing_enabled(self, operation_tracing_enabled):
        """Sets the operation_tracing_enabled of this CouchbaseConfiguration.


        :param operation_tracing_enabled: The operation_tracing_enabled of this CouchbaseConfiguration.  # noqa: E501
        :type: bool
        """

        self._operation_tracing_enabled = operation_tracing_enabled

    @property
    def mutation_tokens_enabled(self):
        """Gets the mutation_tokens_enabled of this CouchbaseConfiguration.  # noqa: E501

        If mutation tokens are enabled, they can be used for advanced durability requirements, as well as optimized RYOW consistency.  # noqa: E501

        :return: The mutation_tokens_enabled of this CouchbaseConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._mutation_tokens_enabled

    @mutation_tokens_enabled.setter
    def mutation_tokens_enabled(self, mutation_tokens_enabled):
        """Sets the mutation_tokens_enabled of this CouchbaseConfiguration.

        If mutation tokens are enabled, they can be used for advanced durability requirements, as well as optimized RYOW consistency.  # noqa: E501

        :param mutation_tokens_enabled: The mutation_tokens_enabled of this CouchbaseConfiguration.  # noqa: E501
        :type: bool
        """

        self._mutation_tokens_enabled = mutation_tokens_enabled

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this CouchbaseConfiguration.  # noqa: E501


        :return: The connect_timeout of this CouchbaseConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this CouchbaseConfiguration.


        :param connect_timeout: The connect_timeout of this CouchbaseConfiguration.  # noqa: E501
        :type: int
        """

        self._connect_timeout = connect_timeout

    @property
    def computation_pool_size(self):
        """Gets the computation_pool_size of this CouchbaseConfiguration.  # noqa: E501

        Sets the pool size (number of threads to use) for all non-blocking operations, default value is the number of CPUs.  # noqa: E501

        :return: The computation_pool_size of this CouchbaseConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._computation_pool_size

    @computation_pool_size.setter
    def computation_pool_size(self, computation_pool_size):
        """Sets the computation_pool_size of this CouchbaseConfiguration.

        Sets the pool size (number of threads to use) for all non-blocking operations, default value is the number of CPUs.  # noqa: E501

        :param computation_pool_size: The computation_pool_size of this CouchbaseConfiguration.  # noqa: E501
        :type: int
        """

        self._computation_pool_size = computation_pool_size

    @property
    def use_ssl(self):
        """Gets the use_ssl of this CouchbaseConfiguration.  # noqa: E501


        :return: The use_ssl of this CouchbaseConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this CouchbaseConfiguration.


        :param use_ssl: The use_ssl of this CouchbaseConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_ssl = use_ssl

    @property
    def ssl_trust_store_file(self):
        """Gets the ssl_trust_store_file of this CouchbaseConfiguration.  # noqa: E501

        The path to the trust store file to use. It contains the trusted certificates.  # noqa: E501

        :return: The ssl_trust_store_file of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._ssl_trust_store_file

    @ssl_trust_store_file.setter
    def ssl_trust_store_file(self, ssl_trust_store_file):
        """Sets the ssl_trust_store_file of this CouchbaseConfiguration.

        The path to the trust store file to use. It contains the trusted certificates.  # noqa: E501

        :param ssl_trust_store_file: The ssl_trust_store_file of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._ssl_trust_store_file = ssl_trust_store_file

    @property
    def ssl_trust_store_pin(self):
        """Gets the ssl_trust_store_pin of this CouchbaseConfiguration.  # noqa: E501

        The PIN to use to access the contents of the trust store.  # noqa: E501

        :return: The ssl_trust_store_pin of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._ssl_trust_store_pin

    @ssl_trust_store_pin.setter
    def ssl_trust_store_pin(self, ssl_trust_store_pin):
        """Sets the ssl_trust_store_pin of this CouchbaseConfiguration.

        The PIN to use to access the contents of the trust store.  # noqa: E501

        :param ssl_trust_store_pin: The ssl_trust_store_pin of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._ssl_trust_store_pin = ssl_trust_store_pin

    @property
    def ssl_trust_store_format(self):
        """Gets the ssl_trust_store_format of this CouchbaseConfiguration.  # noqa: E501

        The format to use for the trust store.  # noqa: E501

        :return: The ssl_trust_store_format of this CouchbaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._ssl_trust_store_format

    @ssl_trust_store_format.setter
    def ssl_trust_store_format(self, ssl_trust_store_format):
        """Sets the ssl_trust_store_format of this CouchbaseConfiguration.

        The format to use for the trust store.  # noqa: E501

        :param ssl_trust_store_format: The ssl_trust_store_format of this CouchbaseConfiguration.  # noqa: E501
        :type: str
        """

        self._ssl_trust_store_format = ssl_trust_store_format

    @property
    def binary_attributes(self):
        """Gets the binary_attributes of this CouchbaseConfiguration.  # noqa: E501

        List of binary attributes.  # noqa: E501

        :return: The binary_attributes of this CouchbaseConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_attributes

    @binary_attributes.setter
    def binary_attributes(self, binary_attributes):
        """Sets the binary_attributes of this CouchbaseConfiguration.

        List of binary attributes.  # noqa: E501

        :param binary_attributes: The binary_attributes of this CouchbaseConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._binary_attributes = binary_attributes

    @property
    def certificate_attributes(self):
        """Gets the certificate_attributes of this CouchbaseConfiguration.  # noqa: E501

        List of certificate attributes.  # noqa: E501

        :return: The certificate_attributes of this CouchbaseConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._certificate_attributes

    @certificate_attributes.setter
    def certificate_attributes(self, certificate_attributes):
        """Sets the certificate_attributes of this CouchbaseConfiguration.

        List of certificate attributes.  # noqa: E501

        :param certificate_attributes: The certificate_attributes of this CouchbaseConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._certificate_attributes = certificate_attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CouchbaseConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CouchbaseConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
