from Domain.entities import Point, Plane


class ServicePlanes:
    def __init__(self, repoPlanes, repoOther, validatePlanes):
        self.__repoPlanes = repoPlanes
        self.__repoOther = repoOther
        self.__validatePlanes = validatePlanes

    @staticmethod
    def make_point(string):
        string = list(string)
        return Point(string[0], string[1])

    def add(self, headc, bodyc, table):
        head = self.make_point(headc)
        body = self.make_point(bodyc)
        self.__validatePlanes.validate_point(head)
        self.__validatePlanes.validate_point(body)
        plane = Plane(head, body)
        self.__validatePlanes.validate(plane)
        self.__repoPlanes.add(plane)
        if table != None:
            return self.insert_table(plane, table)

    def insert_table(self, plane, table):
        points = plane.allPoints
        for point in points:
            table[int(chr(ord(point.y) - 16))][int(point.x)] = '0'
        return table

    def remove(self, headc, bodyc):
        head = self.make_point(headc)
        body = self.make_point(bodyc)
        self.__validatePlanes.validate_point(head)
        self.__validatePlanes.validate_point(body)
        plane = Plane(head, body)
        self.__validatePlanes.validate(plane)
        self.__repoPlanes.remove(plane)

    def dead(self, plane):
        self.__repoOther.remove(plane)
        if self.__repoOther.size() == 0:
            return 'winner'

    def hit(self, point):
        point = self.make_point(point)
        self.__validatePlanes.validate_point(point)
        planes = self.__repoOther.get_all()
        for plane in planes:
            all_points = plane.allPoints
            if point == all_points[0]:
                self.dead(plane)
                return 'D'
            elif point in all_points:
                plane.allPoints.remove(point)
                if len(plane.allPoints) == 1:
                    self.dead(plane)
                return 'H'
        return 'M'

    def get_all(self):
        lst = []
        planes = self.__repoPlanes.get_all()
        for plane in planes:
            lst.append(str(plane))
        return lst

    def check_winner(self):
        if self.__repoPlanes.size() == 0:
            return 'Computer won!'
        elif self.__repoOther.size() == 0:
            return 'Congratulation, You won!'
        else:
            return False
