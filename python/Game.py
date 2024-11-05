from Scoreboard import *
import os, platform

class Game:
    def __init__(self, fileName):
        self.userName = ""
        self.score = 0
        self.scoreboard = Scoreboard(fileName)
    
    def play(self):
        pass

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    def showScores(self):
        self.scoreboard.printScores()