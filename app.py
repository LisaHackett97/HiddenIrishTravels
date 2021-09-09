import os
from flask import (
    Flask, flash, render_template, url_for,
    redirect, request, session, jsonify)
from flask_pymongo import PyMongo
# from flask_user import roles_required, user_manager
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# https://cloudinary.com/blog/creating_an_api_with_python_flask_to_upload_files_to_cloudinary
# code for upload API
#

@app.route("/upload", methods=['POST'])
def upload_file():
  app.logger.info('in upload route')

  cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))
  upload_result = None
  if request.method == 'POST':
    file_to_upload = request.files['file']
    app.logger.info('%s file_to_upload', file_to_upload)
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload)
      app.logger.info(upload_result)
      return jsonify(upload_result)




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
        # if user doesn't exist, update db with details from user
        # Add a timestamp to the user docs
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


# user delete their own recommendation
# admin delete any user recommendation
# if is_admin is tru, redirect to admin page. If not, back to the user page
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
    # if not, is_admin is default of false, redirect user to home page with a messag
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        return render_template("admin.html")
    else:
        flash("You are not authorized to access Admin Page")
        flash("You have been redirected to Home Page")
        return redirect(url_for("home"))

# Admin- to display visitor type and location names from db
# From this page, admin will then be able to edit or delete field details
@app.route("/manage_form_fields")
def manage_form_fields():
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        fields = list(mongo.db.visitor_type.find().sort("visitor_type", 1))
        locations = list(mongo.db.locations.find().sort("location_name", 1))
        return render_template(
            "manage_form_details.html", visitor_type=fields, locations=locations)
    else:
        flash("You are not authorized to access the Page")
        return redirect(url_for("home"))


# To bring admin user to the page to access forms
# to add new details to the categories for dropdown lists
@app.route("/add_field_details")
def add_field_details():
    return render_template("add_field_details.html")


# To access the form to add a new location
@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.insert_one(location)
        flash("new location added")
        return redirect(url_for("manage_form_fields"))
    return render_template("add_field_details.html")


# Add a new visitor type. Update dropdown list on recommendation form
@app.route("/add_visitor_details", methods=["GET", "POST"])
def add_visitor_details():
    if request.method == "POST":
        visitor = {
            "visitor_type": request.form.get("visitor_type")
        }
        mongo.db.visitor_type.insert_one(visitor)
        flash("new visitor added")
        return redirect(url_for("manage_form_fields"))
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
        return redirect(url_for("manage_form_fields"))
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
        return redirect(url_for("manage_form_fields"))
    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


# Delete a visitor type -> Admin task
@app.route("/delete_visitor_type/<visitor_id>")
def delete_visitor_type(visitor_id):
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        mongo.db.visitor_type.remove({"_id": ObjectId(visitor_id)})
        flash("Visitor type deletion successful!")
        return redirect(url_for("manage_form_fields"))
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("home"))


# Delete a location -> Admin task
@app.route("/delete_location/<location_id>")
def delete_location(location_id):
    user = mongo.db.users.find_one({"username": session["user"]})
    if user["is_admin"]:
        mongo.db.locations.remove({"_id": ObjectId(location_id)})
        flash("Location Deleted!")
        return redirect(url_for("manage_form_fields"))
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


# Admin Delete function
# This is access through the overall delete recommendation, with if else check_password_hash
# No further code needed for admin section

# User logout
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
