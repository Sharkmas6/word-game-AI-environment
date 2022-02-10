import csv
from typing import List


# This is a VERY BAD AI that will always guess the first few words from the list
# It uses a list of words from the CSV file words-#.csv (where # is the word length)


class BadAI:
    def __init__(self, word_lenght: int, guess_limit: int):
        self.word_index = 0
        self.words = []
        with open(f'Game/words/words-{word_lenght}.csv', 'r') as file:
            reader = csv.reader(file)
            self.words, _ = zip(*reader)

    def clean(self):
        self.word_index = 0

    def next(self, past_guesses: List[str], past_results: List[int], left: int):
        self.word_index += 1
        return self.words[self.word_index]
