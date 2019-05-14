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


class UserAttributeGroupValue(object):
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
        'id': 'int',
        'group_id': 'int',
        'user_attribute_id': 'int',
        'value_is_hidden': 'bool',
        'rank': 'int',
        'value': 'str',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'group_id',
        'user_attribute_id': 'user_attribute_id',
        'value_is_hidden': 'value_is_hidden',
        'rank': 'rank',
        'value': 'value',
        'can': 'can'
    }

    def __init__(self, id=None, group_id=None, user_attribute_id=None, value_is_hidden=None, rank=None, value=None, can=None):  # noqa: E501
        """UserAttributeGroupValue - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._group_id = None
        self._user_attribute_id = None
        self._value_is_hidden = None
        self._rank = None
        self._value = None
        self._can = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if user_attribute_id is not None:
            self.user_attribute_id = user_attribute_id
        if value_is_hidden is not None:
            self.value_is_hidden = value_is_hidden
        if rank is not None:
            self.rank = rank
        if value is not None:
            self.value = value
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this UserAttributeGroupValue.  # noqa: E501

        Unique Id of this group-attribute relation  # noqa: E501

        :return: The id of this UserAttributeGroupValue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAttributeGroupValue.

        Unique Id of this group-attribute relation  # noqa: E501

        :param id: The id of this UserAttributeGroupValue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this UserAttributeGroupValue.  # noqa: E501

        Id of group  # noqa: E501

        :return: The group_id of this UserAttributeGroupValue.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UserAttributeGroupValue.

        Id of group  # noqa: E501

        :param group_id: The group_id of this UserAttributeGroupValue.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def user_attribute_id(self):
        """Gets the user_attribute_id of this UserAttributeGroupValue.  # noqa: E501

        Id of user attribute  # noqa: E501

        :return: The user_attribute_id of this UserAttributeGroupValue.  # noqa: E501
        :rtype: int
        """
        return self._user_attribute_id

    @user_attribute_id.setter
    def user_attribute_id(self, user_attribute_id):
        """Sets the user_attribute_id of this UserAttributeGroupValue.

        Id of user attribute  # noqa: E501

        :param user_attribute_id: The user_attribute_id of this UserAttributeGroupValue.  # noqa: E501
        :type: int
        """

        self._user_attribute_id = user_attribute_id

    @property
    def value_is_hidden(self):
        """Gets the value_is_hidden of this UserAttributeGroupValue.  # noqa: E501

        If true, the \"value\" field will be null, because the attribute settings block access to this value  # noqa: E501

        :return: The value_is_hidden of this UserAttributeGroupValue.  # noqa: E501
        :rtype: bool
        """
        return self._value_is_hidden

    @value_is_hidden.setter
    def value_is_hidden(self, value_is_hidden):
        """Sets the value_is_hidden of this UserAttributeGroupValue.

        If true, the \"value\" field will be null, because the attribute settings block access to this value  # noqa: E501

        :param value_is_hidden: The value_is_hidden of this UserAttributeGroupValue.  # noqa: E501
        :type: bool
        """

        self._value_is_hidden = value_is_hidden

    @property
    def rank(self):
        """Gets the rank of this UserAttributeGroupValue.  # noqa: E501

        Precedence for resolving value for user  # noqa: E501

        :return: The rank of this UserAttributeGroupValue.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this UserAttributeGroupValue.

        Precedence for resolving value for user  # noqa: E501

        :param rank: The rank of this UserAttributeGroupValue.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def value(self):
        """Gets the value of this UserAttributeGroupValue.  # noqa: E501

        Value of user attribute for group  # noqa: E501

        :return: The value of this UserAttributeGroupValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UserAttributeGroupValue.

        Value of user attribute for group  # noqa: E501

        :param value: The value of this UserAttributeGroupValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def can(self):
        """Gets the can of this UserAttributeGroupValue.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this UserAttributeGroupValue.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this UserAttributeGroupValue.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this UserAttributeGroupValue.  # noqa: E501
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
        if issubclass(UserAttributeGroupValue, dict):
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
        if not isinstance(other, UserAttributeGroupValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
