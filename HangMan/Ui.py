from Exceptions import ValidError, RepoError


class Console:
    def __ui_add_sentence(self, params):
        self.__sentenceController.add(params)

    def __ui_start(self, params):
        self.__start = 1
        result =  self.__sentenceController.select()
        print('output: ' + result)

    def __play(self, letter):
        result = self.__sentenceController.play(letter)
        sentence = result[0]
        ok = result[1]
        hangman = self.__sentenceController.check_winner(ok, sentence)
        if hangman[0] == 0:
            print('output changes to: ' + sentence + ' -> ' + hangman[1])
            return 0
        else:
            print(hangman[1])
            return 1

    def __init__(self, sentenceController):
        self.__sentenceController = sentenceController
        self.__start = 0
        self.__commands = {
            'add_sentence' : self.__ui_add_sentence,
            'start' : self.__ui_start
        }

    def run(self):
        while True:
            if self.__start == 1:
                cmd = input('User guess: ')
                if self.__play(cmd) == 1:
                    return

            else:
                cmd = input('>>>')
                if cmd == '':
                    continue
                parts = cmd.split()
                command = parts[0]
                params = parts[1:]
                if self.__start == 1 and command == 'add_sentence':
                    print('You cannot add a sentence while you are in a game!')
                elif command in self.__commands:
                    try:
                        self.__commands[command](params)
                    except ValueError as ve:
                        print('UI Error!\n' + str(ve))
                    except ValidError as vi:
                        print('Business Error!\n' + str(vi))
                    except RepoError as re:
                        print('Repository Error!\n' + str(re))
                else:
                    print('Invalid command!')
            if cmd == 'exit':
                return