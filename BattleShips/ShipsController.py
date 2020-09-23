from Domain import Ship, Point


class ShipController:
    def __init__(self, repoShips, validateShip, validatePoint):
        self.__repoShips = repoShips
        self.__validateShip = validateShip
        self.__validatePoint = validatePoint

    def add(self, p1x, p1y, p2x, p2y, p3x, p3y, table):
        if self.__repoShips.size == 2:
            ships = self.__repoShips.getAll()
            self.remove(ships[0].p1)
            self.insertTable(table, ships[0], '-')
        p1 = Point(p1x, p1y)
        p2 = Point(p2x, p2y)
        p3 = Point(p3x, p3y)
        self.__validatePoint.validate(p1)
        self.__validatePoint.validate(p2)
        self.__validatePoint.validate(p3)
        self.__validateShip.validate(p1, p2, p3)
        ship = Ship(p1, p2, p3)
        self.__repoShips.add(ship)
        if table != None:
            return self.insertTable(table, ship, '+')

    def insertTable(self, table, ship, char):
        points = ship.points
        print()
        for point in points:
            table[int(point.y)][int(chr(ord(point.x)-16))] = char
        return table

    def remove(self, p1):
        ship = Ship(p1, None, None)
        self.__repoShips.remove(ship)

    def getAll(self):
        objects = self.__repoShips.getAll()
        ships = []
        for ship in objects:
            ships.append(str(ship))
        return ships

    def check_start(self):
        return self.__repoShips.size == 2

    def attack(self, x, y, table):
        point = Point(x, y)
        self.__validatePoint.validate(point)
        message = 0
        for ship in self.__repoShips.getAll():
            points = ship.points
            if point in points:
                table[int(point.y)][int(chr(ord(point.x) - 16))] = 'x'
                ship._points += -1
                self.dead(ship)
                message = 'hits!'
            else:
                table[int(point.y)][int(chr(ord(point.x) - 16))] = 'o'
                message = 'misses!'
        return [table, message]

    def dead(self, ship):
        if ship.points == 0:
            self.__repoShips.remove(ship)