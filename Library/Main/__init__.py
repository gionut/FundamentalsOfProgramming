#from Tests.Tests import*
from Tests.unittests import *
from Presentation.console import*
from Business.service import *
from Validator.validators import *

#tests = Test()
unittests = MyTestCase()
#tests.run_all_tests()

validateBook = ValidateBook()
validateClient = ValidateClient()
validateRental = ValidateRental()

repoBooks = FileRepo("books", Book.read_book, Book.write_book)
repoClients = FileRepo("clients", Client.read_client, Client.write_client)
repoRental = FileRepo("rentals", Rental.read_rental, Rental.write_rental)
undoActions = StackUndoActions()
redoActions = StackUndoActions()

serviceBooks = ServiceBooks(repoBooks, validateBook, undoActions, redoActions)
serviceClients = ServiceClients(repoClients, validateClient, undoActions, redoActions)
serviceRental = ServiceRental(repoRental, repoBooks, repoClients, validateRental, undoActions, redoActions)
serviceUndoRedo = ServiceUndoRedo(undoActions, redoActions)

ui = Console(serviceRental, serviceBooks, serviceClients, serviceUndoRedo)

ui.run()
