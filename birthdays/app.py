import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        isim = request.form.get("name")
        if not isim:
            return redirect("/")
        ay = request.form.get("month")
        if not ay:
            return redirect("/")
        try:
            ay=int(ay)
        except ValueError:
            return redirect("/")
        if ay<1 or ay>12:
            return redirect("/")
        gün = request.form.get("day")
        if not gün:
            return redirect("/")
        try:
            gün=int(gün)
        except ValueError:
            return redirect("/")
        if gün<1 or gün>31:
            return redirect("/")
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", isim, ay, gün)
    else:
        birthdays = db.execute("SELECT * FROM birthdays")
        # TODO: Display the entries in the database on index.html

        return render_template('index.html', birthdays=birthdays)
    return redirect("/")

