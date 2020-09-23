class Point:
    # creating a virtual Point based on it's coordinates in a two dimensional representation
    def __init__(self, y, x):
        self.__x = x
        self.__y = y

    # get the position on the X axis
    @property
    def x(self):
        return self.__x

    # get the position on the Y axis
    @property
    def y(self):
        return self.__y

    # two point are equal if their position on the X axis and on the Y axis coincide
    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    # write a point as a concatenation of th point's position on the Y axis and on the X axis
    def __str__(self):
        return self.__y + self.__x


class Plane:
    # creates a virtual Plane characterised by its head and it's body(of type Point)
    def __init__(self, head, body):
        self.__head = head
        self.__body = body

    # get the Point corresponding to the plane's head
    @property
    def head(self):
        return self.__head

    # get the Point corresponding to the plane's body
    @property
    def body(self):
        return self.__body

    # get the direction of the Plane based on how the body it is placed considering the head
    @property
    def direction(self):
        if self.__head.y < self.__body.y:
            return 'up'
        elif self.__head.y > self.__body.y:
            return 'down'

        elif self.__head.x < self.__body.x:
            return 'left'
        else:
            return 'right'

    # get all the Points(8) of a Plane considering it's direction and it's body
    @property
    def allPoints(self):
        if self.direction == 'up':
            return [self.__head,
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) - 2)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x))),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) + 2)),  # first wing
                    self.__body,
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x))),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) + 1))  # second wing
                    ]
        elif self.direction == 'down':
            return [self.__head,
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) - 2)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x))),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) + 2)),  # first wing
                    self.__body,
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x))),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) + 1))  # second wing
                    ]
        elif self.direction == 'left':
            return [self.__head,
                    Point(chr(ord(self.__body.y) - 2), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y)), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) + 2), str(int(self.__body.x) - 1)),  # first wing
                    self.__body,
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y)), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) + 1))  # second wing
                    ]
        elif self.direction == 'right':
            return [self.__head,
                    Point(chr(ord(self.__body.y) - 2), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y)), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) + 1)),
                    Point(chr(ord(self.__body.y) + 2), str(int(self.__body.x) + 1)),# first wing
                    self.__body,
                    Point(chr(ord(self.__body.y) - 1), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y)), str(int(self.__body.x) - 1)),
                    Point(chr(ord(self.__body.y) + 1), str(int(self.__body.x) - 1))  # second wing
                    ]

    # two Planes are consider equal if they intersect in at least one Point
    def __eq__(self, other):
        return len([point for point in self.allPoints if point in other.allPoints]) != 0

    # the writing of a plane consists of concatenating the head and the body togheter with a line character '-'
    def __str__(self):
        return str(self.__head) + '-' + str(self.__body)
