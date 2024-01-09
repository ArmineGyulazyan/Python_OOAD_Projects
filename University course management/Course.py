import abc
from typing import List
import Assignment
import Student
import Professor

class Course(abc.ABC):

    def __init__(self,name:str, instructor:"Professor.Professor", content:str, quantity:int):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.quantity = quantity
        self.assignments: List["Assignment.Assignment"] = []
        self.students: List["Student.Student"] = []

    def add_assignment(self,assignment:"Assignment.Assignment")->None:
        self.assignments.append(assignment)

    @abc.abstractmethod
    def ensure_to_pass(self):
        ...

###

