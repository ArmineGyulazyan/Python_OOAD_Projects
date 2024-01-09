from typing import List
import Course
import Student
import Assignment


class Professor:

    def __init__(self, name:str, contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.__courses: List[str] = []

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self,value):
        if not isinstance(value, str):
            raise ValueError("The value must be a string")
        self.__contact_info = value

    @property
    def courses(self):
        return self.__courses

    def teach_course(self, course: 'Course.Course')->None:
        self.courses.append(course.name)

    def grade_assignment(self, assignment: 'Assignment.Assignment', student: 'Student.Student')->None:
        assignment.submit(student)






