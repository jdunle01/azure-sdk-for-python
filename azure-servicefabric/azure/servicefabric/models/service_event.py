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

from .fabric_event import FabricEvent


class ServiceEvent(FabricEvent):
    """Represents the base for all Service Events.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ServiceCreatedEvent, ServiceDeletedEvent,
    ServiceNewHealthReportEvent, ServiceHealthReportExpiredEvent

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param service_id: Required. The identity of the service. This ID is an
     encoded representation of the service name. This is used in the REST APIs
     to identify the service resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the service name is "fabric:/myapp/app1/svc1",
     the service identity would be "myapp~app1\\~svc1" in 6.0+ and
     "myapp/app1/svc1" in previous versions.
    :type service_id: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'service_id': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_id': {'key': 'ServiceId', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'ServiceCreated': 'ServiceCreatedEvent', 'ServiceDeleted': 'ServiceDeletedEvent', 'ServiceNewHealthReport': 'ServiceNewHealthReportEvent', 'ServiceHealthReportExpired': 'ServiceHealthReportExpiredEvent'}
    }

    def __init__(self, **kwargs):
        super(ServiceEvent, self).__init__(**kwargs)
        self.service_id = kwargs.get('service_id', None)
        self.kind = 'ServiceEvent'
