"""Classs for the attribute Cancellation Type"""
from uc3m_care.data.attribute.attribute import Attribute
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException

class CancellationType(Attribute):
    """Class for the attribute Cancellation Type"""
    _validation_error_message = "cancellation_type format is not valid"

    def _validate(self, attr_value : str) -> str:
        """Check if value provided is correct"""
        if attr_value != "Temporal" and attr_value != "Final":
            raise VaccineManagementException(self._validation_error_message)