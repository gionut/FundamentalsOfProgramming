from Exceptions import ValidError

class Validate:
    def __init__(self):
        pass

    def validate(self, x):
        if x < 0 or x > 5:
            raise ValidError('Out of the board!')

    def validateSymbol(self, x):
        if len(x) != 1:
            raise ValidError('Symbol must be a single character!')