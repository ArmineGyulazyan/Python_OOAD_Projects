import Course
import Assignment


class Undergraduate_course(Course):

    def __init__(self,name:str, instructor:str, content:str,credit:int,quantity:int):
        super().__init__(name,instructor,content,quantity)
        self.credit = credit

    def add_assignment(self,assignment:Assignment)->None:
        self.assignments.append(assignment)

