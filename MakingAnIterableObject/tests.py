import unittest
from iterable import It, Filter, GnomeSort
from errors import ItError, FilterError

class MyTestCase(unittest.TestCase):
    def test_iter(self):
        l = []
        it = It(l)
        it.add(1)
        it.add(5)
        it.add(19)
        it.add(-13)
        it.add(0)
        it.add(13)

        self.assertEqual(len(it), 6)

        self.assertEqual(it[0], 1)

        it.gnomeSort('descending')

        self.assertEqual(str(it), '19 13 5 1 0 -13 ')

        it.gnomeSort('ascending')

        self.assertEqual(str(it), '-13 0 1 5 13 19 ')

    def test_sort(self):
        def ascending(x, y):
                if x >= y:
                    return True
                return False

        l = [1, 5, 19, -13, 0, 13]
        gs = GnomeSort(l, ascending)
        gs.gnomeSort()
        self.assertEqual(l[0], -13)
        self.assertEqual(l[5], 19)

    def test_filter(self):

        def lessthan10(object):
            try:
                str(object)
            except FilterError:
                print('the list does not contain elements that can be turned into strings')
            if len(str(object)) < 10:
                return True
            return False

        l = ['asa', 10, '12345678910', 'abcdefghijk']
        f = Filter(l, lessthan10)
        f.filter()

        self.assertEqual(len(l), 2)

if __name__ == '__main__':
    unittest.main()
