from texttable import Texttable
from Exceptions import ValidError, RepoError


class Console:
    def __print_table(self):
        board  = self.__controller.getTable()
        table = Texttable()
        table.add_rows(board)
        print(table.draw())

    def __place_asteroids(self):
        self.__controller.place_asteroids()
        self.__print_table()

    def __place_aliens(self):
        self.__controller.place_aliens()

    def __cheat(self, params):
        self.__controller.cheat()
        self.__print_table()

    def __check_winner(self):
        result = self.__controller.check_winner()
        return result

    def __teleport(self):
        self.__controller.teleport()

    def __fire(self, params):
        """
        fire command in Ui calls fire method from the gameController wich returns True or False wether the
        fire was a miss or a hit. If it was a hit then it will call the method __print_table to print the new table.
        Otherwise it will call teleport method for the alien move.
        It also prints on the screen a message so that the player knows the effect of his move
        :param params:
        :return:
        """
        coordinates = params[0]
        result = self.__controller.fire(coordinates)
        if result == True:
            self.__print_table()
            print('Hit. Alien ship destroyed!')
        else:
            self.__teleport()
            print('Miss. Alien ship moves!')

    def __check_if_lose(self):
        return self.__controller.check_lose()

    def __init__(self, controller):
        self.__controller = controller
        self.__commands = {
            'cheat': self.__cheat,
            'fire' : self.__fire
        }

    def run(self):
        self.__print_table()
        self.__place_asteroids()
        self.__place_aliens()
        while True:
            cmd = input('>>>')
            if cmd == 'exit':
                return
            if cmd == '':
                continue
            parts = cmd.split()
            command = parts[0]
            params = parts[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](params)
                except ValueError as ve:
                    print('Ui Error!\n' + str(ve))
                except ValidError as vi:
                    print('Controller Error!\n' + str(vi))
                except RepoError as re:
                    print('Repo Error!\n' + str(re))
            else:
                print('Invalid command!')
            if self.__check_winner():
                print('Game Won!')
                return
            if self.__check_if_lose():
                print('You lost!')
                return
