import unittest
from Domain.entities import Point, Plane
from Infrastructure.repository import Repo
from Exceptions.errors import RepoError, ValidError
from Validators.validators import ValidatePlane
from Business.services import ServicePlanes


class Test(unittest.TestCase):
    def test_point(self):
        point = Point('A', '3')

        # test point's coordinates
        self.assertEqual(point.x, '3')
        self.assertEqual(point.y, 'A')

        sameX_sameY = Point('A', '3')
        sameX_difY = Point('B', '3')
        difX_sameY = Point('A', '2')
        difX_difY = Point('B', '2')

        # check if two points are equal
        self.assertEqual(point, sameX_sameY)
        self.assertEqual(point == sameX_difY, False)
        self.assertEqual(point == difX_sameY, False)
        self.assertFalse(point == difX_difY, True)

        # check the writing of a point
        self.assertEqual(str(point), 'A3')

    def test_plane(self):
        plane = Plane(Point('A', '3'), Point('C', '3'))

        # check if the plane is the same as the one we created earlier
        self.assertEqual(plane.head, Point('A', '3'))
        self.assertEqual(plane.body, Point('C', '3'))

        # check the direction of several planes
        self.assertEqual(plane.direction, 'up')
        self.assertEqual(Plane(Point('C', '5'), Point('C', '7')).direction, 'left')
        self.assertEqual(Plane(Point('H', '7'), Point('F', '7')).direction, 'down')
        self.assertEqual(Plane(Point('G', '4'), Point('G', '2')).direction, 'right')

        # check the rest of the points, includeing the head and the body
        self.assertEqual(plane.allPoints, [Point('A', '3'),
                                           Point('B', '1'), Point('B', '2'), Point('B', '3'), Point('B', '4'), Point('B', '5'),
                                           Point('C', '3'),
                                           Point('D', '2'), Point('D', '3'), Point('D', '4')])
        self.assertEqual(Plane(Point('C', '5'), Point('C', '7')).allPoints, [Point('C', '5'),
                                                                             Point('A', '6'), Point('B', '6'), Point('C', '6'), Point('D', '6'), Point('E', '6'),
                                                                             Point('C', '7'),
                                                                             Point('B', '8'), Point('C', '8'),
                                                                             Point('D', '8')])
        self.assertEqual(Plane(Point('H', '6'), Point('F', '6')).allPoints, [Point('H', '6'),
                                                                             Point('G', '4'), Point('G', '5'), Point('G', '6'), Point('G', '7'), Point('G', '8'),
                                                                             Point('F', '6'),
                                                                             Point('E', '5'), Point('E', '6'),
                                                                             Point('E', '7')])
        self.assertEqual(Plane(Point('F', '4'), Point('F', '2')).allPoints, [Point('F', '4'),
                                                                             Point('D', '3'), Point('E', '3'), Point('F', '3'), Point('G', '3'), Point('H', '3'),
                                                                             Point('F', '2'),
                                                                             Point('E', '1'), Point('F', '1'),
                                                                             Point('G', '1')])

        sameHead_sameBody = Plane(Point('A', '3'), Point('C', '3'))
        sameHead_difBody = Plane(Point('A', '3'), Point('C', '5'))
        difHead_sameBody = Plane(Point('C', '5'), Point('C', '3'))
        difHead_difBody = Plane(Point('G', '4'), Point('G', '2'))

        # checking if two planes are equal or not
        self.assertEqual(plane, sameHead_sameBody)  # two planes are equal if they have at least one point in common
        self.assertEqual(plane, sameHead_difBody)
        self.assertEqual(plane, difHead_sameBody)
        self.assertEqual(plane == difHead_difBody, False)

        # check the writing of a plane
        self.assertEqual(str(plane), "A3-C3")

    def test_repo_planes(self):
        repoPlanes = Repo()

        # initially, repo's size should be 0
        self.assertEqual(repoPlanes.size(), 0)

        plane = Plane(Point('A', '3'), Point('C', '3'))
        wrong_plane = Plane(Point('A', '5'), Point('C', '5'))
        plane1 = Plane(Point('G', '4'), Point('G', '2'))

        # add plane plane. repo's size should be incremented
        repoPlanes.add(plane)
        self.assertEqual(repoPlanes.size(), 1)

        # trying to add a plane with bad coordonates
        try:
            repoPlanes.add(wrong_plane)
        except RepoError as re:
            self.assertEqual(str(re), 'existing object!')

        # add a second plane plane1. repo's size should be 2
        repoPlanes.add(plane1)
        self.assertEqual(repoPlanes.size(), 2)

        # get all planes from the repo
        lst = repoPlanes.get_all()
        self.assertEqual(lst, [plane, plane1])

        # remove plane plane from the repo. repo's size shoud decrement
        repoPlanes.remove(plane)
        self.assertEqual(repoPlanes.size(), 1)

        # trying to remove a plane which does not exists in the repo
        try:
            repoPlanes.remove(wrong_plane)
        except RepoError as re:
            self.assertEqual(str(re), 'inexisting object!')

    def test_validate_planes(self):
        validatePlane = ValidatePlane()
        plane = Plane(Point('A', '3'), Point('C', '3'))
        self.assertEqual(validatePlane.validate(plane), '')
        out_of_grid = Plane(Point('A', '3'), Point('A', '5'))
        try:
            validatePlane.validate(out_of_grid)
        except ValidError as vi:
            self.assertEqual(str(vi), 'The plane is out of grid!')

    def test_service_planes(self):
        repoPlanes = Repo()
        validatePlanes = ValidatePlane()
        repoComputerPlanes = Repo()

        serviceComputerPlanes = ServicePlanes(repoComputerPlanes, repoPlanes, validatePlanes)

        servicePlanes = ServicePlanes(repoPlanes, repoComputerPlanes, validatePlanes)
        head = 'A3'
        body = 'C3'
        servicePlanes.add(head, body)
        self.assertEqual(len(servicePlanes.get_all()), 1)
        bad_head = 'A8'
        bad_body = 'C8'
        try:
            servicePlanes.add(bad_head, bad_body)
        except ValidError as vi:
            self.assertEqual(str(vi), "The plane is out of grid!")
        servicePlanes.remove(head, body)
        self.assertEqual(len(servicePlanes.get_all()), 0)

        servicePlanes.add(head, body)
        servicePlanes.add(Point('C', '5'), Point('C', '7'))

        serviceComputerPlanes.add(head, body)
        serviceComputerPlanes.add(Point('C', '5'), Point('C', '7'))

        string = serviceComputerPlanes.hit(Point('B', '3'))
        self.assertEqual(string, 'hit')
        string = serviceComputerPlanes.hit(Point('F', '3'))
        self.assertEqual(string, 'miss')
        string = serviceComputerPlanes.hit(Point('A', '3'))
        self.assertEqual(repoPlanes.size(), 1)
        self.assertEqual(string, 'dead')
        serviceComputerPlanes.hit('A6')
        serviceComputerPlanes.hit('B6')
        serviceComputerPlanes.hit('C6')
        serviceComputerPlanes.hit('D6')
        serviceComputerPlanes.hit('E6')
        serviceComputerPlanes.hit('C7')
        serviceComputerPlanes.hit('B8')
        serviceComputerPlanes.hit('C8')
        serviceComputerPlanes.hit('D8')
        self.assertEqual(repoPlanes.size(), 0)


if __name__ == "__main__":
    unittest.main()
