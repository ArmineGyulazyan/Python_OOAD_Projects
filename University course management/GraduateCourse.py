import Course
import Professor


class GraduateCourse(Course.Course):
    def __init__(self, name: str, instructor: 'Professor.Professor', content: str, quantity:int, thesis_topic:str):
        super().__init__(name, instructor, content,quantity)
        self.thesis_topic = thesis_topic

    @property
    def thesis_topic(self):
        return self.__thesis_topic

    @thesis_topic.setter
    def thesis_topic(self,value):
        if not isinstance(value, str):
            raise ValueError("The value must be a string")
        self.__thesis_topic = value

    def ensure_to_pass(self)->str:
        print(f"your thesis topic is {self.thesis_topic}")
        document=input("Enter thesis here: ")
        return document
###
