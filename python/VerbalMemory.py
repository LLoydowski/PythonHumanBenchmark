from Game import *
import random

class NumberMemory(Game):
    def __init__(self):
        super().__init__("../data/number_memory.txt")
        self.__words = []
        self.readWords("data/VM_words.txt")

    def play(self):
        self.__score = 0
        self.__lives = 3
        self.__scoreboard.saveScore(self.score)
        self.__randomWord = ""
        self.__seenWords = []

    def getRandomWord(self):
        randomIndex = random.randint(0, len(self.__words))
        self.__randomWord = self.__words[randomIndex]

    def readWords(self, path:str):
        file = open(path, "r")
        content = file.read()
        lines = content.splitlines()
        for line in lines:
            self.__words.append(line)

    def seenWord(self):
        if self.__randomWord not in self.__seenWords:
            self.__lives -= 1
            self.__seenWords.append(self.__randomWord)
        else:
            self.__score += 1

    def newWord(self):
        if self.__randomWord in self.__seenWords:
            self.__lives -= 1
        else:
            self.__score += 1
            self.__seenWords.append(self.__randomWord)


# Tests

game = NumberMemory()

