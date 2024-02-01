import abc
import time
import Users


class Post(abc.ABC):

    def __init__(self,user:Users.User,content:str,date:str):
        self.user = user
        self.content = content
        self.date = date
        self.p_time = time.time()
        # self.comments:Dict[Users.User,List[]] = {}

    def add_post(self):
        self.user.posts.append(self)


    @abc.abstractmethod
    def react(self,reaction:str):
        ...

class Image(Post):
    def __init__(self,user:Users.User,content:str,date:str,format:str):
        super().__init__(user,content,date)
        self.format = format

    def react(self,reaction:str):
        print(reaction)








