import abc
from typing import List
import Assignment
import Student

class Course(abc.ABC):

    def __init__(self,name:str, instructor:str, content:str, quantity:int):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.quantity = quantity
        self.assignments: List = []
        self.students: List[Student] = []

    def enroll_in_course(self, student: Student)->None:
        if len(self.students) >= self.quantity:
            raise ValueError("All seats are taken")
        self.students.append(student)
        

    @abc.abstractmethod
    def add_assignment(self,assignment:Assignment)->None:
        ...