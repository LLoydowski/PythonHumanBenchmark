from Game import *

class NumberMemory(Game):
    def __init__(self):
        super().__init__("number_memory.txt")

    def play(self):
        self.score = 5
        self.scoreboard.saveScore(self.score)