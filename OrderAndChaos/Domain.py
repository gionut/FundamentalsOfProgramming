class Point:
    def __init__(self, x, y, symbol):
        self.__x = x
        self.__y = y
        self.__symbol = symbol

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def symbol(self):
        return self.__symbol

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

