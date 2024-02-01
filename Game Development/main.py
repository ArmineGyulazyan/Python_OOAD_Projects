import Developers
import Publishers
import Games

def main():

    dev1 = Developers.Developer('Max','055669988')
    my_game = Games.Strategy('new chess','strategy','21/3/2024',2,'keep King')
    dev1.add_game(my_game)
    dev1.view_games()
    publisher1 = Publishers.Publisher('Bob','068877889')
    publisher1.introduce_game(my_game,'21/3/2024')
    publisher1.sell_game(my_game)
    publisher1.view_sold_games()


if __name__ == '__main__':
    main()