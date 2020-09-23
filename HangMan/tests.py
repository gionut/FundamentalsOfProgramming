import unittest
from Domain import Sentence
from Repository import FileRepo

class MyTestCase(unittest.TestCase):
    def test_sentence(self):
        sentence = Sentence(['ana', 'are', 'mere.'])
        self.assertEqual(sentence.words, ['ana', 'are', 'mere.'])
        self.assertEqual(str(sentence), 'ana are mere. ')

    def test_repo(self):
        repoSentence = FileRepo('sentence')



if __name__ == '__main__':
    unittest.main()
