from Game import *
import random

class VerbalMemory(Game):
    def __init__(self):
        super().__init__("../data/number_memory.txt")
        self.__words = []
        self.readWords("data/VM_words.txt")
        self.reset()

    def reset(self):
        self.__score = 0
        self.__lives = 3
        # self.__scoreboard.saveScore(self.__score)
        self.__randomWord = ""
        self.__seenWords = []

    def generateRandomWord(self):
        randomIndex = random.randint(0, len(self.__words) - 1)
        self.__randomWord = self.__words[randomIndex]

    def getRandomWord(self):
        return self.__randomWord

    def getLives(self):
        return self.__lives
    
    def getScore(self):
        return self.__score

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

        print(self.__lives)

    def newWord(self):
        if self.__randomWord in self.__seenWords:
            self.__lives -= 1
        else:
            self.__score += 1
            self.__seenWords.append(self.__randomWord)

    def isGameFinnished(self):
        if self.__lives == 0:
            return "lost" 
        
        if len(self.__seenWords) == len(self.__words):
            return "won"
        
        return ""

# Tests

game = VerbalMemory()

