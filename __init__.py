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

from . import modelos
from . import rutas