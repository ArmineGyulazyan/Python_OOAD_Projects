from typing import List
import Course
import Assignment


class Graduate_course(Course):
    def __init__(self, name: str, instructor: str, content: str, quantity:int, thesis_topics:List[str]):
        super().__init__(name, instructor, content,quantity)
        self.thesis_topics = thesis_topics

    def add_assignment(self,assignment:Assignment)->None:
        self.assignments.append(assignment)
