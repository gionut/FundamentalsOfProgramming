from rent import Rental

class Client(Rental):
    def __init__(self, clientid, name):
        self._clientid = clientid
        self._name = name

 ####### clientid SET/GET #######
        @property
        def clientid(self):
            return self._clientid

        @clientid.setter
        def clientid(self, cid):
            self._clientid = cid

####### name SET/GET #######
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, n):
            self._name = n
