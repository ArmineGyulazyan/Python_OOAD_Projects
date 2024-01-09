from typing import Dict
import Assignment
import Student


class HwAssignment(Assignment.Assignment):

    def __init__(self, problem_name: str, description: str):
        super().__init__(problem_name,description)
        self.student_mark: Dict[Student.Student, bool] = {}

    def submit(self,student:"Student.Student")->None:
        self.student_mark[student] = True

    def view_submissions(self)->None:
        for student,mark in self.student_mark.items():
            print(student.name,mark)