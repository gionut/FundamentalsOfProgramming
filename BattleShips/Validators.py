from Exceptions import ValidError


class ValidatePoint:
    def __init__(self):
        pass

    @staticmethod
    def validate(point):
        if chr(ord(point.x)) < 'A' or chr(ord(point.x)) > 'F' or chr(ord(point.y)) < '0' or chr(ord(point.y)) > '6':
            raise ValidError('Point out of grid!')


class ValidateShip:
    def __init__(self):
        pass

    @staticmethod
    def validate(p1, p2, p3):

        if not(p1.x == p2.x == p3.x and abs(ord(p1.y) - ord(p2.y)) == abs(ord(p2.y) - ord(p3.y)) == 1\
            or p1.y == p2.y == p3.y and abs(ord(p1.x) - ord(p2.x)) == abs(ord(p2.x) - ord(p3.x)) == 1):
            raise ValidError('Wrong shape!')

