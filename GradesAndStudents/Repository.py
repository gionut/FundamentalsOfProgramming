from Exceptions import RepoError
from Domain import Student
class Repo:
    def __init__(self):
        self._data = []

    def store(self, object):
        if object in self._data:
            raise RepoError('The object already exists!')
        self._data.append(object)

    def delete(self, objectId):
        if objectId not in self._data:
            raise RepoError('The object does not exist!')
        self._data.remove(objectId)

    def find(self, objectId):
        for obj in self._data:
            if obj == objectId:
                return obj
        raise RepoError('Could not find the object!')

    def getAll(self):
        return self._data[:]

class FileRepo(Repo):
    def __init__(self, file_name, write, read):
        Repo.__init__(self)
        self.__file_name = file_name
        self.__write = write
        self.__read = read
        self.readFromFile()

    def store(self, object):
        self.readFromFile()
        Repo.store(self, object)
        self.saveToFile()

    def delete(self, objectId):
        self.readFromFile()
        Repo.delete(self, objectId)
        self.saveToFile()

    def find(self, objectId):
        self.readFromFile()
        return Repo.find(self, objectId)

    def getAll(self):
        self.readFromFile()
        return Repo.getAll(self)

    def saveToFile(self):
        with open(self.__file_name, 'w') as f:
            for object in self._data:
                obj = self.__write(object)
                f.write(obj + '\n')

    def readFromFile(self):
        self._data = []
        with open(self.__file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    object = self.__read(line)
                    self._data.append(object)

class StudentRepo(FileRepo):
    def __init__(self, file_name, write, read):
        FileRepo.__init__(self, file_name, write, read)

class GradeRepo(FileRepo):
    def __init__(self, file_name, write, read):
        FileRepo.__init__(self, file_name, write, read)

    def getAll(self, sId):
        self.readFromFile()
        grades = []
        for obj in self._data:
            if obj.studentId == sId:
                grades.append(obj)
        return grades

    def update(self):
        self.saveToFile()

