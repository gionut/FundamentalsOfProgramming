from Domain.entities import*
from Errors.exceptions import ValidError


class ValidateBook(object):

# func that validates a book: checks if the id, title and author are not empty strings
    def __init__(self):
        pass
    
    def validate_book(self, book):
        errors = ""
        if len(book.id) <= 0 :
            errors += "invalid id!\n"
        if len(book.title) <= 0:
            errors += "invalid title!\n"
        if len(book.author) <= 0:
            errors += "invalid author!\n"
        if len(errors) > 0:
            raise ValidError(errors)
        

class ValidateClient(object):

# func that validates a client: checks if the id,name are not empty strings
    def __init__(self):
        pass
    
    def validate_client(self, client):
        errors = ""
        if len(client.id) <= 0:
            errors += "invalid id!\n"
        if len(client.name) <= 0:
            errors += "invalid name!\n"
        if len(errors) > 0:
            raise ValidError(errors)

        
class ValidateRental(object):

    def __init__(self):
        pass
    
    def validate_rental(self, rental):
        errors = ""
        if len(rental.get_rented_date()) <= 0:
            errors += "invalid rented date!\n"
        if len(errors) > 0:
            raise ValidError(errors)

