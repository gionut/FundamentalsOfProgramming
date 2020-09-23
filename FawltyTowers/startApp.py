from Ui import Console
from Business import ServiceRoom, ServiceReservation
from Repository import FileRepo
from Validators import ValidateReservation
from Domain import Room, Reservation

validateReservation = ValidateReservation()

repoRooms = FileRepo('rooms', Room.read_room, Room.write_room)
repoReservations = FileRepo('reservations', Reservation.read_reservation, Reservation.write_reservation)

validateReservation = ValidateReservation()

serviceReservation = ServiceReservation(repoReservations, repoRooms, validateReservation)
serviceRoom = ServiceRoom(repoRooms)

console = Console(serviceReservation, serviceRoom)

console.run()