from flask import Flask, render_template,request


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



if __name__ == "__main__":
    app.run(debug= True)


