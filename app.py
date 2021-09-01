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


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
   
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)

        session['user'] = request.form.get("username").lower()
        flash("Congratulations. You have been registered")
        return redirect(url_for("home", username=session["user"]))

    return render_template("registration.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
