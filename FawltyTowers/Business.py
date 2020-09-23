import random
from Validators import ValidateReservation
from Domain import Room, Reservation
from Exceptions import RepoError
import datetime
import time

class ServiceRoom:
    def __init__(self, repoRooms):
        self.__repoRooms = repoRooms


class ServiceReservation:
    def __init__(self, repoReservations, repoRooms, validateReservation):
        self.__repoReservations = repoReservations
        self.__repoRooms = repoRooms
        self.__validateReservation = validateReservation

    def __generate_code(self):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        code = ''
        for x in range(4):
            code += random.choice(digits)
        return code

    def __check_room(self, roomType):
        room = Room(None, roomType, None)
        for r in self.__repoRooms.getAll():
            if r == room and r.free:
                r.free = 0
                return r
        raise RepoError('No more rooms of that type!')

    def create(self, name, roomType, guests, arrival, departure):
        code = self.__generate_code()
        room = self.__check_room(roomType)
        arrival = arrival.split('.')
        arrival = datetime.datetime(2020, int(arrival[0]), int(arrival[1]))
        reservation = Reservation(code, name, room, guests, arrival, departure)
        self.__validateReservation.validate(reservation)
        self.__repoReservations.add(reservation)
