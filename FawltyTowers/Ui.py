from Exceptions import RepoError, ValidError


class Console:
    def __reserve(self, params):
        if len(params) != 5:
            raise ValueError('reserve function requiers exactly 5 parameters!')
        name = params[0]
        roomType = params[1]
        guests = params[2]
        arrival = params[3]
        departure = params[4]
        self.__serviceReservation.create(name, roomType, int(guests) , arrival, departure)

    def __init__(self, serviceResevation, serviceRoom):
        self.__serviceReservation = serviceResevation
        self.__serviceRoom = serviceRoom
        self.__commands = {
            'reserve' : self.__reserve
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
                except ValueError as ve:
                    print('Ui Error!\n' + str(ve))
                except ValidError as vi:
                    print('Business Error!\n' + str(vi))
                except RepoError as re:
                    print('Repository Error!\n' + str(re))
            else:
                print('Invalid command!')

