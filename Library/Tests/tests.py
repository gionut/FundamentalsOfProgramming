import unittest
from Domain.entities import Book
from Validator.validators import ValidateBook
from Infrastructure.repo import Repo
from Business.service import*
from Errors.exceptions import*



class MyTestCase(unittest.TestCase):
    def test_repo(self):
        repoBooks = Repo()
        repoBooks.add(Book('0000', 'title', 'author'))
        repoBooks.add(Book('0001', 'title', 'author'))

        self.assertEqual(len(repoBooks), 2)

        l = []
        for i in repoBooks:
            l.append(i)
        self.assertEqual(len(l), 2)

        self.assertEqual(repoBooks[0], Book('0000', 'title', 'author'))
        repoBooks[0] = Book('0001', 'title', 'author')
        self.assertEqual(repoBooks[0], Book('0001', 'title', 'author'))

    def test_service(self):
        repoBooks = Repo()
        repoBooks.add(Book('0', 't', 'a'))
        repoBooks.add(Book('0001', 'title', 'author'))
        serviceBooks = ServiceBooks(repoBooks, None, None, None)

        serviceBooks.sort()
        self.assertEqual(repoBooks[0].id, '0001')

        serviceBooks.filter()
        self.assertEqual(len(repoBooks), 1)

if __name__ == '__main__':
    unittest.main()
