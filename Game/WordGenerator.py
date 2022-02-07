import random
import csv


class WordGenerator:
    def __init__(self, length):
        self.length = length
        self.words = []
        self.distribution = []
        self.load_words()

    def load_words(self):
        try:
            with open(f'Game/words/words-{self.length}.csv', 'r') as file:
                reader = csv.reader(file)
                self.words, self.distribution = zip(*reader)
                self.distribution = [int(x) for x in self.distribution]

        except FileNotFoundError:
            print(f'File not found: words/words-{self.length}.csv')
            return []

        except Exception as e:
            print(f'Error: {e}')
            return []

    def generate_word(self):
        reult = random.choices(self.words, self.distribution)
        return reult[0].upper()

    def generate_list_of_words(self, number_of_words):
        return [self.generate_word() for _ in range(number_of_words)]
