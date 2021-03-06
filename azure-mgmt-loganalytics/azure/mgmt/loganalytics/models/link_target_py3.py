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


class LinkTarget(Model):
    """Metadata for a workspace that isn't linked to an Azure subscription.

    :param customer_id: The GUID that uniquely identifies the workspace.
    :type customer_id: str
    :param display_name: The display name of the workspace.
    :type display_name: str
    :param workspace_name: The DNS valid workspace name.
    :type workspace_name: str
    :param location: The location of the workspace.
    :type location: str
    """

    _attribute_map = {
        'customer_id': {'key': 'customerId', 'type': 'str'},
        'display_name': {'key': 'accountName', 'type': 'str'},
        'workspace_name': {'key': 'workspaceName', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, customer_id: str=None, display_name: str=None, workspace_name: str=None, location: str=None, **kwargs) -> None:
        super(LinkTarget, self).__init__(**kwargs)
        self.customer_id = customer_id
        self.display_name = display_name
        self.workspace_name = workspace_name
        self.location = location
