"""test for json files"""
import unittest
from pathlib import Path
import json
from freezegun import freeze_time
from datetime import datetime
from datetime import timedelta
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH, \
                      JSON_FILES_RF2_PATH, \
                      JSON_FILES_COLLECTION
from uc3m_care import CancellationJsonStore, PatientsJsonStore, AppointmentsJsonStore

DATE = "2022-03-08"

# parameter of the non-right tests
param_list_nok = [('Case_NV_02', 'test_dup_node1.json', 'Wrong JSON Format'),
                  ('Case_NV_03', 'test_del_node1.json', 'Wrong JSON Format'),
                  ('Case_NV_04', 'test_del_node3.json', 'Label in Json incorrect'), # since there are none
                  ('Case_NV_05', 'test_dup_node3.json', 'Wrong JSON Format'),
                  ('Case_NV_06', 'test_del_node5.json', 'Wrong JSON Format'),
                  ('Case_NV_07', 'test_mod_node2.json', 'Wrong JSON Format'),
                  ('Case_NV_08', 'test_dup_node2.json', 'Wrong JSON Format'),
                  ('Case_NV_09', 'test_del_node6.json', 'Wrong JSON Format'),
                  ('Case_NV_10', 'test_dup_node6.json', 'Wrong JSON Format'),
                  ('Case_NV_11', 'test_del_node8.json', 'Wrong JSON Format'),
                  ('Case_NV_12', 'test_dup_node8.json', 'Wrong JSON Format'),
                  ('Case_NV_13', 'test_del_node10.json', 'Wrong JSON Format'),
                  ('Case_NV_14', 'test_dup_node10.json', 'Wrong JSON Format'),
                  ('Case_NV_15', 'test_del_node11.json', 'Wrong JSON Format'),
                  ('Case_NV_16', 'test_dup_node4.json', 'Wrong JSON Format'),
                  ('Case_NV_17', 'test_mod_node4.json', 'Wrong JSON Format'),
                  ('Case_NV_18', 'test_del_node12.json', 'Wrong JSON Format'),
                  ('Case_NV_19', 'test_dup_node12.json', 'Wrong JSON Format'),
                  ('Case_NV_20', 'test_del_node14.json', 'Wrong JSON Format'),
                  ('Case_NV_21', 'test_dup_node14.json', 'Wrong JSON Format'),
                  ('Case_NV_22', 'test_del_node16.json', 'Wrong JSON Format'),
                  ('Case_NV_23', 'test_dup_node16.json', 'Wrong JSON Format'),
                  ('Case_NV_24', 'test_del_node18.json', 'Wrong JSON Format'),
                  ('Case_NV_25', 'test_dup_node18.json', 'Wrong JSON Format'),
                  ('Case_NV_26', 'test_del_node20.json', 'Wrong JSON Format'),
                  ('Case_NV_27', 'test_dup_node20.json', 'Wrong JSON Format'),
                  ('Case_NV_28', 'test_del_node22.json', 'Wrong JSON Format'),
                  ('Case_NV_29', 'test_dup_node22.json', 'Wrong JSON Format'),
                  ('Case_NV_30', 'test_del_quotation.json', 'Wrong JSON Format'),
                  ('Case_NV_31', 'test_dup_quotation.json', 'Wrong JSON Format'),
                  ('Case_NV_32', 'test_mod_quotation.json', 'Wrong JSON Format'),
                  ('Case_NV_33', 'test_del_separator.json', 'Wrong JSON Format'),
                  ('Case_NV_34', 'test_dup_separator.json', 'Wrong JSON Format'),
                  ('Case_NV_35', 'test_mod_separator.json', 'Wrong JSON Format'),
                  ('Case_NV_36', 'test_del_separator2.json', 'Wrong JSON Format'),
                  ('Case_NV_37', 'test_dup_separator2.json', 'Wrong JSON Format'),
                  ('Case_NV_37', 'test_dup_separator2.json', 'Wrong JSON Format'),
                  ('Case_NV_38', 'test_mod_separator2.json', 'Wrong JSON Format'),
                  ('Case_NV_39', 'test_del_node45.json', 'Label in Json incorrect'),
                  ('Case_NV_40', 'test_dup_node24.json', 'Label in Json incorrect'),
                  ('Case_NV_41', 'test_mod_node24.json', 'Label in Json incorrect'),
                  ('Case_NV_42',
                   'test_del_node48.json',
                   'Value in Json incorrect'),
                  ('Case_NV_43',
                   'test_dup_node28.json',
                   'Value in Json incorrect'),
                  ('Case_NV_44',
                   'test_mod_node28.json',
                   'Value in Json incorrect'),
                  ('Case_NV_45', 'test_del_node51.json', 'Label in Json incorrect'),
                  ('Case_NV_46', 'test_dup_node31.json', 'Label in Json incorrect'),
                  ('Case_NV_47', 'test_mod_node31.json', 'Label in Json incorrect'),
                  ('Case_NV_48',
                   'test_del_node54.json',
                   'Value in Json incorrect'),
                  ('Case_NV_49',
                   'test_dup_node35.json',
                   'Value in Json incorrect'),
                  ('Case_NV_50',
                   'test_mod_node35.json',
                   'Value in Json incorrect'),
                  ('Case_NV_51', 'test_del_node57.json', 'Label in Json incorrect'),
                  ('Case_NV_52', 'test_dup_node38.json', 'Label in Json incorrect'),
                  ('Case_NV_53', 'test_mod_node38.json', 'Label in Json incorrect'),
                  ('Case_NV_54',
                   'test_del_node60.json',
                   'Value in Json incorrect'),
                  # ('Case_NV_55',
                  #  'test_dup_node42.json',
                  #  'Value in Json incorrect'),
                  # we do not include it since the error is impossible to be located
                  ('Case_NV_56',
                   'test_mod_node42.json',
                   'Value in Json incorrect')]


