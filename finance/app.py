import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocksTotal=0
    stocks=db.execute("SELECT symbol, price, shares FROM portfolios WHERE user_id = ? GROUP BY symbol HAVING shares > 0 ORDER BY price DESC", session["user_id"])
    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    for stock in stocks:
        stock_info=lookup(stock['symbol'])
        if not stock_info is None:
            stocksTotal+=stock_info['price']*stock['shares']
            db.execute("UPDATE portfolios SET price = ? WHERE symbol = ? AND user_id=?", stock_info['price'], stock['symbol'], session["user_id"])
    return render_template('index.html', stocks=stocks, balance=balance[0]['cash'], stocksTotal=stocksTotal)

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
        Quote_symbol = request.form.get("symbol")
        owned=db.execute("SELECT shares, symbol FROM portfolios WHERE id = ? AND symbol = ?", session["user_id"], Quote_symbol)
        price=lookup(Quote_symbol)
        if price is None:
            return apology("the quote does not exist")
        symbols = [row['symbol'] for row in owned]
        shares=request.form.get("shares")
        if shares == "" or shares.isalpha():
            return apology("MISSING SHARES", 400)
        if not is_int(shares):
            return apology("fractional not supported", 400)
        if int(shares) <= 0:
            return apology("share number can't be negative number or zero!", 400)
        shares=int(shares)
        if price['price']*shares<balance:
            balance-=price['price']*shares
            db.execute("INSERT INTO history (shares, symbol, price, user_id, state, timestamp) VALUES (?, ?,?,?,?,datetime('now'))", shares, Quote_symbol, str(price['price']), session["user_id"], "bought")
            if Quote_symbol in symbols:
                shares+=owned[0]['shares']
                db.execute("UPDATE portfolios SET shares = ? price= ? WHERE symbol = ? and user_id= ?", shares, str(price['price']), Quote_symbol, session["user_id"])
            else:
                db.execute("INSERT INTO portfolios (shares, symbol, user_id, price) VALUES (?, ?,?, ?)", shares, Quote_symbol, session["user_id"], str(price['price']))
            db.execute("UPDATE users SET cash=? WHERE id=?", balance, session["user_id"])
            return redirect("/")
        else:
            return apology("balance not enough")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history=db.execute("SELECT * FROM history WHERE user_id=? ORDER BY timestamp",session["user_id"])
    return render_template("/history.html", histories=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("enter a symbol")
        Quote_symbol = request.form.get("symbol")
        price=lookup(Quote_symbol)
        if price is None:
            return apology("the quote does not exist")
        return render_template("quoted.html", Quote=price)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif request.form.get("password")!=request.form.get("confirmation") :
            return apology("password and confirmation does not match", 400)

        # Add the username into db
        result = db.execute("SELECT username FROM users WHERE username = :username", username=request.form.get("username"))
        if len(result) > 0:
            return apology("username already exists")
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
        username = request.form.get("username")
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
        Quote_symbol = request.form.get("symbol")
        try:
            owned=db.execute("SELECT shares FROM portfolios WHERE user_id = ? AND symbol = ?", session["user_id"], Quote_symbol)[0]['shares']
        except:
            return apology("please enter an existing stock in your portfolio")
        price=lookup(Quote_symbol)['price']
        toSell=int(request.form.get("share"))
        if toSell<=owned:
            balance+=price*toSell
            owned-=toSell
            db.execute("INSERT INTO history (shares, symbol, price, user_id, state, timestamp) VALUES (?, ?,?,?,?,datetime('now'))", toSell, Quote_symbol, price, session["user_id"], "sold")
            db.execute("UPDATE portfolios SET shares = ? WHERE symbol = ? and user_id= ?", owned, Quote_symbol, session["user_id"])
            db.execute("UPDATE users SET cash=? WHERE id=?", balance, session["user_id"])
            return index()
        else:
            return apology("not enough share")
    else:
        return render_template("sell.html")
