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


class ChangeNotReimportedEntry(Model):
    """The object entry in a change that is not re-imported.

    :param anchor: The anchor.
    :type anchor: str
    :param parent_anchor: The parent anchor.
    :type parent_anchor: str
    :param primary_object_class: The primary object class.
    :type primary_object_class: str
    :param object_classes: The list of object classes.
    :type object_classes: list[str]
    :param dn_attributes: The delta attributes for distinguished names.
    :type dn_attributes:
     list[~azure.mgmt.adhybridhealthservice.models.AttributeDelta]
    :param attributes: The attributes.
    :type attributes:
     list[~azure.mgmt.adhybridhealthservice.models.AttributeDelta]
    :param dn: The distinguished name.
    :type dn: str
    """

    _attribute_map = {
        'anchor': {'key': 'anchor', 'type': 'str'},
        'parent_anchor': {'key': 'parentAnchor', 'type': 'str'},
        'primary_object_class': {'key': 'primaryObjectClass', 'type': 'str'},
        'object_classes': {'key': 'objectClasses', 'type': '[str]'},
        'dn_attributes': {'key': 'dnAttributes', 'type': '[AttributeDelta]'},
        'attributes': {'key': 'attributes', 'type': '[AttributeDelta]'},
        'dn': {'key': 'dn', 'type': 'str'},
    }

    def __init__(self, *, anchor: str=None, parent_anchor: str=None, primary_object_class: str=None, object_classes=None, dn_attributes=None, attributes=None, dn: str=None, **kwargs) -> None:
        super(ChangeNotReimportedEntry, self).__init__(**kwargs)
        self.anchor = anchor
        self.parent_anchor = parent_anchor
        self.primary_object_class = primary_object_class
        self.object_classes = object_classes
        self.dn_attributes = dn_attributes
        self.attributes = attributes
        self.dn = dn