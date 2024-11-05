from Game import *
import time, random, os, platform

class NumberMemory(Game):
    def __init__(self):
        super().__init__("../data/number_memory.txt")
        self.level = 1
        self.__randomNumber = 0


    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    

    def generateRandomNumber(self):
        self.__randomNumber = random.randint(10**(self.level - 1), 10 ** self.level - 1)
        
    
    def rememberRound(self):
        lost = False

        while not lost:
            self.clear()
            self.generateRandomNumber()
            print("Remember that number:")
            print(self.__randomNumber)

            time.sleep(1 + self.level * 0.5)
            
            self.clear()

            print("What was the number?")

            userNumber = input("Your answer: ")

            if int(userNumber) == self.__randomNumber:
                self.score += 1
                self.level += 1
            else:
                lost = True
    
    def printScore(self):
        print(f"Your score: {self.score}!")


    def play(self):
        self.score = 0
        self.rememberRound()
        self.printScore()
        self.scoreboard.saveScore(self.score)