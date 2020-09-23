from rent import Rental

class Book(Rental):

    def __init__(self, bookid, title, author):
        self._bookid = bookid
        self._title = title
        self._author = author

####### bookid SET/GET #######
    @property
    def bookid(self):
        return self._bookid

    @bookid.setter
    def bookid(self, bid):
        self._bookid = bid

####### title SET/GET #######
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

####### author SET/GET #######
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, a):
        self._author = a









