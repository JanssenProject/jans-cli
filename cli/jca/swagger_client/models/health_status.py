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

class HealthStatus(object):
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
        'status': 'str',
        'error': 'str',
        'checks': 'list[HealthStatusItem]'
    }

    attribute_map = {
        'status': 'status',
        'error': 'error',
        'checks': 'checks'
    }

    def __init__(self, status=None, error=None, checks=None):  # noqa: E501
        """HealthStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._error = None
        self._checks = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if checks is not None:
            self.checks = checks

    @property
    def status(self):
        """Gets the status of this HealthStatus.  # noqa: E501

        Health parameter name  # noqa: E501

        :return: The status of this HealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HealthStatus.

        Health parameter name  # noqa: E501

        :param status: The status of this HealthStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this HealthStatus.  # noqa: E501

        error message in case of error  # noqa: E501

        :return: The error of this HealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this HealthStatus.

        error message in case of error  # noqa: E501

        :param error: The error of this HealthStatus.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def checks(self):
        """Gets the checks of this HealthStatus.  # noqa: E501


        :return: The checks of this HealthStatus.  # noqa: E501
        :rtype: list[HealthStatusItem]
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this HealthStatus.


        :param checks: The checks of this HealthStatus.  # noqa: E501
        :type: list[HealthStatusItem]
        """

        self._checks = checks

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
        if issubclass(HealthStatus, dict):
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
        if not isinstance(other, HealthStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
