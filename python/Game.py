from Scoreboard import *

class Game:
    def __init__(self, fileName):
        self.userName = ""
        self.score = 0
        self.scoreboard = Scoreboard(fileName)
    
    def play(self):
        pass
    
    def showScores(self):
        self.scoreboard.printScores()