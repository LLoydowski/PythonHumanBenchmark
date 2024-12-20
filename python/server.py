from flask import Flask, render_template, request, flash, url_for, make_response, redirect
import VerbalMemory, userManagement, ReactionTime, asyncio, time, NumberMemory

class Server:
    def __init__(self):
        self.__app = Flask(__name__, template_folder="./website")

        self.__vmGames = {} # username: str, game: VerbalMemory
        self.__rtGames = {}
        self.__nmGames = {}

        self.__userManager = userManagement.userManager()
        
    def run(self):
        @self.__app.route("/number", methods=["GET", "POST"])
        def number():
            username = request.cookies.get("username") 

            if not username:
                return redirect("/login")

            if(self.__userManager.checkDoesUserExist(username) == False):
                return render_template("noUser.html", username=username)
            
            if username not in list(self.__nmGames.keys()):
                self.__nmGames[username] = NumberMemory.NumberMemory()


            if request.method == "POST":
                data = request.get_json()
                action = data["action"]

                if action == "newGame":
                    self.__nmGames[username].reset()

                    self.__nmGames[username].generateRandomNumber()
                    self.__nmGames[username].generateSleepTime()

                    randNumb = self.__nmGames[username].getRandomNumber()
                    sleepTime = self.__nmGames[username].getSleepTime()

                    return{
                        "randNumb": randNumb,
                        "sleepTime": sleepTime
                    }
                elif action == "guess" and self.__nmGames[username].getStatus() != "lost":
                    guess = data["guess"]
                    result = self.__nmGames[username].checkInput(guess)

                    if not result:
                        self.__nmGames[username].setStatusToLost()
                        score = self.__nmGames[username].getScore()
                        self.__nmGames[username].scoreboard.setScore(username, score)
                        return {
                            "status": "lost"
                        }

                    self.__nmGames[username].nextLevel()

                    self.__nmGames[username].generateRandomNumber()
                    self.__nmGames[username].generateSleepTime()

                    randNumb = self.__nmGames[username].getRandomNumber()
                    sleepTime = self.__nmGames[username].getSleepTime()
                    score = self.__nmGames[username].getScore()

                    return{
                        "status": "",
                        "randNumb": randNumb,
                        "sleepTime": sleepTime,
                        "score": score
                    }
                else:
                    return {"status": "lost"}
            
            return render_template("numberMemory.html")


        @self.__app.route('/reaction', methods=["GET", "POST"])
        def reaction():
            username = request.cookies.get("username") 

            if not username:
                return redirect("/login")

            if(self.__userManager.checkDoesUserExist(username) == False):
                return render_template("noUser.html", username=username)
            
            if username not in list(self.__rtGames.keys()):
                self.__rtGames[username] = ReactionTime.ReactionTime()

            if request.method == "POST":
                data = request.get_json()
                action = data["action"]

                if action == "newGame":
                    self.__rtGames[username].generateWaitTime()
                    startTime = asyncio.run(self.__rtGames[username].startCountdown())
                    return {"sStartTime": startTime}
                
                elif action == "clicked":
                    self.__rtGames[username].stopTimer()
                    endTime = time.time()

                    return {"sEndTime": endTime}
                
                elif action == "validation":
                    sStartTime = data["sStartTime"]
                    sEndTime = data["sEndTime"]
                    cStartTime = data["cStartTime"]
                    cEndTime = data["cEndTime"]

                    sReaction = sEndTime - sStartTime
                    cReaction = cEndTime - cStartTime

                    timesDiffrence = sReaction - cReaction

                    if(timesDiffrence > 175):
                        return {"status": "You either have bad internet connection or you cheated. Therefore your score won't be saved. Sorry!"}

                    self.__rtGames[username].scoreboard.setScore(username, cReaction)
                    
                    return {"status": cReaction}

            return render_template("reactionTime.html")
        
        @self.__app.route('/verbal', methods=["GET", "POST"])
        def verbal():
            username = request.cookies.get("username") 

            if not username:
                return redirect("/login")

            if(self.__userManager.checkDoesUserExist(username) == False):
                return render_template("noUser.html", username=username)

            if username not in list(self.__vmGames.keys()):
                self.__vmGames[username] = VerbalMemory.VerbalMemory()

                self.__vmGames[username].reset()
                self.__vmGames[username].generateRandomWord()


            status = self.__vmGames[username].isGameFinnished()

            if status != "":
                self.__vmGames[username].reset()

            if request.method == "POST":
                choose = request.get_json()["chooice"]

                if choose == "new" and status == "":
                    self.__vmGames[username].newWord()
                    self.__vmGames[username].generateRandomWord()
                elif choose == "seen" and status == "":
                    self.__vmGames[username].seenWord()
                    self.__vmGames[username].generateRandomWord()
                elif choose == "newGame":
                    self.__vmGames[username].reset()
                    self.__vmGames[username].generateRandomWord()

                if self.__vmGames[username].getLives() == 0:
                    self.__vmGames[username].scoreboard.setScore(username, self.__vmGames[username].getScore())
                
                return {
                    "status": self.__vmGames[username].isGameFinnished(),
                    "randWord": self.__vmGames[username].getRandomWord(),
                    "score": self.__vmGames[username].getScore(),
                    "lives": self.__vmGames[username].getLives()
                }
            return render_template('verbalMemory.html')

        @self.__app.route("/login", methods=["POST", "GET"])
        def login():
            response = render_template("login.html")

            if request.method == "POST":
                data = request.get_json()

                username = data["name"]
                password = data["password"]

                if self.__userManager.checkDoesUserExist(username) == False:
                    return {"status": "User with this name doesn't exist. <a href='/signup'> Try creating account instead. </a>"}

                if self.__userManager.checkIsPasswordCorrect(username, password) == False:
                    return {"status": "Username or password is incorrect."}

                return {"status": ""}

            return response

        @self.__app.route("/signup", methods=["POST", "GET"])
        def signup():
            response = render_template("signup.html")

            if request.method == "POST":
                json = request.get_json()

                name = json["name"]
                password = json["password"]

                status = self.__userManager.checkIsPasswordValid(password)

                if status != "":
                    return {
                        "status": status
                    } 

                if self.__userManager.checkDoesUserExist(name):
                    return {
                        "status": "User with this name already exists"
                    }
                else:
                    self.__userManager.addUser(name, password)
                    return {
                        "status": "User created succefully"
                    } 


            return response
        
        @self.__app.route("/scores", methods=["GET"])
        def scores():
            username = request.cookies.get("username") 

            if not username:
                return redirect("/login")

            if(self.__userManager.checkDoesUserExist(username) == False):
                return render_template("noUser.html", username=username)

            tempRT = ReactionTime.ReactionTime()
            rt = tempRT.scoreboard.getPlayerScore(username)

            tempVM = VerbalMemory.VerbalMemory()
            vm = tempVM.scoreboard.getPlayerScore(username)

            tempNM = NumberMemory.NumberMemory()
            nm = tempNM.scoreboard.getPlayerScore(username)

            return render_template("scores.html", vm=vm, rt=rt, nm=nm)

        @self.__app.route('/', methods=["GET"])
        def index():

            return render_template('index.html')

        self.__app.run(host="0.0.0.0", port=85, debug=True, use_reloader=False)