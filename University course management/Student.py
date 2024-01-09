from typing import List
import Course
import Assignment

class Student:

    def __init__(self, name:str, contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.__courses_enrolled: List['Course.Course'] = []

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise ValueError("The value must be a string")
        self.__contact_info = value

    @property
    def courses_enrolled(self):
        return self.__courses_enrolled

    def enroll_in_course(self, course: 'Course.Course')->None:
        if len(course.students) >= course.quantity:
            raise ValueError("All seats are taken")
        self.courses_enrolled.append(course)
        course.students.append(self)

    def submit_assignment(self,assignment:'Assignment.Assignment'):
        assignment.submit(self)

    def view_progress(self, course: 'Course.Course'):

        if course not in self.courses_enrolled:
            raise ValueError("Not enrolled in the course")
        if isinstance(course, Course.Course) and hasattr(course, "credit"):
            print(f"credit for course is {course.credit}")

        for assignment in course.assignments:
            if isinstance(assignment, Assignment.Assignment):
                assignment.view_submissions()




###