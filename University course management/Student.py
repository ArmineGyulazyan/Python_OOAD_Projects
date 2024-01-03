from typing import Union
import Student
import Undergraduate_course
import Gradate_course
import HwAssignment

class Student:

    def __init__(self, name:str, contact_info:str):
        self.name = name
        self.contact_info = contact_info

    def view_progress(self,course:Union[Undergraduate_course,Gradate_course],student:Student):
        if student not in course.students:
            raise ValueError("Student is not enrolled in the course")
        if isinstance(course, Undergraduate_course):
            print(course.credit)
        for assignment in course.assignments:
            if isinstance(assignment, HwAssignment):
                assignment.view_submissions()
            else:
                assignment.view_submissions()
