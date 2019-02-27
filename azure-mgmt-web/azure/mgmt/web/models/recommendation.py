# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class Recommendation(ProxyOnlyResource):
    """Represents a recommendation result generated by the recommendation engine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param creation_time: Timestamp when this instance was created.
    :type creation_time: datetime
    :param recommendation_id: A GUID value that each recommendation object is
     associated with.
    :type recommendation_id: str
    :param resource_id: Full ARM resource ID string that this recommendation
     object is associated with.
    :type resource_id: str
    :param resource_scope: Name of a resource type this recommendation
     applies, e.g. Subscription, ServerFarm, Site. Possible values include:
     'ServerFarm', 'Subscription', 'WebSite'
    :type resource_scope: str or ~azure.mgmt.web.models.ResourceScopeType
    :param rule_name: Unique name of the rule.
    :type rule_name: str
    :param display_name: UI friendly name of the rule (may not be unique).
    :type display_name: str
    :param message: Recommendation text.
    :type message: str
    :param level: Level indicating how critical this recommendation can
     impact. Possible values include: 'Critical', 'Warning', 'Information',
     'NonUrgentSuggestion'
    :type level: str or ~azure.mgmt.web.models.NotificationLevel
    :param channels: List of channels that this recommendation can apply.
     Possible values include: 'Notification', 'Api', 'Email', 'Webhook', 'All'
    :type channels: str or ~azure.mgmt.web.models.Channels
    :ivar category_tags: The list of category tags that this recommendation
     belongs to.
    :vartype category_tags: list[str]
    :param action_name: Name of action recommended by this object.
    :type action_name: str
    :param enabled: True if this recommendation is still valid (i.e.
     "actionable"). False if it is invalid.
    :type enabled: int
    :param states: The list of states of this recommendation. If it's null
     then it should be considered "Active".
    :type states: list[str]
    :param start_time: The beginning time in UTC of a range that the
     recommendation refers to.
    :type start_time: datetime
    :param end_time: The end time in UTC of a range that the recommendation
     refers to.
    :type end_time: datetime
    :param next_notification_time: When to notify this recommendation next in
     UTC. Null means that this will never be notified anymore.
    :type next_notification_time: datetime
    :param notification_expiration_time: Date and time in UTC when this
     notification expires.
    :type notification_expiration_time: datetime
    :param notified_time: Last timestamp in UTC this instance was actually
     notified. Null means that this recommendation hasn't been notified yet.
    :type notified_time: datetime
    :param score: A metric value measured by the rule.
    :type score: float
    :param is_dynamic: True if this is associated with a dynamically added
     rule
    :type is_dynamic: bool
    :param extension_name: Extension name of the portal if exists.
    :type extension_name: str
    :param blade_name: Deep link to a blade on the portal.
    :type blade_name: str
    :param forward_link: Forward link to an external document associated with
     the rule.
    :type forward_link: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'category_tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'recommendation_id': {'key': 'properties.recommendationId', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'resource_scope': {'key': 'properties.resourceScope', 'type': 'str'},
        'rule_name': {'key': 'properties.ruleName', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'level': {'key': 'properties.level', 'type': 'NotificationLevel'},
        'channels': {'key': 'properties.channels', 'type': 'Channels'},
        'category_tags': {'key': 'properties.categoryTags', 'type': '[str]'},
        'action_name': {'key': 'properties.actionName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'int'},
        'states': {'key': 'properties.states', 'type': '[str]'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'next_notification_time': {'key': 'properties.nextNotificationTime', 'type': 'iso-8601'},
        'notification_expiration_time': {'key': 'properties.notificationExpirationTime', 'type': 'iso-8601'},
        'notified_time': {'key': 'properties.notifiedTime', 'type': 'iso-8601'},
        'score': {'key': 'properties.score', 'type': 'float'},
        'is_dynamic': {'key': 'properties.isDynamic', 'type': 'bool'},
        'extension_name': {'key': 'properties.extensionName', 'type': 'str'},
        'blade_name': {'key': 'properties.bladeName', 'type': 'str'},
        'forward_link': {'key': 'properties.forwardLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Recommendation, self).__init__(**kwargs)
        self.creation_time = kwargs.get('creation_time', None)
        self.recommendation_id = kwargs.get('recommendation_id', None)
        self.resource_id = kwargs.get('resource_id', None)
        self.resource_scope = kwargs.get('resource_scope', None)
        self.rule_name = kwargs.get('rule_name', None)
        self.display_name = kwargs.get('display_name', None)
        self.message = kwargs.get('message', None)
        self.level = kwargs.get('level', None)
        self.channels = kwargs.get('channels', None)
        self.category_tags = None
        self.action_name = kwargs.get('action_name', None)
        self.enabled = kwargs.get('enabled', None)
        self.states = kwargs.get('states', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.next_notification_time = kwargs.get('next_notification_time', None)
        self.notification_expiration_time = kwargs.get('notification_expiration_time', None)
        self.notified_time = kwargs.get('notified_time', None)
        self.score = kwargs.get('score', None)
        self.is_dynamic = kwargs.get('is_dynamic', None)
        self.extension_name = kwargs.get('extension_name', None)
        self.blade_name = kwargs.get('blade_name', None)
        self.forward_link = kwargs.get('forward_link', None)
