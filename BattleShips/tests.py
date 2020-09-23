import unittest
from Domain import Ship, Point
from Repository import RepoShips
from Validators import ValidateShip, ValidatePoint
from ShipsController import ShipController
from Ui import Console

class MyTestCase(unittest.TestCase):
    def test_add(self):
        repoShips = RepoShips()
        validatePoint = ValidatePoint()
        validateShip = ValidateShip()
        shipController = ShipController(repoShips, validateShip, validatePoint)
        self.assertEqual(repoShips.size, 0)
        shipController.add('C', '3', 'D', '3', 'E', '3')
        self.assertEqual(repoShips.size, 1)
        ships = shipController.getAll()
        self.assertEqual(ships, ['C3D3E3'])
        shipController.add('D', '3', 'D', '4', 'D', '5')

if __name__ == '__main__':
    unittest.main()
