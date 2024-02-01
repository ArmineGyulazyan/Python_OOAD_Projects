import abc
class Game(abc.ABC):
    def __init__(self,title:str,genre:str,release_date:str,players_num:int):
        self.title=title
        self.genre=genre
        self.release_date = release_date
        self.players_num = players_num

    @abc.abstractmethod
    def player_quantity(self,character:str):
        ...

    @abc.abstractmethod
    def game_type(self):
        ...


class Strategy(Game):
    def __init__(self,title:str,genre:str,release_date:str,players_num:int,plan:str):
        super().__init__(title,genre,release_date,players_num)
        self.plan = plan

    def player_quantity(self,character:str):
        print(self.players_num)

    def game_type(self):
        print(self.genre)
