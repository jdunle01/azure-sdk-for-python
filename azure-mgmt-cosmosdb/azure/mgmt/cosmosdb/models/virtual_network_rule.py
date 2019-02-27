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


class VirtualNetworkRule(Model):
    """Virtual Network ACL Rule object.

    :param id: Resource ID of a subnet, for example:
     /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
    :type id: str
    :param ignore_missing_vnet_service_endpoint: Create firewall rule before
     the virtual network has vnet service endpoint enabled.
    :type ignore_missing_vnet_service_endpoint: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'ignore_missing_vnet_service_endpoint': {'key': 'ignoreMissingVNetServiceEndpoint', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkRule, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.ignore_missing_vnet_service_endpoint = kwargs.get('ignore_missing_vnet_service_endpoint', None)
