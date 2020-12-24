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

class CustomScript(object):
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
        'name': 'str',
        'aliases': 'list[str]',
        'description': 'str',
        'script': 'str',
        'script_type': 'str',
        'programming_language': 'str',
        'module_properties': 'list[CustomScriptModuleProperties]',
        'configuration_properties': 'list[CustomScriptConfigurationProperties]',
        'level': 'int',
        'revision': 'int',
        'enabled': 'bool',
        'script_error': 'CustomScriptScriptError',
        'modified': 'bool',
        'internal': 'bool'
    }

    attribute_map = {
        'dn': 'dn',
        'inum': 'inum',
        'name': 'name',
        'aliases': 'aliases',
        'description': 'description',
        'script': 'script',
        'script_type': 'scriptType',
        'programming_language': 'programmingLanguage',
        'module_properties': 'moduleProperties',
        'configuration_properties': 'configurationProperties',
        'level': 'level',
        'revision': 'revision',
        'enabled': 'enabled',
        'script_error': 'scriptError',
        'modified': 'modified',
        'internal': 'internal'
    }

    def __init__(self, dn=None, inum=None, name=None, aliases=None, description=None, script=None, script_type=None, programming_language=None, module_properties=None, configuration_properties=None, level=None, revision=None, enabled=None, script_error=None, modified=None, internal=None):  # noqa: E501
        """CustomScript - a model defined in Swagger"""  # noqa: E501
        self._dn = None
        self._inum = None
        self._name = None
        self._aliases = None
        self._description = None
        self._script = None
        self._script_type = None
        self._programming_language = None
        self._module_properties = None
        self._configuration_properties = None
        self._level = None
        self._revision = None
        self._enabled = None
        self._script_error = None
        self._modified = None
        self._internal = None
        self.discriminator = None
        if dn is not None:
            self.dn = dn
        if inum is not None:
            self.inum = inum
        if name is not None:
            self.name = name
        if aliases is not None:
            self.aliases = aliases
        if description is not None:
            self.description = description
        if script is not None:
            self.script = script
        if script_type is not None:
            self.script_type = script_type
        if programming_language is not None:
            self.programming_language = programming_language
        if module_properties is not None:
            self.module_properties = module_properties
        if configuration_properties is not None:
            self.configuration_properties = configuration_properties
        if level is not None:
            self.level = level
        if revision is not None:
            self.revision = revision
        if enabled is not None:
            self.enabled = enabled
        if script_error is not None:
            self.script_error = script_error
        if modified is not None:
            self.modified = modified
        if internal is not None:
            self.internal = internal

    @property
    def dn(self):
        """Gets the dn of this CustomScript.  # noqa: E501


        :return: The dn of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this CustomScript.


        :param dn: The dn of this CustomScript.  # noqa: E501
        :type: str
        """

        self._dn = dn

    @property
    def inum(self):
        """Gets the inum of this CustomScript.  # noqa: E501

        XRI i-number. Identifier to uniquely identify the script.  # noqa: E501

        :return: The inum of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._inum

    @inum.setter
    def inum(self, inum):
        """Sets the inum of this CustomScript.

        XRI i-number. Identifier to uniquely identify the script.  # noqa: E501

        :param inum: The inum of this CustomScript.  # noqa: E501
        :type: str
        """

        self._inum = inum

    @property
    def name(self):
        """Gets the name of this CustomScript.  # noqa: E501

        Name should contain only letters, digits and underscores.  # noqa: E501

        :return: The name of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomScript.

        Name should contain only letters, digits and underscores.  # noqa: E501

        :param name: The name of this CustomScript.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def aliases(self):
        """Gets the aliases of this CustomScript.  # noqa: E501

        List of possible alias for the script.  # noqa: E501

        :return: The aliases of this CustomScript.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this CustomScript.

        List of possible alias for the script.  # noqa: E501

        :param aliases: The aliases of this CustomScript.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def description(self):
        """Gets the description of this CustomScript.  # noqa: E501

        Details describing the script.  # noqa: E501

        :return: The description of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomScript.

        Details describing the script.  # noqa: E501

        :param description: The description of this CustomScript.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def script(self):
        """Gets the script of this CustomScript.  # noqa: E501

        Actual script.  # noqa: E501

        :return: The script of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this CustomScript.

        Actual script.  # noqa: E501

        :param script: The script of this CustomScript.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def script_type(self):
        """Gets the script_type of this CustomScript.  # noqa: E501

        Type of script.  # noqa: E501

        :return: The script_type of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this CustomScript.

        Type of script.  # noqa: E501

        :param script_type: The script_type of this CustomScript.  # noqa: E501
        :type: str
        """
        allowed_values = ["person_authentication", "introspection", "resource_owner_password_credentials", "application_session", "cache_refresh", "update_user", "user_registration", "client_registration", "id_generator", "uma_rpt_policy", "uma_rpt_claims", "uma_claims_gathering", "consent_gathering", "dynamic_scope", "spontaneous_scope", "end_session", "post_authn", "scim", "ciba_end_user_notification", "persistence_extension", "idp"]  # noqa: E501
        if script_type not in allowed_values:
            raise ValueError(
                "Invalid value for `script_type` ({0}), must be one of {1}"  # noqa: E501
                .format(script_type, allowed_values)
            )

        self._script_type = script_type

    @property
    def programming_language(self):
        """Gets the programming_language of this CustomScript.  # noqa: E501

        Programming language of the custom script.  # noqa: E501

        :return: The programming_language of this CustomScript.  # noqa: E501
        :rtype: str
        """
        return self._programming_language

    @programming_language.setter
    def programming_language(self, programming_language):
        """Sets the programming_language of this CustomScript.

        Programming language of the custom script.  # noqa: E501

        :param programming_language: The programming_language of this CustomScript.  # noqa: E501
        :type: str
        """
        allowed_values = ["python", "javascript"]  # noqa: E501
        if programming_language not in allowed_values:
            raise ValueError(
                "Invalid value for `programming_language` ({0}), must be one of {1}"  # noqa: E501
                .format(programming_language, allowed_values)
            )

        self._programming_language = programming_language

    @property
    def module_properties(self):
        """Gets the module_properties of this CustomScript.  # noqa: E501

        Module-level properties applicable to the script.  # noqa: E501

        :return: The module_properties of this CustomScript.  # noqa: E501
        :rtype: list[CustomScriptModuleProperties]
        """
        return self._module_properties

    @module_properties.setter
    def module_properties(self, module_properties):
        """Sets the module_properties of this CustomScript.

        Module-level properties applicable to the script.  # noqa: E501

        :param module_properties: The module_properties of this CustomScript.  # noqa: E501
        :type: list[CustomScriptModuleProperties]
        """

        self._module_properties = module_properties

    @property
    def configuration_properties(self):
        """Gets the configuration_properties of this CustomScript.  # noqa: E501

        Configuration properties applicable to the script.  # noqa: E501

        :return: The configuration_properties of this CustomScript.  # noqa: E501
        :rtype: list[CustomScriptConfigurationProperties]
        """
        return self._configuration_properties

    @configuration_properties.setter
    def configuration_properties(self, configuration_properties):
        """Sets the configuration_properties of this CustomScript.

        Configuration properties applicable to the script.  # noqa: E501

        :param configuration_properties: The configuration_properties of this CustomScript.  # noqa: E501
        :type: list[CustomScriptConfigurationProperties]
        """

        self._configuration_properties = configuration_properties

    @property
    def level(self):
        """Gets the level of this CustomScript.  # noqa: E501

        Script level.  # noqa: E501

        :return: The level of this CustomScript.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CustomScript.

        Script level.  # noqa: E501

        :param level: The level of this CustomScript.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def revision(self):
        """Gets the revision of this CustomScript.  # noqa: E501

        Update revision number of the script.  # noqa: E501

        :return: The revision of this CustomScript.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this CustomScript.

        Update revision number of the script.  # noqa: E501

        :param revision: The revision of this CustomScript.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def enabled(self):
        """Gets the enabled of this CustomScript.  # noqa: E501

        boolean value indicating if script enabled.  # noqa: E501

        :return: The enabled of this CustomScript.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CustomScript.

        boolean value indicating if script enabled.  # noqa: E501

        :param enabled: The enabled of this CustomScript.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def script_error(self):
        """Gets the script_error of this CustomScript.  # noqa: E501


        :return: The script_error of this CustomScript.  # noqa: E501
        :rtype: CustomScriptScriptError
        """
        return self._script_error

    @script_error.setter
    def script_error(self, script_error):
        """Sets the script_error of this CustomScript.


        :param script_error: The script_error of this CustomScript.  # noqa: E501
        :type: CustomScriptScriptError
        """

        self._script_error = script_error

    @property
    def modified(self):
        """Gets the modified of this CustomScript.  # noqa: E501

        boolean value indicating if the script is modified.  # noqa: E501

        :return: The modified of this CustomScript.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this CustomScript.

        boolean value indicating if the script is modified.  # noqa: E501

        :param modified: The modified of this CustomScript.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def internal(self):
        """Gets the internal of this CustomScript.  # noqa: E501

        boolean value indicating if the script is interanl.  # noqa: E501

        :return: The internal of this CustomScript.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this CustomScript.

        boolean value indicating if the script is interanl.  # noqa: E501

        :param internal: The internal of this CustomScript.  # noqa: E501
        :type: bool
        """

        self._internal = internal

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
        if issubclass(CustomScript, dict):
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
        if not isinstance(other, CustomScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
