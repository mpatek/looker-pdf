# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LegacyFeature(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'enabled_locally': 'bool',
        'enabled': 'bool',
        'disallowed_as_of_version': 'str',
        'disable_on_upgrade_to_version': 'str',
        'end_of_life_version': 'str',
        'documentation_url': 'str',
        'approximate_disable_date': 'datetime',
        'approximate_end_of_life_date': 'datetime',
        'has_disabled_on_upgrade': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'enabled_locally': 'enabled_locally',
        'enabled': 'enabled',
        'disallowed_as_of_version': 'disallowed_as_of_version',
        'disable_on_upgrade_to_version': 'disable_on_upgrade_to_version',
        'end_of_life_version': 'end_of_life_version',
        'documentation_url': 'documentation_url',
        'approximate_disable_date': 'approximate_disable_date',
        'approximate_end_of_life_date': 'approximate_end_of_life_date',
        'has_disabled_on_upgrade': 'has_disabled_on_upgrade',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, description=None, enabled_locally=None, enabled=None, disallowed_as_of_version=None, disable_on_upgrade_to_version=None, end_of_life_version=None, documentation_url=None, approximate_disable_date=None, approximate_end_of_life_date=None, has_disabled_on_upgrade=None, can=None):  # noqa: E501
        """LegacyFeature - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._enabled_locally = None
        self._enabled = None
        self._disallowed_as_of_version = None
        self._disable_on_upgrade_to_version = None
        self._end_of_life_version = None
        self._documentation_url = None
        self._approximate_disable_date = None
        self._approximate_end_of_life_date = None
        self._has_disabled_on_upgrade = None
        self._can = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled_locally is not None:
            self.enabled_locally = enabled_locally
        if enabled is not None:
            self.enabled = enabled
        if disallowed_as_of_version is not None:
            self.disallowed_as_of_version = disallowed_as_of_version
        if disable_on_upgrade_to_version is not None:
            self.disable_on_upgrade_to_version = disable_on_upgrade_to_version
        if end_of_life_version is not None:
            self.end_of_life_version = end_of_life_version
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if approximate_disable_date is not None:
            self.approximate_disable_date = approximate_disable_date
        if approximate_end_of_life_date is not None:
            self.approximate_end_of_life_date = approximate_end_of_life_date
        if has_disabled_on_upgrade is not None:
            self.has_disabled_on_upgrade = has_disabled_on_upgrade
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this LegacyFeature.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LegacyFeature.

        Unique Id  # noqa: E501

        :param id: The id of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LegacyFeature.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LegacyFeature.

        Name  # noqa: E501

        :param name: The name of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this LegacyFeature.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegacyFeature.

        Description  # noqa: E501

        :param description: The description of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled_locally(self):
        """Gets the enabled_locally of this LegacyFeature.  # noqa: E501

        Whether this feature has been enabled by a user  # noqa: E501

        :return: The enabled_locally of this LegacyFeature.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_locally

    @enabled_locally.setter
    def enabled_locally(self, enabled_locally):
        """Sets the enabled_locally of this LegacyFeature.

        Whether this feature has been enabled by a user  # noqa: E501

        :param enabled_locally: The enabled_locally of this LegacyFeature.  # noqa: E501
        :type: bool
        """

        self._enabled_locally = enabled_locally

    @property
    def enabled(self):
        """Gets the enabled of this LegacyFeature.  # noqa: E501

        Whether this feature is currently enabled  # noqa: E501

        :return: The enabled of this LegacyFeature.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LegacyFeature.

        Whether this feature is currently enabled  # noqa: E501

        :param enabled: The enabled of this LegacyFeature.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def disallowed_as_of_version(self):
        """Gets the disallowed_as_of_version of this LegacyFeature.  # noqa: E501

        Looker version where this feature became a legacy feature  # noqa: E501

        :return: The disallowed_as_of_version of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._disallowed_as_of_version

    @disallowed_as_of_version.setter
    def disallowed_as_of_version(self, disallowed_as_of_version):
        """Sets the disallowed_as_of_version of this LegacyFeature.

        Looker version where this feature became a legacy feature  # noqa: E501

        :param disallowed_as_of_version: The disallowed_as_of_version of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._disallowed_as_of_version = disallowed_as_of_version

    @property
    def disable_on_upgrade_to_version(self):
        """Gets the disable_on_upgrade_to_version of this LegacyFeature.  # noqa: E501

        Looker version where this feature will be automatically disabled  # noqa: E501

        :return: The disable_on_upgrade_to_version of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._disable_on_upgrade_to_version

    @disable_on_upgrade_to_version.setter
    def disable_on_upgrade_to_version(self, disable_on_upgrade_to_version):
        """Sets the disable_on_upgrade_to_version of this LegacyFeature.

        Looker version where this feature will be automatically disabled  # noqa: E501

        :param disable_on_upgrade_to_version: The disable_on_upgrade_to_version of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._disable_on_upgrade_to_version = disable_on_upgrade_to_version

    @property
    def end_of_life_version(self):
        """Gets the end_of_life_version of this LegacyFeature.  # noqa: E501

        Future Looker version where this feature will be removed  # noqa: E501

        :return: The end_of_life_version of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._end_of_life_version

    @end_of_life_version.setter
    def end_of_life_version(self, end_of_life_version):
        """Sets the end_of_life_version of this LegacyFeature.

        Future Looker version where this feature will be removed  # noqa: E501

        :param end_of_life_version: The end_of_life_version of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._end_of_life_version = end_of_life_version

    @property
    def documentation_url(self):
        """Gets the documentation_url of this LegacyFeature.  # noqa: E501

        URL for documentation about this feature  # noqa: E501

        :return: The documentation_url of this LegacyFeature.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this LegacyFeature.

        URL for documentation about this feature  # noqa: E501

        :param documentation_url: The documentation_url of this LegacyFeature.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def approximate_disable_date(self):
        """Gets the approximate_disable_date of this LegacyFeature.  # noqa: E501

        Approximate date that this feature will be automatically disabled.  # noqa: E501

        :return: The approximate_disable_date of this LegacyFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._approximate_disable_date

    @approximate_disable_date.setter
    def approximate_disable_date(self, approximate_disable_date):
        """Sets the approximate_disable_date of this LegacyFeature.

        Approximate date that this feature will be automatically disabled.  # noqa: E501

        :param approximate_disable_date: The approximate_disable_date of this LegacyFeature.  # noqa: E501
        :type: datetime
        """

        self._approximate_disable_date = approximate_disable_date

    @property
    def approximate_end_of_life_date(self):
        """Gets the approximate_end_of_life_date of this LegacyFeature.  # noqa: E501

        Approximate date that this feature will be removed.  # noqa: E501

        :return: The approximate_end_of_life_date of this LegacyFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._approximate_end_of_life_date

    @approximate_end_of_life_date.setter
    def approximate_end_of_life_date(self, approximate_end_of_life_date):
        """Sets the approximate_end_of_life_date of this LegacyFeature.

        Approximate date that this feature will be removed.  # noqa: E501

        :param approximate_end_of_life_date: The approximate_end_of_life_date of this LegacyFeature.  # noqa: E501
        :type: datetime
        """

        self._approximate_end_of_life_date = approximate_end_of_life_date

    @property
    def has_disabled_on_upgrade(self):
        """Gets the has_disabled_on_upgrade of this LegacyFeature.  # noqa: E501

        Whether this legacy feature may have been automatically disabled when upgrading to the current version.  # noqa: E501

        :return: The has_disabled_on_upgrade of this LegacyFeature.  # noqa: E501
        :rtype: bool
        """
        return self._has_disabled_on_upgrade

    @has_disabled_on_upgrade.setter
    def has_disabled_on_upgrade(self, has_disabled_on_upgrade):
        """Sets the has_disabled_on_upgrade of this LegacyFeature.

        Whether this legacy feature may have been automatically disabled when upgrading to the current version.  # noqa: E501

        :param has_disabled_on_upgrade: The has_disabled_on_upgrade of this LegacyFeature.  # noqa: E501
        :type: bool
        """

        self._has_disabled_on_upgrade = has_disabled_on_upgrade

    @property
    def can(self):
        """Gets the can of this LegacyFeature.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this LegacyFeature.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this LegacyFeature.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this LegacyFeature.  # noqa: E501
        :type: dict(str, bool)
        """

        self._can = can

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
        if issubclass(LegacyFeature, dict):
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
        if not isinstance(other, LegacyFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
