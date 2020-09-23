from Exceptions.errors import RepoError


class Repo:

    # creates a repository, a list of objects
    def __init__(self):
        self._entities = []

    # returning the size of the repository
    def size(self):
        return len(self._entities)

    # returning all the elements in the repository
    def get_all(self):
        return self._entities[:]

    # add an object into a repository containing objects of the same kind, if the object does not already exists
    def add(self, obj):
        if obj in self._entities:
            raise RepoError('existing object!')
        self._entities.append(obj)

    # remove an object from the repository, if the object exists
    def remove(self, obj):
        if obj not in self._entities:
            raise RepoError("inexisting object!")
        self._entities.remove(obj)
