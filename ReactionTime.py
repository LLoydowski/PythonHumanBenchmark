from Game import *

class ReactionTime(Game):
    def __init__(self):
        super().__init__("reaction_time.txt")

    def play(self):
        self.score = 10
        self.scoreboard.saveScore(self.score)