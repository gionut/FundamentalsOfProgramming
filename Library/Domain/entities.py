

class Book(object):
# abstract data type for a book with an id, a title and an author
    
    def __init__(self, bookId, title, author):
        self.__bookId = bookId
        self.__title = title
        self.__author = author

### GET id ###
    @property
    def id(self):
        return self.__bookId
        
### SET/GET title ###
    @property
    def title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value
    
### SET/GET author ###
    @property
    def author(self):
        return self.__author

    def set_author(self, value):
        self.__author = value
        
    def __eq__(self, other):
        return self.id == other.id
    
    def __str__(self):
        nr = 35 - len(self.title)
        spacest = ""
        for x in range(nr):
            spacest += " "
        nr = 20 - len(self.id)
        spacesi = ""
        for x in range(nr):
            spacesi += " "
        return ("id->" + self.id + spacesi + " title->" + self.title + spacest + " author->" + self.author)


    @staticmethod
    def read_book(line):
        parts = line.split(", ")
        return Book(parts[0], parts[1], parts[2])

    @staticmethod
    def write_book(book):
        return book.id + ", " + book.title + ", " + book.author
    
class Client(object):

    def __init__(self, clientId, name):
        self.__clientId = clientId
        self.__name = name
    
### GET id ###
    
    @property
    def id(self):
        return self.__clientId
    
### SET/GET name ###
    
    @property
    def name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    def __eq__(self, other):
        return self.id == other.id
    
    def  __str__(self):
        nr = 20 - len(self.id)
        spacesi = ""
        for x in range(nr):
            spacesi += " "
        return ("id->" + self.id + spacesi + " name->" + self.name)

    @staticmethod
    def read_client(line):
        parts = line.split(", ")
        return Client(parts[0], parts[1])

    @staticmethod
    def write_client(client):
        return client.id + ", " + client.name

    
class Rental(object):

    def __init__(self, rentalId, book, client, rented_date, returned_date):
        self.__rentalId = rentalId
        self.__client = client
        self.__book = book 
        self.__rented_date = rented_date
        self.__returned_date = returned_date
    
    def get_rentalId(self):
        return self.__rentalId
    
    def get_book(self):
        return self.__book
    
    def get_client(self):
        return self.__client
    
    def get_rented_date(self):
        return self.__rented_date
    
    def get_returned_date(self):
        return self.__returned_date
    
    def set_returned_date(self, value):
        self.__returned_date = value
        
    def __eq__ (self, other):
        return self.get_rentalId() == other.get_rentalId()
        
    def __str__ (self):
        nr = 10 - len(self.get_rentalId())
        spacesid = ""
        for x in range(nr):
            spacesid += " "
        nr = 30 - len(self.get_book().title)
        spacest = ""
        for x in range(nr):
            spacest += " "
        nr = 20 - len(self.get_client().name)
        spacesn = ""
        for x in range(nr):
            spacesn += " "
        return ("id->" + self.get_rentalId() + spacesid + "name->" + self.get_client().name + spacesn + 
                "title->" + self.get_book().title + spacest + "rentedDate->" + self.__rented_date 
                +"     returnedDate->" + self.__returned_date)

    @staticmethod
    def read_rental(line):
        parts = line.split(", ")
        return Rental(parts[0], Book(parts[1], parts[2], parts[3]), Client(parts[4], parts[5]), parts[6], parts[7])

    @staticmethod
    def write_rental(rental):
        return (rental.get_rentalId() + ", " + rental.get_book().id + ", " + rental.get_book().title + ", " +
                rental.get_book().author + ", " + rental.get_client().id + ", " + rental.get_client().name + ", "
                    + rental.get_rented_date() + ", " + rental.get_returned_date())

class UndoAction():
    def __init__(self, repoUndo, action, rev_action, object, newobj):
        self.__repoUndo = repoUndo
        self.__action = action
        self.__object = object
        self.__newobj = newobj
        self.__rev_action = rev_action

    def get_rev_action(self):
        return self.__rev_action

    def execute(self):
        self.__action(self.__repoUndo, self.__object, self.__newobj)

    def get_reverse(self):
        return UndoAction(self.__repoUndo, self.__rev_action, self.__action, self.__object, self.__newobj)

    def get_obj_reversed(self):
        return UndoAction(self.__repoUndo, self.__action, None, self.__newobj, self.__object)

    def __eq__(self,other):
        return self.__repoUndo == other.__repoUndo and self.__action == other.__action and self.__object==other.__object


class ComplexUndoAction(UndoAction):

    def __init__(self):
        self.__undoActions = []

    def add_action(self, action):
        self.__undoActions.append(action)

    def execute(self):
        for i in range(len(self.__undoActions) - 1, -1, -1):
            self.__undoActions[i].execute()

    def get_reverse(self):
        rez = ComplexUndoAction()
        for i in range(len(self.__undoActions) - 1, -1, -1):
            rez.__undoActions.append(self.__undoActions[i].get_reverse())
        return rez

    def get_rev_action(self):
        return 1