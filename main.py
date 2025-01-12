from flask import Flask, render_template,request, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    
    return render_template("index.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/spotify.html")
def port_single_1():
    return render_template("spotify.html")

@app.route("/flight.html")
def port_single_2():
    return render_template("flight.html")

@app.route("/cookie.html")
def cookie():
    return render_template("cookie.html")

@app.route("/amazon.html")
def amazon():
    return render_template("amazon.html")

@app.route("/habit.html")
def habit():
    return render_template("habit.html")

@app.route("/health.html")
def health():
    return render_template("health.html")

@app.route("/pom.html")
def pomodoro():
    return render_template("pom.html")

@app.route("/submitted", methods = ["POST"])
def handle_data():
    req = request.form
    firstname = req["fname"]
    lastname = req["lname"]
    email = req["email"]
    message = req["message"]
    submit(firstname, lastname, email, message)

    return "<h1>Thank You For Reaching Out"

def submit(fname,lname,email,message):
    from pymongo import MongoClient
    from datetime import datetime
    import os

    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client["contact-me"]
    collection = db["aksmelittle"]

    collection.insert_one({
        "fname": fname,
        "lname": lname,
        "email": email,
        "message": message,
        "createdAt": datetime.now()
    })



if __name__ == "__main__":
    app.run(debug= True)


