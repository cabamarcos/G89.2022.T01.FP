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


    def test_Case_NV_02(self):
        """Invalid syntax, node 1 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

             test_file = self.test_json + "/test_dup_node1"
        self.assertEqual('The json format is not correct', message.exception.message)


    def test_Case_NV_03(self):
        """Invalid syntax, node 1 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node1"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_04(self):
        """Invalid syntax, node 3 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node3"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_05(self):
        """Invalid syntax, node 3 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node3.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_06(self):
        """Invalid syntax, node 5 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node5.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_07(self):
        """Invalid syntax, node 5 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node2.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_08(self):
        """Invalid syntax, node 5 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node2.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_09(self):
        """Invalid syntax, node 6 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node6.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_10(self):
        """Invalid syntax, node 6 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node6.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_11(self):
        """Invalid syntax, node 11 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node11.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_12(self):
        """Invalid syntax, node 11 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node4.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_13(self):
        """Invalid syntax, node 11 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node4.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_14(self):
        """Invalid syntax, node 12 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node12.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_15(self):
        """Invalid syntax, node 12 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node12.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_16(self):
        """Invalid syntax, node 14 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node14.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_17(self):
        """Invalid syntax, node 14 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node14.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_18(self):
        """Invalid syntax, node 16 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node16.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_19(self):
        """Invalid syntax, node 16 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node16.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_20(self):
        """Invalid syntax, node 18 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node18.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_21(self):
        """Invalid syntax, node 18 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node18.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_22(self):
        """Invalid syntax, node 20 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node20.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_23(self):
        """Invalid syntax, node 20 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node20.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_24(self):
        """Invalid syntax, node 22 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node22.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_25(self):
        """Invalid syntax, node 22 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node22.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_26(self):
        """Invalid syntax, node quotation deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_quotation.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_27(self):
        """Invalid syntax, node quotation duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_quotation.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_28(self):
        """Invalid syntax, node quotation modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_quotation.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_29(self):
        """Invalid syntax, node separator deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_separator.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_30(self):
        """Invalid syntax, node separator duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_separator.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_31(self):
        """Invalid syntax, node separator modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_separator.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_32(self):
        """Invalid syntax, node separator2 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_separator2.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_33(self):
        """Invalid syntax, node separator2 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_separator2.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_34(self):
        """Invalid syntax, node separator2 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_separator2.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_35(self):
        """Invalid syntax, node 45 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node45.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_36(self):
        """Invalid syntax, node 45 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json +  "/test_dup_node24.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_37(self):
        """Invalid syntax, node 45 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node24.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_38(self):
        """Invalid syntax, node 48 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node45.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_39(self):
        """Invalid syntax, node 48 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node28.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_40(self):
        """Invalid syntax, node 48 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node28.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_41(self):
        """Invalid syntax, node 51 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node51.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_42(self):
        """Invalid syntax, node 51 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node31.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_43(self):
        """Invalid syntax, node 51 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node31.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_44(self):
        """Invalid syntax, node 54 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node54.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_45(self):
        """Invalid syntax, node 54 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node35.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_46(self):
        """Invalid syntax, node 54 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node35.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_47(self):
        """Invalid syntax, node 57 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node57.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_48(self):
        """Invalid syntax, node 57 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node38.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_49(self):
        """Invalid syntax, node 57 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node38.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_50(self):
        """Invalid syntax, node 60 deleted"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_del_node60.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_51(self):
        """Invalid syntax, node 60 duplicated"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_dup_node42.json"

        self.assertEqual('The json format is not correct', message.exception.message)

    def test_Case_NV_52(self):
        """Invalid syntax, node 60 modified"""
        with self.assertRaises(VaccineManagementException) as message:

            test_file = self.test_json + "/test_mod_node42.json"

        self.assertEqual('The json format is not correct', message.exception.message)






