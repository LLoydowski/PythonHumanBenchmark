import Scoreboard

class userManager:
    def __init__(self, usersFilePath = "./data/users.txt"):
        self.__usersFilePath = usersFilePath
        self.readUsersFile()

    def readUsersFile(self) -> None:
        file = open(self.__usersFilePath, "r")
        content = file.read()
        self.__users = {}

        lines = content.splitlines()

        for line in lines:
            words = line.split(' ')
            username = words[0]
            password = words[1]

            self.__users[username] = password

    def saveUsersFile(self):
        file = open(self.__usersFilePath, "w")
        file.write(self.usersToString())

    def printUsers(self):
        print(self.__users)

    def addUser(self, username: str, password: str) -> None:
        self.__users[username] = password
    
    def checkDoesUserExist(self, username: str) -> bool:
        ...

    def checkIsPasswordCorrect(self, username: str, password: str) -> bool:
        ...

    def setUserScore(self, username: str, scoreboard: Scoreboard, score: float) -> None:
        ...

    def usersToString(self) -> str:
        usersStr = ""
        for user in self.__users:
            usersStr += f"{user} {self.__users[user]} \n"
