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


class ResultMakerFilterablesListen(object):
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
        'dashboard_filter_name': 'str',
        'field': 'str'
    }

    attribute_map = {
        'dashboard_filter_name': 'dashboard_filter_name',
        'field': 'field'
    }

    def __init__(self, dashboard_filter_name=None, field=None):  # noqa: E501
        """ResultMakerFilterablesListen - a model defined in Swagger"""  # noqa: E501
        self._dashboard_filter_name = None
        self._field = None
        self.discriminator = None
        if dashboard_filter_name is not None:
            self.dashboard_filter_name = dashboard_filter_name
        if field is not None:
            self.field = field

    @property
    def dashboard_filter_name(self):
        """Gets the dashboard_filter_name of this ResultMakerFilterablesListen.  # noqa: E501

        The name of a dashboard filter to listen to.  # noqa: E501

        :return: The dashboard_filter_name of this ResultMakerFilterablesListen.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_filter_name

    @dashboard_filter_name.setter
    def dashboard_filter_name(self, dashboard_filter_name):
        """Sets the dashboard_filter_name of this ResultMakerFilterablesListen.

        The name of a dashboard filter to listen to.  # noqa: E501

        :param dashboard_filter_name: The dashboard_filter_name of this ResultMakerFilterablesListen.  # noqa: E501
        :type: str
        """

        self._dashboard_filter_name = dashboard_filter_name

    @property
    def field(self):
        """Gets the field of this ResultMakerFilterablesListen.  # noqa: E501

        The name of the field in the filterable to filter with the value of the dashboard filter.  # noqa: E501

        :return: The field of this ResultMakerFilterablesListen.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ResultMakerFilterablesListen.

        The name of the field in the filterable to filter with the value of the dashboard filter.  # noqa: E501

        :param field: The field of this ResultMakerFilterablesListen.  # noqa: E501
        :type: str
        """

        self._field = field

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
        if issubclass(ResultMakerFilterablesListen, dict):
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
        if not isinstance(other, ResultMakerFilterablesListen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
