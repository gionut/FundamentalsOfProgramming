from texttable import Texttable
from Exceptions import ValidError

class Console:
    def __init__(self, gameController):
        self.__gameController = gameController
        self.__commands = {
            'cheat' : self.__ui_cheat,
            'wrap' : self.__ui_wrap
        }

    def __print_table(self, table):
        table = self.__gameController.get_table()
        t = Texttable()
        t.add_rows(table)
        print(t.draw())

    def __place_stars(self):
        self.__gameController.place_stars()

    def __place_Endeavour(self):
        table = self.__gameController.place_Endeavour()
        self.__print_table(table)

    def __place_Blingon(self):
        self.__gameController.place_Blingon()

    def __ui_cheat(self, params):
        table = self.__gameController.show_Blingons()
        self.__print_table(table)

    def __ui_wrap(self,params):
        if len(params) != 1:
            raise ValueError('wrap <coordinate> !')
        table = self.__gameController.wrap(params[0])
        self.__print_table(table)

    def run(self):
        self.__place_stars()
        self.__place_Endeavour()
        self.__place_Blingon()
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
            else:
                print('Invalid command!')

