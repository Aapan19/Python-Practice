# Home Work 3
# Exam attend to exam get marks

import random

class Exam:
    def __init__(self, marks=0):
        self.marks = marks
        self.attend = False

    def attend_to_exam(self, attend):
        self.attend = attend
        if attend:
            self.marks = random.randint(75, 100)
        else:
            self.marks = 0

    def get_marks(self):
        if self.attend:
            return self.marks
        else:
            return "Student did not attend the exam"
        
tamim = Exam()
tamim.attend_to_exam(True)
print(tamim.get_marks()) 