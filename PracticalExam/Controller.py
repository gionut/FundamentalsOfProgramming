import random

class Controller:
    def __init__(self, repoGame, validate):
        self.__repoGame = repoGame
        self.__validate = validate
        self._p = 1

    def getTable(self):
        return self.__repoGame.getTable

    def randomly(self):
        coords = [1, 2, 3, 4, 5, 6, 7]
        return random.choice(coords)

    def place_asteroids(self):
        table = self.__repoGame.getTable
        i = 0
        while i < 8:
            x = self.randomly()
            y = self.randomly()
            if self.__validate.asteroid(table, x, y):
                self.__repoGame.mark_table(x, y, '*')
            else:
                i -= 1
            i += 1

    def place_aliens(self):
        table = self.__repoGame.getTable
        i = 0
        while i < 2:
            rc = random.choice(['x', 'y'])
            if rc == 'x':
                x = 1
                y = self.randomly()
            else:
                x = self.randomly()
                y = 1
            if self.__validate.alien(table, x, y):
                self.__repoGame.addAlien((x, y))
                self.__repoGame.mark_table(x, y, '')
            else:
                i -= 1
            i += 1

    def cheat(self):
        table = self.__repoGame.getTable
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == '':
                    self.__repoGame.mark_table(i, j, 'X')

    def fire(self, coordinates):
        """
        function that creates the coordinates from a string(ex: G1 -> x = 7, y = 1), validates
        the coordinates and call method destroy and mark_table from Repository if the coordinates were valid and
        matches to an alien ship's position, returning True.
        Otherwise it will return False or one of the errors Valid Error if the coordinates are wrong or Repo Error
        if the coordinates lead to an occupied spot
        :param coordinates:
        :return: True/ False
        """
        table = self.__repoGame.getTable
        coordinates = list(coordinates)
        x = int(coordinates[1])
        y = ord(coordinates[0])-64
        self.__validate.fire(x, y)
        self.__repoGame.addFire(x, y)
        if table[x][y] == '' or table[x][y] == 'X':
            self.__repoGame.destroy((x, y))
            self.__repoGame.mark_table(x, y, '-')
            return True
        return False

    def teleport(self):
        self.__repoGame.empty_aliens()
        self._p +=1
        p = self._p
        table = self.__repoGame.getTable
        i = 0
        while i < 2:
            rc = random.choice(['x', 'y'])
            if rc == 'x':
                x = p
                y = self.randomly()
            else:
                x = self.randomly()
                y = p
            if self.__validate.alien(table, x, y):
                self.__repoGame.addAlien((x, y))
                self.__repoGame.mark_table(x, y, '')
            else:
                i -= 1
            i += 1


    def check_lose(self):
        aliens = self.__repoGame.get_aliens()
        table = self.__repoGame.getTable
        for alien in aliens:
            x = alien[0]
            y = alien[1]
            if abs(x-4) == 1 and abs(y-4) == 1:
                return True
        return False

    def check_winner(self):
        table = self.__repoGame.getTable
        if self.__repoGame.getAliens() == 0:
            return True
        return False
