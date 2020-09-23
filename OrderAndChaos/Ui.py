from texttable import Texttable
from Exceptions import ValidError, RepoError
import random
import string


class Console:
    def __display_board(self):
        table = Texttable()
        table.add_rows(self.__table)
        print(table.draw())

    def __ui_place(self, params):
        if len(params) != 3:
            raise ValueError('#3 params for <place> command!')
        x = int(params[0])
        y = int(params[1])
        symbol = params[2]
        self.__table = self.__playerController.place(self.__table, x-1, y-1, symbol)
        self.__display_board()

    def __computer_place(self):
        x_coord = ['1', '2', '3', '4', '5', '6']
        y_coord = ['1', '2', '3', '4', '5', '6']
        x = random.choice(x_coord)
        y = random.choice(y_coord)
        symbol = chr(random.randrange(1, 120))
        while True:
            try:
                self.__table = self.__computerController.place(self.__table, int(x)-1, int(y)-1, symbol)
                break
            except RepoError:
                continue
        self.__display_board()

    def __check_win(self):
        ok = self.__playerController.check_win()
        if ok == 1:
            print('Order Won!')
            return
        ok = self.__computerController.full_board(self.__table)
        if ok ==1:
            print('Chaos Won!')
            return

    def __init__(self, playerController, computerController):
        self.__table = [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.__playerController = playerController
        self.__computerController = computerController
        self.__commands = {
            'place': self.__ui_place
        }

    def run(self):
        self.__display_board()
        while True:
            self.__check_win()
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
                    if command == 'place':
                        self.__computer_place()
                except ValueError as ve:
                    print('Ui Error!\n' + str(ve))
                except ValidError as vi:
                    print('Controller Error!\n' + str(vi))
                except RepoError as re:
                    print('Repository Error!\n' + str(re))
            else:
                print('Invalid command!')



