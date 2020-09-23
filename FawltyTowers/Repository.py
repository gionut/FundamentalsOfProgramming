from Exceptions import RepoError


class Repo:
    def __init__(self):
        self._data = []

    def add(self, object):
        if object in self._data():
            raise RepoError('Existing Object!')
        self._data.append(object)

    def getAll(self):
        return self._data


class FileRepo(Repo):
    def __init__(self, filename, read, write):
        Repo.__init__(self)
        self.__filename = filename
        self.__read = read
        self.__write = write
        self.__read_all_from_file()

    def __read_all_from_file(self):
        self._data = []
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                obj = self.__read(line)
                self._data.append(obj)

    def __write_all_to_file(self):
        with open(self.__filename, 'w') as f:
            for obj in self._data:
                line = self.__write(obj)
                f.write(line+'\n')

    def add(self, object):
        self.__read_all_from_file()
        Repo.add(self, object)
        self.__write_all_to_file()

    def getAll(self):
        self.__read_all_from_file()
        return Repo.getAll(self)

