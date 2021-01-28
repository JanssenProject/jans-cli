# coding: utf-8

"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.base_resource import BaseResource  # noqa: F401,E501

class UserResource(BaseResource):
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
        'external_id': 'str',
        'user_name': 'str',
        'name': 'Name',
        'display_name': 'str',
        'nick_name': 'str',
        'profile_url': 'str',
        'title': 'str',
        'user_type': 'str',
        'preferred_language': 'str',
        'locale': 'str',
        'timezone': 'str',
        'active': 'bool',
        'password': 'str',
        'emails': 'list[Email]',
        'phone_numbers': 'list[PhoneNumber]',
        'ims': 'list[InstantMessagingAddress]',
        'photos': 'list[Photo]',
        'addresses': 'list[Address]',
        'groups': 'list[Group]',
        'entitlements': 'list[Entitlement]',
        'roles': 'list[Role]',
        'x509_certificates': 'list[X509Certificate]',
        'urnietfparamsscimschemasextensiongluu2_0_user': 'object'
    }
    if hasattr(BaseResource, "swagger_types"):
        swagger_types.update(BaseResource.swagger_types)

    attribute_map = {
        'external_id': 'externalId',
        'user_name': 'userName',
        'name': 'name',
        'display_name': 'displayName',
        'nick_name': 'nickName',
        'profile_url': 'profileUrl',
        'title': 'title',
        'user_type': 'userType',
        'preferred_language': 'preferredLanguage',
        'locale': 'locale',
        'timezone': 'timezone',
        'active': 'active',
        'password': 'password',
        'emails': 'emails',
        'phone_numbers': 'phoneNumbers',
        'ims': 'ims',
        'photos': 'photos',
        'addresses': 'addresses',
        'groups': 'groups',
        'entitlements': 'entitlements',
        'roles': 'roles',
        'x509_certificates': 'x509Certificates',
        'urnietfparamsscimschemasextensiongluu2_0_user': 'urn:ietf:params:scim:schemas:extension:gluu:2.0:User'
    }
    if hasattr(BaseResource, "attribute_map"):
        attribute_map.update(BaseResource.attribute_map)

    def __init__(self, external_id=None, user_name=None, name=None, display_name=None, nick_name=None, profile_url=None, title=None, user_type=None, preferred_language=None, locale=None, timezone=None, active=None, password=None, emails=None, phone_numbers=None, ims=None, photos=None, addresses=None, groups=None, entitlements=None, roles=None, x509_certificates=None, urnietfparamsscimschemasextensiongluu2_0_user=None, *args, **kwargs):  # noqa: E501
        """UserResource - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._user_name = None
        self._name = None
        self._display_name = None
        self._nick_name = None
        self._profile_url = None
        self._title = None
        self._user_type = None
        self._preferred_language = None
        self._locale = None
        self._timezone = None
        self._active = None
        self._password = None
        self._emails = None
        self._phone_numbers = None
        self._ims = None
        self._photos = None
        self._addresses = None
        self._groups = None
        self._entitlements = None
        self._roles = None
        self._x509_certificates = None
        self._urnietfparamsscimschemasextensiongluu2_0_user = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if nick_name is not None:
            self.nick_name = nick_name
        if profile_url is not None:
            self.profile_url = profile_url
        if title is not None:
            self.title = title
        if user_type is not None:
            self.user_type = user_type
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if locale is not None:
            self.locale = locale
        if timezone is not None:
            self.timezone = timezone
        if active is not None:
            self.active = active
        if password is not None:
            self.password = password
        if emails is not None:
            self.emails = emails
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if ims is not None:
            self.ims = ims
        if photos is not None:
            self.photos = photos
        if addresses is not None:
            self.addresses = addresses
        if groups is not None:
            self.groups = groups
        if entitlements is not None:
            self.entitlements = entitlements
        if roles is not None:
            self.roles = roles
        if x509_certificates is not None:
            self.x509_certificates = x509_certificates
        if urnietfparamsscimschemasextensiongluu2_0_user is not None:
            self.urnietfparamsscimschemasextensiongluu2_0_user = urnietfparamsscimschemasextensiongluu2_0_user
        BaseResource.__init__(self, *args, **kwargs)

    @property
    def external_id(self):
        """Gets the external_id of this UserResource.  # noqa: E501

        Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643  # noqa: E501

        :return: The external_id of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserResource.

        Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643  # noqa: E501

        :param external_id: The external_id of this UserResource.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def user_name(self):
        """Gets the user_name of this UserResource.  # noqa: E501

        Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users)  # noqa: E501

        :return: The user_name of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserResource.

        Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users)  # noqa: E501

        :param user_name: The user_name of this UserResource.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this UserResource.  # noqa: E501


        :return: The name of this UserResource.  # noqa: E501
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserResource.


        :param name: The name of this UserResource.  # noqa: E501
        :type: Name
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this UserResource.  # noqa: E501

        Name of the user suitable for display to end-users  # noqa: E501

        :return: The display_name of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserResource.

        Name of the user suitable for display to end-users  # noqa: E501

        :param display_name: The display_name of this UserResource.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def nick_name(self):
        """Gets the nick_name of this UserResource.  # noqa: E501

        Casual way to address the user in real life  # noqa: E501

        :return: The nick_name of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this UserResource.

        Casual way to address the user in real life  # noqa: E501

        :param nick_name: The nick_name of this UserResource.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def profile_url(self):
        """Gets the profile_url of this UserResource.  # noqa: E501

        URI pointing to a location representing the User's online profile  # noqa: E501

        :return: The profile_url of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this UserResource.

        URI pointing to a location representing the User's online profile  # noqa: E501

        :param profile_url: The profile_url of this UserResource.  # noqa: E501
        :type: str
        """

        self._profile_url = profile_url

    @property
    def title(self):
        """Gets the title of this UserResource.  # noqa: E501


        :return: The title of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserResource.


        :param title: The title of this UserResource.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def user_type(self):
        """Gets the user_type of this UserResource.  # noqa: E501

        Used to identify the relationship between the organization and the user  # noqa: E501

        :return: The user_type of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserResource.

        Used to identify the relationship between the organization and the user  # noqa: E501

        :param user_type: The user_type of this UserResource.  # noqa: E501
        :type: str
        """

        self._user_type = user_type

    @property
    def preferred_language(self):
        """Gets the preferred_language of this UserResource.  # noqa: E501

        Preferred language as used in the Accept-Language HTTP header  # noqa: E501

        :return: The preferred_language of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """Sets the preferred_language of this UserResource.

        Preferred language as used in the Accept-Language HTTP header  # noqa: E501

        :param preferred_language: The preferred_language of this UserResource.  # noqa: E501
        :type: str
        """

        self._preferred_language = preferred_language

    @property
    def locale(self):
        """Gets the locale of this UserResource.  # noqa: E501

        Used for purposes of localizing items such as currency and dates  # noqa: E501

        :return: The locale of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserResource.

        Used for purposes of localizing items such as currency and dates  # noqa: E501

        :param locale: The locale of this UserResource.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def timezone(self):
        """Gets the timezone of this UserResource.  # noqa: E501


        :return: The timezone of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserResource.


        :param timezone: The timezone of this UserResource.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def active(self):
        """Gets the active of this UserResource.  # noqa: E501


        :return: The active of this UserResource.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserResource.


        :param active: The active of this UserResource.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def password(self):
        """Gets the password of this UserResource.  # noqa: E501


        :return: The password of this UserResource.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserResource.


        :param password: The password of this UserResource.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def emails(self):
        """Gets the emails of this UserResource.  # noqa: E501


        :return: The emails of this UserResource.  # noqa: E501
        :rtype: list[Email]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UserResource.


        :param emails: The emails of this UserResource.  # noqa: E501
        :type: list[Email]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this UserResource.  # noqa: E501


        :return: The phone_numbers of this UserResource.  # noqa: E501
        :rtype: list[PhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this UserResource.


        :param phone_numbers: The phone_numbers of this UserResource.  # noqa: E501
        :type: list[PhoneNumber]
        """

        self._phone_numbers = phone_numbers

    @property
    def ims(self):
        """Gets the ims of this UserResource.  # noqa: E501


        :return: The ims of this UserResource.  # noqa: E501
        :rtype: list[InstantMessagingAddress]
        """
        return self._ims

    @ims.setter
    def ims(self, ims):
        """Sets the ims of this UserResource.


        :param ims: The ims of this UserResource.  # noqa: E501
        :type: list[InstantMessagingAddress]
        """

        self._ims = ims

    @property
    def photos(self):
        """Gets the photos of this UserResource.  # noqa: E501


        :return: The photos of this UserResource.  # noqa: E501
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this UserResource.


        :param photos: The photos of this UserResource.  # noqa: E501
        :type: list[Photo]
        """

        self._photos = photos

    @property
    def addresses(self):
        """Gets the addresses of this UserResource.  # noqa: E501


        :return: The addresses of this UserResource.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this UserResource.


        :param addresses: The addresses of this UserResource.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def groups(self):
        """Gets the groups of this UserResource.  # noqa: E501


        :return: The groups of this UserResource.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserResource.


        :param groups: The groups of this UserResource.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def entitlements(self):
        """Gets the entitlements of this UserResource.  # noqa: E501


        :return: The entitlements of this UserResource.  # noqa: E501
        :rtype: list[Entitlement]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """Sets the entitlements of this UserResource.


        :param entitlements: The entitlements of this UserResource.  # noqa: E501
        :type: list[Entitlement]
        """

        self._entitlements = entitlements

    @property
    def roles(self):
        """Gets the roles of this UserResource.  # noqa: E501


        :return: The roles of this UserResource.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserResource.


        :param roles: The roles of this UserResource.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

    @property
    def x509_certificates(self):
        """Gets the x509_certificates of this UserResource.  # noqa: E501


        :return: The x509_certificates of this UserResource.  # noqa: E501
        :rtype: list[X509Certificate]
        """
        return self._x509_certificates

    @x509_certificates.setter
    def x509_certificates(self, x509_certificates):
        """Sets the x509_certificates of this UserResource.


        :param x509_certificates: The x509_certificates of this UserResource.  # noqa: E501
        :type: list[X509Certificate]
        """

        self._x509_certificates = x509_certificates

    @property
    def urnietfparamsscimschemasextensiongluu2_0_user(self):
        """Gets the urnietfparamsscimschemasextensiongluu2_0_user of this UserResource.  # noqa: E501

        Extended attributes  # noqa: E501

        :return: The urnietfparamsscimschemasextensiongluu2_0_user of this UserResource.  # noqa: E501
        :rtype: object
        """
        return self._urnietfparamsscimschemasextensiongluu2_0_user

    @urnietfparamsscimschemasextensiongluu2_0_user.setter
    def urnietfparamsscimschemasextensiongluu2_0_user(self, urnietfparamsscimschemasextensiongluu2_0_user):
        """Sets the urnietfparamsscimschemasextensiongluu2_0_user of this UserResource.

        Extended attributes  # noqa: E501

        :param urnietfparamsscimschemasextensiongluu2_0_user: The urnietfparamsscimschemasextensiongluu2_0_user of this UserResource.  # noqa: E501
        :type: object
        """

        self._urnietfparamsscimschemasextensiongluu2_0_user = urnietfparamsscimschemasextensiongluu2_0_user

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
        if issubclass(UserResource, dict):
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
        if not isinstance(other, UserResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
