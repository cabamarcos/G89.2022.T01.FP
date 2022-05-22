"""Tests for cancel_appointment method"""
from unittest import TestCase
import os
import shutil
from freezegun import freeze_time
from datetime import timedelta
from datetime import datetime
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH, JSON_FILES_RF2_PATH, JSON_FILES_COLLECTION
from uc3m_care import AppointmentsJsonStore
from uc3m_care import PatientsJsonStore


DATE = "2022-03-08"


class TestCancelAppointment(TestCase):
    @freeze_time(DATE)
    def test_cancel_appointment(self):
        """valid test"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()

        # first , prepare my test , remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()

        # add a patient in the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")
        # check the method
        value = my_manager.get_vaccine_date(file_test, DATE)
        file_test2 = JSON_FILES_COLLECTION + "test_ok.json"
        cancel_appointment = my_manager.cancel_appointment(file_test2)
        self.assertEqual("ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b", value)
        # check store_date
        self.assertIsNotNone(file_store_date.find_item(value))