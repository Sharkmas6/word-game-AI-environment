import time
from Game import Game


class Tester:
    def __init__(self, word_lenght, test_count, guess_limit):
        self.word_lenght = word_lenght
        self.test_count = test_count
        self.count_total_guesses = 0
        self.fails = 0
        self.guess_limit = guess_limit

    def test(self, solver, printMode=0):
        # start timer
        start_time = time.time()
        game = Game.Game(self.word_lenght, self.guess_limit)
        try:
            solver = solver(self.word_lenght, self.guess_limit)
        except Exception as e:
            print("Failed to initialize solver:", e)
            return

        for i in range(self.test_count):
            game.restart_game()
            try:
                solver.clean()
            except Exception as e:
                # You don't have clean the solver
                pass
            while game.guesses_left > 0:
                try:
                    guess = solver.next(
                        game.guesses, game.results, game.guesses_left)
                except Exception as e:
                    print("Failed to get next guess:", e)
                    return
                result = game.next(guess)
                if result[0] == -2:
                    # Invalid input
                    print('Invalid input!')
                    break
                if result == [1]*self.word_lenght:
                    break
                if printMode == 1:
                    game.draw_board()
                elif printMode == 2:
                    game.color_print_guesses()
            if game.guesses_left <= 0:
                if printMode > 0:
                    print(
                        f'\033[1;31;40m Failed to find word: {game.fail() } \033[0;0m \n')
                self.fails += 1
            else:
                self.count_total_guesses += self.guess_limit - game.guesses_left
                if printMode > 0:
                    print(
                        f'\033[1;32;40m Found word: {game.fail() } \033[0;0m \n')
        # end timer
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'{self.test_count} tests took {exec_time} seconds.')
        print(f'{self.fails} tests failed.')
        if (self.test_count - self.fails) == 0:
            average_guesses = -1
            print(
                f'Average guesses: -1')
            print(f'Score: 0')

        else:
            average_guesses = self.count_total_guesses / \
                (self.test_count - self.fails)
            print(
                f'Average guesses: {average_guesses}')
            score = int(((self.guess_limit-average_guesses)**2) /
                        (exec_time*self.fails)*self.test_count**2)
            print(f'Score: {score}')
