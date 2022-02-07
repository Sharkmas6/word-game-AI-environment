# Testing environment for Worlde AIs

Develop your algorithm solving Wordle using this simple test environment.

## Requirements:

- [Python 3.6+](https://www.python.org/downloads/)

The colored tiles used as feedback might not be supported by your terminal. If you use Windows please use a windows terminal instead of CMD or PowerShell.

## How to start:

- Clone the repository:
- Run the game to see how it works:
  ```bash
  python3 main.py
  ```
- Run the test with a simple AI:
  ```bash
  python3 main.py --test
  ```
- Open the `BadAI.py` file to see how the "AI" works.
- Edit it to make it better. You can use the `YourAI.py` as a template, but you have to change the `SOLVER` variable in `main.py` to point to AI class.
- Run the test with your AI:
  ```bash
  python3 main.py --test
  ```
- Try to max out the score and have fun!

## CLI arguments:

- `--test`: Run the test with simple AI.
- `--help`: Show this help.
- `--cases [int]`: Run the test with specified number of cases.
- `--guesses [int]`: Specify allowed number of guesses.
- `--length [int]`: Specify the length of the word.
- `--print [int]`: Specify the print mode (0: no print, 1: print Wordle like boxes, 2: print guesses with feedback, 3: print only test results).

## How to use:

To create your own solution start with `YourAI.py` file as a template. It has only three methodes:

### **init**

Initiates the algorithm. Run only once at the beginning. You can use it to initialize your variables, do some preprocessing, load data, etc.

Parameters:

- `self`: The object.
- `word_length`: The length of the word to be guessed.
- `guess_limit`: The maximum number of guesses allowed.

### clean

Cleans the solver before each game. Use it to reset your variables.

Parameters:

- `self`: The object.

### next

Asks the solver for the next guess based on the current state of the game.

Parameters:

- `self`: The object.
- `past_guesses`: A list of past guesses.
- `past_results`: A list of past results\*.
- `left`: The number of guesses left.

\* See how to interpret the results in [Results interpretation](#results-interpretation).

## Results interpretation:

Result of a guess is always a list of N integers, where N is the length of the word.
Meaning of each integer:

- 1: The letter is in the word and in the right position.
- 0: The letter is in the word, but in the wrong position.
- -1: The letter is not in the word.
- -2: Invalid word. It's is not counted as a guess. (the whole list is filled with -2)

## Acknoledgements:

This test environment is based on [Wordle](https://www.powerlanguage.co.uk/wordle/).

Words come from dataset by [Rachael Tatman](https://www.kaggle.com/rtatman/english-word-frequency/version/1) and are based on Google Web Trillion Word Corpus.

## License:

Licensed under the MIT License.

Created by [Maciej Gamrot](https://github.com/maciekgamma)
