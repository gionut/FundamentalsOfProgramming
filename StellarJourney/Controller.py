import random


class GameControler:
    def __init__(self, repoGame, validate):
        self.__repoGame = repoGame
        self.__validate = validate
        self.__E = None

    def get_table(self):
        table = self.__repoGame.get_table()
        return table

    def __random(self):
        return random.randint(1,8)

    def place_stars(self):
        count_stars = 0
        while count_stars < 10:
            x = self.__random()
            y = self.__random()
            if not self.__validate.validate_star(self.get_table(), x, y, '*'):
                count_stars -= 1
            else :
                self.__repoGame.mark_point(x, y, '*')
            count_stars += 1
        return self.get_table()

    def place_Endeavour(self):
        while True:
            x = self.__random()
            y = self.__random()
            if self.__validate.validate_point(self.get_table(), x, y):
                self.__repoGame.mark_point(x, y, 'E')
                break
        self.__E = [x, y]
        self.search_for_Blington(x, y)
        return self.get_table()

    def place_Blingon(self):
        count_blingons = 0
        while count_blingons < 3:
            x = self.__random()
            y = self.__random()
            if not self.__validate.validate_point(self.get_table(), x, y):
                count_blingons -= 1
            else:
                self.__repoGame.mark_point(x, y, '')
            count_blingons += 1

    def search_for_Blington(self, x, y):
        table = self.get_table()
        if self.__validate.check_adjacence(table, x, y, ''):
            for a in [x,x-1,x+1]:
                for b in [y-1,y,y+1]:
                    try:
                        if table[a][b] == '':
                            table[a][b] = 'B'
                    except Exception:
                        continue

    def show_Blingons(self):
        table = self.get_table()
        for x in range(9):
            for y in range(9):
                if table[x][y] == '':
                    table[x][y] = 'B'
        return table

    def wrap(self, coordinates):
        table = self.get_table()
        coordinates = list(coordinates)
        self.__validate.validate_input(coordinates[0], coordinates[1])
        x = ord(coordinates[0]) - 16 - ord('0')
        y = ord(coordinates[1]) - ord('0')
        self.__validate.wrap(table, self.__E, x, y)
        self.__repoGame.mark_point(self.__E[0], self.__E[1], ' ')
        self.__repoGame.mark_point(x, y, 'E')
        self.__E = [x, y]
        return table




