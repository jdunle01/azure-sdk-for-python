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

from .execution_activity import ExecutionActivity


class AzureFunctionActivity(ExecutionActivity):
    """Azure Function activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param method: Required. Rest API method for target endpoint. Possible
     values include: 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'TRACE'
    :type method: str or
     ~azure.mgmt.datafactory.models.AzureFunctionActivityMethod
    :param function_name: Required. Name of the Function that the Azure
     Function Activity will call. Type: string (or Expression with resultType
     string)
    :type function_name: object
    :param headers: Represents the headers that will be sent to the request.
     For example, to set the language and type on a request: "headers" : {
     "Accept-Language": "en-us", "Content-Type": "application/json" }. Type:
     string (or Expression with resultType string).
    :type headers: object
    :param body: Represents the payload that will be sent to the endpoint.
     Required for POST/PUT method, not allowed for GET method Type: string (or
     Expression with resultType string).
    :type body: object
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'method': {'required': True},
        'function_name': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'method': {'key': 'typeProperties.method', 'type': 'str'},
        'function_name': {'key': 'typeProperties.functionName', 'type': 'object'},
        'headers': {'key': 'typeProperties.headers', 'type': 'object'},
        'body': {'key': 'typeProperties.body', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AzureFunctionActivity, self).__init__(**kwargs)
        self.method = kwargs.get('method', None)
        self.function_name = kwargs.get('function_name', None)
        self.headers = kwargs.get('headers', None)
        self.body = kwargs.get('body', None)
        self.type = 'AzureFunctionActivity'
