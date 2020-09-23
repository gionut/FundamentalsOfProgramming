import random

class SentenceController:
    def __init__(self, repoSentences):
        self.__repoSentences = repoSentences
        self.__sentence = None
        self.__scramble = ''
        self.__score = 0

    def select(self):
        self.__sentence = random.choice(self.__repoSentences.getAll())
        sentence = self.__sentence
        self.__scramble = self.scramble(sentence)
        return [self.__scramble, self.__score]

    def scramble(self, sentence):
        letters = []
        for word in sentence.words:
            letters_in_word = list(word)
            n = len(letters_in_word) -1
            self.__score += n+1
            for letter in letters_in_word[1:n]:
                letters.append(letter)

        random.shuffle(letters)

        for word in sentence.words:
            letters_in_word = list(word)
            n = len(letters_in_word) -1
            scrambled_word = letters_in_word[0]
            for x in range(n-1):
                scrambled_word += letters[0]
                letters.remove(letters[0])
            scrambled_word += letters_in_word[n] + ' '
            self.__scramble += scrambled_word
        return self.__scramble

    def swap(self, word1, letter1, word2, letter2):
        words = self.__scramble.split()
        stword = words[word1]
        ndword = words[word2]
        stword = list(stword)
        ndword = list(ndword)
        aux = stword[letter1]
        stword[letter1] = ndword[letter2]
        ndword[letter2] = aux
        if word1 == word2:
            stra = ''
            contor = 0
            for letter in words[word1]:
                if contor == letter1:
                    letter = stword[letter1]
                elif contor == letter2:
                    letter = ndword[letter2]
                stra += letter
                contor += 1
        else:
            str1 = ''
            words[word1] = str1.join(stword)
            str2 = ''
            words[word2] = str1.join(ndword)
        str1 = ''
        for word in words:
            if word1 == word2 and word == words[word1]:
                str1 += stra + ' '
            else:
                str1 += word + ' '
        self.__scramble = str1.strip()
        self.__score = self.__score - 1
        return (self.__scramble, self.__score)


