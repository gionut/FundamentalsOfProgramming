from Exceptions import ValidError, RepoError
from texttable import Texttable
import random

class Console:
    def __ui_ship(self, params):
        if type(params) == str:
            controller = self.__computerController
        else:
            controller = self.__shipsController
            params = list(params[0])
            if len(params) != 6:
                raise ValueError('ship command requiers exactly one parameter!\nship <𝑪𝟏𝑳𝟏𝑪𝟐𝑳𝟐𝑪𝟑𝑳𝟑>')
        p1x = params[0]
        p1y = params[1]
        p2x = params[2]
        p2y = params[3]
        p3x = params[4]
        p3y = params[5]
        if controller == self.__computerController:
            controller.add(p1x, p1y, p2x, p2y, p3x, p3y, None)
        else:
            self._table = controller.add(p1x, p1y, p2x, p2y, p3x, p3y, self._table)
            self.print_table(self._table)

    def __ui_print_ship(self, params):
        ships = self.__shipsController.getAll()
        for ship in ships:
            print(ship)

    def __ui_start(self, params):
        if not self.__shipsController.check_start():
            raise ValueError('You must place two ships before starting the game!')
        self._start = 1
        while self.__computerController.check_start() != True:
            x_coord = ['A','B', 'C', 'D', 'E', 'F']
            y_coord = ['1', '2', '3', '4', '5', '6']
            ship = ''
            p1x = random.choice(x_coord)
            p1y = random.choice(y_coord)
            p1 = p1x + p1y
            possible_choices = ['l', 'r', 'u', 'd']
            direction = random.choice(possible_choices)
            if direction == 'l':
                p2 = chr(ord(p1x) - 1) + p1y
                p3 = chr(ord(p1x) - 2) + p1y
            elif direction == 'r':
                p2 = chr(ord(p1x) + 1) + p1y
                p3 = chr(ord(p1x) + 2) + p1y
            elif direction == 'u':
                p2 = p1x + chr(ord(p1y) - 1)
                p3 = p1x + chr(ord(p1y) - 2)
            else:
                p2 = p1x + chr(ord(p1y) + 1)
                p3 = p1x + chr(ord(p1y) + 2)
            ship = p1 + p2 + p3 + ' ' + str(self.__computerController)
            try:
                self.__ui_ship(ship)
            except Exception:
                continue

    def __ui_printc(self,params):
        ships = self.__computerController.getAll()
        for ship in ships:
            print(ship)

    def __ui_attack(self, params):
        if len(params) != 1:
            raise ValueError('attack <square>')
        params = list(params[0])
        squarex = params[0]
        squarey = params[1]
        result = self.__computerController.attack(squarex, squarey, self._target)
        print('Player ' + result[1])
        self._target = result[0]
        self.print_table(self._target)

    def __ui_computer_attack(self):
        x_coord = ['A', 'B', 'C', 'D', 'E', 'F']
        y_coord = ['1', '2', '3', '4', '5', '6']
        p1x = random.choice(x_coord)
        p1y = random.choice(y_coord)
        ok = False
        while not ok:
            try:
                result = self.__shipsController.attack(p1x, p1y, self._table)
                ok = True
            except Exception:
                continue
        print('Computer ' + result[1])
        self._table = result[0]
        self.print_table(self._table)

    def print_table(self, table):
        t = Texttable()
        t.add_rows(table)
        print(t.draw())

    def __check_winner(self):
        if len(self.__shipsController.getAll()) == 0:
            return [1, 'Game over, Computer won!\n      💀']
        elif len(self.__computerController.getAll()) == 0:
            return [1, 'Congratulations, You won!\n     👑']
        return [0]

    def __init__(self, shipsController, computerController):
        self._start = 0
        self.__shipsController = shipsController
        self.__computerController = computerController
        self._table = [['', 'A', 'B', 'C', 'D', 'E', 'F'],
                       ['1', '-', '-', '-', '-', '-', '-'],
                       ['2', '-', '-', '-', '-', '-', '-'],
                       ['3', '-', '-', '-', '-', '-', '-'],
                       ['4', '-', '-', '-', '-', '-', '-'],
                       ['5', '-', '-', '-', '-', '-', '-'],
                       ['6', '-', '-', '-', '-', '-', '-']
                       ]
        self._target = [['', 'A', 'B', 'C', 'D', 'E', 'F'],
                       ['1', '-', '-', '-', '-', '-', '-'],
                       ['2', '-', '-', '-', '-', '-', '-'],
                       ['3', '-', '-', '-', '-', '-', '-'],
                       ['4', '-', '-', '-', '-', '-', '-'],
                       ['5', '-', '-', '-', '-', '-', '-'],
                       ['6', '-', '-', '-', '-', '-', '-']
                       ]
        self.__commands = {
            'ship': self.__ui_ship,
            'print': self.__ui_print_ship,
            'cheat': self.__ui_printc,
            'start': self.__ui_start,
            'attack': self.__ui_attack
        }

    def run(self):
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
                    if command == 'attack':
                        self.__ui_computer_attack()
                except ValueError as ve:
                    print('UI Error\n' + str(ve))
                except RepoError as re:
                    print('Infrastructure Error!\n' + str(re))
                except ValidError as vi:
                    print('Business Error!\n' + str(vi))
            else:
                print('Invalid command!')
            if self._start == 1:
                result =  self.__check_winner()
                if result[0] == 1:
                    print(result[1])
                    return
