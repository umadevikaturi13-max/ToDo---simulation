from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

total_amount = 1000

@app.route("/")
def start():
    return render_template("start.html")    


@app.route("/game", methods=["POST"])
def game(): 

    name = request.form.get("name")
    age = request.form.get("age")
    character = request.form.get("character")

    return render_template(
        "game.html",
        name=name,
        age=age,
        character=character,
        amount=total_amount
    )


@app.route("/time")
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")

    return {
        "time": current_time,
        "date": current_date
    }


if __name__ == "__main__":
    app.run(debug=True)