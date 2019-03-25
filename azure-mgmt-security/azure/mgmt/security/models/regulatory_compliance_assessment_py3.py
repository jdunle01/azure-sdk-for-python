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

from .resource_py3 import Resource


class RegulatoryComplianceAssessment(Resource):
    """Regulatory compliance assessment details and state.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar description: The description of the regulatory compliance assessment
    :vartype description: str
    :ivar assessment_type: The expected type of assessment contained in the
     AssessmentDetailsLink
    :vartype assessment_type: str
    :ivar assessment_details_link: Link to more detailed assessment results
     data. The response type will be according to the assessmentType field
    :vartype assessment_details_link: str
    :param state: Aggregative state based on the assessment's scanned
     resources states. Possible values include: 'Passed', 'Failed', 'Skipped',
     'Unsupported'
    :type state: str or ~azure.mgmt.security.models.State
    :ivar passed_resources: The given assessment's related resources count
     with passed state.
    :vartype passed_resources: int
    :ivar failed_resources: The given assessment's related resources count
     with failed state.
    :vartype failed_resources: int
    :ivar skipped_resources: The given assessment's related resources count
     with skipped state.
    :vartype skipped_resources: int
    :ivar unsupported_resources: The given assessment's related resources
     count with unsupported state.
    :vartype unsupported_resources: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'description': {'readonly': True},
        'assessment_type': {'readonly': True},
        'assessment_details_link': {'readonly': True},
        'passed_resources': {'readonly': True},
        'failed_resources': {'readonly': True},
        'skipped_resources': {'readonly': True},
        'unsupported_resources': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'assessment_type': {'key': 'properties.assessmentType', 'type': 'str'},
        'assessment_details_link': {'key': 'properties.assessmentDetailsLink', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'passed_resources': {'key': 'properties.passedResources', 'type': 'int'},
        'failed_resources': {'key': 'properties.failedResources', 'type': 'int'},
        'skipped_resources': {'key': 'properties.skippedResources', 'type': 'int'},
        'unsupported_resources': {'key': 'properties.unsupportedResources', 'type': 'int'},
    }

    def __init__(self, *, state=None, **kwargs) -> None:
        super(RegulatoryComplianceAssessment, self).__init__(**kwargs)
        self.description = None
        self.assessment_type = None
        self.assessment_details_link = None
        self.state = state
        self.passed_resources = None
        self.failed_resources = None
        self.skipped_resources = None
        self.unsupported_resources = None