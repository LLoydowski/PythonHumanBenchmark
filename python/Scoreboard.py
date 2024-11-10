class Scoreboard:
    def __init__(self, fileName) -> None:
        self.scores = {}
        self.fileName = fileName
        self.getScores()
    
    def fillScores(self):
        pass
    
    def scoresToString(self) -> str:
        usersStr = ""
        for user in self.scores:
            usersStr += f"{user} {self.scores[user]} \n"

        return usersStr

    def getScores(self):
        file = open(self.fileName, "r")
        content = file.read()
        lines = content.splitlines()

        for line in lines:
            words = line.split(" ")
            username = words[0]
            score = words[1]
            self.scores[username] = score

    def setScore(self, username, score):
        self.scores[username] = score
        self.saveScore()

    def saveScore(self):
        file = open(self.fileName, "w")
        file.write(self.scoresToString())
    
    def printScores(self):
        print("Scores:\n.......")