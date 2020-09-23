from Domain import Point
from Exceptions import RepoError

class PlayerController:
    def __init__(self, validate, repoPoints):
        self.__validate = validate
        self.__repoPoints = repoPoints

    def place(self, table, x, y, symbol):
        self.__validate.validate(x)
        self.__validate.validate(y)
        self.__validate.validateSymbol(symbol)
        point = Point(x, y, symbol)
        self.__repoPoints.add(point)
        if table[x][y] == ' ':
            table[x][y] = symbol
        else:
            raise RepoError('Existing Point!')
        return table

    def check_win(self):
        points = self.__repoPoints.getAll()
        if len(points) >=5:
            points.sort(key=lambda px: px.x)
            pointsx = points
            ourX = pointsx[0].x
            ourSymbol = points[0].symbol
            contor = 0
            for point in pointsx:
                if point.x == ourX and point.symbol == ourSymbol:
                    contor += 1
            if contor == 6:
                return 1
            points.sort(key=lambda py: py.y)
            pointsy = points
            ourY = pointsy[0].y
            contor = 0
            for point in pointsy:
                if point.y == ourY and points.symbol == ourSymbol:
                    contor += 1
            if contor == 6:
                return 1
        return 0

class ComputerController(PlayerController):
    def __init__(self, validate, repoPoints):
        PlayerController.__init__(self, validate, repoPoints)

    def full_board(self,table):
        for x in table:
            for y in x:
                if y == ' ':
                    return 0
        return 1

