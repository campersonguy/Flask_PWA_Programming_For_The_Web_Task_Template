from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def homepage():
    return render_template("partials/homepage.html")


@app.route("/login")
def login():
    data = dbHandler.listUserData()
    return render_template("partials/login.html", content=data)


@app.route("/signup")
@app.route("/signup", methods=["POST", "GET"])
def signup():
    data = dbHandler.listUserData()
    if request.method == "POST":
        user = request.form["user"]
        pw = request.form["pw"]
        email = request.form["email"]
        dbHandler.insertContact(user, pw, email)
        return redirect(url_for("top_crimes"))
    else:
        return render_template("partials/signup.html", content=data)


@app.route("/top_crimes")
def topcrimes():
    view1 = dbHandler.sortPostData1()
    view2 = dbHandler.sortPostData2()
    return render_template("partials/top_crimes.html", view1=view1, view2=view2)


@app.route("/search_crimes")
def searchcrimes():
    view = dbHandler.listPostData()
    return render_template("partials/search_crimes.html", view=view)


@app.route("/submit_crimes")
def submitcrimes():
    return render_template("partials/submit_crimes.html")


@app.route("/leaderboard")
def leaderboardp():
    return render_template("partials/leaderboard.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
