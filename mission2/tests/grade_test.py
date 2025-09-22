from unittest import TestCase

from constant import GOLD, GRADE_CUTLINE, MON, NORMAL, SAT, SILVER
from src.grade import GradeFactory
from src.member import Member
from src.administrator import Administrator
from src.file_reader import FileReader

import pandas as pd

sample_days = [SAT, SAT, MON]

class GradeTests(TestCase):
    def test_grade(self):
        self.assertEqual(str(GradeFactory.create_grade(GRADE_CUTLINE[GOLD])), GOLD)
        self.assertEqual(str(GradeFactory.create_grade(GRADE_CUTLINE[SILVER])), SILVER)
        self.assertEqual(str(GradeFactory.create_grade(GRADE_CUTLINE[NORMAL])), NORMAL)
        with self.assertRaises(ValueError):
            GradeFactory.create_grade(-1)
        

    