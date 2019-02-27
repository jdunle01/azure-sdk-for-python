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

from .proxy_only_resource_py3 import ProxyOnlyResource


class RestoreRequest(ProxyOnlyResource):
    """Description of a restore request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param storage_account_url: Required. SAS URL to the container.
    :type storage_account_url: str
    :param blob_name: Name of a blob which contains the backup.
    :type blob_name: str
    :param overwrite: Required. <code>true</code> if the restore operation can
     overwrite target app; otherwise, <code>false</code>. <code>true</code> is
     needed if trying to restore over an existing app.
    :type overwrite: bool
    :param site_name: Name of an app.
    :type site_name: str
    :param databases: Collection of databases which should be restored. This
     list has to match the list of databases included in the backup.
    :type databases: list[~azure.mgmt.web.models.DatabaseBackupSetting]
    :param ignore_conflicting_host_names: Changes a logic when restoring an
     app with custom domains. <code>true</code> to remove custom domains
     automatically. If <code>false</code>, custom domains are added to
     the app's object when it is being restored, but that might fail due to
     conflicts during the operation. Default value: False .
    :type ignore_conflicting_host_names: bool
    :param ignore_databases: Ignore the databases and only restore the site
     content. Default value: False .
    :type ignore_databases: bool
    :param app_service_plan: Specify app service plan that will own restored
     site.
    :type app_service_plan: str
    :param operation_type: Operation type. Possible values include: 'Default',
     'Clone', 'Relocation', 'Snapshot', 'CloudFS'. Default value: "Default" .
    :type operation_type: str or
     ~azure.mgmt.web.models.BackupRestoreOperationType
    :param adjust_connection_strings: <code>true</code> if
     SiteConfig.ConnectionStrings should be set in new app; otherwise,
     <code>false</code>.
    :type adjust_connection_strings: bool
    :param hosting_environment: App Service Environment name, if needed (only
     when restoring an app to an App Service Environment).
    :type hosting_environment: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'storage_account_url': {'required': True},
        'overwrite': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'storage_account_url': {'key': 'properties.storageAccountUrl', 'type': 'str'},
        'blob_name': {'key': 'properties.blobName', 'type': 'str'},
        'overwrite': {'key': 'properties.overwrite', 'type': 'bool'},
        'site_name': {'key': 'properties.siteName', 'type': 'str'},
        'databases': {'key': 'properties.databases', 'type': '[DatabaseBackupSetting]'},
        'ignore_conflicting_host_names': {'key': 'properties.ignoreConflictingHostNames', 'type': 'bool'},
        'ignore_databases': {'key': 'properties.ignoreDatabases', 'type': 'bool'},
        'app_service_plan': {'key': 'properties.appServicePlan', 'type': 'str'},
        'operation_type': {'key': 'properties.operationType', 'type': 'BackupRestoreOperationType'},
        'adjust_connection_strings': {'key': 'properties.adjustConnectionStrings', 'type': 'bool'},
        'hosting_environment': {'key': 'properties.hostingEnvironment', 'type': 'str'},
    }

    def __init__(self, *, storage_account_url: str, overwrite: bool, kind: str=None, blob_name: str=None, site_name: str=None, databases=None, ignore_conflicting_host_names: bool=False, ignore_databases: bool=False, app_service_plan: str=None, operation_type="Default", adjust_connection_strings: bool=None, hosting_environment: str=None, **kwargs) -> None:
        super(RestoreRequest, self).__init__(kind=kind, **kwargs)
        self.storage_account_url = storage_account_url
        self.blob_name = blob_name
        self.overwrite = overwrite
        self.site_name = site_name
        self.databases = databases
        self.ignore_conflicting_host_names = ignore_conflicting_host_names
        self.ignore_databases = ignore_databases
        self.app_service_plan = app_service_plan
        self.operation_type = operation_type
        self.adjust_connection_strings = adjust_connection_strings
        self.hosting_environment = hosting_environment
