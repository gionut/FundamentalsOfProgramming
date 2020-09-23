from Exceptions.errors import ValidError


class ValidatePlane:
    def __init__(self):
        pass

    @staticmethod
    def validate(plane):
        # checks if a plane is not out of grid by considering it's direction
        # and the head's coordinates or if it has the correct form
        if plane.direction == 'up':
            if plane.head.x != plane.body.x or plane.head.y != chr(ord(plane.body.y) - 2):
                raise ValueError("Wrong shape! A plane has a head, two wings and a body.")
        elif plane.direction == 'down':
            if plane.head.x != plane.body.x or plane.head.y != chr(ord(plane.body.y) + 2):
                raise ValueError("Wrong shape! A plane has a head, two wings and a body.")
        elif plane.direction == 'left':
            if plane.head.y != plane.body.y or plane.head.x != chr(ord(plane.body.x) - 2):
                raise ValueError("Wrong shape! A plane has a head, two wings and a body.")
        elif plane.direction == 'right':
            if plane.head.y != plane.body.y or plane.head.x != chr(ord(plane.body.x) + 2):
                raise ValueError("Wrong shape! A plane has a head, two wings and a body.")

        if plane.head.x < '0' or plane.head.x > '8' or plane.head.y < 'A' or plane.head.y > 'Z':
            raise ValidError('The plane is out of grid!')
        elif plane.body.x < '0' or plane.body.x > '8' or plane.body.y < 'A' or plane.body.y > 'Z':
            raise ValidError('The plane is out of grid!')

        if plane.direction == 'up' and (plane.head.x == '1' or plane.head.x == '8' or plane.head.x == '2' or plane.head.x == '7'
                                        or plane.head.y == 'G' or plane.head.y == 'H' or  plane.head.y == 'F'):
            raise ValidError('The plane is out of grid!')
        elif plane.direction == 'down' and (plane.head.x == '1' or plane.head.x == '8' or plane.head.x == '2' or plane.head.x == '7'
                                            or plane.head.y == 'B' or plane.head.y == 'A' or plane.head.y == 'C'):
            raise ValidError('The plane is out of grid!')
        elif plane.direction == 'left' and (plane.head.x == '6' or plane.head.x == '7' or plane.head.x == '8'
                                            or plane.head.y == 'H' or plane.head.y == 'A' or plane.head.y == 'G' or plane.head.y == 'B'):
            raise ValidError('The plane is out of grid!')
        elif plane.direction == 'right' and (plane.head.x == '1' or plane.head.x == '2' or plane.head.x == '3'
                                             or plane.head.y == 'H' or plane.head.y == 'A' or plane.head.y == 'G' or plane.head.y == 'B'):
            raise ValidError('The plane is out of grid!')
        return ''

    def validate_point(self, point):
        if point.x < '0' or point.x > '8' or point.y <'A' or point.y > 'Z':
            raise ValidError("incorrect point!")
