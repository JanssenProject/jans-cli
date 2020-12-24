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

class NativePersistenceConfiguration(object):
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
        'default_put_expiration': 'int',
        'default_cleanup_batch_size': 'int',
        'delete_expired_on_get_request': 'bool'
    }

    attribute_map = {
        'default_put_expiration': 'defaultPutExpiration',
        'default_cleanup_batch_size': 'defaultCleanupBatchSize',
        'delete_expired_on_get_request': 'deleteExpiredOnGetRequest'
    }

    def __init__(self, default_put_expiration=None, default_cleanup_batch_size=None, delete_expired_on_get_request=None):  # noqa: E501
        """NativePersistenceConfiguration - a model defined in Swagger"""  # noqa: E501
        self._default_put_expiration = None
        self._default_cleanup_batch_size = None
        self._delete_expired_on_get_request = None
        self.discriminator = None
        if default_put_expiration is not None:
            self.default_put_expiration = default_put_expiration
        if default_cleanup_batch_size is not None:
            self.default_cleanup_batch_size = default_cleanup_batch_size
        if delete_expired_on_get_request is not None:
            self.delete_expired_on_get_request = delete_expired_on_get_request

    @property
    def default_put_expiration(self):
        """Gets the default_put_expiration of this NativePersistenceConfiguration.  # noqa: E501

        defaultPutExpiration timeout value.  # noqa: E501

        :return: The default_put_expiration of this NativePersistenceConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._default_put_expiration

    @default_put_expiration.setter
    def default_put_expiration(self, default_put_expiration):
        """Sets the default_put_expiration of this NativePersistenceConfiguration.

        defaultPutExpiration timeout value.  # noqa: E501

        :param default_put_expiration: The default_put_expiration of this NativePersistenceConfiguration.  # noqa: E501
        :type: int
        """

        self._default_put_expiration = default_put_expiration

    @property
    def default_cleanup_batch_size(self):
        """Gets the default_cleanup_batch_size of this NativePersistenceConfiguration.  # noqa: E501

        defaultCleanupBatchSize page size.  # noqa: E501

        :return: The default_cleanup_batch_size of this NativePersistenceConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._default_cleanup_batch_size

    @default_cleanup_batch_size.setter
    def default_cleanup_batch_size(self, default_cleanup_batch_size):
        """Sets the default_cleanup_batch_size of this NativePersistenceConfiguration.

        defaultCleanupBatchSize page size.  # noqa: E501

        :param default_cleanup_batch_size: The default_cleanup_batch_size of this NativePersistenceConfiguration.  # noqa: E501
        :type: int
        """

        self._default_cleanup_batch_size = default_cleanup_batch_size

    @property
    def delete_expired_on_get_request(self):
        """Gets the delete_expired_on_get_request of this NativePersistenceConfiguration.  # noqa: E501


        :return: The delete_expired_on_get_request of this NativePersistenceConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._delete_expired_on_get_request

    @delete_expired_on_get_request.setter
    def delete_expired_on_get_request(self, delete_expired_on_get_request):
        """Sets the delete_expired_on_get_request of this NativePersistenceConfiguration.


        :param delete_expired_on_get_request: The delete_expired_on_get_request of this NativePersistenceConfiguration.  # noqa: E501
        :type: bool
        """

        self._delete_expired_on_get_request = delete_expired_on_get_request

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
        if issubclass(NativePersistenceConfiguration, dict):
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
        if not isinstance(other, NativePersistenceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
