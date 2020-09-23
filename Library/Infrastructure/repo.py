from Errors.exceptions import *
import re
from iterable import It
from errors import ItError
from Presentation.console import evil_write

class Repo(It):

# func that creates a repository of  objects
    def __init__(self):
        self._entities = []
        It.__init__(self, self._entities)

    def add(self, obj):
        if obj in self._entities:
            raise RepoError("existing id!\n")
        self._entities.append(obj)
    
    def search(self, objId):
        if objId not in self._entities:
            raise RepoError("inexisting id!\n")
        for x in self._entities:
            if x == objId:
                return x

    def length(self):
        return len(self._entities)
    
    def fget_all(self):
        return self._entities[:]
    
    def remove(self, obj):
        self._entities.remove(obj)
     
    def undoSearch(self, entity):
        if entity not in self._entities:
            raise RepoError("no such entity!")
        for i in range(len(self._entities)):
            if self._entities[i] == entity:
                del self._entities[i]
                return

    def undoUpdate(self, entity, newEntity):
        if entity not in self._entities:
            raise RepoError("no such entity!")
        for i in range(len(self._entities)):
            if self._entities[i] == entity:
                self._entities[i] = newEntity
                return


class FileRepo(Repo):

    def __init__(self, filename, read_object, write_object):
        Repo.__init__(self)
        self.__filename = filename
        self.__read_object = read_object
        self.__write_object = write_object

    def __read_all_from_file(self):
        self._entities = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__read_object(line)
                    self._entities.append(obj)

    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for obj in self._entities:
                line = self.__write_object(obj)
                # f.write(line + "\n")
                evil_write(f, line + "\n")

    def add(self, entity, newentity):
        self.__read_all_from_file()
        Repo.add(self, entity)
        self.__write_all_to_file()

    def update(self, entity, newEntity):
        self.__read_all_from_file()
        Repo.undoUpdate(self, entity, newEntity)
        self.__write_all_to_file()

        self.__write_all_to_file()

    def remove(self, entity, newentity):
        self.__read_all_from_file()
        Repo.remove(self, entity)
        self.__write_all_to_file()

    def search_id(self, id):
        self.__read_all_from_file()
        l = []
        for x in self._entities:
            if re.search(id, x.id, re.IGNORECASE):
                l.append(x)
        return l

    def search_title(self, title):
        self.__read_all_from_file()
        l = []
        for x in self._entities:
            if re.search(title, x.title, re.IGNORECASE):
                l.append(x)
        return l

    def search_author(self, author):
        self.__read_all_from_file()
        l = []
        for x in self._entities:
            if re.search(author, x.author, re.IGNORECASE):
                l.append(x)
        return l

    def search_name(self, name):
        self.__read_all_from_file()
        l = []
        for x in self._entities:
            if re.search(name, x.name, re.IGNORECASE):
                l.append(x)
        return l

    def get_all(self):
        self.__read_all_from_file()
        return Repo.fget_all(self)

class StackUndoActions(object):

        def __init__(self):
            self.__undoActions = []

        def push(self, action):
            self.__undoActions.append(action)

        def pop(self):
            if len(self.__undoActions) == 0:
                raise UndoError("no more undo!")
            return self.__undoActions.pop()

        def clear(self):
            self.__undoActions = []