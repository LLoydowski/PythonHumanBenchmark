from Game import *
import time, random

class ReactionTime(Game):
    def __init__(self):
        super().__init__("data/reaction_time.txt")
        self.__best_time_ms = float('inf')
        self.__scores = []
        self.__startTime = 0
        self.__stopTime = 0
        self.__reactionTime = 0
    
    def averageScore(self):
        result = 0
        for i in self.__scores:
            result += int(i)
        
        return int(result / len(self.__scores))
    
    def startTimer(self) -> None:
        self.__startTime = time.time()

    def stopTimer(self) -> None:
        self.__stopTime = time.time()
    
    def calculateReactionTime(self) -> float:
        deltaTime = self.__stopTime - self.__startTime
        reactTime = round(deltaTime * 1000)
        self.__reactionTime = reactTime

    def reactionRound(self):
            input("Press 'Enter' to start...")          
            self.clear()

            time.sleep(random.uniform(1, 5))

            print("Click!")

            self.startTimer()
            input()
            self.stopTimer()

            self.calculateReactionTime()

            if self.checkIsTimeCheated():
                print("You cheated!")
            else:
                print(f"Your reaction time was: {self.__reaction_time_ms:.0f} ms")

    def checkIsTimeCheated(self) -> bool:
        if self.__reactionTime < 50:
            return True
        
        return False

    def getReactionTime(self):
        return self.__reactionTime


    def play(self):

        rounds = 5
        for _ in range(rounds):
            self.reactionRound()
        
        print(f"Your average score: {self.averageScore()}")
        self.scoreboard.saveScore(self.__best_time_ms)

# a = ReactionTime()
# a.play()