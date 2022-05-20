"""Tests for get_vaccine_date method"""
from unittest import TestCase
import os
import shutil
from freezegun import freeze_time
from datetime import timedelta
from datetime import datetime
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care import JSON_FILES_PATH, JSON_FILES_RF2_PATH
from uc3m_care import AppointmentsJsonStore
from uc3m_care import PatientsJsonStore

DATE = "2022-03-08"

param_list_nok = [("test_dup_all.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_char_plus.json", "phone number is not valid"),
                  ("test_dup_colon.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_comillas.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_comma.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_content.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_data1.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_data1_content.json", "patient system id is not valid"),
                  ("test_dup_data2.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_data2_content.json", "phone number is not valid"),
                  ("test_dup_field1.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_field2.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_final_bracket.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_initial_bracket.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_label1.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_label1_content.json", "Bad label patient_id"),
                  ("test_dup_label2.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_dup_label2_content.json", "Bad label contact phone"),
                  ("test_dup_phone.json", "phone number is not valid"),
                  ("test_empty.json", "Bad label patient_id"),
                  ("test_mod_char_plus.json", "phone number is not valid"),
                  ("test_mod_data1.json", "patient system id is not valid"),
                  ("test_mod_data2.json", "phone number is not valid"),
                  ("test_mod_label1.json", "Bad label patient_id"),
                  ("test_mod_label2.json", "Bad label contact phone"),
                  ("test_mod_phone.json", "phone number is not valid"),
                  ("test_no_char_plus.json", "phone number is not valid"),
                  ("test_no_colon.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_no_comillas.json", "JSON Decode Error - Wrong JSON Format"),
                  ("test_no_phone.json", "phone number is not valid")
                  ]


class TestGetVaccineDate(TestCase):
    """testing get_vaccine_date"""

    @freeze_time(DATE)
    def test_get_date_ok(self):
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
        self.assertEqual("ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b", value)
        # check store_date
        self.assertIsNotNone(file_store_date.find_item(value))

    @freeze_time(DATE)
    def test_get_date_no_ok_parameter(self):
        """tests no ok"""
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
        for file_name, expected_value in param_list_nok:
            with self.subTest(test=file_name):
                file_test = JSON_FILES_RF2_PATH + file_name
                hash_original = file_store_date.data_hash()

                # check
                with self.assertRaises(VaccineManagementException) as c_m:
                    date = my_manager.get_vaccine_date(file_test, DATE)
                self.assertEqual(c_m.exception.message, expected_value)

                # compare
                hash_new = file_store_date.data_hash()

                self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok(self):
        """The length of the patient system id is 32 characters long """
        file_test = JSON_FILES_RF2_PATH + "test_no_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, DATE)
        self.assertEqual(c_m.exception.message, "patient system id is not valid")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_not_quotes(self):
        """ no quotes """
        file_test = JSON_FILES_RF2_PATH + "test_nok_no_comillas.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, DATE)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

        # we compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_data_manipulated(self):
        """ data manipulated """
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store = JSON_FILES_PATH + "store_patient.json"
        file_store_date = JSON_FILES_PATH + "store_date.json"

        if os.path.isfile(JSON_FILES_PATH + "swap.json"):
            os.remove(JSON_FILES_PATH + "swap.json")
        if not os.path.isfile(JSON_FILES_PATH + "store_patient_manipulated.json"):
            shutil.copy(JSON_FILES_RF2_PATH + "store_patient_manipulated.json",
                        JSON_FILES_PATH + "store_patient_manipulated.json")

        # rename
        if os.path.isfile(file_store):
            print(file_store)
            print(JSON_FILES_PATH + "swap.json")
            os.rename(file_store, JSON_FILES_PATH + "swap.json")
        os.rename(JSON_FILES_PATH + "store_patient_manipulated.json", file_store)

        file_store_date = AppointmentsJsonStore()
        # read the file
        hash_original = file_store_date.data_hash()

        # check

        exception_message = "Exception not raised"
        try:
            my_manager.get_vaccine_date(file_test, DATE)

        except Exception as exception_raised:
            exception_message = exception_raised.__str__()

        # restore patient's store
        os.rename(file_store, JSON_FILES_PATH + "store_patient_manipulated.json")
        if os.path.isfile(JSON_FILES_PATH + "swap.json"):
            print(JSON_FILES_PATH + "swap.json")
            print(file_store)
            os.rename(JSON_FILES_PATH + "swap.json", file_store)

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(exception_message, "Patient's data have been manipulated")
        self.assertEqual(hash_new, hash_original)

# new tests
    @freeze_time(DATE)
    def test_get_date_no_ok_outdated(self):
        """ outdated date """
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        # get prev date
        yesterday_date = datetime.strptime(DATE, "%Y-%m-%d") - timedelta(days=1)
        yesterday_date = str(yesterday_date).split(" ", maxsplit=1)[0]

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, yesterday_date)
        self.assertEqual(c_m.exception.message, "Vaccine date is outdated")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_BV_one_char_less(self):
        """ one character less """
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_one_char_less = "2200-01-0"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_one_char_less)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_BV_one_char_more(self):
        """One character more"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_one_char_more = "2200-01-015"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_one_char_more)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_dash(self):
        """Missing dash"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_invalid = "2200--01-05"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_vaccine_date_no_ok_BV_month_exc(self):
        """Month does not exist"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_invalid = "2200-13-07"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_BV_month_0(self):
        """ month 0 """
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_invalid = "2200-00-09"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_BV_days_exceed(self):
        """ day too big """
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_invalid = "2200-01-32"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_date_no_ok_BV_day_0(self):
        """day 0"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file
        hash_original = file_store_date.data_hash()

        date_invalid = "2200-08-00"

        # check
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # read the file
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)

    @freeze_time(DATE)
    def test_get_vaccine_date_no_ok_BV_year_0(self):
        """Year 0"""
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        file_store_date = AppointmentsJsonStore()

        # read the file to compare file content before and after method call
        hash_original = file_store_date.data_hash()

        date_invalid = "0000-01-01"

        # check the method
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, date_invalid)
        self.assertEqual(c_m.exception.message, "Vaccine date has an invalid format")

        # read the file again to compare
        hash_new = file_store_date.data_hash()

        self.assertEqual(hash_new, hash_original)
