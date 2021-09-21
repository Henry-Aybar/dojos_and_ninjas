from flask_app import app
from flask import  render_template, request, redirect, session, flash
from flask_app.models.dojo import Dojo


##==========================##
##   Main Page / new dojo   ##
##==========================##
@app.route("/dojos")
def books():
    all_dojos = Dojo.get_dojos()
    return render_template("dojos.html", all_dojos = all_dojos)

@app.route("/new_dojo", methods = ["POST"])
def new_dojo():
    data = {
        "name" : request.form['name'],
    }
    Dojo.new_dojo(data)
    return redirect("/dojos")

##==========================##
##   View Dojo Ninja List   ##
##==========================##

@app.route("/dojos/<int:dojo_id>")
def dojo_list(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    dojo = Dojo.dojo_list(data)
    return render_template("show_dojo_info.html", dojo = dojo)