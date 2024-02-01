from typing import List
import Games


class Developer:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
        self.games: List[Games.Game] = []

    def add_game(self,game:Games.Game):
        self.games.append(game)


    def view_games(self):
        for game in self.games:
            print(game.title,game.genre)
