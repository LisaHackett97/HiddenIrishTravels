import os
from flask import (
    Flask, flash, render_template, url_for,
    redirect, request, session, url_for)
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


# Search on home page for all recommendations
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recommendations = list(
        mongo.db.recommendations.find({"$text": {"$search": query}}))
    return render_template("home.html", recommendations=recommendations)


# Search on user page only
@app.route("/search_user_page", methods=["GET", "POST"])
def search_user_page():
    query = request.form.get("query")
    recommendations = list(mongo.db.recommendations.find(
        {"$text": {"$search": query}}))
    return render_template("user_page.html", recommendations=recommendations)


# Access session user page
@app.route("/user_page/<username>", methods=["GET", "POST"])
def user_page(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recommendations = list(mongo.db.recommendations.find())

    if session["user"]:
        return render_template(
            "user_page.html",
            username=username, recommendations=recommendations)


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
            "title": request.form.get("recommend-title"),
            "visitor_type": request.form.get("visitor_type"),
            "location_name": request.form.get("location_name"),
            "details": request.form.get("recommend-details"),
            "created_by": session["user"]
        }
        mongo.db.recommendations.insert_one(recommendation)
        flash("Success. You have added a new recommendation!")
        return redirect(url_for("home"))
    locations = mongo.db.locations.find().sort("location_name", 1)
    visitor_type = mongo.db.visitor_type.find().sort("visitor_type", 1)
    return render_template(
        "add_recommendation.html",
        visitor_type=visitor_type, locations=locations)


@app.route(
    "/edit_recommendations/<recommendation_id>",
    methods=["GET", "POST"])
def edit_recommendations(recommendation_id):
    if request.method == "POST":
        submit = {
            "title": request.form.get("recommend-title"),
            "visitor_type": request.form.get("visitor_type"),
            "location_name": request.form.get("location_name"),
            "details": request.form.get("recommend-details"),
            "created_by": session["user"]
        }
        mongo.db.recommendations.update(
            {"_id": ObjectId(recommendation_id)}, submit)
        flash("Recommendation successfully updated!")
    recommendation = mongo.db.recommendations.find_one(
        {"_id": ObjectId(recommendation_id)})
    locations = mongo.db.locations.find().sort("location_name", 1)
    visitor_type = mongo.db.visitor_type.find().sort("visitor_type", 1)
    return render_template(
        "edit_recommendations.html", recommendation=recommendation,
        visitor_type=visitor_type, locations=locations)


@app.route("/delete_recommendation/<recommendation_id>")
def delete_recommendation(recommendation_id):
    mongo.db.recommendations.remove({"_id": ObjectId(recommendation_id)})
    flash("You have successfully deleted the recommendation.")
    return redirect(url_for("user_page", username=session["user"]))


@app.route("/admin")
def admin():    
    return render_template("admin.html")
    
@app.route("/get_fields")
def get_fields():
    fields = list(mongo.db.visitor_type.find().sort("visitor_type", 1))
    locations = list(mongo.db.locations.find().sort("location_name", 1))
    return render_template("manage_dropdown_details.html", visitor_type=fields, locations=locations)



@app.route("/logout")
def logout():
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
