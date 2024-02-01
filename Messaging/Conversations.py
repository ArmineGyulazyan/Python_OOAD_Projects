from typing import Dict,List
import Users
import Messages


class Conversation:
    def __init__(self,title:str,creator:Users.User):
        self.title = title
        self.creator = creator
        self.users: List[Users.User] = [creator]
        self.history: Dict[Users.User,List[Messages.Message]] = {}

    def add_user(self,user:Users.User):
        self.users.append(user)
        self.history[user] = []

    def is_part(self,user:Users.User):
        if user in self.users:
            return True
        return False

    def send_message(self,user:Users.User,message:Messages.Message):
        if self.is_part(user):
            if user in self.history:
                self.history[user].append(message)

    def search_messages(self,user:Users.User,message:Messages.Message):
        if user in self.history:
            if message in self.history[user]:
                print(f'The message is  {message.txtt}')









