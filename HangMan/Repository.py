from Exceptions import RepoError
from Domain import Sentence


class Repo:
    def __init__(self):
        self._data = []

    def add(self, sentence):
        if sentence in self._data:
            raise RepoError('There can be no duplicate sentences!')
        self._data.append(sentence)

    def getAll(self):
        return self._data


class FileRepo(Repo):
    def __init__(self, filename):
        Repo.__init__(self)
        self.__filename = filename
        self.__read_all_from_file()

    def __read_all_from_file(self):
        self._data = []
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                line = line.split()
                sentence = Sentence.read_sentence(line)
                self._data.append(sentence)

    def __save_all_to_file(self):
        with open(self.__filename, 'w') as f:
            for sentence in self._data:
                obj = sentence.write_sentence()
                f.write(obj + '\n')

    def add(self, sentence):
        self.__read_all_from_file()
        Repo.add(self, sentence)
        self.__save_all_to_file()

    def getAll(self):
        self.__read_all_from_file()
        return Repo.getAll(self)
