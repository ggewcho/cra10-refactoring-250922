from unittest import TestCase
import unittest

from main import main
from src.administrator import Administrator
from src.file_reader import FileReader

import pandas as pd

SAMPLE_DATA_PATH = "attendance_weekday_500.txt"
WRONG_DATA_PATH = "tests/wrond_data.csv"
SAMPLE_RESULT_PATH = "tests/sample_result.csv"

NAME = "name"
POINT = "point"
GRADE = "grade"

class MainTests(TestCase):
    @classmethod
    def setUpClass(self):
        self.args = FileReader.parse_file(SAMPLE_DATA_PATH)
        self.admin = Administrator()
        self.admin.update(self.args)
        self.result_df = pd.read_csv(SAMPLE_RESULT_PATH)
        self.result_df = self.result_df.set_index("name")

    def test_main(self):
        main()

    def test_no_file(self):
        with self.assertRaises(FileNotFoundError):
            FileReader.parse_file(WRONG_DATA_PATH)

    def test_member_num(self):
        self.assertEqual(len(self.admin.member_dict), 19)
        self.assertEqual(len(self.result_df), 19)

    def test_member_score(self):
        for member in self.admin.member_dict.values():
            self.assertEqual(member.score, self.result_df.loc[member.name][POINT]) 
    
    def test_member_grade(self):
        for member in self.admin.member_dict.values():
            self.assertEqual(str(member.grade), self.result_df.loc[member.name][GRADE]) 

    def test_print_result(self):
        self.admin.print_result()