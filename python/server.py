from flask import Flask, render_template, request, flash, url_for


class Server:
    def __init__(self):
        self.__app = Flask(__name__, template_folder="./website")

    def run(self):
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

        self.__app.run(host="0.0.0.0", port=80)
