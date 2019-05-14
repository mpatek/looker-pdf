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
from looker.models.scheduled_plan_destination import ScheduledPlanDestination  # noqa: F401,E501
from looker.models.user_public import UserPublic  # noqa: F401,E501


class ScheduledPlan(object):
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
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'title': 'str',
        'user_id': 'int',
        'user': 'UserPublic',
        'run_as_recipient': 'bool',
        'enabled': 'bool',
        'next_run_at': 'datetime',
        'last_run_at': 'datetime',
        'look_id': 'int',
        'dashboard_id': 'int',
        'lookml_dashboard_id': 'str',
        'filters_string': 'str',
        'dashboard_filters': 'str',
        'require_results': 'bool',
        'require_no_results': 'bool',
        'require_change': 'bool',
        'send_all_results': 'bool',
        'crontab': 'str',
        'datagroup': 'str',
        'timezone': 'str',
        'query_id': 'str',
        'scheduled_plan_destination': 'list[ScheduledPlanDestination]',
        'run_once': 'bool',
        'include_links': 'bool',
        'pdf_paper_size': 'str',
        'pdf_landscape': 'bool',
        'embed': 'bool',
        'color_theme': 'str',
        'long_tables': 'bool',
        'can': 'dict(str, bool)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'title': 'title',
        'user_id': 'user_id',
        'user': 'user',
        'run_as_recipient': 'run_as_recipient',
        'enabled': 'enabled',
        'next_run_at': 'next_run_at',
        'last_run_at': 'last_run_at',
        'look_id': 'look_id',
        'dashboard_id': 'dashboard_id',
        'lookml_dashboard_id': 'lookml_dashboard_id',
        'filters_string': 'filters_string',
        'dashboard_filters': 'dashboard_filters',
        'require_results': 'require_results',
        'require_no_results': 'require_no_results',
        'require_change': 'require_change',
        'send_all_results': 'send_all_results',
        'crontab': 'crontab',
        'datagroup': 'datagroup',
        'timezone': 'timezone',
        'query_id': 'query_id',
        'scheduled_plan_destination': 'scheduled_plan_destination',
        'run_once': 'run_once',
        'include_links': 'include_links',
        'pdf_paper_size': 'pdf_paper_size',
        'pdf_landscape': 'pdf_landscape',
        'embed': 'embed',
        'color_theme': 'color_theme',
        'long_tables': 'long_tables',
        'can': 'can'
    }

    def __init__(self, id=None, name=None, created_at=None, updated_at=None, title=None, user_id=None, user=None, run_as_recipient=None, enabled=None, next_run_at=None, last_run_at=None, look_id=None, dashboard_id=None, lookml_dashboard_id=None, filters_string=None, dashboard_filters=None, require_results=None, require_no_results=None, require_change=None, send_all_results=None, crontab=None, datagroup=None, timezone=None, query_id=None, scheduled_plan_destination=None, run_once=None, include_links=None, pdf_paper_size=None, pdf_landscape=None, embed=None, color_theme=None, long_tables=None, can=None):  # noqa: E501
        """ScheduledPlan - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._title = None
        self._user_id = None
        self._user = None
        self._run_as_recipient = None
        self._enabled = None
        self._next_run_at = None
        self._last_run_at = None
        self._look_id = None
        self._dashboard_id = None
        self._lookml_dashboard_id = None
        self._filters_string = None
        self._dashboard_filters = None
        self._require_results = None
        self._require_no_results = None
        self._require_change = None
        self._send_all_results = None
        self._crontab = None
        self._datagroup = None
        self._timezone = None
        self._query_id = None
        self._scheduled_plan_destination = None
        self._run_once = None
        self._include_links = None
        self._pdf_paper_size = None
        self._pdf_landscape = None
        self._embed = None
        self._color_theme = None
        self._long_tables = None
        self._can = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if title is not None:
            self.title = title
        if user_id is not None:
            self.user_id = user_id
        if user is not None:
            self.user = user
        if run_as_recipient is not None:
            self.run_as_recipient = run_as_recipient
        if enabled is not None:
            self.enabled = enabled
        if next_run_at is not None:
            self.next_run_at = next_run_at
        if last_run_at is not None:
            self.last_run_at = last_run_at
        if look_id is not None:
            self.look_id = look_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if lookml_dashboard_id is not None:
            self.lookml_dashboard_id = lookml_dashboard_id
        if filters_string is not None:
            self.filters_string = filters_string
        if dashboard_filters is not None:
            self.dashboard_filters = dashboard_filters
        if require_results is not None:
            self.require_results = require_results
        if require_no_results is not None:
            self.require_no_results = require_no_results
        if require_change is not None:
            self.require_change = require_change
        if send_all_results is not None:
            self.send_all_results = send_all_results
        if crontab is not None:
            self.crontab = crontab
        if datagroup is not None:
            self.datagroup = datagroup
        if timezone is not None:
            self.timezone = timezone
        if query_id is not None:
            self.query_id = query_id
        if scheduled_plan_destination is not None:
            self.scheduled_plan_destination = scheduled_plan_destination
        if run_once is not None:
            self.run_once = run_once
        if include_links is not None:
            self.include_links = include_links
        if pdf_paper_size is not None:
            self.pdf_paper_size = pdf_paper_size
        if pdf_landscape is not None:
            self.pdf_landscape = pdf_landscape
        if embed is not None:
            self.embed = embed
        if color_theme is not None:
            self.color_theme = color_theme
        if long_tables is not None:
            self.long_tables = long_tables
        if can is not None:
            self.can = can

    @property
    def id(self):
        """Gets the id of this ScheduledPlan.  # noqa: E501

        Unique Id  # noqa: E501

        :return: The id of this ScheduledPlan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledPlan.

        Unique Id  # noqa: E501

        :param id: The id of this ScheduledPlan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ScheduledPlan.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduledPlan.

        Name  # noqa: E501

        :param name: The name of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this ScheduledPlan.  # noqa: E501

        Date and time when ScheduledPlan was created  # noqa: E501

        :return: The created_at of this ScheduledPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ScheduledPlan.

        Date and time when ScheduledPlan was created  # noqa: E501

        :param created_at: The created_at of this ScheduledPlan.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ScheduledPlan.  # noqa: E501

        Date and time when ScheduledPlan was last updated  # noqa: E501

        :return: The updated_at of this ScheduledPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ScheduledPlan.

        Date and time when ScheduledPlan was last updated  # noqa: E501

        :param updated_at: The updated_at of this ScheduledPlan.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def title(self):
        """Gets the title of this ScheduledPlan.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ScheduledPlan.

        Title  # noqa: E501

        :param title: The title of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def user_id(self):
        """Gets the user_id of this ScheduledPlan.  # noqa: E501

        User Id which owns this ScheduledPlan  # noqa: E501

        :return: The user_id of this ScheduledPlan.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ScheduledPlan.

        User Id which owns this ScheduledPlan  # noqa: E501

        :param user_id: The user_id of this ScheduledPlan.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user(self):
        """Gets the user of this ScheduledPlan.  # noqa: E501


        :return: The user of this ScheduledPlan.  # noqa: E501
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ScheduledPlan.


        :param user: The user of this ScheduledPlan.  # noqa: E501
        :type: UserPublic
        """

        self._user = user

    @property
    def run_as_recipient(self):
        """Gets the run_as_recipient of this ScheduledPlan.  # noqa: E501

        Whether schedule is ran as recipient (only applicable for email recipients)  # noqa: E501

        :return: The run_as_recipient of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_recipient

    @run_as_recipient.setter
    def run_as_recipient(self, run_as_recipient):
        """Sets the run_as_recipient of this ScheduledPlan.

        Whether schedule is ran as recipient (only applicable for email recipients)  # noqa: E501

        :param run_as_recipient: The run_as_recipient of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._run_as_recipient = run_as_recipient

    @property
    def enabled(self):
        """Gets the enabled of this ScheduledPlan.  # noqa: E501

        Whether the ScheduledPlan is enabled  # noqa: E501

        :return: The enabled of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScheduledPlan.

        Whether the ScheduledPlan is enabled  # noqa: E501

        :param enabled: The enabled of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def next_run_at(self):
        """Gets the next_run_at of this ScheduledPlan.  # noqa: E501

        When the ScheduledPlan will next run (null if running once)  # noqa: E501

        :return: The next_run_at of this ScheduledPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._next_run_at

    @next_run_at.setter
    def next_run_at(self, next_run_at):
        """Sets the next_run_at of this ScheduledPlan.

        When the ScheduledPlan will next run (null if running once)  # noqa: E501

        :param next_run_at: The next_run_at of this ScheduledPlan.  # noqa: E501
        :type: datetime
        """

        self._next_run_at = next_run_at

    @property
    def last_run_at(self):
        """Gets the last_run_at of this ScheduledPlan.  # noqa: E501

        When the ScheduledPlan was last run  # noqa: E501

        :return: The last_run_at of this ScheduledPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run_at

    @last_run_at.setter
    def last_run_at(self, last_run_at):
        """Sets the last_run_at of this ScheduledPlan.

        When the ScheduledPlan was last run  # noqa: E501

        :param last_run_at: The last_run_at of this ScheduledPlan.  # noqa: E501
        :type: datetime
        """

        self._last_run_at = last_run_at

    @property
    def look_id(self):
        """Gets the look_id of this ScheduledPlan.  # noqa: E501

        Id of a look  # noqa: E501

        :return: The look_id of this ScheduledPlan.  # noqa: E501
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """Sets the look_id of this ScheduledPlan.

        Id of a look  # noqa: E501

        :param look_id: The look_id of this ScheduledPlan.  # noqa: E501
        :type: int
        """

        self._look_id = look_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this ScheduledPlan.  # noqa: E501

        Id of a dashboard  # noqa: E501

        :return: The dashboard_id of this ScheduledPlan.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this ScheduledPlan.

        Id of a dashboard  # noqa: E501

        :param dashboard_id: The dashboard_id of this ScheduledPlan.  # noqa: E501
        :type: int
        """

        self._dashboard_id = dashboard_id

    @property
    def lookml_dashboard_id(self):
        """Gets the lookml_dashboard_id of this ScheduledPlan.  # noqa: E501

        Id of a LookML dashboard  # noqa: E501

        :return: The lookml_dashboard_id of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._lookml_dashboard_id

    @lookml_dashboard_id.setter
    def lookml_dashboard_id(self, lookml_dashboard_id):
        """Sets the lookml_dashboard_id of this ScheduledPlan.

        Id of a LookML dashboard  # noqa: E501

        :param lookml_dashboard_id: The lookml_dashboard_id of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._lookml_dashboard_id = lookml_dashboard_id

    @property
    def filters_string(self):
        """Gets the filters_string of this ScheduledPlan.  # noqa: E501

        Query string to run look or dashboard with  # noqa: E501

        :return: The filters_string of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._filters_string

    @filters_string.setter
    def filters_string(self, filters_string):
        """Sets the filters_string of this ScheduledPlan.

        Query string to run look or dashboard with  # noqa: E501

        :param filters_string: The filters_string of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._filters_string = filters_string

    @property
    def dashboard_filters(self):
        """Gets the dashboard_filters of this ScheduledPlan.  # noqa: E501

        (DEPRECATED) Alias for filters_string field  # noqa: E501

        :return: The dashboard_filters of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_filters

    @dashboard_filters.setter
    def dashboard_filters(self, dashboard_filters):
        """Sets the dashboard_filters of this ScheduledPlan.

        (DEPRECATED) Alias for filters_string field  # noqa: E501

        :param dashboard_filters: The dashboard_filters of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._dashboard_filters = dashboard_filters

    @property
    def require_results(self):
        """Gets the require_results of this ScheduledPlan.  # noqa: E501

        Delivery should occur if running the dashboard or look returns results  # noqa: E501

        :return: The require_results of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._require_results

    @require_results.setter
    def require_results(self, require_results):
        """Sets the require_results of this ScheduledPlan.

        Delivery should occur if running the dashboard or look returns results  # noqa: E501

        :param require_results: The require_results of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._require_results = require_results

    @property
    def require_no_results(self):
        """Gets the require_no_results of this ScheduledPlan.  # noqa: E501

        Delivery should occur if the dashboard look does not return results  # noqa: E501

        :return: The require_no_results of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._require_no_results

    @require_no_results.setter
    def require_no_results(self, require_no_results):
        """Sets the require_no_results of this ScheduledPlan.

        Delivery should occur if the dashboard look does not return results  # noqa: E501

        :param require_no_results: The require_no_results of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._require_no_results = require_no_results

    @property
    def require_change(self):
        """Gets the require_change of this ScheduledPlan.  # noqa: E501

        Delivery should occur if data have changed since the last run  # noqa: E501

        :return: The require_change of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._require_change

    @require_change.setter
    def require_change(self, require_change):
        """Sets the require_change of this ScheduledPlan.

        Delivery should occur if data have changed since the last run  # noqa: E501

        :param require_change: The require_change of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._require_change = require_change

    @property
    def send_all_results(self):
        """Gets the send_all_results of this ScheduledPlan.  # noqa: E501

        Will run an unlimited query and send all results.  # noqa: E501

        :return: The send_all_results of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._send_all_results

    @send_all_results.setter
    def send_all_results(self, send_all_results):
        """Sets the send_all_results of this ScheduledPlan.

        Will run an unlimited query and send all results.  # noqa: E501

        :param send_all_results: The send_all_results of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._send_all_results = send_all_results

    @property
    def crontab(self):
        """Gets the crontab of this ScheduledPlan.  # noqa: E501

        Vixie-Style crontab specification when to run  # noqa: E501

        :return: The crontab of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """Sets the crontab of this ScheduledPlan.

        Vixie-Style crontab specification when to run  # noqa: E501

        :param crontab: The crontab of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._crontab = crontab

    @property
    def datagroup(self):
        """Gets the datagroup of this ScheduledPlan.  # noqa: E501

        Name of a datagroup; if specified will run when datagroup triggered (can't be used with cron string)  # noqa: E501

        :return: The datagroup of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._datagroup

    @datagroup.setter
    def datagroup(self, datagroup):
        """Sets the datagroup of this ScheduledPlan.

        Name of a datagroup; if specified will run when datagroup triggered (can't be used with cron string)  # noqa: E501

        :param datagroup: The datagroup of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._datagroup = datagroup

    @property
    def timezone(self):
        """Gets the timezone of this ScheduledPlan.  # noqa: E501

        Timezone for interpreting the specified crontab (default is Looker instance timezone)  # noqa: E501

        :return: The timezone of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ScheduledPlan.

        Timezone for interpreting the specified crontab (default is Looker instance timezone)  # noqa: E501

        :param timezone: The timezone of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def query_id(self):
        """Gets the query_id of this ScheduledPlan.  # noqa: E501

        Query id  # noqa: E501

        :return: The query_id of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ScheduledPlan.

        Query id  # noqa: E501

        :param query_id: The query_id of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def scheduled_plan_destination(self):
        """Gets the scheduled_plan_destination of this ScheduledPlan.  # noqa: E501

        Scheduled plan destinations  # noqa: E501

        :return: The scheduled_plan_destination of this ScheduledPlan.  # noqa: E501
        :rtype: list[ScheduledPlanDestination]
        """
        return self._scheduled_plan_destination

    @scheduled_plan_destination.setter
    def scheduled_plan_destination(self, scheduled_plan_destination):
        """Sets the scheduled_plan_destination of this ScheduledPlan.

        Scheduled plan destinations  # noqa: E501

        :param scheduled_plan_destination: The scheduled_plan_destination of this ScheduledPlan.  # noqa: E501
        :type: list[ScheduledPlanDestination]
        """

        self._scheduled_plan_destination = scheduled_plan_destination

    @property
    def run_once(self):
        """Gets the run_once of this ScheduledPlan.  # noqa: E501

        Whether the plan in question should only be run once (usually for testing)  # noqa: E501

        :return: The run_once of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._run_once

    @run_once.setter
    def run_once(self, run_once):
        """Sets the run_once of this ScheduledPlan.

        Whether the plan in question should only be run once (usually for testing)  # noqa: E501

        :param run_once: The run_once of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._run_once = run_once

    @property
    def include_links(self):
        """Gets the include_links of this ScheduledPlan.  # noqa: E501

        Whether links back to Looker should be included in this ScheduledPlan  # noqa: E501

        :return: The include_links of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._include_links

    @include_links.setter
    def include_links(self, include_links):
        """Sets the include_links of this ScheduledPlan.

        Whether links back to Looker should be included in this ScheduledPlan  # noqa: E501

        :param include_links: The include_links of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._include_links = include_links

    @property
    def pdf_paper_size(self):
        """Gets the pdf_paper_size of this ScheduledPlan.  # noqa: E501

        The size of paper a PDF should be rendered for  # noqa: E501

        :return: The pdf_paper_size of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._pdf_paper_size

    @pdf_paper_size.setter
    def pdf_paper_size(self, pdf_paper_size):
        """Sets the pdf_paper_size of this ScheduledPlan.

        The size of paper a PDF should be rendered for  # noqa: E501

        :param pdf_paper_size: The pdf_paper_size of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._pdf_paper_size = pdf_paper_size

    @property
    def pdf_landscape(self):
        """Gets the pdf_landscape of this ScheduledPlan.  # noqa: E501

        Whether the paper should be landscape  # noqa: E501

        :return: The pdf_landscape of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._pdf_landscape

    @pdf_landscape.setter
    def pdf_landscape(self, pdf_landscape):
        """Sets the pdf_landscape of this ScheduledPlan.

        Whether the paper should be landscape  # noqa: E501

        :param pdf_landscape: The pdf_landscape of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._pdf_landscape = pdf_landscape

    @property
    def embed(self):
        """Gets the embed of this ScheduledPlan.  # noqa: E501

        Whether this schedule is in an embed context or not  # noqa: E501

        :return: The embed of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._embed

    @embed.setter
    def embed(self, embed):
        """Sets the embed of this ScheduledPlan.

        Whether this schedule is in an embed context or not  # noqa: E501

        :param embed: The embed of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._embed = embed

    @property
    def color_theme(self):
        """Gets the color_theme of this ScheduledPlan.  # noqa: E501

        Color scheme of the dashboard if applicable  # noqa: E501

        :return: The color_theme of this ScheduledPlan.  # noqa: E501
        :rtype: str
        """
        return self._color_theme

    @color_theme.setter
    def color_theme(self, color_theme):
        """Sets the color_theme of this ScheduledPlan.

        Color scheme of the dashboard if applicable  # noqa: E501

        :param color_theme: The color_theme of this ScheduledPlan.  # noqa: E501
        :type: str
        """

        self._color_theme = color_theme

    @property
    def long_tables(self):
        """Gets the long_tables of this ScheduledPlan.  # noqa: E501

        Whether or not to expand table vis to full length  # noqa: E501

        :return: The long_tables of this ScheduledPlan.  # noqa: E501
        :rtype: bool
        """
        return self._long_tables

    @long_tables.setter
    def long_tables(self, long_tables):
        """Sets the long_tables of this ScheduledPlan.

        Whether or not to expand table vis to full length  # noqa: E501

        :param long_tables: The long_tables of this ScheduledPlan.  # noqa: E501
        :type: bool
        """

        self._long_tables = long_tables

    @property
    def can(self):
        """Gets the can of this ScheduledPlan.  # noqa: E501

        Operations the current user is able to perform on this object  # noqa: E501

        :return: The can of this ScheduledPlan.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """Sets the can of this ScheduledPlan.

        Operations the current user is able to perform on this object  # noqa: E501

        :param can: The can of this ScheduledPlan.  # noqa: E501
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
        if issubclass(ScheduledPlan, dict):
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
        if not isinstance(other, ScheduledPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other