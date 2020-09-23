from Exceptions import ValidError


class Validate:
    def __init__(self):
        pass

    def check_adjacence(self,table, x, y, char):
        return ((x != 1 and (table[x - 1][y - 1] == char or table[x - 1][y] == char or (y != 8 and table[x - 1][y + 1] == char))) or
         table[x][y - 1] == char or table[x][y] == char or (y != 8 and table[x][y + 1] == char) or
         (x != 8 and (table[x + 1][y - 1] == char or table[x + 1][y] == char or (y != 8 and table[x + 1][y + 1] == char))))

    def validate_star(self, table, x, y, char):
        if self.check_adjacence(table, x, y, char):
            return 0
        return 1

    def validate_point(self, table, x, y):
        if table[x][y] != ' ':
            return 0
        return 1

    def validate_input(self, x, y):
        if ord(x) < ord('A') or ord(x) > ord('H') or ord(y) < ord('0') or ord(y) > ord('9'):
            raise ValueError('Wrong Coordinates!')

    def wrap(self, table, E, x, y):
        if x != E[0] and y != E[1] and abs(x - E[0]) != abs(y - E[1]):
            raise ValidError('Cannot wrap at ' + chr(ord(str(x))+16) + str(y) +'!\n')

        if table[x][y] == '*':
            raise ValidError('Star crushing!')

        for a in range(min(x, E[0]), max(x, E[0])):
            if table[a][y] == '*':
                raise ValidError('Star crushing!')

        for a in range(min(y, E[1]), max(y, E[1])):
            if table[x][a] == '*':
                raise ValidError('Star crushing!')



