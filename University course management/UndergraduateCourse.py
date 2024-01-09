import Course
import Professor

class UndergraduateCourse(Course.Course):

    def __init__(self,name:str, instructor:"Professor.Professor", content:str,quantity:int,credit:int):
        super().__init__(name,instructor,content,quantity)
        self.credit = credit

    def ensure_to_pass(self):
        return self.credit
###

