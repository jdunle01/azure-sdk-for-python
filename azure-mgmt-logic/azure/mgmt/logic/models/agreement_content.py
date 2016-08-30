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


class AgreementContent(Model):
    """AgreementContent.

    :param as2: The AS2 agreement content.
    :type as2: :class:`AS2AgreementContent
     <azure.mgmt.logic.models.AS2AgreementContent>`
    :param x12: The X12 agreement content.
    :type x12: :class:`X12AgreementContent
     <azure.mgmt.logic.models.X12AgreementContent>`
    :param edifact: The EDIFACT agreement content.
    :type edifact: :class:`EdifactAgreementContent
     <azure.mgmt.logic.models.EdifactAgreementContent>`
    """ 

    _attribute_map = {
        'as2': {'key': 'AS2', 'type': 'AS2AgreementContent'},
        'x12': {'key': 'X12', 'type': 'X12AgreementContent'},
        'edifact': {'key': 'Edifact', 'type': 'EdifactAgreementContent'},
    }

    def __init__(self, as2=None, x12=None, edifact=None):
        self.as2 = as2
        self.x12 = x12
        self.edifact = edifact