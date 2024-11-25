from Game import *
import time, random

class NumberMemory(Game):
    def __init__(self):
        super().__init__("data/number_memory.txt")
        self.score = 1
        self.__status = ""
        self.__randomNumber = 0
    
    def reset(self):
        self.__score = 1
        self.__status = ""

    def generateRandomNumber(self):
        self.__randomNumber = random.randint(10**(self.__score - 1), 10 ** self.__score - 1)
    
    def getRandomNumber(self):
        return self.__randomNumber
    
    def generateSleepTime(self):
        self.__sleepTime = 1 + self.__score * 0.5

    def getSleepTime(self):
        return self.__sleepTime
    
    def checkInput(self, numberInput):
        if numberInput == self.__randomNumber:
            return True            
        return False
    
    def nextLevel(self):
        self.__score += 1

    def setStatusToLost(self):
        self.__status = "lost"

    def getStatus(self):
        return self.__status
    
    def getScore(self):
        return self.__score
    
    def rememberRound(self):
        while self.__status != "lost":
            self.clear()
            self.generateRandomNumber()
            print("Remember that number:")
            print(self.__randomNumber)

            self.generateRandomNumber()
            time.sleep(self.__sleepTime)
            
            self.clear()

            print("What was the number?")

            userNumber = input("Your answer: ")

            if int(userNumber) == self.__randomNumber:
                self.nextLevel()
            else:
                self.__status = "lost"
    
    def printScore(self):
        print(f"Your score: {self.__score}!")


    def play(self):
        self.reset()
        print("Enter your name:")
        username = input("> ")

        self.rememberRound()
        self.printScore()
        self.scoreboard.setScore(username, self.score)