from abc import ABC, abstractmethod

from constant import GOLD, GRADE_CUTLINE, NORMAL, SILVER

class GradeFactory:
    
    @staticmethod
    def create_grade(score):
        if score >= GRADE_CUTLINE[GOLD]:
            return Gold()
        elif score >= GRADE_CUTLINE[SILVER]:
            return Silver()
        elif score >= GRADE_CUTLINE[NORMAL]:
            return Normal()
        else:
            raise ValueError("NO available Grade :", score)

class Grade(ABC):
    @abstractmethod
    def __repr__(self):
        pass

class Gold(Grade):
    def __repr__(self):
        super().__repr__()
        return GOLD

class Silver(Grade):
    def __repr__(self):
        super().__repr__()
        return SILVER
    
class Normal(Grade):
    def __repr__(self):
        super().__repr__()
        return NORMAL