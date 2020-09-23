from Errors.exceptions import*

evil_global_str = None

def evil_write(f, n):
    s = str(n)

    if evil_global_str is not None:
        f.write(s.replace(evil_global_str, ""))
    else:
        f.write(s)

def evil_print(n):
    s = str(n)

    if evil_global_str is not None:
      print(s.replace(evil_global_str, ""))
    else:
      print(s)

def be_evil(params):
    global evil_global_str
    evil_global_str = params[0]
    print("Being evil with " + evil_global_str)

class Console(object):
    
    def __ui_add_book(self, params):
        if len(params) != 3:
            raise ValueError("it requiers exactly 3 parameters!")
        bookId = params[0]
        title = params[1]
        author = params[2]
        self.__serviceBooks.add(bookId, title, author)
    
    def __ui_add_client(self, params):
        if len(params) != 2:
            raise ValueError("it requiers exactly 2 parameters")
        clientId = params[0]
        name = params[1]
        self.__serviceClients.add(clientId, name)
        
    def __ui_print_books(self, params):
        if len(params) != 0:
            raise ValueError("print_books function does not have parameters!")
        books = self.__serviceBooks.get_books()
        for book in books:
            evil_print(str(book))
            
    def __ui_print_clients(self, params):
        if len(params) != 0:
            raise ValueError("print_clients function does not have parameters!")
        clients = self.__serviceClients.get_clients()
        for client in clients:
            evil_print(str(client))
            
    def __ui_remove_book(self, params):
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 parameters")
        bookId = params[0]
        self.__serviceBooks.remove(bookId)
     
    def __ui_remove_client(self, params):
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 parameters")
        clientId = params[0]
        self.__serviceRental.remove(clientId)
        
    def __ui_update_book_title(self, params):
        if len(params) != 2:
            raise ValueError("it requiers exactly 2 params")
        bookId = params[0]
        newTitle = params[1]
        self.__serviceBooks.update_title(bookId, newTitle)
        
    def __ui_update_book_author(self, params):
        if len(params) != 2:
            raise ValueError("it requiers exactly 2 params")
        bookId = params[0]
        newAuthor = params[1]
        self.__serviceBooks.update_author(bookId, newAuthor)
        
    def __ui_update_client(self, params):
        if len(params) != 2:
            raise ValueError("it requiers exactly 2 params")
        clientId = params[0]
        newName = params[1]
        self.__serviceClients.update_client(clientId, newName)
    
    def __ui_rent_book(self, params):
        if len(params) != 4:
            raise ValueError("it requiers exactly 4 params")
        rentalId = params[0]
        clientId = params[1]
        bookId = params[2]
        rentedDate = params[3]
        self.__serviceRental.add(rentalId, bookId, clientId, rentedDate, "-")
            
    def __ui_print_rental(self, params):
        if len(params) != 0:
            raise ValueError("it requiers exactly 0 params")
        rentals = self.__serviceRental.get_rentals()
        for rental in rentals:
            evil_print(rental)
            
    def __ui_return_book(self, params):
        if len(params) != 3:
            raise ValueError("it requiers exactly 3 params")
        rentalId = params[0]
        bookId = params[1]
        returned_date = params[2]
        self.__serviceRental.return_book(rentalId, bookId, returned_date)

    def __ui_book_by_id(self, params):
        l = []
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 param")
        bookId = params[0]
        l = self.__serviceBooks.search_by_id(bookId)
        for x in l:
            evil_print(str(x))

    def __ui_book_by_title(self, params):
        l = []
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 param")
        title = params[0]
        l = self.__serviceBooks.search_by_title(title)
        for x in l:
            evil_print(str(x))

    def __ui_book_by_author(self, params):
        l = []
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 param")
        author = params[0]
        l = self.__serviceBooks.search_by_author(author)
        for x in l:
            evil_print(str(x))

    def __ui_client_by_name(self, params):
        l = []
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 param")
        name = params[0]
        l = self.__serviceClients.search_by_name(name)
        for x in l:
            evil_print(str(x))

    def __ui_client_by_id(self, params):
        l = []
        if len(params) != 1:
            raise ValueError("it requiers exactly 1 param")
        clientId = params[0]
        l = self.__serviceClients.search_by_id(clientId)
        for x in l:
            evil_print(str(x))

    def __ui_most_rented_books(self, params):
        if len(params) != 0:
            raise ValueError("it has no params")
        y = self.__serviceRental.most_rented_books()
        l = list(y.items())
        l.sort(reverse=True)
        y = dict(l)
        for x in y:
            for i in y[x]:
                evil_print(str(i))

    def __ui_most_active_clients(self, params):
        if len(params) != 0:
            raise ValueError("it has no params")
        y = self.__serviceRental.most_active_clients()
        l = list(y.items())
        l.sort(reverse=True)
        y = dict(l)
        for x in y:
            for i in y[x]:
                evil_print(str(i))

    def __ui_most_rented_authors(self, params):
        if len(params) != 0:
            raise ValueError("it has no params")
        y = self.__serviceRental.most_rented_authors()
        l = list(y.items())
        l.sort(reverse=True)
        y = dict(l)
        for x in y:
            for i in y[x]:
                evil_print(str(i))

    def __ui_undo(self, params):
        if len(params)!=0:
            raise ValueError("it has no params")
        self.__serviceUndoRedo.undo()

    def __ui_redo(self, params):
        if len(params)!=0:
            raise ValueError("it has no params")
        self.__serviceUndoRedo.redo()

    def __init__(self, serviceRental, serviceBooks, serviceClients, serviceUndoRedo):
        self.__serviceBooks = serviceBooks
        self.__serviceClients = serviceClients
        self.__serviceRental = serviceRental
        self.__serviceUndoRedo = serviceUndoRedo
        self.__commands = {
            "add_book": self.__ui_add_book,
            "print_books": self.__ui_print_books,
            "add_client": self.__ui_add_client,
            "print_clients": self.__ui_print_clients,
            "remove_book": self.__ui_remove_book,
            "remove_client": self.__ui_remove_client,
            "update_book_title": self.__ui_update_book_title,
            "update_book_author": self.__ui_update_book_author,
            "rent_book": self.__ui_rent_book,
            "print_rentals": self.__ui_print_rental,
            "return_book": self.__ui_return_book,
            "update_client": self.__ui_update_client,
            "book_by_id": self.__ui_book_by_id,
            "book_by_title": self.__ui_book_by_title,
            "book_by_author": self.__ui_book_by_author,
            "client_by_id": self.__ui_client_by_id,
            "client_by_name": self.__ui_client_by_name,
            "most_rented_books": self.__ui_most_rented_books,
            "most_active_clients": self.__ui_most_active_clients,
            "most_rented_authors": self.__ui_most_rented_authors,
            "undo": self.__ui_undo,
            "redo": self.__ui_redo,
            "be_evil": be_evil
            }

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            cmd = cmd.strip()
            if cmd == "":
                continue
            parts = cmd.split()
            name_cmd = parts[0]
            params = parts[1:]
            if name_cmd in self.__commands:
                try:
                    self.__commands[name_cmd](params)
                except ValueError as ve:
                    evil_print("UI error:\n" + str(ve))
                except ValidError as vale:
                    evil_print("Business Error:\n" + str(vale))
                except RepoError as re:
                    evil_print("Repo Error:\n" + str(re))
                except UndoError as ue:
                    evil_print("UndoError:\n" + str(ue))
            else:
                evil_print("invalid command!\n")
    
