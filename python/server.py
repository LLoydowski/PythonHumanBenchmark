from flask import Flask, render_template, request, flash, url_for, make_response
import VerbalMemory


class Server:
    def __init__(self):
        self.__app = Flask(__name__, template_folder="./website")
        self.__vm = VerbalMemory.VerbalMemory()
        
    def run(self):
        @self.__app.route('/verbal', methods=["GET", "POST"])
        def verbal():
            self.__vm.generateRandomWord()
            randomWord = self.__vm.getRandomWord()

            if request.method == "POST":
                choose = request.get_json()["choose"]

                print(f"Data: {choose}")

                if(choose == "new"):
                    self.__vm.newWord()
                    
                else:
                    self.__vm.seenWord()


                res = make_response("Test")
                res.headers['Content-Type'] = 'text/plain'
                return res
                 

            return render_template('vm_game.html', word=randomWord)
        
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
