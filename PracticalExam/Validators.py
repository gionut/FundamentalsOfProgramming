from Exceptions import ValidError


class Validate:
    def __init__(self):
        pass

    def check_adjacence(self, table, x, y):
        if x != 1:
            if y != 1:
                if table[x-1][y-1] != ' ':
                    return False
            if table[x-1][y] != ' ':
                return False
            if y != 7:
                if table[x-1][y+1] != ' ':
                    return False
        if y != 1:
            if table[x][y-1] != ' ':
                return False
        if table[x][y] != ' ':
            return False
        if y != 7 :
            if table[x][y+1] != ' ':
                return False
        if x != 7 :
            if y != 1 :
                if table[x + 1][y - 1] != ' ':
                    return False
            if table[x + 1][y] != ' ' :
                return False
            if y != 7 :
                if(table[x + 1][y + 1] != ' '):
                    return False
        return True

    def asteroid(self, table, x, y):
        if table[x][y] != ' ':
            return False

        if not self.check_adjacence(table, x, y):
            return False
        return True

    def alien(self, table, x, y):
        if table[x][y] != ' ':
            return False
        return True

    def fire(self, x, y):
        if x < 1 or x > 7 or y < 1 or y > 7:
            raise ValidError('Invalid Point!')
