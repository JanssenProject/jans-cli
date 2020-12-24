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

class UmaResource(object):
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
        'dn': 'str',
        'inum': 'str',
        'id': 'str',
        'name': 'str',
        'icon_url': 'str',
        'scopes': 'list[str]',
        'scope_expression': 'str',
        'clients': 'list[str]',
        'resources': 'list[str]',
        'rev': 'str',
        'creator': 'str',
        'description': 'str',
        'type': 'str',
        'creation_date': 'date',
        'expiration_date': 'date',
        'deletable': 'bool'
    }

    attribute_map = {
        'dn': 'dn',
        'inum': 'inum',
        'id': 'id',
        'name': 'name',
        'icon_url': 'iconUrl',
        'scopes': 'scopes',
        'scope_expression': 'scopeExpression',
        'clients': 'clients',
        'resources': 'resources',
        'rev': 'rev',
        'creator': 'creator',
        'description': 'description',
        'type': 'type',
        'creation_date': 'creationDate',
        'expiration_date': 'expirationDate',
        'deletable': 'deletable'
    }

    def __init__(self, dn=None, inum=None, id=None, name=None, icon_url=None, scopes=None, scope_expression=None, clients=None, resources=None, rev=None, creator=None, description=None, type=None, creation_date=None, expiration_date=None, deletable=None):  # noqa: E501
        """UmaResource - a model defined in Swagger"""  # noqa: E501
        self._dn = None
        self._inum = None
        self._id = None
        self._name = None
        self._icon_url = None
        self._scopes = None
        self._scope_expression = None
        self._clients = None
        self._resources = None
        self._rev = None
        self._creator = None
        self._description = None
        self._type = None
        self._creation_date = None
        self._expiration_date = None
        self._deletable = None
        self.discriminator = None
        if dn is not None:
            self.dn = dn
        if inum is not None:
            self.inum = inum
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if icon_url is not None:
            self.icon_url = icon_url
        if scopes is not None:
            self.scopes = scopes
        if scope_expression is not None:
            self.scope_expression = scope_expression
        if clients is not None:
            self.clients = clients
        if resources is not None:
            self.resources = resources
        if rev is not None:
            self.rev = rev
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if creation_date is not None:
            self.creation_date = creation_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if deletable is not None:
            self.deletable = deletable

    @property
    def dn(self):
        """Gets the dn of this UmaResource.  # noqa: E501


        :return: The dn of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this UmaResource.


        :param dn: The dn of this UmaResource.  # noqa: E501
        :type: str
        """

        self._dn = dn

    @property
    def inum(self):
        """Gets the inum of this UmaResource.  # noqa: E501

        XRI i-number. Client Identifier to uniquely identify the UMAResource.  # noqa: E501

        :return: The inum of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._inum

    @inum.setter
    def inum(self, inum):
        """Sets the inum of this UmaResource.

        XRI i-number. Client Identifier to uniquely identify the UMAResource.  # noqa: E501

        :param inum: The inum of this UmaResource.  # noqa: E501
        :type: str
        """

        self._inum = inum

    @property
    def id(self):
        """Gets the id of this UmaResource.  # noqa: E501

        Resource id.  # noqa: E501

        :return: The id of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UmaResource.

        Resource id.  # noqa: E501

        :param id: The id of this UmaResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UmaResource.  # noqa: E501

        A human-readable name of the scope.  # noqa: E501

        :return: The name of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UmaResource.

        A human-readable name of the scope.  # noqa: E501

        :param name: The name of this UmaResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon_url(self):
        """Gets the icon_url of this UmaResource.  # noqa: E501

        A URL for a graphic icon representing the resource.  # noqa: E501

        :return: The icon_url of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this UmaResource.

        A URL for a graphic icon representing the resource.  # noqa: E501

        :param icon_url: The icon_url of this UmaResource.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def scopes(self):
        """Gets the scopes of this UmaResource.  # noqa: E501

        Applicable resource scopes.  # noqa: E501

        :return: The scopes of this UmaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this UmaResource.

        Applicable resource scopes.  # noqa: E501

        :param scopes: The scopes of this UmaResource.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def scope_expression(self):
        """Gets the scope_expression of this UmaResource.  # noqa: E501

        Resource scope expression.  # noqa: E501

        :return: The scope_expression of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._scope_expression

    @scope_expression.setter
    def scope_expression(self, scope_expression):
        """Sets the scope_expression of this UmaResource.

        Resource scope expression.  # noqa: E501

        :param scope_expression: The scope_expression of this UmaResource.  # noqa: E501
        :type: str
        """

        self._scope_expression = scope_expression

    @property
    def clients(self):
        """Gets the clients of this UmaResource.  # noqa: E501

        List of client assosiated with the resource.  # noqa: E501

        :return: The clients of this UmaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this UmaResource.

        List of client assosiated with the resource.  # noqa: E501

        :param clients: The clients of this UmaResource.  # noqa: E501
        :type: list[str]
        """

        self._clients = clients

    @property
    def resources(self):
        """Gets the resources of this UmaResource.  # noqa: E501

        List of assosiated resource.  # noqa: E501

        :return: The resources of this UmaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this UmaResource.

        List of assosiated resource.  # noqa: E501

        :param resources: The resources of this UmaResource.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def rev(self):
        """Gets the rev of this UmaResource.  # noqa: E501

        Resource revision.  # noqa: E501

        :return: The rev of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """Sets the rev of this UmaResource.

        Resource revision.  # noqa: E501

        :param rev: The rev of this UmaResource.  # noqa: E501
        :type: str
        """

        self._rev = rev

    @property
    def creator(self):
        """Gets the creator of this UmaResource.  # noqa: E501

        Resource creator or owner.  # noqa: E501

        :return: The creator of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this UmaResource.

        Resource creator or owner.  # noqa: E501

        :param creator: The creator of this UmaResource.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this UmaResource.  # noqa: E501

        Resource description.  # noqa: E501

        :return: The description of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UmaResource.

        Resource description.  # noqa: E501

        :param description: The description of this UmaResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this UmaResource.  # noqa: E501

        Resource type.  # noqa: E501

        :return: The type of this UmaResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UmaResource.

        Resource type.  # noqa: E501

        :param type: The type of this UmaResource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def creation_date(self):
        """Gets the creation_date of this UmaResource.  # noqa: E501

        Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this resource will created.  # noqa: E501

        :return: The creation_date of this UmaResource.  # noqa: E501
        :rtype: date
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UmaResource.

        Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this resource will created.  # noqa: E501

        :param creation_date: The creation_date of this UmaResource.  # noqa: E501
        :type: date
        """

        self._creation_date = creation_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this UmaResource.  # noqa: E501

        Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this resource will expire.  # noqa: E501

        :return: The expiration_date of this UmaResource.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this UmaResource.

        Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this resource will expire.  # noqa: E501

        :param expiration_date: The expiration_date of this UmaResource.  # noqa: E501
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def deletable(self):
        """Gets the deletable of this UmaResource.  # noqa: E501

        Specifies whether client is deletable.  # noqa: E501

        :return: The deletable of this UmaResource.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this UmaResource.

        Specifies whether client is deletable.  # noqa: E501

        :param deletable: The deletable of this UmaResource.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

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
        if issubclass(UmaResource, dict):
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
        if not isinstance(other, UmaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
