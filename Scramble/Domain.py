class Sentence:
    def __init__(self, words):
        self.__words = words

    def __str__(self):
        sentence = ''
        for word in self.words:
            word.strip()
            sentence += word + ' '
        return sentence.strip()

    @property
    def words(self):
        words = self.__words.split()
        return words

    @staticmethod
    def read_sentence(line):
        line = line.strip()
        return Sentence(line)

    def write_sentence(self):
        return str(self)

