from typing import List
import Course
import Student
import Assignment


class Professor:

    def __init__(self, name:str, contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.courses: List[Course] = []

    def create_course(self,course:Course)->None:
        self.courses.append(course)

    def grade_assignment(self,assignment: Assignment,student:Student)->None:
        assignment.submit(student)






