from Game import *
import time, random

class ReactionTime(Game):
    def __init__(self):
        super().__init__("data/reaction_time.txt")
        self.__scores = []
        self.__startTime = 0
        self.__stopTime = 0
        self.__reactionTime = 0
        self.__waitTime = 0
    
    def averageScore(self):
        result = 0
        for i in self.__scores:
            result += int(i)
        
        return int(result / len(self.__scores))
    
    def startTimer(self) -> None:
        self.__startTime = time.time()

    def stopTimer(self) -> int:
        self.__stopTime = time.time()

        self.calculateReactionTime()
        return self.__reactionTime

    
    def calculateReactionTime(self) -> None:
        deltaTime = self.__stopTime - self.__startTime
        reactTime = round(deltaTime * 1000)
        self.__reactionTime = reactTime


    def calculateRealTime(self, time) -> float:
        deltaTime = time - self.__startTime
        reactTime = round(deltaTime * 1000)
        return reactTime
    
    async def startCountdown(self) -> int:
        time.sleep(self.__waitTime)
        self.startTimer()
        return time.time()
    
    def generateWaitTime(self) -> None:
        self.__waitTime = random.uniform(1, 5)
    
    def getWaitTime(self) -> int:
        return self.__waitTime

    def reactionRound(self):
            input("Press 'Enter' to start...")          
            self.clear()

            self.generateWaitTime()
            time.sleep(self.__waitTime)

            print("Click!")

            self.startTimer()
            input()
            self.stopTimer()

            self.calculateReactionTime()

            if self.checkIsTimeCheated():
                print("You cheated!")
            else:
                print(f"Your reaction time was: {self.__reactionTime:.0f} ms")
                self.__scores.append(self.__reactionTime)

    def checkIsTimeCheated(self) -> bool:
        if self.__reactionTime < 50:
            return True
        
        return False

    def getReactionTime(self):
        return self.__reactionTime


    def play(self):
        print("Enter your name: ")
        username = input("> ")

        rounds = 5
        for _ in range(rounds):
            self.reactionRound()
        
        print(f"Your average score: {self.averageScore()}")
        self.scoreboard.setScore(username, self.averageScore())

# a = ReactionTime()
# a.play()