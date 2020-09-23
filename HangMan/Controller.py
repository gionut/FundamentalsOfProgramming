from Domain import Sentence
import random


class SentenceController:
    def __init__(self, repoSentences, validateSentence):
        self.__letters = []
        self.__remain = ''
        self.__hangman = ['h','a','n','g','m','a','n']
        self.__sentence = None
        self.__repoSentences = repoSentences
        self.__validateSentence = validateSentence

    def add(self, sentence):
        sentence = Sentence(sentence)
        self.__validateSentence.validate(sentence)
        self.__repoSentences.add(sentence)

    def select(self):
        sentence = random.choice(self.__repoSentences.getAll())
        return self.hangman_style(sentence)

    def hangman_style(self, sentence):
        self.__sentence = sentence
        hangman_sentence = ''
        for word in sentence.words:
            l = list(word)
            if l[0] not in self.__letters:
                self.__letters.append(l[0])
            if l[len(l)-1] not in self.__letters:
                self.__letters.append(l[len(l)-1])

        for word in sentence.words:
            l = list(word)
            hangman_word = ''
            for letter in l:
                if letter not in self.__letters:
                    letter = '_'
                hangman_word += letter
            hangman_sentence += hangman_word + ' '
        return hangman_sentence.strip()

    def play(self, letter):
        ok = 0
        hangman_sentence = ''
        if letter not in self.__letters:
            self.__letters.append(letter)
        for word in self.__sentence.words:
            l = list(word)
            hangman_word = ''
            for x in l:
                if x not in self.__letters:
                    x = '_'
                if x == letter:
                    ok = 1
                hangman_word += x
            hangman_sentence += hangman_word + ' '
        return [hangman_sentence.strip(), ok]

    def check_winner(self, ok, sentence):
        if len(self.__hangman) == 0:
            return [-1, '\nH̶A̶N̶G̶M̶A̶N̶!\n   💀\nʇsol no⅄!']
        if ok == 0:
            letter = self.__hangman[0]
            self.__remain += letter
            self.__hangman.remove(letter)
            return [0, self.__remain]
        else:
            if '_' not in sentence:
                return [-1, '\n𝓒𝓞𝓝𝓖𝓡𝓐𝓣𝓤𝓛𝓐𝓣𝓘𝓞𝓝𝓢!\n       🎉👑🎉\n▀▄▀▄▀▄ уＯ𝕦 𝔀𝐨𝓃! ▄▀▄▀▄▀']
            return [0, self.__remain]




