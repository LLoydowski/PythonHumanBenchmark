class Scoreboard:
    def __init__(self, fileName) -> None:
        self.scores = {}
        self.fileName = fileName
    
    def fillScores(self):
        pass

    def saveScore(self, score):
        file = open(self.fileName, "w")
        file.write(str(score))
    
    def printScores(self):
        print("Scores:\n.......")