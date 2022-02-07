# Testing environment for a 'Words game' solving AI

Develop your solving algorithm for a game based on Wordle using this simple test environment.

## Requirements:

- [Python 3.6+](https://www.python.org/downloads/)

## How to start:

- Clone the repository:
- Run the game to see how it works:
  ```bash
  python3 main.py
  ```
- Run the test with simple AI:
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

## Acknoledgements:

This test environment is based on [Wordle](https://www.powerlanguage.co.uk/wordle/).

Words come from dataset by [Rachael Tatman](https://www.kaggle.com/rtatman/english-word-frequency/version/1) and are based on Google Web Trillion Word Corpus.

## License:

Licensed under the MIT License.

Created by [Maciej Gamrot](https://github.com/maciekgamma)
#   w o r d - g a m e - A I - e n v i r o n m e n t 
 
 