# "The Cancellation couldn't been created. It already exists."
# "The give date_signature does not correspond to any appointment"
# "The appointment is not active, it has been already cancelled."
# "The date of the appointment has passed"

class TestCancellation(unittest.TestCase):
    """Test the JSONs """

    def setUp(self) -> None:
        """setUp"""
        ...

    @freeze_time(DATE)
    def test_Case_Valid_01(self):    # Existing file and correct content
        """
        Valid JSON
        """
        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()

        # Generate a valid json file
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
            "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
            "+34123456789", "6")
        my_manager.get_vaccine_date(file_test, DATE)

        valid_json = JSON_FILES_COLLECTION + "test_ok.json"

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
        date_signature = my_manager.cancel_appointment(valid_json)
        self.assertEqual(expected_date_signature, date_signature)
        self.assertIsNotNone(cancellation_json_storage.find_item(date_signature))

    @freeze_time(DATE)
    def test_Json_Case_Valid_2(self):
        """
        We need to check if reason is duplicated outside of the parametrized
        test case, sice it is valid
        """

        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()


        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
            "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
            "+34123456789", "6")
        my_manager.get_vaccine_date(file_test, DATE)

        valid_json2 = JSON_FILES_COLLECTION + "test_dup_node42.json"

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
        my_date_signature = my_manager.cancel_appointment(valid_json2)
        self.assertEqual(expected_date_signature, my_date_signature)
        self.assertIsNotNone(cancellation_json_storage.find_item(my_date_signature))

    @freeze_time(DATE)
    def test_Case_NV(self):
        """all invalid cases"""
        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"

        # Generate a valid json file
        file_test = JSON_FILES_RF2_PATH + "test_ok.json"
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
         "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
         "+34123456789", "6")
        my_manager.get_vaccine_date(file_test, DATE)
        
        for case_name, node_name, exception_name in param_list_nok:
            with self.subTest(test=case_name):
                with self.assertRaises(VaccineManagementException) as context:
                    cancellation_json = JSON_FILES_COLLECTION + node_name
                    date_signature = my_manager.cancel_appointment(cancellation_json)
                self.assertEqual(exception_name, context.exception.message)
                self.assertIsNone(cancellation_json_storage.find_item(
                    expected_date_signature
                ))

    @freeze_time(DATE)
    def test_the_appointment_does_not_exist(self):
        """cancellation already exists"""
        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"

        # Generate a valid json file
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
            "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
            "+34123456789", "6")

        with self.assertRaises(VaccineManagementException) as context:
            cancellation_json = JSON_FILES_COLLECTION + "test_ok.json"
            date_signature = my_manager.cancel_appointment(cancellation_json)
        self.assertEqual(
            "There is no appointment with the given data",
            context.exception.message
        )
        self.assertIsNone(cancellation_json_storage.find_item(expected_date_signature))


    @freeze_time(DATE)
    def test_not_valid_appointment_day_has_passed(self):
        """The appointment has already been cancelled"""
        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"

        # Generate a valid json file
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
            "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
            "+34123456789", "6")
        # create an appointment issued at date
        my_manager.get_vaccine_date(JSON_FILES_RF2_PATH + "test_ok.json", DATE)

        # freeze the time to DATE + 1 so the appointment expires
        freezer = freeze_time(datetime.fromisoformat(DATE) + timedelta(days=1))

        freezer.start()
        with self.assertRaises(VaccineManagementException) as context:
            cancellation_json = JSON_FILES_COLLECTION + "test_ok.json"
            date_signature = my_manager.cancel_appointment(cancellation_json)
        self.assertEqual(
            "The date of the appointment has passed",
            context.exception.message
        )
        self.assertIsNone(cancellation_json_storage.find_item(expected_date_signature))
        freezer.stop()

    @freeze_time(DATE)
    def test_not_valid_appointment_has_already_been_cancelled(self):
        """The appointment has already been cancelled"""
        PatientsJsonStore().empty_json_file()
        AppointmentsJsonStore().empty_json_file()
        cancellation_json_storage = CancellationJsonStore()
        cancellation_json_storage.empty_json_file()

        expected_date_signature = "ced0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"

        cancellation_json = JSON_FILES_COLLECTION + "test_ok.json"

        # Generate a valid json file
        my_manager = VaccineManager()
        my_manager.request_vaccination_id(
            "78924cb0-075a-4099-a3ee-f3b562e805b9", "minombre tienelalongitudmaxima", "Regular",
            "+34123456789", "6")
        # create an appointment issued at date
        my_manager.get_vaccine_date(JSON_FILES_RF2_PATH + "test_ok.json", DATE)

        date_signature = my_manager.cancel_appointment(cancellation_json)

        with self.assertRaises(VaccineManagementException) as context:
            date_signature = my_manager.cancel_appointment(cancellation_json)
        self.assertEqual(
            "The Cancellation has been already processed.",
            context.exception.message
        )
        self.assertIsNotNone(cancellation_json_storage.find_item(expected_date_signature))