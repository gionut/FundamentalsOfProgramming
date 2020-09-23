from Exceptions import RepoError


class Repo:
    def __init__(self):
        self._points = []

    def add(self, point):
        if point in self._points:
            raise RepoError('Existing Point!')
        self._points.append(point)

    def getAll(self):
        return self._points