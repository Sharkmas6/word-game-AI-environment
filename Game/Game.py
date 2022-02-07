from Game import WordGenerator
from Game import GuessHandler


class Game:
    def __init__(self, word_length, guess_limit):
        self.__word_length = word_length
        self.__guess_limit = guess_limit
        self.__wordGenerator = WordGenerator.WordGenerator(word_length)
        self.guesses_left = 0

    def restart_game(self):
        self.__word = self.__wordGenerator.generate_word()
        self.__guessHandler = GuessHandler.GuessHandler(self.__word)
        self.guesses_left = self.__guess_limit

    def next(self, guess):
        guess = guess.lower()
        if not guess in self.__wordGenerator.words:
            return [-2] * self.__word_length
        if len(guess) != self.__word_length:
            return [-2] * self.__word_length
        if not guess.isalpha():
            return [-2] * self.__word_length
        self.guesses_left -= 1
        result = self.__guessHandler.guess(guess.upper())
        return result

    @property
    def guesses(self):
        return self.__guessHandler.guesses

    @property
    def results(self):
        return self.__guessHandler.results

    def fail(self):
        word = self.__word
        self.guesses_left = -1
        return word

    def draw_board(self):
        results = self.__guessHandler.results
        for r in results:
            for w in r:
                if w == 1:
                    print("🟩", end='')
                elif w == -1:
                    print("🟥", end='')
                else:
                    print("🟨", end='')
            print('\n', end='')
        print("\n")

    def color_print_guesses(self):
        results = self.__guessHandler.results
        guesses = self.__guessHandler.guesses
        for i in range(len(results)):
            for j in range(len(results[i])):
                r = results[i][j]
                l = guesses[i][j]
                if r == 1:
                    print(f"\033[0;30;42m{l}", end='')
                elif r == -1:
                    print(f"\033[0;37;41m{l}", end='')
                else:
                    print(f"\033[0;30;43m{l}", end='')
            print('\033[0;0m\n', end='')
        print("\n")
