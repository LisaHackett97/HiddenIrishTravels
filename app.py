import os
from flask import (
    Flask, flash, render_template, url_for,
    redirect, request, session)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)



app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    recommendations = list(mongo.db.recommendations.find())
    return render_template("home.html", recommendations=recommendations)


# Access session user page
@app.route("/user_page/<username>", methods=["GET", "POST"])
def user_page(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user_page.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check is user exists in db.
        # Look in users collection for key of username
        # Value is the data from the user input
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if existing user variable found a match in db
        # If truthy, then check if passwords match
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "user_page", username=session['user']))
            else:
                # invald password
                flash("incorrect Username and/password")
                return redirect(url_for('login'))
        else:
            flash("incorrect Username and/password")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # checking if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists. Please choose another!")
            return redirect(url_for("registration"))
        # if user doesn't exist, update db with detials from user
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)
        session['user'] = request.form.get("username").lower()
        flash("Congratulations. You have been registered")
        return redirect(url_for("user_page", username=session["user"]))

    return render_template("registration.html")


@app.route("/add_recommendation", methods=["GET", "POST"])
def add_recommendation():
    if request.method == "POST":
        recommendation = {
            "location": request.form.get("location")
        }
    return render_template('add_recommendation.html')


@app.route("/logout")
def logout():
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
