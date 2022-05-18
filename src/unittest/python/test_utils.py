"""Test setup for the Python unittest module."""
import json
from pathlib import Path
from shutil import rmtree
import os


class TestUtils:
    """Test setup for the Python unittest module."""
    json_store = str(Path.home()) + "\\Desktop\\uni\\segundo\\software_devel\\G89.2022.T01.FP\\src\\JsonFiles\\db"
    json_collection = str(Path.home()) + "\\Desktop\\uni\\segundo\\software_devel\\G89.2022.T01.FP\\src\\" \
                                         "JsonFiles\\collection"
    patient_registry = json_store + "\\patient_registry.json"
    vaccination_appointments = json_store + "\\vaccination_appointments.json"
    vaccination_administration = json_store + "\\vaccine_administration.json"

    @classmethod
    def setup_folders(cls):
        """Create folders for testing."""
        Path(cls.json_store).mkdir(parents=True, exist_ok=True)
        Path(cls.json_collection).mkdir(parents=True, exist_ok=True)
        Path(cls.patient_registry) \
            .touch(mode=0o777, exist_ok=True)
        Path(cls.vaccination_appointments) \
            .touch(mode=0o777, exist_ok=True)
        Path(cls.vaccination_administration) \
            .touch(mode=0o777, exist_ok=True)

        cls.clear_json_file(cls.patient_registry)
        cls.clear_json_file(cls.vaccination_appointments)
        cls.clear_json_file(cls.vaccination_administration)

    @classmethod
    def cleanup_all_folders(cls):
        """Cleanup folders for testingbb."""
        rmtree(cls.json_store)

    @classmethod
    def read_json_file(cls, path):
        """jsjs"""
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @classmethod
    def clear_json_file(cls, path):
        """hjajaf"""
        with open(path, "w", encoding="utf-8") as file:
            json.dump([], file)
