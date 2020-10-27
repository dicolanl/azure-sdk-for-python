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


class IncidentLabel(Model):
    """Represents an incident label.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param label_name: Required. The name of the label
    :type label_name: str
    :ivar label_type: The type of the label. Possible values include: 'User',
     'System'
    :vartype label_type: str or
     ~azure.mgmt.securityinsight.models.IncidentLabelType
    """

    _validation = {
        'label_name': {'required': True},
        'label_type': {'readonly': True},
    }

    _attribute_map = {
        'label_name': {'key': 'labelName', 'type': 'str'},
        'label_type': {'key': 'labelType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IncidentLabel, self).__init__(**kwargs)
        self.label_name = kwargs.get('label_name', None)
        self.label_type = None
