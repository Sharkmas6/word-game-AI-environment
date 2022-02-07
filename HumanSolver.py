from Game import Game


class HumanSolver:
    def __init__(self, word_length=6, guess_limit=6, mode=2):
        self.__word_length = word_length
        self.__guess_limit = guess_limit
        self.__mode = mode
        self.game = Game.Game(word_length, guess_limit)

    def gameLoop(self):
        self.game.restart_game()
        end_game = False
        print(
            f'Starting game for {self.__word_length} with {self.__guess_limit} chances!')
        while not end_game:
            guess = input('Guess a word:')
            result = self.game.next(guess)

            if result[0] == -2:
                # Invalid input
                print('Invalid input! Try again.')
                continue

            if self.__mode == 1:
                self.game.draw_board()
            else:
                self.game.color_print_guesses()

            if result == [1]*self.__word_length:
                print('You won!')
                end_game = True
                continue

            if self.game.guesses_left <= 0:
                print(f'You lost! The word was {self.game.fail()}')
                end_game = True
                continue

            print(f'Guesses left: {self.game.guesses_left}')
