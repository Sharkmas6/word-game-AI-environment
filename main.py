import sys
import argparse

import Tester
import HumanSolver
import BadAI

# Edit only the following line to change the AI Class to test
SOLVER = BadAI.BadAI

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run the word game')
    parser.add_argument('-l', '--length', type=int,
                        help='Word length', default=6)
    parser.add_argument('-g', '--guesses', type=int,
                        help='Guesses limit', default=6)
    parser.add_argument('-t', '--test', action='store_true',
                        help='Run the tests')
    parser.add_argument('-c', '--cases', type=int,
                        help='Number of test cases', default=100)
    parser.add_argument('-p', '--print', type=int,
                        help='Print mode (0: no print, 1: print results boxes, 2: print guesses, 3: print game results)', default=0)
    args = parser.parse_args()

    # By default, run the game to play in terminal
    if not args.test:
        hs = HumanSolver.HumanSolver(args.length, args.guesses)
        hs.gameLoop()
        exit(0)
    tester = Tester.Tester(args.length, args.cases, args.guesses)
    tester.test(SOLVER, args.print)
