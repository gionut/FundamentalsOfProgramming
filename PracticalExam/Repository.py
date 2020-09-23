from Exceptions import RepoError


class Repo:
    def __init__(self):
        self._table = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
                       ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['4', ' ', ' ', ' ', 'E', ' ', ' ', ' '],
                       ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self._fires = [(4, 4)]
        self._aliens = []

    @property
    def getTable(self):
        return self._table

    def addFire(self, x, y):
        if (x, y) in self._fires:
            raise RepoError('Cannot fire at this point!')
        self._fires.append((x, y))

    def mark_table(self, x, y, symbol):
        self._table[x][y] = symbol

    def destroy(self, alien):
        self._aliens.remove(alien)

    def addAlien(self, alien):
        self._aliens.append(alien)

    def get_aliens(self):
        return self._aliens

    def getAliens(self):
        return len(self._aliens)

    def empty_aliens(self):
        for i in range(len(self._table)):
            for j in range(len(self._table[i])):
                if self._table[i][j] == 'X' or self._table[i][j] == '':
                    self._table[i][j] = ' '
        self._aliens = []