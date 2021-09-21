from flask_app import app
from flask import  render_template, request, redirect, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


##==========================##
## New Ninja/ create Ninja  ##
##==========================##
@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_dojos()
    return render_template("/ninjas.html", dojos = dojos)

@app.route("/create_ninja", methods = ["POST"])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id'],
    }
    Ninja.create_ninja(data)
    return redirect("/dojos")