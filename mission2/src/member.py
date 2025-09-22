from constant import DAYS, SCORE_OF_DAY, TRAINING_DAY, TRAINING_DAY_BONUS_CONDITION, TRAINING_DAY_BONUS_SCORE, WEEKEND, WEEKEND_BONUS_CONDITION, WEEKEND_BONUS_SCORE
from src.grade import GradeFactory, Normal


class Member:
    member_num = 0

    def __init__(self, name):
        Member.member_num += 1
        self.mid = Member.member_num
        self.name = name
        self._day_attendance_dict = {day:0 for day in DAYS}
        self.score = 0
        self.grade = None

    def attend(self, day):
        self._day_attendance_dict[day] += 1

    def update(self):
        self.score = self._get_score()
        self.grade = GradeFactory.create_grade(self.score)

    def _get_score(self):
        score = self._get_attendance_score()
        score += self._get_bonus_score()
        return score
    
    def _get_attendance_score(self):
        score = 0
        for day, cnt in self._day_attendance_dict.items():
            score += cnt * SCORE_OF_DAY[day]
        return score    

    def _get_bonus_score(self):
        score = 0
        if sum([self._day_attendance_dict[day] for day in TRAINING_DAY]) >= TRAINING_DAY_BONUS_CONDITION:
            score += TRAINING_DAY_BONUS_SCORE
        if sum([self._day_attendance_dict[day] for day in WEEKEND]) >= WEEKEND_BONUS_CONDITION:
            score += WEEKEND_BONUS_SCORE
        return score

        
    def is_removable_member(self):
        if isinstance(self.grade, Normal) and \
            sum([self._day_attendance_dict[day] for day in TRAINING_DAY]) == 0 and \
            sum([self._day_attendance_dict[day] for day in WEEKEND]) == 0:
            return True

    def __repr__(self):
        score = self._get_score()
        grade = GradeFactory.create_grade(score)
        return f"NAME : {self.name}, POINT : {score}, GRADE : {grade}"