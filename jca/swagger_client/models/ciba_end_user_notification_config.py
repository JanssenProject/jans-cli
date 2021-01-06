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

class CIBAEndUserNotificationConfig(object):
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
        'api_key': 'str',
        'auth_domain': 'str',
        'database_url': 'str',
        'project_id': 'str',
        'storage_bucket': 'str',
        'messaging_sender_id': 'str',
        'app_id': 'str',
        'notification_url': 'str',
        'notification_key': 'str',
        'public_vapid_key': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'auth_domain': 'authDomain',
        'database_url': 'databaseURL',
        'project_id': 'projectId',
        'storage_bucket': 'storageBucket',
        'messaging_sender_id': 'messagingSenderId',
        'app_id': 'appId',
        'notification_url': 'notificationUrl',
        'notification_key': 'notificationKey',
        'public_vapid_key': 'publicVapidKey'
    }

    def __init__(self, api_key=None, auth_domain=None, database_url=None, project_id=None, storage_bucket=None, messaging_sender_id=None, app_id=None, notification_url=None, notification_key=None, public_vapid_key=None):  # noqa: E501
        """CIBAEndUserNotificationConfig - a model defined in Swagger"""  # noqa: E501
        self._api_key = None
        self._auth_domain = None
        self._database_url = None
        self._project_id = None
        self._storage_bucket = None
        self._messaging_sender_id = None
        self._app_id = None
        self._notification_url = None
        self._notification_key = None
        self._public_vapid_key = None
        self.discriminator = None
        if api_key is not None:
            self.api_key = api_key
        if auth_domain is not None:
            self.auth_domain = auth_domain
        if database_url is not None:
            self.database_url = database_url
        if project_id is not None:
            self.project_id = project_id
        if storage_bucket is not None:
            self.storage_bucket = storage_bucket
        if messaging_sender_id is not None:
            self.messaging_sender_id = messaging_sender_id
        if app_id is not None:
            self.app_id = app_id
        if notification_url is not None:
            self.notification_url = notification_url
        if notification_key is not None:
            self.notification_key = notification_key
        if public_vapid_key is not None:
            self.public_vapid_key = public_vapid_key

    @property
    def api_key(self):
        """Gets the api_key of this CIBAEndUserNotificationConfig.  # noqa: E501

        API Key  # noqa: E501

        :return: The api_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this CIBAEndUserNotificationConfig.

        API Key  # noqa: E501

        :param api_key: The api_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def auth_domain(self):
        """Gets the auth_domain of this CIBAEndUserNotificationConfig.  # noqa: E501

        Auth Domain  # noqa: E501

        :return: The auth_domain of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._auth_domain

    @auth_domain.setter
    def auth_domain(self, auth_domain):
        """Sets the auth_domain of this CIBAEndUserNotificationConfig.

        Auth Domain  # noqa: E501

        :param auth_domain: The auth_domain of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._auth_domain = auth_domain

    @property
    def database_url(self):
        """Gets the database_url of this CIBAEndUserNotificationConfig.  # noqa: E501

        Database URL  # noqa: E501

        :return: The database_url of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._database_url

    @database_url.setter
    def database_url(self, database_url):
        """Sets the database_url of this CIBAEndUserNotificationConfig.

        Database URL  # noqa: E501

        :param database_url: The database_url of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._database_url = database_url

    @property
    def project_id(self):
        """Gets the project_id of this CIBAEndUserNotificationConfig.  # noqa: E501

        Project ID  # noqa: E501

        :return: The project_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CIBAEndUserNotificationConfig.

        Project ID  # noqa: E501

        :param project_id: The project_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def storage_bucket(self):
        """Gets the storage_bucket of this CIBAEndUserNotificationConfig.  # noqa: E501

        Storage Bucket  # noqa: E501

        :return: The storage_bucket of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._storage_bucket

    @storage_bucket.setter
    def storage_bucket(self, storage_bucket):
        """Sets the storage_bucket of this CIBAEndUserNotificationConfig.

        Storage Bucket  # noqa: E501

        :param storage_bucket: The storage_bucket of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._storage_bucket = storage_bucket

    @property
    def messaging_sender_id(self):
        """Gets the messaging_sender_id of this CIBAEndUserNotificationConfig.  # noqa: E501

        Messaging Sender ID  # noqa: E501

        :return: The messaging_sender_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._messaging_sender_id

    @messaging_sender_id.setter
    def messaging_sender_id(self, messaging_sender_id):
        """Sets the messaging_sender_id of this CIBAEndUserNotificationConfig.

        Messaging Sender ID  # noqa: E501

        :param messaging_sender_id: The messaging_sender_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._messaging_sender_id = messaging_sender_id

    @property
    def app_id(self):
        """Gets the app_id of this CIBAEndUserNotificationConfig.  # noqa: E501

        App ID  # noqa: E501

        :return: The app_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CIBAEndUserNotificationConfig.

        App ID  # noqa: E501

        :param app_id: The app_id of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def notification_url(self):
        """Gets the notification_url of this CIBAEndUserNotificationConfig.  # noqa: E501

        Notification URL  # noqa: E501

        :return: The notification_url of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._notification_url

    @notification_url.setter
    def notification_url(self, notification_url):
        """Sets the notification_url of this CIBAEndUserNotificationConfig.

        Notification URL  # noqa: E501

        :param notification_url: The notification_url of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._notification_url = notification_url

    @property
    def notification_key(self):
        """Gets the notification_key of this CIBAEndUserNotificationConfig.  # noqa: E501

        Notification Key  # noqa: E501

        :return: The notification_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._notification_key

    @notification_key.setter
    def notification_key(self, notification_key):
        """Sets the notification_key of this CIBAEndUserNotificationConfig.

        Notification Key  # noqa: E501

        :param notification_key: The notification_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._notification_key = notification_key

    @property
    def public_vapid_key(self):
        """Gets the public_vapid_key of this CIBAEndUserNotificationConfig.  # noqa: E501

        Public Vapid Key  # noqa: E501

        :return: The public_vapid_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._public_vapid_key

    @public_vapid_key.setter
    def public_vapid_key(self, public_vapid_key):
        """Sets the public_vapid_key of this CIBAEndUserNotificationConfig.

        Public Vapid Key  # noqa: E501

        :param public_vapid_key: The public_vapid_key of this CIBAEndUserNotificationConfig.  # noqa: E501
        :type: str
        """

        self._public_vapid_key = public_vapid_key

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
        if issubclass(CIBAEndUserNotificationConfig, dict):
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
        if not isinstance(other, CIBAEndUserNotificationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other