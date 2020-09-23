class Console:
    def __select(self):
        result = self.__sentenceController.select()
        sentence = result[0]
        score = result[1]
        self.__print_sentence(sentence, score)

    def __print_sentence(self, sentence, score):
        print(sentence + ' [ score is ' + str(score) + ' ]')

    def __ui_swap(self, params):
        word1 = params[0]
        letter1 = params[1]
        word2 = params[3]
        letter2 = params[4]
        result = self.__sentenceController.swap(int(word1)-1, int(letter1)-1, int(word2)-1, int(letter2)-1)
        self.__print_sentence(result[0], result[1])

    def __init__(self, sentenceController):
        self.__sentenceController = sentenceController
        self.__commands = {
            'swap': self.__ui_swap
        }

    def run(self):
        self.__select()
        while True:
            cmd = input('>>>')
            if cmd =='exit':
                return
            if cmd == '':
                continue
            parts = cmd.split()
            command = parts[0]
            params = parts[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](params)
                except ValueError as ve:
                    print('Ui Error!\n' + str(ve))
            else:
                print('Invalid command!')
