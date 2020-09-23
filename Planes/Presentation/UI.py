from Exceptions.errors import ValidError, RepoError, ComputerError
import random
from texttable import Texttable


class Console:
    def __ui_add_plane(self, params):
        if len(params) != 2:
            raise ValueError("add function requiers exactly two parameters!\n"
                             "add_palne(<head>, <body>)")
        head = params[0]
        body = params[1]
        self._table = self.__servicePlanes.add(head, body, self._table)
        t = Texttable()
        t.add_rows(self._table)
        print(t.draw())

    def __ui_remove_plane(self, params):
        if len(params) != 2:
            raise ValueError("remove function requiers exactly two parameters!\n"
                             "remove_palne(<head>, <body>)")
        head = params[0]
        body = params[1]
        self.__servicePlanes.remove(head, body)

    def __ui_print_planes(self, params):
        if len(params) != 0:
            raise ValueError("print function requiers no parameters!")
        lst = self.__servicePlanes.get_all()
        for obj in lst:
            print(obj)

    def print_table(self, point, string, service):
        point = list(point)
        y = int(chr(ord(point[0]) - 16))
        x = int(point[1])
        if service == self.__servicePlanes:
            if self._computer_table[y][x] == '':
                self._computer_table[y][x] = string
            else:
                raise ValueError("You already hit that spot. Try another one!")
            p = Texttable()
            p.add_rows(self._computer_table)
            print(p.draw())
        else:
            self._table[y][x] = string
            c = Texttable()
            c.add_rows(self._table)
            print(c.draw())

    def __ui_hit(self, params):
        if len(params) != 1 and len(params) != 2:
            raise ValueError("hit function requiers exactly one parameter!\n"
                             "hit(<point>)")
        if len(params) == 2:
            service = params[1]
        else:
            service = self.__servicePlanes
        point = params[0]
        string = service.hit(point)
        self.print_table(point, string, service)

    def __ui_computer_add(self):
        y_coord = ['B', 'C', 'D', 'E', 'F', 'G']
        x_coord = ['2', '3', '4', '5', '6', '7']
        y = random.choice(y_coord)
        x = random.choice(x_coord)
        head = y + x
        possible_boddies = [y + chr(ord(x) - 2), y + chr(ord(x) + 2), chr(ord(y) - 2) + x, chr(ord(y) + 2) + x]
        body = random.choice(possible_boddies)
        self.__serviceOther.add(head, body, None)

    def __ui_computers_move(self):
        y_coord = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        x_coord = ['1', '2', '3', '4', '5', '6', '7', '8']
        params = []
        point = random.choice(y_coord) + random.choice(x_coord)
        service = self.__serviceOther
        params.append(point)
        params.append(service)
        print('Computer:')
        self.__ui_hit(params)

    def __ui_check_winner(self):
        string = self.__servicePlanes.check_winner()
        if string:
            print(string)
            return True
        else:
            return False

    def __init__(self, servicePlanes, serviceOther):
        self.__servicePlanes = servicePlanes
        self.__serviceOther = serviceOther
        self._table = [['', '1', '2', '3', '4', '5', '6', '7', '8'],
                       ['A', '', '', '', '', '', '', '', ''],
                       ['B', '', '', '', '', '', '', '', ''],
                       ['C', '', '', '', '', '', '', '', ''],
                       ['D', '', '', '', '', '', '', '', ''],
                       ['E', '', '', '', '', '', '', '', ''],
                       ['F', '', '', '', '', '', '', '', ''],
                       ['G', '', '', '', '', '', '', '', ''],
                       ['H', '', '', '', '', '', '', '', '']
                       ]
        self._computer_table = [['', '1', '2', '3', '4', '5', '6', '7', '8'],
                                ['A', '', '', '', '', '', '', '', ''],
                                ['B', '', '', '', '', '', '', '', ''],
                                ['C', '', '', '', '', '', '', '', ''],
                                ['D', '', '', '', '', '', '', '', ''],
                                ['E', '', '', '', '', '', '', '', ''],
                                ['F', '', '', '', '', '', '', '', ''],
                                ['G', '', '', '', '', '', '', '', ''],
                                ['H', '', '', '', '', '', '', '', '']
                                ]
        self.__commands = {
            "add_plane": self.__ui_add_plane,
            "remove_plane": self.__ui_remove_plane,
            "print_planes": self.__ui_print_planes,
            "hit": self.__ui_hit
        }

    def run(self):
        while True:
            cmd = input(">>>")
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
                    if command == 'add_plane':
                        ok = 1
                        while ok == 1:
                            try:
                                self.__ui_computer_add()
                                ok = 0
                            except Exception:
                                ok = 1
                    if command == 'hit':
                        self.__ui_computers_move()
                    if self.__ui_check_winner():
                        return
                except ValueError as ve:
                    print("UI Error!\n" + str(ve))
                except ValidError as vi:
                    print("Business Error!\n" + str(vi))
                except RepoError as re:
                    print("Repository Error!\n" + str(re))
                except ComputerError:
                    pass
            else:
                print("invalid command!")

