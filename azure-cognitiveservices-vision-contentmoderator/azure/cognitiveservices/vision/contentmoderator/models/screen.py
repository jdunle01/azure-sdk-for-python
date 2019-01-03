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


class Screen(Model):
    """The response for a Screen text request.

    :param original_text: The original text.
    :type original_text: str
    :param normalized_text: The normalized text.
    :type normalized_text: str
    :param auto_corrected_text: The autocorrected text
    :type auto_corrected_text: str
    :param misrepresentation: The misrepresentation text.
    :type misrepresentation: list[str]
    :param classification: The classification details of the text.
    :type classification:
     ~azure.cognitiveservices.vision.contentmoderator.models.Classification
    :param status: The evaluate status.
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.Status
    :param pii: Personal Identifier Information details.
    :type pii: ~azure.cognitiveservices.vision.contentmoderator.models.PII
    :param language: Language of the input text content.
    :type language: str
    :param terms:
    :type terms:
     list[~azure.cognitiveservices.vision.contentmoderator.models.DetectedTerms]
    :param tracking_id: Unique Content Moderator transaction Id.
    :type tracking_id: str
    """

    _attribute_map = {
        'original_text': {'key': 'OriginalText', 'type': 'str'},
        'normalized_text': {'key': 'NormalizedText', 'type': 'str'},
        'auto_corrected_text': {'key': 'AutoCorrectedText', 'type': 'str'},
        'misrepresentation': {'key': 'Misrepresentation', 'type': '[str]'},
        'classification': {'key': 'Classification', 'type': 'Classification'},
        'status': {'key': 'Status', 'type': 'Status'},
        'pii': {'key': 'PII', 'type': 'PII'},
        'language': {'key': 'Language', 'type': 'str'},
        'terms': {'key': 'Terms', 'type': '[DetectedTerms]'},
        'tracking_id': {'key': 'TrackingId', 'type': 'str'},
    }

    def __init__(self, original_text=None, normalized_text=None, auto_corrected_text=None, misrepresentation=None, classification=None, status=None, pii=None, language=None, terms=None, tracking_id=None):
        super(Screen, self).__init__()
        self.original_text = original_text
        self.normalized_text = normalized_text
        self.auto_corrected_text = auto_corrected_text
        self.misrepresentation = misrepresentation
        self.classification = classification
        self.status = status
        self.pii = pii
        self.language = language
        self.terms = terms
        self.tracking_id = tracking_id