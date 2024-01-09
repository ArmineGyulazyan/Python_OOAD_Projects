import abc
import Student


class Assignment(abc.ABC):

    def __init__(self, problem_name: str, description: str):
        self.problem_name = problem_name
        self.description = description

    @abc.abstractmethod
    def submit(self, student: "Student.Student"):
        ...

    @abc.abstractmethod
    def view_submissions(self):
        ...
###