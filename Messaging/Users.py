import Messages


class User:

    def __init__(self,name:str,contact:str):
        self.name = name
        self.contact = contact

    def react_to(self,message:Messages.Message,reactionn:str):
        message.react(reactionn)
