from market import app
from flask import render_template
from market.modelos import Item

@app.route("/")
@app.route("/home")
def home_page():
	return render_template("market/home.html")

@app.route("/market")
def market_page():
	items = Item.query.all()
	return render_template("market/market.html", items=items)