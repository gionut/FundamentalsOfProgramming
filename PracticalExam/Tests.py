import unittest
from Ui import Console
from Controller import Controller
from Repository import Repo
from Validators import Validate
from Exceptions import ValidError, RepoError

class MyTestCase(unittest.TestCase):
    def test_fire(self):
        repoGame = Repo()
        validate = Validate()
        controller = Controller(repoGame, validate)
        with self.assertRaises(ValidError): controller.fire('J1')
        with self.assertRaises(ValidError): controller.fire('A9')
        with self.assertRaises(ValidError): controller.fire('J9')
        self.assertEqual(controller.fire('A1'), False)


        repoGame.addAlien((1,2))
        repoGame.mark_table(1, 2, 'X')
        self.assertEqual(controller.fire('B1'), True)
        repoGame.addAlien((1,3))
        repoGame.mark_table(1, 3, '')
        self.assertEqual(controller.fire('C1'), True)

        self.assertEqual(repoGame.getAliens(), 0)
        self.assertEqual(repoGame.getTable[1][2], '-')
        self.assertEqual(repoGame.getAliens(), 0)
        self.assertEqual(repoGame.getTable[1][3], '-')


if __name__ == '__main__':
    unittest.main()
