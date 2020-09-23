class Sentence:
    def __init__(self, sentence):
        self.__sentence = sentence

    @property
    def words(self):
        return self.__sentence

    def __eq__(self, other):
        return self.__sentence == other.words

    def __str__(self):
        string = ''
        for word in self.__sentence:
            word.strip()
            string += word + ' '
        return string.strip()


    @staticmethod
    def read_sentence(line):
        return Sentence(line)

    def write_sentence(self):
        return str(self)

