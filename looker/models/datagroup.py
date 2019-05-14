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


class Datagroup(object):
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
        'created_at': 'int',
        'id': 'int',
        'model_name': 'str',
        'name': 'str',
        'stale_before': 'int',
        'trigger_check_at': 'int',
        'trigger_error': 'str',
        'trigger_value': 'str',
        'triggered_at': 'int',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'model_name': 'model_name',
        'name': 'name',
        'stale_before': 'stale_before',
        'trigger_check_at': 'trigger_check_at',
        'trigger_error': 'trigger_error',
        'trigger_value': 'trigger_value',
        'triggered_at': 'triggered_at',
        'can': 'can'
    }

    def __init__(self, created_at=None, id=None, model_name=None, name=None, stale_before=None, trigger_check_at=None, trigger_error=None, trigger_value=None, triggered_at=None, can=None):  # noqa: E501
        """Datagroup - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._id = None
        self._model_name = None
        self._name = None
        self._stale_before = None
        self._trigger_check_at = None
        self._trigger_error = None
        self._trigger_value = None
        self._triggered_at = None
        self._can = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if model_name is not None:
            self.model_name = model_name
        if name is not None:
            self.name = name
        if stale_before is not None:
            self.stale_before = stale_before
        if trigger_check_at is not None:
            self.trigger_check_at = trigger_check_at
        if trigger_error is not None:
            self.trigger_error = trigger_error
        if trigger_value is not None:
            self.trigger_value = trigger_value
        if triggered_at is not None:
            self.triggered_at = triggered_at
        if can is not None:
            self.can = can

    @property
    def created_at(self):
        """Gets the created_at of this Datagroup.  # noqa: E501

        UNIX timestamp at which this entry was created.  # noqa: E501

        :return: The created_at of this Datagroup.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datagroup.

        UNIX timestamp at which this entry was created.  # noqa: E501

        :param created_at: The created_at of this Datagroup.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Datagroup.  # noqa: E501

        ID of the datagroup. Also used as the unique identifier.  # noqa: E501

        :return: The id of this Datagroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datagroup.

        ID of the datagroup. Also used as the unique identifier.  # noqa: E501

        :param id: The id of this Datagroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def model_name(self):
        """Gets the model_name of this Datagroup.  # noqa: E501

        Name of the model containing the datagroup. Unique when combined with name.  # noqa: E501

        :return: The model_name of this Datagroup.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this Datagroup.

        Name of the model containing the datagroup. Unique when combined with name.  # noqa: E501

        :param model_name: The model_name of this Datagroup.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def name(self):
        """Gets the name of this Datagroup.  # noqa: E501

        Name of the datagroup. Unique when combined with model_name.  # noqa: E501

        :return: The name of this Datagroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datagroup.

        Name of the datagroup. Unique when combined with model_name.  # noqa: E501

        :param name: The name of this Datagroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def stale_before(self):
        """Gets the stale_before of this Datagroup.  # noqa: E501

        UNIX timestamp before which cache entries are considered stale. Cannot be in the future.  # noqa: E501

        :return: The stale_before of this Datagroup.  # noqa: E501
        :rtype: int
        """
        return self._stale_before

    @stale_before.setter
    def stale_before(self, stale_before):
        """Sets the stale_before of this Datagroup.

        UNIX timestamp before which cache entries are considered stale. Cannot be in the future.  # noqa: E501

        :param stale_before: The stale_before of this Datagroup.  # noqa: E501
        :type: int
        """

        self._stale_before = stale_before

    @property
    def trigger_check_at(self):
        """Gets the trigger_check_at of this Datagroup.  # noqa: E501

        UNIX timestamp at which this entry trigger was last checked.  # noqa: E501

        :return: The trigger_check_at of this Datagroup.  # noqa: E501
        :rtype: int
        """
        return self._trigger_check_at

    @trigger_check_at.setter
    def trigger_check_at(self, trigger_check_at):
        """Sets the trigger_check_at of this Datagroup.

        UNIX timestamp at which this entry trigger was last checked.  # noqa: E501

        :param trigger_check_at: The trigger_check_at of this Datagroup.  # noqa: E501
        :type: int
        """

        self._trigger_check_at = trigger_check_at

    @property
    def trigger_error(self):
        """Gets the trigger_error of this Datagroup.  # noqa: E501

        The message returned with the error of the last trigger check.  # noqa: E501

        :return: The trigger_error of this Datagroup.  # noqa: E501
        :rtype: str
        """
        return self._trigger_error

    @trigger_error.setter
    def trigger_error(self, trigger_error):
        """Sets the trigger_error of this Datagroup.

        The message returned with the error of the last trigger check.  # noqa: E501

        :param trigger_error: The trigger_error of this Datagroup.  # noqa: E501
        :type: str
        """

        self._trigger_error = trigger_error

    @property
    def trigger_value(self):
        """Gets the trigger_value of this Datagroup.  # noqa: E501

        The value of the trigger when last checked.  # noqa: E501

        :return: The trigger_value of this Datagroup.  # noqa: E501
        :rtype: str
        """
        return self._trigger_value

    @trigger_value.setter
    def trigger_value(self, trigger_value):
        """Sets the trigger_value of this Datagroup.

        The value of the trigger when last checked.  # noqa: E501

        :param trigger_value: The trigger_value of this Datagroup.  # noqa: E501
        :type: str
        """

        self._trigger_value = trigger_value

    @property
    def triggered_at(self):
        """Gets the triggered_at of this Datagroup.  # noqa: E501

        UNIX timestamp at which this entry became triggered. Cannot be in the future.  # noqa: E501

        :return: The triggered_at of this Datagroup.  # noqa: E501
        :rtype: int
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        """Sets the triggered_at of this Datagroup.

        UNIX timestamp at which this entry became triggered. Cannot be in the future.  # noqa: E501

        :param triggered_at: The triggered_at of this Datagroup.  # noqa: E501
        :type: int
        """

        self._triggered_at = triggered_at

    @property
    def can(self):
        """Gets the can of this Datagroup.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this Datagroup.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this Datagroup.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this Datagroup.  # noqa: E501
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
        if issubclass(Datagroup, dict):
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
        if not isinstance(other, Datagroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
