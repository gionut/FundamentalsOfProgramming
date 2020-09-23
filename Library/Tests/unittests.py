import unittest
from Domain.entities import Book
from Validator.validators import ValidateBook
from Infrastructure.repo import Repo
from Business.service import*
from Errors.exceptions import*


class MyTestCase(unittest.TestCase):
    def test_str_book(self):
        book = Book("0000", "title", "author")
        self.assertEqual(str(book), "id->0000                 title->title                               author->author" )

    def test_str_client(self):
        client = Client("aaaa", "Jenel")
        self.assertEqual(str(client), "id->aaaa                 name->Jenel" )

    def test_str_rental(self):
        rental = Rental("0001",Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"), "2019.11.07", "2019.11.11")
        self.assertEqual(str(rental),"id->0001      name->Groza Adriana       title->Jane Eyre                     rentedDate->2019.11.07     returnedDate->2019.11.11")


    def test_create_book(self):
        book = Book("0000", "title", "author")
        assert(book.id == "0000")
        assert(book.title == "title")
        assert(book.author == "author")
        book.set_title("title1")
        book.set_author("author1")
        assert(book.title == "title1")
        assert(book.author == "author1")
        book1 = Book("0000", "title", "author")
        assert(book == book1)

    def test_validate_book(self):
        validatorbook = ValidateBook()
        book = Book("0000", "title", "author")
        validatorbook.validate_book(book)
        book = Book("", "title", "author")
        try:
            validatorbook.validate_book(book)
            assert (False)
        except Exception as ex:
            assert str(ex) == "invalid id!\n"
        book = Book("0000", "", "author")
        try:
            validatorbook.validate_book(book)
            assert (False)
        except Exception as ex:
            assert (str(ex) == "invalid title!\n")
        book = Book("0000", "title", "")
        try:
            validatorbook.validate_book(book)
            assert (False)
        except Exception as ex:
            assert (str(ex) == "invalid author!\n")
        book = Book("", "", "")
        try:
            validatorbook.validate_book(book)
            assert (False)
        except Exception as ex:
            assert (str(ex) == "invalid id!\ninvalid title!\ninvalid author!\n")

    def test_repo_books(self):
        repoBooks = Repo()
        assert repoBooks.length() == 0
        book = Book("0000", "title", "author")
        repoBooks.add(book)
        objId = Book(book.id, None, None)
        foundBook = repoBooks.search(objId)
        assert foundBook.title == book.title
        assert foundBook.author == book.author
        assert repoBooks.length() == 1
        book = Book("0000", "title1", "author1")
        try:
            repoBooks.add(book)
            assert (False)
        except Exception as ex:
            assert (str(ex) == "existing id!\n")
        book1 = Book("0001", "title", "author")
        repoBooks.add(book1)
        assert repoBooks.length() == 2
        non_existing_book = Book("0005", None, None)
        try:
            repoBooks.search(non_existing_book)
            assert (False)
        except Exception as ex:
            assert (str(ex) == "inexisting id!\n")
        books = repoBooks.get_all()
        assert books == [book, book1]

    def test_srv_book(self):
        repo = Repo()
        valid = ValidateBook()
        srvBook = ServiceBooks(repo, valid)
        assert srvBook.get_nr_books() == 0
        bookId = "0000"
        title = "title"
        author = "author"
        srvBook.add(bookId, title, author)
        assert srvBook.get_nr_books() == 1
        foundBook = srvBook.get_book_by_id("0000")
        assert foundBook.title == title
        assert foundBook.author == author
        try:
            srvBook.add("0000", "title1", "author1")
        except RepoError as re:
            assert str(re) == "existing id!\n"
        try:
            srvBook.add("", "", "")
        except ValidError as ve:
            assert str(ve) == "invalid id!\ninvalid title!\ninvalid author!\n"
        books = srvBook.get_books()
        assert books == [Book("0000", "title", "author")]
        srvBook.update_title("0000", "title")
        self.assertEqual(srvBook.get_book_by_id("0000").title, "title")
        srvBook.update_author("0000", "author1")
        self.assertEqual(srvBook.get_book_by_id("0000").author, "author1")
        srvBook.remove("0000")
        self.assertEqual(srvBook.get_books(), [])

    def test_create_client(self):
        client = Client("aaaa", "Jenel")
        assert client.id == "aaaa"
        assert client.name == "Jenel"
        client.set_name("Jean")
        assert client.id == "aaaa"
        assert client.name == "Jean"
        client1 = Client("aaaa", "Dan")
        assert client == client1

    def test_validate_client(self):
        validateClient = ValidateClient()
        client = Client("aaaa", "Jenel")
        validateClient.validate_client(client)
        client_bad_id = Client("", "Badid")
        try:
            validateClient.validate_client(client_bad_id)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "invalid id!\n")
        client_bad_name = Client("aaaa", "")
        try:
            validateClient.validate_client(client_bad_name)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "invalid name!\n")
        client_bad = Client("", "")
        try:
            validateClient.validate_client(client_bad)
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "invalid id!\ninvalid name!\n")


    def test_srv_client(self):
        repo = Repo()
        validateClient = ValidateClient()
        srvClient = ServiceClients(repo, validateClient)
        assert (srvClient.get_nr_clients() == 0)
        clientId = "aaaa"
        name = "Jenel"
        srvClient.add(clientId, name)
        assert (srvClient.get_nr_clients() == 1)
        assert (srvClient.get_client_by_id("aaaa").name == "Jenel")
        try:
            srvClient.add("aaaa", "jean")
            assert (False)
        except RepoError as re:
            assert (str(re) == "existing id!\n")
        try:
            srvClient.get_client_by_id("bbbb")
            assert (False)
        except RepoError as re:
            assert (str(re) == "inexisting id!\n")
        assert (srvClient.get_clients() == [Client("aaaa", "Jenel")])
        srvClient.update_client("aaaa", "NAME")
        self.assertEqual(srvClient.get_client_by_id("aaaa").name, "NAME")
        srvClient.remove("aaaa")
        self.assertEqual(srvClient.get_clients(), [])

    def test_create_rental(self):
        book = Book("0000", "title", "author")
        client = Client("aaaa", "Jenel")
        rental = Rental("0000", book, client, "12.12.2012", "17.01.2013")
        assert rental.get_rentalId() == "0000"
        assert rental.get_book() == book
        assert rental.get_client() == client
        assert rental.get_rented_date() == "12.12.2012"
        assert rental.get_returned_date() == "17.01.2013"
        rental.set_returned_date("01.01.2013")
        assert rental.get_returned_date() == "01.01.2013"

    def test_validate_rental(self):
        book = Book("0000", "title", "author")
        client = Client("aaaa", "Jenel")
        rental = Rental("0000", book, client, "12.12.2012", "17.01.2013")
        validateRental = ValidateRental()
        validateRental.validate_rental(rental)
        try:
            validateRental.validate_rental(Rental("0000", book, client, "", "date"))
            assert (False)
        except ValidError as ve:
            assert (str(ve) == "invalid rented date!\n")

    def test_repo_rental(self):
        repoRental = Repo()
        book = Book("0000", "title", "author")
        client = Client("aaaa", "Jenel")
        rental = Rental("0000", book, client, "12.12.2012", "17.01.2013")
        assert (repoRental.length() == 0)
        repoRental.add(rental)
        assert (repoRental.length() == 1)
        try:
            repoRental.add(rental)
            assert (False)
        except RepoError as re:
            assert (str(re) == "existing id!\n")
        assert (repoRental.length() == 1)
        non_existing_rental = Rental("0001", book, client, "date", "date")
        try:
            repoRental.search(non_existing_rental)
            assert (False)
        except RepoError as re:
            assert (str(re) == "inexisting id!\n")
        assert (repoRental.get_all() == [rental])

    def test_srv_rental(self):
        repoBooks = FileRepo("file", Book.read_book, Book.write_book)
        repoClients = FileRepo("file", Client.read_client, Client.write_client)
        repoRental = FileRepo("file", Rental.read_rental, Rental.write_rental)
        repoUndo = Repo()
        repoRedo = Repo()
        validateRental = ValidateRental()
        rentalId = "0000"
        book = Book("0000", "title", "author")
        repoBooks.add(book, None)
        client = Client("aaaa", "Jenel")
        repoClients.add(client)
        rentedDate = "date"
        returnedDate = "date"
        srvRental = ServiceRental(repoRental, repoBooks, repoClients, validateRental, repoUndo, repoRedo)
        assert (srvRental.get_nr_rentals() == 0)
        srvRental.add(rentalId, book.id, client.id, rentedDate, returnedDate)
        assert (srvRental.get_nr_rentals() == 1)
        srvRental.return_book("0000", "0000", "date")
        self.assertEqual(srvRental.get_rentals(), [Rental("0000", book, client, "date", "date")])

    def test_search_by_id(self):
        repoBooks = Repo()
        validateBooks = ValidateBook()
        serviceBooks = ServiceBooks(repoBooks, validateBooks)
        repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
        repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
        repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
        l = serviceBooks.search_by_id("0000")
        self.assertEqual(l[0].id, "0000")
        self.assertEqual(l[0].title, "Portretul lui Dorian Gray")
        self.assertEqual(l[0].author, "Oscar Wilde")

    def test_search_by_title(self):
        repoBooks = Repo()
        validateBooks = ValidateBook()
        serviceBooks = ServiceBooks(repoBooks, validateBooks)
        repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
        repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
        repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
        l = serviceBooks.search_by_title("y")
        self.assertEqual(l[0], Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
        self.assertEqual(l[1], Book("0002", "Jane Eyre", "Charlotte Bronte"))

    def test_search_by_author(self):
        repoBooks = Repo()
        validateBooks = ValidateBook()
        serviceBooks = ServiceBooks(repoBooks, validateBooks)
        repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
        repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
        repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
        l = serviceBooks.search_by_author("bronte")
        self.assertEqual(l, [Book("0001", "La rascruce de vanturi", "Emilly Bronte") ,Book("0002", "Jane Eyre", "Charlotte Bronte")])

    def test_search_clients_by_id(self):
        repoClients = Repo()
        validateClients = ValidateClient()
        serviceClients = ServiceClients(repoClients, validateClients)
        repoClients.add(Client("aaaa", "Groza Ionut"))
        repoClients.add(Client("aaab", "Groza Sami"))
        repoClients.add(Client("aaac", "Groza Marius"))
        l = serviceClients.search_by_id("AaA")
        self.assertEqual(l, [Client("aaaa", "Groza Ionut"), Client("aaab", "Groza Sami"), Client("aaac", "Groza Marius")])

    def test_search_clients_by_name(self):
        repoClients = Repo()
        validateClients = ValidateClient()
        serviceClients = ServiceClients(repoClients, validateClients)
        repoClients.add(Client("aaaa", "Groza Ionut"))
        repoClients.add(Client("aaab", "Groza Sami"))
        repoClients.add(Client("aaac", "Groza Marius"))
        l = serviceClients.search_by_name("gROzA")
        self.assertEqual(l, [Client("aaaa", "Groza Ionut"), Client("aaab", "Groza Sami"), Client("aaac", "Groza Marius")])

    def test_most_rented_books(self):
        repoRental = Repo()
        repoClients = Repo()
        repoBooks = Repo()
        validateBook = ValidateBook()
        repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
        repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
        repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
        validateClient = ValidateClient()
        repoClients.add(Client("aaaa", "Groza Ionut"))
        repoClients.add(Client("aaab", "Groza Sami"))
        repoClients.add(Client("aaac", "Groza Marius"))
        repoRental.add(
            Rental("0000", Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee"), Client("aaaa", "Groza Ionut"),
                   "data", "data"))
        repoRental.add(
            Rental("0001", Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"), "data", ""))
        repoRental.add(
            Rental("0002", Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee"), Client("aaaa", "Groza Ionut"),
                   "data", ""))
        validateRental = ValidateRental()
        serviceBooks = ServiceBooks(repoBooks, validateBook)
        serviceClients = ServiceClients(repoClients, validateClient)
        serviceRental = ServiceRental(repoRental, repoBooks, repoClients, validateRental)
        l = serviceRental.most_rented_books()
        self.assertEqual(l[2],[Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee")])

    def test_most_rented_authors(self):
            repoRental = Repo()
            repoClients = Repo()
            repoBooks = Repo()
            validateBook = ValidateBook()
            repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
            repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
            repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
            validateClient = ValidateClient()
            repoClients.add(Client("aaaa", "Groza Ionut"))
            repoClients.add(Client("aaab", "Groza Sami"))
            repoClients.add(Client("aaac", "Groza Marius"))
            repoRental.add(
                Rental("0000", Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee"),
                       Client("aaaa", "Groza Ionut"),
                       "data", "data"))
            repoRental.add(
                Rental("0001", Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"), "data",
                       ""))
            repoRental.add(
                Rental("0002", Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee"),
                       Client("aaaa", "Groza Ionut"),
                       "data", ""))
            validateRental = ValidateRental()
            serviceBooks = ServiceBooks(repoBooks, validateBook)
            serviceClients = ServiceClients(repoClients, validateClient)
            serviceRental = ServiceRental(repoRental, repoBooks, repoClients, validateRental)
            l = serviceRental.most_rented_authors()
            self.assertEqual(l[2], [ "Harper Lee"])

    def test_most_active_clients(self):
            repoRental = Repo()
            repoClients = Repo()
            repoBooks = Repo()
            validateBook = ValidateBook()
            repoBooks.add(Book("0000", "Portretul lui Dorian Gray", "Oscar Wilde"))
            repoBooks.add(Book("0001", "La rascruce de vanturi", "Emilly Bronte"))
            repoBooks.add(Book("0002", "Jane Eyre", "Charlotte Bronte"))
            validateClient = ValidateClient()
            repoClients.add(Client("aaaa", "Groza Ionut"))
            repoClients.add(Client("aaab", "Groza Sami"))
            repoClients.add(Client("aaac", "Groza Marius"))
            repoRental.add(
                Rental("0001", Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"),
                       "2019.11.07", "2019.11.11"))
            repoRental.add(Rental("0002", Book("0007", "Sa ucizi o pasare cantatoare", "Harper Lee"),
                                  Client("aaaa", "Groza Ionut"), "2019.11.11", "2019.11.27"))
            repoRental.add(
                Rental("0003", Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"),
                       "2019.11.12", "2019.11.15"))
            repoRental.add(Rental("0004", Book("0008", "Preaiubita", "Tony Morrison"), Client("aaad", "Groza Adriana"),
                                  "2019.11.17", "2019.11.19"))
            repoRental.add(Rental("0005", Book("0008", "Preaiubita", "Tony Morrison"), Client("aaad", "Groza Adriana"),
                                  "2019.11.24", "2019.11.27"))
            repoRental.add(
                Rental("0006", Book("0002", "Jane Eyre", "Charlotte Bronte"), Client("aaad", "Groza Adriana"),
                       "2019.11.20", "2019.11.23"))
            validateRental = ValidateRental()
            serviceBooks = ServiceBooks(repoBooks, validateBook)
            serviceClients = ServiceClients(repoClients, validateClient)
            serviceRental = ServiceRental(repoRental, repoBooks, repoClients, validateRental)
            l = serviceRental.most_active_clients()
            self.assertEqual(l[16], [Client("aaaa", "Groza Ionut")])
if __name__ == '__main__':
    unittest.main()
