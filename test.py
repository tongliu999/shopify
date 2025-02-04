from random import randint

class wordGame:
    def __init__(self):
        self.word = self.randomWord()

    def guessWord(self, newWord):
        if newWord == self.word:
            return True
        else:
            return False

    def randomWord(self):
        wordSet = {"able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"}
        return list(wordSet)[randint(0, len(wordSet) - 1)]

def main():
    game = wordGame()
    print(game.word)
    userGuess = input()
    if (game.guessWord(userGuess)):
        print ("Win")
    else:
        print("Lose")


if __name__ == "__main__":
    main()

