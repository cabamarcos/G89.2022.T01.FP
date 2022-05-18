"""# HSBGKJBAFNLAKM"""
import unittest
from uc3m_care.vaccine_manager import VaccineManager
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from test_utils import TestUtils
from pathlib import Path
import json

class MyTestCase(unittest.TestCase):
    """Code for all test cases"""

    def test_something(self):
        """example test"""
        # execute sth
        # check the result using assertions
        self.assertEqual(True, True)

    @classmethod
    def setUpClass(cls) -> None:
        # CREATE THE FOLDERS AND FILES FOR TESTING
        # setUpClass JUST AFTER THE OBJECT HAS BEEN CREATED
        TestUtils.setup_folders()

    @classmethod
    def tearDownClass(cls) -> None:
        # DELETE THE JSON FILES AT THE END OF THE TEST PROCESS
        # IF YOU WANT TO SEE THE CONTENT OF THE FILES
        # PLEASE COMMENT THE SENTENCE BELOW
        # AND AT THE END OF THE TESTS YOU CAN TAKE A LOOK AT THE CONTENT
        # tearDownClass IS EXECUTED AT THE END OF THE PROCESS
        TestUtils.cleanup_all_folders()

    def setUp(self) -> None:
        """setUp IS EXECUTED ONCE BEFORE EACH TEST"""
        TestUtils.cleanup_all_folders()
        self.patient_id = "ab7eb12e-3e84-4f17-92d3-a454e2049d7a"
        self.registration_type = "Regular"
        self.name_surname = "Maria Garcia"
        self.phone_number = "674839567"
        self.age = 45
        self.json_store = str(Path.home()) + "\\Desktop\\uni\\segundo\\software_devel\\G89.2022.T01.GE3_\\json\\db"
        self.collection = TestUtils.json_collection
        self.test_json = str(Path.home()) + "\\Desktop\\uni\\segundo\\software_devel\\G89.2022.T01.GE3_\\json\\collection"
        self.patient_registry = self.json_store + "\\patient_registry.json"
        self.my_manager = VaccineManager()
        TestUtils.setup_folders()

    def test_Case_Valid_01(self):    # Existing file and correct content
        """
        This test checks if the valid jason file is recognized with no error
        """
        # Request the vaccination id
        test_file = self.test_json + "/test_ok.json"
        # Get the vaccine date
        result =

    def test_Case_NV_02(self):
        """Invalid sintax, node 1 duplicated"""
        test_file = self.test_json + "/test_ok.json"
        result =

