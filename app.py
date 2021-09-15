import os
from flask import (
    Flask, flash, render_template, url_for,
    redirect, request, session, jsonify)
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
if os.path.exists("env.py"):
    import env

load_dotenv()

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Follow a tutorial on cloudinary.com
# Link in credits section of README
# Link to Admin Page Only. future feature for user to upload own image
@app.route("/upload", methods=["GET", "POST"])
@cross_origin()
def upload():
    cloudinary.config(
        cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'),
        api_secret=os.getenv('API_SECRET'))
    upload_result = None
    if request.method == 'POST':
        file_to_upload = request.files['file']
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload)
        flash("Success")
        return jsonify(upload_result)
    return render_template("upload.html")


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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    query = request.form.get("query")
    recommendations = list(mongo.db.recommendations.find(
        {"$text": {"$search": query}}))
    return render_template(
        "user_page.html", recommendations=recommendations, username=username)


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


# user login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """
        Check if user exists in db.
        Look in users collection for key of username
        Value is the data from the user input
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if existing user variable found a match in db
        # If truthy, then check if passwords match
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "user_page", username=session['user']))
            else:
                # invald password
                flash("Incorrect Username and/password")
                return redirect(url_for('login'))
        else:
            flash("Incorrect Username and/password")
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
        # if user doesn't exist, update db with details from user
        # Add a timestamp to the user docs
        # Credit following post to fix issue with datetime
        # https://www.programiz.com/python-programming/datetime/strftime
        created_at = datetime.today().strftime('%d/%m/%Y, %H:%M')
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "timestamp": created_at,
            "is_admin": False}
        mongo.db.users.insert_one(registration)
        session['user'] = request.form.get("username").lower()
        flash("Congratulations. You have been registered")
        return redirect(url_for("user_page", username=session["user"]))
    return render_template("registration.html")


# user add a new recommendation
@app.route("/add_recommendation", methods=["GET", "POST"])
def add_recommendation():
    if request.method == "POST":
        recommendation = {
            "title": request.form.get("recommend-title"),
            "visitor_type": request.form.get("visitor_type"),
            "location_name": request.form.get("location_name"),
            "details": request.form.get("recommend-details"),
            "created_by": session["user"],
            "image_url": request.form.get("image_name")
        }
        mongo.db.recommendations.insert_one(recommendation)
        flash("Success. You have added a new recommendation!")
        return redirect(url_for("home"))
    locations = mongo.db.locations.find().sort("location_name", 1)
    visitor_type = mongo.db.visitor_type.find().sort("visitor_type", 1)
    image_url = mongo.db.images.find().sort("image_name", 1)
    return render_template(
        "add_recommendation.html",
        visitor_type=visitor_type, locations=locations, image_name=image_url)


# user edit their own recommendation
@app.route("/edit_recommendations/<recommendation_id>",
            methods=["GET", "POST"])
def edit_recommendations(recommendation_id):
    if request.method == "POST":
        submit = {
            "title": request.form.get("recommend-title"),
            "visitor_type": request.form.get("visitor_type"),
            "location_name": request.form.get("location_name"),
            "details": request.form.get("recommend-details"),
            "created_by": session["user"],
            "image_url": request.form.get("image_name")
        }
        mongo.db.recommendations.update(
            {"_id": ObjectId(recommendation_id)}, submit)
        flash("Recommendation successfully updated!")
    recommendation = mongo.db.recommendations.find_one(
        {"_id": ObjectId(recommendation_id)})
    locations = mongo.db.locations.find().sort("location_name", 1)
    visitor_type = mongo.db.visitor_type.find().sort("visitor_type", 1)
    image_url = mongo.db.images.find().sort("image_name", 1)
    return render_template(
        "edit_recommendations.html", recommendation=recommendation,
        visitor_type=visitor_type, locations=locations,  image_name=image_url)


"""
user can delete their own recommendation
admin can delete any user recommendation
if is_admin is true, redirect to admin page. If not, back to the user page
"""


@app.route("/delete_recommendation/<recommendation_id>")
def delete_recommendation(recommendation_id):
    mongo.db.recommendations.remove({"_id": ObjectId(recommendation_id)})
    flash("You have successfully deleted the recommendation.")
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("user_page", username=session["user"]))


# Admin routes and functions

@app.route("/admin")
def admin():
    # if user is_admin, gives access to admin page
    # if not, is_admin is default of false,
    # redirect user to home page with msg
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        return render_template("admin.html")
    else:
        flash("You are not authorized to access Admin Page")
        flash("You have been redirected to Home Page")
        return redirect(url_for("home"))


