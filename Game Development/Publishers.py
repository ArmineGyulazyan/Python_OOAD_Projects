from typing import List
import Games



class Publisher:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.released_games: List[Games.Game] = []
        self.sold_games: List[Games.Game] = []

    def introduce_game(self, game:Games.Game, date:str):
        if date == game.release_date:
            self.released_games.append(game)

    def sell_game(self,game:Games.Game):
        self.sold_games.append(game)

    def view_sold_games(self):
        for game in self.sold_games:
            print(game.title)

    def view_rel_games(self):
        for game in self.released_games:
            print(game.title, game.release_date)
