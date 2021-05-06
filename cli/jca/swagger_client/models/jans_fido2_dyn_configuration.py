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

class JansFido2DynConfiguration(object):
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
        'issuer': 'str',
        'base_endpoint': 'str',
        'clean_service_interval': 'int',
        'clean_service_batch_chunk_size': 'int',
        'use_local_cache': 'bool',
        'disable_jdk_logger': 'bool',
        'logging_level': 'str',
        'logging_layout': 'str',
        'external_logger_configuration': 'str',
        'metric_reporter_interval': 'int',
        'metric_reporter_keep_data_days': 'int',
        'metric_reporter_enabled': 'bool',
        'person_custom_object_class_list': 'list[str]',
        'fido2_configuration': 'Fido2Configuration'
    }

    attribute_map = {
        'issuer': 'issuer',
        'base_endpoint': 'baseEndpoint',
        'clean_service_interval': 'cleanServiceInterval',
        'clean_service_batch_chunk_size': 'cleanServiceBatchChunkSize',
        'use_local_cache': 'useLocalCache',
        'disable_jdk_logger': 'disableJdkLogger',
        'logging_level': 'loggingLevel',
        'logging_layout': 'loggingLayout',
        'external_logger_configuration': 'externalLoggerConfiguration',
        'metric_reporter_interval': 'metricReporterInterval',
        'metric_reporter_keep_data_days': 'metricReporterKeepDataDays',
        'metric_reporter_enabled': 'metricReporterEnabled',
        'person_custom_object_class_list': 'personCustomObjectClassList',
        'fido2_configuration': 'fido2Configuration'
    }

    def __init__(self, issuer=None, base_endpoint=None, clean_service_interval=None, clean_service_batch_chunk_size=None, use_local_cache=None, disable_jdk_logger=None, logging_level=None, logging_layout=None, external_logger_configuration=None, metric_reporter_interval=None, metric_reporter_keep_data_days=None, metric_reporter_enabled=None, person_custom_object_class_list=None, fido2_configuration=None):  # noqa: E501
        """JansFido2DynConfiguration - a model defined in Swagger"""  # noqa: E501
        self._issuer = None
        self._base_endpoint = None
        self._clean_service_interval = None
        self._clean_service_batch_chunk_size = None
        self._use_local_cache = None
        self._disable_jdk_logger = None
        self._logging_level = None
        self._logging_layout = None
        self._external_logger_configuration = None
        self._metric_reporter_interval = None
        self._metric_reporter_keep_data_days = None
        self._metric_reporter_enabled = None
        self._person_custom_object_class_list = None
        self._fido2_configuration = None
        self.discriminator = None
        if issuer is not None:
            self.issuer = issuer
        if base_endpoint is not None:
            self.base_endpoint = base_endpoint
        if clean_service_interval is not None:
            self.clean_service_interval = clean_service_interval
        if clean_service_batch_chunk_size is not None:
            self.clean_service_batch_chunk_size = clean_service_batch_chunk_size
        if use_local_cache is not None:
            self.use_local_cache = use_local_cache
        if disable_jdk_logger is not None:
            self.disable_jdk_logger = disable_jdk_logger
        if logging_level is not None:
            self.logging_level = logging_level
        if logging_layout is not None:
            self.logging_layout = logging_layout
        if external_logger_configuration is not None:
            self.external_logger_configuration = external_logger_configuration
        if metric_reporter_interval is not None:
            self.metric_reporter_interval = metric_reporter_interval
        if metric_reporter_keep_data_days is not None:
            self.metric_reporter_keep_data_days = metric_reporter_keep_data_days
        if metric_reporter_enabled is not None:
            self.metric_reporter_enabled = metric_reporter_enabled
        if person_custom_object_class_list is not None:
            self.person_custom_object_class_list = person_custom_object_class_list
        if fido2_configuration is not None:
            self.fido2_configuration = fido2_configuration

    @property
    def issuer(self):
        """Gets the issuer of this JansFido2DynConfiguration.  # noqa: E501

        URL using the https scheme for Issuer identifier.  # noqa: E501

        :return: The issuer of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this JansFido2DynConfiguration.

        URL using the https scheme for Issuer identifier.  # noqa: E501

        :param issuer: The issuer of this JansFido2DynConfiguration.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def base_endpoint(self):
        """Gets the base_endpoint of this JansFido2DynConfiguration.  # noqa: E501

        The base URL for Fido2 endpoints.  # noqa: E501

        :return: The base_endpoint of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._base_endpoint

    @base_endpoint.setter
    def base_endpoint(self, base_endpoint):
        """Sets the base_endpoint of this JansFido2DynConfiguration.

        The base URL for Fido2 endpoints.  # noqa: E501

        :param base_endpoint: The base_endpoint of this JansFido2DynConfiguration.  # noqa: E501
        :type: str
        """

        self._base_endpoint = base_endpoint

    @property
    def clean_service_interval(self):
        """Gets the clean_service_interval of this JansFido2DynConfiguration.  # noqa: E501

        Time interval for the Clean Service in seconds.  # noqa: E501

        :return: The clean_service_interval of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._clean_service_interval

    @clean_service_interval.setter
    def clean_service_interval(self, clean_service_interval):
        """Sets the clean_service_interval of this JansFido2DynConfiguration.

        Time interval for the Clean Service in seconds.  # noqa: E501

        :param clean_service_interval: The clean_service_interval of this JansFido2DynConfiguration.  # noqa: E501
        :type: int
        """

        self._clean_service_interval = clean_service_interval

    @property
    def clean_service_batch_chunk_size(self):
        """Gets the clean_service_batch_chunk_size of this JansFido2DynConfiguration.  # noqa: E501

        Each clean up iteration fetches chunk of expired data per base dn and removes it from storage.  # noqa: E501

        :return: The clean_service_batch_chunk_size of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._clean_service_batch_chunk_size

    @clean_service_batch_chunk_size.setter
    def clean_service_batch_chunk_size(self, clean_service_batch_chunk_size):
        """Sets the clean_service_batch_chunk_size of this JansFido2DynConfiguration.

        Each clean up iteration fetches chunk of expired data per base dn and removes it from storage.  # noqa: E501

        :param clean_service_batch_chunk_size: The clean_service_batch_chunk_size of this JansFido2DynConfiguration.  # noqa: E501
        :type: int
        """

        self._clean_service_batch_chunk_size = clean_service_batch_chunk_size

    @property
    def use_local_cache(self):
        """Gets the use_local_cache of this JansFido2DynConfiguration.  # noqa: E501

        Boolean value to indicate if Local Cache is to be used.  # noqa: E501

        :return: The use_local_cache of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_local_cache

    @use_local_cache.setter
    def use_local_cache(self, use_local_cache):
        """Sets the use_local_cache of this JansFido2DynConfiguration.

        Boolean value to indicate if Local Cache is to be used.  # noqa: E501

        :param use_local_cache: The use_local_cache of this JansFido2DynConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_local_cache = use_local_cache

    @property
    def disable_jdk_logger(self):
        """Gets the disable_jdk_logger of this JansFido2DynConfiguration.  # noqa: E501

        Boolean value specifying whether to enable JDK Loggers.  # noqa: E501

        :return: The disable_jdk_logger of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._disable_jdk_logger

    @disable_jdk_logger.setter
    def disable_jdk_logger(self, disable_jdk_logger):
        """Sets the disable_jdk_logger of this JansFido2DynConfiguration.

        Boolean value specifying whether to enable JDK Loggers.  # noqa: E501

        :param disable_jdk_logger: The disable_jdk_logger of this JansFido2DynConfiguration.  # noqa: E501
        :type: bool
        """

        self._disable_jdk_logger = disable_jdk_logger

    @property
    def logging_level(self):
        """Gets the logging_level of this JansFido2DynConfiguration.  # noqa: E501

        Logging level for Fido2 logger.  # noqa: E501

        :return: The logging_level of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._logging_level

    @logging_level.setter
    def logging_level(self, logging_level):
        """Sets the logging_level of this JansFido2DynConfiguration.

        Logging level for Fido2 logger.  # noqa: E501

        :param logging_level: The logging_level of this JansFido2DynConfiguration.  # noqa: E501
        :type: str
        """

        self._logging_level = logging_level

    @property
    def logging_layout(self):
        """Gets the logging_layout of this JansFido2DynConfiguration.  # noqa: E501

        Logging layout used for Fido2.  # noqa: E501

        :return: The logging_layout of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._logging_layout

    @logging_layout.setter
    def logging_layout(self, logging_layout):
        """Sets the logging_layout of this JansFido2DynConfiguration.

        Logging layout used for Fido2.  # noqa: E501

        :param logging_layout: The logging_layout of this JansFido2DynConfiguration.  # noqa: E501
        :type: str
        """

        self._logging_layout = logging_layout

    @property
    def external_logger_configuration(self):
        """Gets the external_logger_configuration of this JansFido2DynConfiguration.  # noqa: E501

        Path to external Fido2 logging configuration.  # noqa: E501

        :return: The external_logger_configuration of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._external_logger_configuration

    @external_logger_configuration.setter
    def external_logger_configuration(self, external_logger_configuration):
        """Sets the external_logger_configuration of this JansFido2DynConfiguration.

        Path to external Fido2 logging configuration.  # noqa: E501

        :param external_logger_configuration: The external_logger_configuration of this JansFido2DynConfiguration.  # noqa: E501
        :type: str
        """

        self._external_logger_configuration = external_logger_configuration

    @property
    def metric_reporter_interval(self):
        """Gets the metric_reporter_interval of this JansFido2DynConfiguration.  # noqa: E501

        The interval for metric reporter in seconds.  # noqa: E501

        :return: The metric_reporter_interval of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._metric_reporter_interval

    @metric_reporter_interval.setter
    def metric_reporter_interval(self, metric_reporter_interval):
        """Sets the metric_reporter_interval of this JansFido2DynConfiguration.

        The interval for metric reporter in seconds.  # noqa: E501

        :param metric_reporter_interval: The metric_reporter_interval of this JansFido2DynConfiguration.  # noqa: E501
        :type: int
        """

        self._metric_reporter_interval = metric_reporter_interval

    @property
    def metric_reporter_keep_data_days(self):
        """Gets the metric_reporter_keep_data_days of this JansFido2DynConfiguration.  # noqa: E501

        The days to keep report data.  # noqa: E501

        :return: The metric_reporter_keep_data_days of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._metric_reporter_keep_data_days

    @metric_reporter_keep_data_days.setter
    def metric_reporter_keep_data_days(self, metric_reporter_keep_data_days):
        """Sets the metric_reporter_keep_data_days of this JansFido2DynConfiguration.

        The days to keep report data.  # noqa: E501

        :param metric_reporter_keep_data_days: The metric_reporter_keep_data_days of this JansFido2DynConfiguration.  # noqa: E501
        :type: int
        """

        self._metric_reporter_keep_data_days = metric_reporter_keep_data_days

    @property
    def metric_reporter_enabled(self):
        """Gets the metric_reporter_enabled of this JansFido2DynConfiguration.  # noqa: E501

        Boolean value specifying whether to enable Metric Reporter.  # noqa: E501

        :return: The metric_reporter_enabled of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._metric_reporter_enabled

    @metric_reporter_enabled.setter
    def metric_reporter_enabled(self, metric_reporter_enabled):
        """Sets the metric_reporter_enabled of this JansFido2DynConfiguration.

        Boolean value specifying whether to enable Metric Reporter.  # noqa: E501

        :param metric_reporter_enabled: The metric_reporter_enabled of this JansFido2DynConfiguration.  # noqa: E501
        :type: bool
        """

        self._metric_reporter_enabled = metric_reporter_enabled

    @property
    def person_custom_object_class_list(self):
        """Gets the person_custom_object_class_list of this JansFido2DynConfiguration.  # noqa: E501

        Custom object class list for dynamic person enrolment.  # noqa: E501

        :return: The person_custom_object_class_list of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._person_custom_object_class_list

    @person_custom_object_class_list.setter
    def person_custom_object_class_list(self, person_custom_object_class_list):
        """Sets the person_custom_object_class_list of this JansFido2DynConfiguration.

        Custom object class list for dynamic person enrolment.  # noqa: E501

        :param person_custom_object_class_list: The person_custom_object_class_list of this JansFido2DynConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._person_custom_object_class_list = person_custom_object_class_list

    @property
    def fido2_configuration(self):
        """Gets the fido2_configuration of this JansFido2DynConfiguration.  # noqa: E501


        :return: The fido2_configuration of this JansFido2DynConfiguration.  # noqa: E501
        :rtype: Fido2Configuration
        """
        return self._fido2_configuration

    @fido2_configuration.setter
    def fido2_configuration(self, fido2_configuration):
        """Sets the fido2_configuration of this JansFido2DynConfiguration.


        :param fido2_configuration: The fido2_configuration of this JansFido2DynConfiguration.  # noqa: E501
        :type: Fido2Configuration
        """

        self._fido2_configuration = fido2_configuration

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
        if issubclass(JansFido2DynConfiguration, dict):
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
        if not isinstance(other, JansFido2DynConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other