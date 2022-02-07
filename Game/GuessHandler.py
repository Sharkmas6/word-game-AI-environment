class GuessHandler:
    def __init__(self, word):
        self.word = word
        self.number_of_guesses = 0
        self.guesses = []
        self.results = []

    def guess(self, word):
        # get feedback on the guess
        result = self.check_guess(word)

        # store the guess and it's result
        self.guesses.append(word)
        self.results.append(result)

        return result

    def check_guess(self, word):
        response = []
        for i in range(len(word)):
            if word[i] == self.word[i]:
                response.append(1)
            elif word[i] in self.word:
                response.append(0)
            else:
                response.append(-1)
        return response