# Admin- to display visitor type and location names from db
# From this page, admin will then be able to edit or delete field details
@app.route("/manage_form_details")
def manage_form_details():
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        fields = list(mongo.db.visitor_type.find().sort("visitor_type", 1))
        locations = list(mongo.db.locations.find().sort("location_name", 1))
        return render_template(
            "manage_form_details.html",
            visitor_type=fields, locations=locations)
    else:
        flash(
            "You are not authorized to access the Page")
        return redirect(url_for("home"))


# To bring admin user to the page to access forms
# where they can then add new details to the categories for dropdown lists
@app.route("/add_field_details")
def add_field_details():
    return render_template("add_field_details.html")


# To access the form to add a new location
@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        # Check if data entered already exists in locations collection
        location_check = mongo.db.locations.find_one(
            {"location_name": request.form.get("location_name")})
        # Flash a message if data already in db
        if location_check:
            flash("Location already exists in the DB")
            return render_template("add_field_details.html")
        # If data is new, add to the db collection
        location = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.insert_one(location)
        flash("Successfully added {} to the DB".format(
            request.form.get("location_name")))
        return redirect(url_for("add_location"))
    return render_template("add_field_details.html")


# Add a new visitor type. Update dropdown list on recommendation form
@app.route("/add_visitor_details", methods=["GET", "POST"])
def add_visitor_details():
    if request.method == "POST":
        # Check if data entered already exists in visitor collection
        visitor_check = mongo.db.visitor_type.find_one(
            {"visitor_type": request.form.get("visitor_type")})
        # Flash a message if data already in db
        if visitor_check:
            flash("Visitor Type already exists")
            return render_template("add_field_details.html")
        # If data is new, add to the db collection
        visitor = {"visitor_type": request.form.get("visitor_type")}
        mongo.db.visitor_type.insert_one(visitor)
        flash("Successfully added, {} to the DB".format(
            request.form.get("visitor_type")))
        return redirect(url_for("add_visitor_details"))
    return render_template("add_field_details.html")


# Edit visitor types that user can select from
@app.route("/edit_visitor_type/<visitor_id>", methods=["GET", "POST"])
def edit_visitor_type(visitor_id):
    if request.method == "POST":
        v_submit = {
            "visitor_type": request.form.get("visitor_type")
        }
        mongo.db.visitor_type.update({"_id": ObjectId(visitor_id)}, v_submit)
        flash("Update Successful")
        return redirect(url_for("manage_form_details"))
    visitor = mongo.db.visitor_type.find_one({"_id": ObjectId(visitor_id)})
    return render_template("edit_visitor_type.html", visitor=visitor)


# Edit locations that user can select from
@app.route("/edit_location/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    if request.method == "POST":
        l_submit = {
            "location_name": request.form.get("location_name")}
        mongo.db.locations.update({"_id": ObjectId(location_id)}, l_submit)
        flash("Update Successful")
        return redirect(url_for("manage_form_details"))
    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


# Admin function to delete a visitor type in the  selection user can choose
@app.route("/delete_visitor/<visitor_id>")
def delete_visitor(visitor_id):
    mongo.db.visitor_type.remove({"_id": ObjectId(visitor_id)})
    flash("Deletion Successful")
    return redirect(url_for("manage_form_details"))


# Delete a location -> Admin task
@app.route("/delete_location/<location_id>")
def delete_location(location_id):
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        mongo.db.locations.remove({"_id": ObjectId(location_id)})
        flash("Location Deleted!")
        return redirect(url_for("manage_form_details"))
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("home"))


# Delete a user -> Admin task
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash("User Deleted!")
        return redirect(url_for("users_admin"))
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("home"))


# Search on admin user page only
@app.route("/search_admin_user_page", methods=["GET", "POST"])
def search_admin_user_page():
    query = request.form.get("query")
    users = list(mongo.db.recommendations.find(
        {"$text": {"$search": query}}))
    return render_template("users_admin.html", users=users)


# app route for page for admin to view users
# Displays option to delete
@app.route("/users_admin")
def users_admin():
    username = list(mongo.db.users.find())
    return render_template(
        "users_admin.html", username=username)


# Admin page to display users
# Will display delete Recommendations option
@app.route("/recommend_admin_delete", methods=["GET", "POST"])
def recommend_admin_delete():
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        recommendations = list(mongo.db.recommendations.find())
        return render_template(
                "recommend_admin_delete.html",
                username=username, recommendations=recommendations)
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("home"))


"""
Admin Delete function is not located on this section of code.
It is accessed through the overall delete recommendation,
with the if else check on admin
No further code needed for admin section
"""


# User logout
@app.route("/logout")
def logout():
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for('home'))


@app.errorhandler(404)
def invalid_route(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
