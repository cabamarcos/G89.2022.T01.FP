"""Subclass of JsonParer for parsing inputs of get_vaccine_date"""
from uc3m_care.parser.json_parser import JsonParser
from uc3m_care.data.attribute.attribute_date_signature import DateSignature
from uc3m_care.data.attribute.attribute_cancellation_type import CancellationType
from uc3m_care.data.attribute.attribute_reason import Reason
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException


class CancellationJsonParser(JsonParser):
    """Subclass of JsonParer for parsing inputs of get_vaccine_date"""
    NV_reason_label = "Label in Json incorrect"
    NV_reason_value = "Value in Json incorrect"
    NV_cancellation_label = "Label in Json incorrect"
    NV_cancellation_value = "Value in Json incorrect"
    NV_date_signature_label = "Label in Json incorrect"
    NV_date_signature_value = "Value in Json incorrect"
    date_key = "date_signature"
    cancellation_key = "cancellation_type"
    reason_key = "reason"

    _JSON_KEYS = [
        date_key,
        cancellation_key,
        reason_key
    ]

    _ERROR_MESSAGES = [
        NV_date_signature_label,
        NV_cancellation_label,
        NV_reason_label
    ]

    def __init__(self, input_file):
        super().__init__(input_file)
        self.validate_date_signature()
        self.validate_cancellation_type()
        self.validate_reason()


    def validate_date_signature(self):
        """validate that the key date_signature from the JSON is correct"""
        date_signature = self._json_content[self.date_key]

        try:
            DateSignature(date_signature)
        except Exception as exception:
            raise VaccineManagementException(self.NV_date_signature_value) from exception

    def validate_cancellation_type(self):
        """validate that the key cancellation_type from the JSON is correct"""
        cancellation_type = self._json_content[self.cancellation_key]

        try:
            CancellationType(cancellation_type)
        except Exception as exception:
            raise VaccineManagementException(self.NV_cancellation_value) from exception

    def validate_reason(self):
        """validate that the key reason from the JSON is correct"""
        reason = self._json_content[self.reason_key]

        try:
            Reason(reason)
        except Exception as exception:
            raise VaccineManagementException(self.NV_reason_value) from exception
