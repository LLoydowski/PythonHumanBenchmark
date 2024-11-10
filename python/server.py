from flask import Flask, render_template, request, flash, url_for, make_response
import VerbalMemory


class Server:
    def __init__(self):
        self.__app = Flask(__name__, template_folder="./website")
        self.__vm = VerbalMemory.VerbalMemory()
        self.__vm.generateRandomWord()
        
    def run(self):
        @self.__app.route('/verbal', methods=["GET", "POST"])
        def verbal():
            randomWord = self.__vm.getRandomWord()

            response = render_template('vm_game.html', word=randomWord, lives=self.__vm.getLives(), score=self.__vm.getScore(), status="")
            
            # response.set_cookie("test", "TestCookie")

            if(self.__vm.isGameFinnished() != ""):
                response = render_template('vm_game.html', word=randomWord, lives=self.__vm.getLives(), score=self.__vm.getScore(), status=self.__vm.isGameFinnished())

            if request.method == "POST":
                choose = request.get_json()["choose"]

                print(f"Data: {choose} \n Word: {randomWord}")

                if(choose == "new"):
                    self.__vm.newWord()
                else:
                    self.__vm.seenWord()

                newScore = self.__vm.getScore() 
                newLives = self.__vm.getLives() 

                print(f"Score: {newScore} \nLives: {newLives}")

                self.__vm.generateRandomWord()

                response = render_template('vm_game.html', word=randomWord, lives=newLives, score=newScore, status="")

            return response

        @self.__app.route("/login")
        def login():
            response = render_template("login.html")
            return response

        @self.__app.route("/set_name", methods=["POST"])
        def save_name():

            name = request.form["name"]

            response = make_response(f"Name set to {name}")
            response.set_cookie("player_name", name)

            return response
        
        @self.__app.route('/', methods=["GET", "POST"])
        def index():
            if request.method == "POST":
                data = request.form['data']

                if not data:
                    flash("Data is required")
                    return
                else:
                    print(f"Fata: {data}")

            return render_template('index.html')

        self.__app.run(host="0.0.0.0", port=85, debug=True)


server = Server()
server.run()