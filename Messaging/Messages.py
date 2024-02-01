import abc
from typing import Union,List,Tuple

class Message(abc.ABC):

    def __init__(self,*reactions:Union[List[str],Tuple[str]]):
        self.reactions = reactions


    @abc.abstractmethod
    def react(self,reaction:str):
        ...

    @abc.abstractmethod
    def view_content(self):
        ...


class Text(Message):

    def __init__(self,*reactions:Union[List[str],Tuple[str]],txtt:str):
        super().__init__(*reactions)
        self.txtt = txtt

    def react(self,reaction:str):
        if reaction in self.reactions:
            print(f'the message is {reaction}')

    def view_content(self):
        print(f'the content is {self.txtt}')

