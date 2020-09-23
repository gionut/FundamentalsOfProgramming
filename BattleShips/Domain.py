
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    def __str__(self):
        return self.__x + self.__y


class Ship:
    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self._points = 3

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    @property
    def p3(self):
        return self.__p3

    @property
    def points(self):
        return [self.__p1, self.__p2, self.__p3]

    def __eq__(self, other):
        return self.__p1 in (other.p1, other.p2, other.p3) or self.__p2 in (other.p1, other.p2, other.p3) or \
               self.__p3 in (other.p1, other.p2, other.p3)

    def __str__(self):
        return str(self.__p1) + str(self.__p2) + str(self.__p3)
