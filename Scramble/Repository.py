from Domain import Sentence


class Repo:
    def __init__(self):
        self._data = []

    def getAll(self):
        return self._data

class FileRepo(Repo):
    def __init__(self, filename):
        self.__filename = filename
        self.read_all_from_file()

    def read_all_from_file(self):
        self._data = []
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                obj = Sentence.read_sentence(line)
                self._data.append(obj)

    def save_all_from_file(self):
        with open(filename, 'w') as f:
            for obj in self._data:
                f.write(obj.write_sentence() + '\n')

    def getAll(self):
        self.read_all_from_file()
        return Repo.getAll(self)
