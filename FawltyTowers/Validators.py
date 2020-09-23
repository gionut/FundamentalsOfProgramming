class ValidateReservation:
    def __init__(self):
        pass

    def validate(self, reservation):
        errors = ''
        if reservation.name == '':
            errors += 'Empty family Name!\n'

        if reservation.guests < 1 or reservation.guests > 4:
            errors += 'Invalid number of guests!\n'