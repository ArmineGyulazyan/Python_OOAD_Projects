from typing import Dict
import Assignment
import Student

class InClassAssignment(Assignment):

    def __init__(self, problem_name: str, description: str, score):
        super().__init__(problem_name,description)
        self.score = score
        self.student_score: Dict[str, int] = {}

    def submit(self,student:Student)->None:
        self.student_score[student] = self.score

    def view_submissions(self)->None:
        for student,score in self.student_score.items():
            print(student,score)