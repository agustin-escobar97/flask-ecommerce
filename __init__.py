import os
from flask import Flask, request, render_template, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

#configura SQLite3 para forzar llaves foranea
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
	if isinstance(dbapi_connection, SQLite3Connection):
		cursor = dbapi_connection.cursor()
		cursor.execute("PRAGMA foreign_keys=ON;")
		cursor.close()

db = SQLAlchemy(app)
now = datetime.now()


class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=30), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	description = db.Column(db.String(length=1024), nullable=False, unique=True)

	def __repr__(self):
		return f"Item {self.name}"

@app.route("/")
@app.route("/home")
def home_page():
	return render_template("market/home.html")

@app.route("/market")
def market_page():
	items = Item.query.all()
	return render_template("market/market.html", items=items)