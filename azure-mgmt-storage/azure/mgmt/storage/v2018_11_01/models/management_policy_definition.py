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

from msrest.serialization import Model


class ManagementPolicyDefinition(Model):
    """An object that defines the Lifecycle rule. Each definition is made up with
    a filters set and an actions set.

    All required parameters must be populated in order to send to Azure.

    :param actions: Required. An object that defines the action set.
    :type actions:
     ~azure.mgmt.storage.v2018_11_01.models.ManagementPolicyAction
    :param filters: An object that defines the filter set.
    :type filters:
     ~azure.mgmt.storage.v2018_11_01.models.ManagementPolicyFilter
    """

    _validation = {
        'actions': {'required': True},
    }

    _attribute_map = {
        'actions': {'key': 'actions', 'type': 'ManagementPolicyAction'},
        'filters': {'key': 'filters', 'type': 'ManagementPolicyFilter'},
    }

    def __init__(self, **kwargs):
        super(ManagementPolicyDefinition, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.filters = kwargs.get('filters', None)
