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

class Fido2Configuration(object):
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
        'authenticator_certs_folder': 'str',
        'mds_certs_folder': 'str',
        'mds_tocs_folder': 'str',
        'server_metadata_folder': 'str',
        'requested_parties': 'list[RequestedParties]',
        'user_auto_enrollment': 'bool',
        'unfinished_request_expiration': 'int',
        'authentication_history_expiration': 'int',
        'requested_credential_types': 'list[str]'
    }

    attribute_map = {
        'authenticator_certs_folder': 'authenticatorCertsFolder',
        'mds_certs_folder': 'mdsCertsFolder',
        'mds_tocs_folder': 'mdsTocsFolder',
        'server_metadata_folder': 'serverMetadataFolder',
        'requested_parties': 'requestedParties',
        'user_auto_enrollment': 'userAutoEnrollment',
        'unfinished_request_expiration': 'unfinishedRequestExpiration',
        'authentication_history_expiration': 'authenticationHistoryExpiration',
        'requested_credential_types': 'requestedCredentialTypes'
    }

    def __init__(self, authenticator_certs_folder=None, mds_certs_folder=None, mds_tocs_folder=None, server_metadata_folder=None, requested_parties=None, user_auto_enrollment=None, unfinished_request_expiration=None, authentication_history_expiration=None, requested_credential_types=None):  # noqa: E501
        """Fido2Configuration - a model defined in Swagger"""  # noqa: E501
        self._authenticator_certs_folder = None
        self._mds_certs_folder = None
        self._mds_tocs_folder = None
        self._server_metadata_folder = None
        self._requested_parties = None
        self._user_auto_enrollment = None
        self._unfinished_request_expiration = None
        self._authentication_history_expiration = None
        self._requested_credential_types = None
        self.discriminator = None
        if authenticator_certs_folder is not None:
            self.authenticator_certs_folder = authenticator_certs_folder
        if mds_certs_folder is not None:
            self.mds_certs_folder = mds_certs_folder
        if mds_tocs_folder is not None:
            self.mds_tocs_folder = mds_tocs_folder
        if server_metadata_folder is not None:
            self.server_metadata_folder = server_metadata_folder
        if requested_parties is not None:
            self.requested_parties = requested_parties
        if user_auto_enrollment is not None:
            self.user_auto_enrollment = user_auto_enrollment
        if unfinished_request_expiration is not None:
            self.unfinished_request_expiration = unfinished_request_expiration
        if authentication_history_expiration is not None:
            self.authentication_history_expiration = authentication_history_expiration
        if requested_credential_types is not None:
            self.requested_credential_types = requested_credential_types

    @property
    def authenticator_certs_folder(self):
        """Gets the authenticator_certs_folder of this Fido2Configuration.  # noqa: E501

        Authenticators certificates fodler.  # noqa: E501

        :return: The authenticator_certs_folder of this Fido2Configuration.  # noqa: E501
        :rtype: str
        """
        return self._authenticator_certs_folder

    @authenticator_certs_folder.setter
    def authenticator_certs_folder(self, authenticator_certs_folder):
        """Sets the authenticator_certs_folder of this Fido2Configuration.

        Authenticators certificates fodler.  # noqa: E501

        :param authenticator_certs_folder: The authenticator_certs_folder of this Fido2Configuration.  # noqa: E501
        :type: str
        """

        self._authenticator_certs_folder = authenticator_certs_folder

    @property
    def mds_certs_folder(self):
        """Gets the mds_certs_folder of this Fido2Configuration.  # noqa: E501

        MDS TOC root certificates folder.  # noqa: E501

        :return: The mds_certs_folder of this Fido2Configuration.  # noqa: E501
        :rtype: str
        """
        return self._mds_certs_folder

    @mds_certs_folder.setter
    def mds_certs_folder(self, mds_certs_folder):
        """Sets the mds_certs_folder of this Fido2Configuration.

        MDS TOC root certificates folder.  # noqa: E501

        :param mds_certs_folder: The mds_certs_folder of this Fido2Configuration.  # noqa: E501
        :type: str
        """

        self._mds_certs_folder = mds_certs_folder

    @property
    def mds_tocs_folder(self):
        """Gets the mds_tocs_folder of this Fido2Configuration.  # noqa: E501

        MDS TOC files folder.  # noqa: E501

        :return: The mds_tocs_folder of this Fido2Configuration.  # noqa: E501
        :rtype: str
        """
        return self._mds_tocs_folder

    @mds_tocs_folder.setter
    def mds_tocs_folder(self, mds_tocs_folder):
        """Sets the mds_tocs_folder of this Fido2Configuration.

        MDS TOC files folder.  # noqa: E501

        :param mds_tocs_folder: The mds_tocs_folder of this Fido2Configuration.  # noqa: E501
        :type: str
        """

        self._mds_tocs_folder = mds_tocs_folder

    @property
    def server_metadata_folder(self):
        """Gets the server_metadata_folder of this Fido2Configuration.  # noqa: E501

        Authenticators metadata in json format.  # noqa: E501

        :return: The server_metadata_folder of this Fido2Configuration.  # noqa: E501
        :rtype: str
        """
        return self._server_metadata_folder

    @server_metadata_folder.setter
    def server_metadata_folder(self, server_metadata_folder):
        """Sets the server_metadata_folder of this Fido2Configuration.

        Authenticators metadata in json format.  # noqa: E501

        :param server_metadata_folder: The server_metadata_folder of this Fido2Configuration.  # noqa: E501
        :type: str
        """

        self._server_metadata_folder = server_metadata_folder

    @property
    def requested_parties(self):
        """Gets the requested_parties of this Fido2Configuration.  # noqa: E501

        Authenticators metadata in json format.  # noqa: E501

        :return: The requested_parties of this Fido2Configuration.  # noqa: E501
        :rtype: list[RequestedParties]
        """
        return self._requested_parties

    @requested_parties.setter
    def requested_parties(self, requested_parties):
        """Sets the requested_parties of this Fido2Configuration.

        Authenticators metadata in json format.  # noqa: E501

        :param requested_parties: The requested_parties of this Fido2Configuration.  # noqa: E501
        :type: list[RequestedParties]
        """

        self._requested_parties = requested_parties

    @property
    def user_auto_enrollment(self):
        """Gets the user_auto_enrollment of this Fido2Configuration.  # noqa: E501

        Allow to enroll users on enrollment/authentication requests.  # noqa: E501

        :return: The user_auto_enrollment of this Fido2Configuration.  # noqa: E501
        :rtype: bool
        """
        return self._user_auto_enrollment

    @user_auto_enrollment.setter
    def user_auto_enrollment(self, user_auto_enrollment):
        """Sets the user_auto_enrollment of this Fido2Configuration.

        Allow to enroll users on enrollment/authentication requests.  # noqa: E501

        :param user_auto_enrollment: The user_auto_enrollment of this Fido2Configuration.  # noqa: E501
        :type: bool
        """

        self._user_auto_enrollment = user_auto_enrollment

    @property
    def unfinished_request_expiration(self):
        """Gets the unfinished_request_expiration of this Fido2Configuration.  # noqa: E501

        Expiration time in seconds for pending enrollment/authentication requests  # noqa: E501

        :return: The unfinished_request_expiration of this Fido2Configuration.  # noqa: E501
        :rtype: int
        """
        return self._unfinished_request_expiration

    @unfinished_request_expiration.setter
    def unfinished_request_expiration(self, unfinished_request_expiration):
        """Sets the unfinished_request_expiration of this Fido2Configuration.

        Expiration time in seconds for pending enrollment/authentication requests  # noqa: E501

        :param unfinished_request_expiration: The unfinished_request_expiration of this Fido2Configuration.  # noqa: E501
        :type: int
        """

        self._unfinished_request_expiration = unfinished_request_expiration

    @property
    def authentication_history_expiration(self):
        """Gets the authentication_history_expiration of this Fido2Configuration.  # noqa: E501

        Expiration time in seconds for approved authentication requests.  # noqa: E501

        :return: The authentication_history_expiration of this Fido2Configuration.  # noqa: E501
        :rtype: int
        """
        return self._authentication_history_expiration

    @authentication_history_expiration.setter
    def authentication_history_expiration(self, authentication_history_expiration):
        """Sets the authentication_history_expiration of this Fido2Configuration.

        Expiration time in seconds for approved authentication requests.  # noqa: E501

        :param authentication_history_expiration: The authentication_history_expiration of this Fido2Configuration.  # noqa: E501
        :type: int
        """

        self._authentication_history_expiration = authentication_history_expiration

    @property
    def requested_credential_types(self):
        """Gets the requested_credential_types of this Fido2Configuration.  # noqa: E501

        List of Requested Credential Types.  # noqa: E501

        :return: The requested_credential_types of this Fido2Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._requested_credential_types

    @requested_credential_types.setter
    def requested_credential_types(self, requested_credential_types):
        """Sets the requested_credential_types of this Fido2Configuration.

        List of Requested Credential Types.  # noqa: E501

        :param requested_credential_types: The requested_credential_types of this Fido2Configuration.  # noqa: E501
        :type: list[str]
        """

        self._requested_credential_types = requested_credential_types

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
        if issubclass(Fido2Configuration, dict):
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
        if not isinstance(other, Fido2Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
