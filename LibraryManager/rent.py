
class Rental:
    def __init__(self, rentalid, bookid, clientid, rendate, retdate ):
        self._rentalid = rentalid
        self._rendate = rendate
        self._retdate = retdate
        super().__init__(bookid, clientid)

    @property
    def rentalid(self):
        return self._rentalid

    @setter.rentalid
    def rentalid(self, renid):
        self._rentalid  = renid
