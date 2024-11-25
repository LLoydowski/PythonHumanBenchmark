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
        self.saveUsersFile()
    
    def checkDoesUserExist(self, username: str) -> bool:
        users = list(self.__users.keys())

        if username in users:
            return True
        
        return False

    def checkIsPasswordCorrect(self, username: str, password: str) -> bool:
        if self.__users[username] == password:
            return True
        return False

    def checkIsPasswordValid(self, password: str) -> str: # status
        length = len(password)

        if password == "":
            return "Password can't be empty"

        numbersCounter = 0
        specialSignCounter = 0
        upperCaseCounter = 0

        numbers = "123456789"
        letters = "qwertyuiopasdfghjklzxcvbnm"
        upperLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        specialCharacters = "!@#$%^&*(()_+"

        for char in password:
            
            isCharValid = False

            if char in letters:
                isCharValid = True
            
            if char in numbers:
                isCharValid = True
                numbersCounter += 1

            if char in specialCharacters:
                isCharValid = True
                specialSignCounter += 1

            if char in upperLetters:
                isCharValid = True
                upperCaseCounter += 1

            if not isCharValid:
                return f"Char {char} can't be used"
            
        if length < 8:
            return "Your password neets to be at least 8 characters long"
        
        if numbersCounter < 3:
            return "Your password needs to have at least 3 numbers"
        
        if upperCaseCounter == 0:
            return "Your password needs to have at least 1 upper case letter"
        
        if specialSignCounter == 0:
            return "Your password needs to have at least 1 special sign"
        
        return ""
                

    def usersToString(self) -> str:
        usersStr = ""
        for user in self.__users:
            usersStr += f"{user} {self.__users[user]} \n"
        
        return usersStr
