from Infrastructure.repo import*
from Errors.exceptions import *
from Domain.entities import *
import datetime
from iterable import GnomeSort, Filter
from errors import FilterError

class ServiceBooks(object):

# func that manage a repo of books  
    def __init__(self, repoBooks, validateBooks, undoActions, redoActions):
        self.__repoBooks = repoBooks
        self.__validateBooks = validateBooks
        self.__undoActions = undoActions
        self.__redoActions = redoActions

    def filter(self):
        def lessthan(object):
            try:
                str(object)
            except FilterError:
                print('the list does not contain elements that can be turned into strings')
            if len(str(object)) < 80:
                return True
            return False

        f = Filter(self.__repoBooks, lessthan)
        f.filter()

    def sort(self):
        def descending(x, y):
            if len(x.title) < len(y.title):
                return True
            return False
        gs = GnomeSort(self.__repoBooks, descending)
        gs.gnomeSort()

    def add(self, bookId, title, author):
        # adds a book to the repo of books if it is valid and its id does not exist in the repo
        book = Book(bookId, title, author)
        self.__validateBooks.validate_book(book)
        self.__repoBooks.add(book, None)
        undoAction = UndoAction(self.__repoBooks, FileRepo.remove, FileRepo.add, book, None)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()

    def get_nr_books(self):
        # get the length of the repo
        return self.__repoBooks.length()
    
    def get_book_by_id(self, bookId):
        book = Book(bookId, None, None)
        return self.__repoBooks.search(book)

    def get_books(self):
        return self.__repoBooks.get_all()
    
    def remove(self, bookId):
        # removes a book from the repo
        book = self.get_book_by_id(bookId)
        self.__repoBooks.remove(book, None)
        undoAction = UndoAction(self.__repoBooks, FileRepo.add, FileRepo.remove, book, None)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()
    
    def update_title(self, bookId, newTitle):
        book = self.get_book_by_id(bookId)
        book1 = Book(book.id, newTitle, book.author)
        self.__repoBooks.update(book, book1)
        undoAction = UndoAction(self.__repoBooks, FileRepo.update, None, book1, book)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()

    def update_author(self, bookId, newAuthor):
        book = self.get_book_by_id(bookId)
        book1 = Book(book.id, book.title, newAuthor)
        self.__repoBooks.update(book, book1)
        undoAction = UndoAction(self.__repoBooks, FileRepo.update, book1, book)
        self.__repoUndo.add(undoAction)
        redoAction = RedoAction(self.__repoBooks, FileRepo.update, book, book1)
        self.__repoRedo.add(redoAction)


    def search_by_id(self, id):
        l = self.__repoBooks.search_id(id)
        return l

    def search_by_title(self, title):
        l = self.__repoBooks.search_title(title)
        return l

    def search_by_author(self, author):
        l = self.__repoBooks.search_author(author)
        return l


class ServiceClients(object):

# func that manage a repo of clients  
    def __init__(self, repoClients, validateClients, undoActions, redoActions):
        self.__repoClients = repoClients
        self.__validateClients = validateClients
        self.__undoActions = undoActions
        self.__redoActions = redoActions
        
    def add(self, clientId, name):
        # adds a book to the repo of books if it is valid and its id does not exist in the repo
        client = Client(clientId, name)
        self.__validateClients.validate_client(client)
        self.__repoClients.add(client, None)
        undoAction = UndoAction(self.__repoClients, FileRepo.remove, FileRepo.add, client, None)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()
    
    def get_nr_clients(self):
        # get the length of the repo
        return self.__repoClients.length()
    
    def get_client_by_id(self, clientId):
        client = Client(clientId, None)
        return self.__repoClients.search(client)
    
    def get_clients(self):
        return self.__repoClients.get_all()
    
    def remove(self, clientId):
        # removes a client from the repo
        client = self.get_client_by_id(clientId)
        self.__repoClients.remove(client, None)
        undoAction = UndoAction(self.__repoClients, FileRepo.add, FileRepo.remove, client, None)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()
    
    def update_client(self, clientId, newName):
        client = self.get_client_by_id(clientId)
        client1 = Client(clientId, newName)
        self.__repoClients.update(client, client1)
        undoAction = UndoAction(self.__repoClients, FileRepo.update, None, client1, client)
        self.__undoActions.push(undoAction)
        self.__redoActions.clear()

    def search_by_id(self, id):
        l = self.__repoClients.search_id(id)
        return l

    def search_by_name(self, name):
        l = self.__repoClients.search_name(name)
        return l

    
