from random import randint

class wordGame:
    def __init__(self):
        self.guesses = 5
        self.wordSet = {"able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"}
        self.word = self.randomWord()
        self.wordLetter = set(self.word)
        print("Welcome to Word Guess! You have", self.guesses, "turns to guess the word. Please enter your first guess:")

    def guessWord(self, newWord):
        if newWord not in self.wordSet:
            print("Not a valid word.")
            return False
        elif newWord == self.word:
            print("You got it! Amazing!")
            return True
        else:
            print("Wrong guess! Try again:")
            hint = self.hint(newWord)
            print("Here's a hint: ", hint)
            self.guesses -= 1
            print("You have", self.guesses, "guesses left.")
            return False

    def randomWord(self):
        return list(self.wordSet)[randint(0, len(self.wordSet) - 1)]

    def hint(self, newWord):
        res = ""
        for i in range (len(newWord)):
            if newWord[i] == self.word[i]:
                res += "1"
            elif newWord[i] in self.wordLetter:
                res += "0"
            else:
                res += "-"
        return res


def main():
    game = wordGame()
    print(game.word)
    while True:
        userGuess = input()
        rightGuess = game.guessWord(userGuess)
        if game.guesses == 0:
            print("You're out of turns, game over!")
            break
    


if __name__ == "__main__":
    main()

