"""Class for the attribute Vaccine Date"""
from datetime import datetime
from uc3m_care.data.attribute.attribute import Attribute
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException


class VaccineDate(Attribute):
    """Class for validating the attribute date"""
    _validation_pattern = r"[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    _validation_error_message = "The format of the date is not correct"

    def _validate( self, attr_value: str ) -> float:
        """ Checks if date fullfils the requirements """
        super()._validate(attr_value)
        # Check the date
        try:
            vaccine_date = datetime.fromisoformat(attr_value)
        except ValueError as err:
            raise VaccineManagementException(self._validation_error_message) from err

        vaccine_date_timestamp = vaccine_date.timestamp()

        if vaccine_date_timestamp < datetime.now().timestamp():
            raise VaccineManagementException("The date for the Vaccine has passed")

        return vaccine_date_timestamp
