from Exceptions import RepoError


class RepoShips:
    def __init__(self):
        self._ships = []

    def add(self, ship):
        if ship in self._ships:
            raise RepoError('The ships overlap!')
        self._ships.append(ship)

    def remove(self, ship):
        self._ships.remove(ship)

    def getAll(self):
        return self._ships[:]

    @property
    def size(self):
        return len(self._ships)