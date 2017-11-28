class Guess:

    def __init__(self, word):

        self.guessedChars = ""
        self.numTries = 0
        self.secretWord = word
        self.currentStatus = '_'*len(word)

        #pass


    def display(self):
        print("Current: ", self.currentStatus)
        print("Tries: ", self.numTries)
        #pass


    def guess(self, character):

        if character in self.guessedChars:
            pass
        else:
            if self.secretWord.find(character) == -1:
                self.numTries = self.numTries + 1
            else:
                for i in range(len(self.secretWord)):
                    if self.secretWord[i] == character:
                        self.currentStatus = self.currentStatus[:i] + self.secretWord[i] + self.currentStatus[i+1:]
                if self.currentStatus == self.secretWord:
                    return True

            self.guessedChars = self.guessedChars + " " + character


        #pass
