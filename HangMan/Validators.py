from Exceptions import ValidError


class ValidateSentence:
    def __init__(self):
        pass

    def validate(self, sentence):
        errors = ''
        if len(sentence.words) < 1:
            errors += 'The sentence must conrain at least one word!\n'

        for word in sentence.words:
            if len(word) < 3:
                errors += 'Every word in the sentence must contain at least 3 letters!\n'

        if len(errors) != 0:
            raise ValidError(errors)