import datetime


class Room:
    def __init__(self, nr, type, free):
        self.__nr = nr
        self.__type = type
        self.__free = 1

    @property
    def free(self):
        return self.__free

    @property
    def type(self):
        return type

    def __str__(self):
             return str(self.__nr) + ' ' + str(self.__type)

    def __eq__(self, other):
        return self.__type == other.type

    @staticmethod
    def read_room(line):
        line = line.split()
        return Room(line[0], line[1], None)

    @staticmethod
    def write_room(obj):
        return str(obj)

class Reservation:
    def __init__(self, code, name, room, guests, arrival, departure):
        self.__code = code
        self.__name = name
        self.__guests = guests
        self.__room = room
        self.__departure = departure
        self.__arrival = arrival

    @property
    def code(self):
        return self.__code

    def __eq__(self, other):
        return self.__code == other.code

    def __str(self):
        return str(self.__code) + str(self.__name) + str(self.__room) +str(self.__guests)\
               +str(self.__arrival.strftime('%m')) + '.' + str(self.__arrival.strftime('%d'))\
        +str(self.__departure.strftime('%m')) + '.' + str(self.__departure.strftime('%m'))

    @staticmethod
    def read_reservation(line):
        line = line.split()
        room = Room(line[2], line[3], None)
        arrival = line[5].split('.')
        departure = line[6].split('.')
        arrival = datetime.datetime(2020, int(arrival[0]), int(arrival[1]))
        departure = datetime.datetime(2020, int(departure[0]), int(departure[1]))
        return Reservation(line[0], line[1], room, line[4], arrival, departure)

    @staticmethod
    def write_reservation(obj):
        return str(obj)