class ServiceRental(object):

# func that manage a repo of rentals  
    def __init__ (self, repoRental, repoBooks, repoClients, validateRental, undoActions, redoActions):
        self.__repoRental = repoRental
        self.__repoBooks = repoBooks
        self.__repoClients = repoClients
        self.__validateRental = validateRental
        self.__undoActions = undoActions
        self.__redoActions = redoActions

    def add(self, rentalId, bookId, clientId, rentedDate, returnedDate):
        # adds a rental to the repo of rentals if it is valid and its id does not exist in the repo
        rentals = self.__repoRental.get_all()
        for rental in rentals:
            if bookId == rental.get_book().id:
                if rental.get_returned_date() == "-":
                    raise ValidError("Book with the id " + bookId + " is not available!")
        book = self.__repoBooks.search(Book(bookId, None, None))
        client = self.__repoClients.search(Client(clientId, None))
        rental = Rental(rentalId, book, client, rentedDate, returnedDate)
        self.__validateRental.validate_rental(rental)
        self.__repoRental.add(rental, None)
        action = UndoAction(self.__repoRental, FileRepo.remove, FileRepo.add, rental, None)
        self.__undoActions.push(action)
        self.__redoActions.clear()

    def get_nr_rentals(self):
        # get the length of the repo
        return self.__repoRental.length()
    
    def get_rentals(self):
        return self.__repoRental.get_all()

    def remove(self, clientId):
        client = self.__repoClients.search(Client(clientId, ""))
        action = ComplexUndoAction()
        for rental in self.__repoRental.get_all():
            if rental.get_client() == client:
                self.__repoRental.remove(rental, None)
                action.add_action(UndoAction(self.__repoRental, FileRepo.add, FileRepo.remove, rental, None))
        self.__repoClients.remove(client, None)
        action.add_action(UndoAction(self.__repoClients, FileRepo.add, FileRepo.remove, client, None))
        self.__undoActions.push(action)
        self.__redoActions.clear()

    def return_book(self, rentalId, returned_date):
        # removes a rental from the repo
        rentals = self.__repoRental.get_all()
        for rental in rentals:
            if rentalId == rental.get_rentalId():
                rental.set_returned_date(returned_date)

    def most_rented_books(self):
        dict = {}
        l = self.__repoRental.get_all()
        ll = []
        for x in l:
            if x.get_book() not in ll:
                ll.append(x.get_book())
                count = 0
                for y in l:
                    if y.get_book() == x.get_book():
                        count += 1
                if count in dict.keys():
                    dict[count].append(x.get_book())
                else:
                    dict[count] = [x.get_book()]
        return dict

    def most_active_clients(self):
        dict = {}
        l = self.__repoRental.get_all()
        ll = []
        for x in l:
            if x.get_client() not in ll:
                ll.append(x.get_client())
                days = 0
                for y in l:
                    if y.get_client() == x.get_client():
                        date = y.get_rented_date().split('.')
                        rented_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
                        if y.get_returned_date() != "-":
                            date = y.get_returned_date().split('.')
                            returned_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
                            days += (returned_date - rented_date).days
                        else:
                            days += (datetime.datetime.today() - rented_date).days
                if days in dict.keys():
                    dict[days].append(x.get_client())
                else:
                    dict[days] = [x.get_client()]
        return dict

    def most_rented_authors(self):
        dict = {}
        l = self.__repoRental.get_all()
        ll = []
        for x in l:
            if x.get_book().author not in ll:
                ll.append(x.get_book().author)
                count = 0
                for y in l:
                    if y.get_book().author == x.get_book().author:
                        count += 1
                if count in dict.keys():
                    dict[count].append(x.get_book().author)
                else:
                    dict[count] = [x.get_book().author]
        return dict


class ServiceUndoRedo(object):

    def __init__(self, undoActions, redoActions):
        self.__undoActions = undoActions
        self.__redoActions = redoActions

    def undo(self):
        action = self.__undoActions.pop()
        action.execute()
        if action.get_rev_action() == None:
            rev_action = action.get_obj_reversed()
            self.__redoActions.push(rev_action)
        else:
            rev_action = action.get_reverse()
            self.__redoActions.push(rev_action)

    def redo(self):
        action = self.__redoActions.pop()
        action.execute()
        if action.get_rev_action() == None:
            rev_action = action.get_obj_reversed()
            self.__undoActions.push(rev_action)
        else:
            rev_action = action.get_reverse()
            self.__undoActions.push(rev_action)
