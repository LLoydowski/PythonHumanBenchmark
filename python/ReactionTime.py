from Game import *
import time, random

class ReactionTime(Game):
    def __init__(self):
        super().__init__("../data/reaction_time.txt")
        self.__best_time_ms = float('inf')
        self.__scores = []
    
    def averageScore(self):
        result = 0
        for i in self.__scores:
            result += int(i)
        
        return int(result / len(self.__scores))

    def reactionRound(self):
            input("Press 'Enter' to start...")          
            self.clear()

            time.sleep(random.uniform(1, 5))

            print("Click!")

            start_time = time.time()
            input()
            reaction_time_ms = (time.time() - start_time) * 1000 

            reaction_time_ms = round(reaction_time_ms)

            if reaction_time_ms < 50:
                print("cheated!")
                return
            else:
                print(f"Your reaction time was: {reaction_time_ms:.0f} ms")
                self.__scores.append(reaction_time_ms)
            


    def play(self):

        rounds = 5
        for _ in range(rounds):
            self.reactionRound()
        
        print(f"Your average score: {self.averageScore()}")
        self.scoreboard.saveScore(self.__best_time_ms)

a = ReactionTime()
a.play()