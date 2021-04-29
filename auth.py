import functools
from flask import (Blueprint, flash, g, render_template, request, url_for, session, redirect)
from werkzeug.security import check_password_hash, generate_password_hash
from market.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		db, c = get_db()
		error = None
		c.execute("SELECT id from prueba.user WHERE username = %s", (username,))
		if username is None:
			error = "El usename no puede estar vacío"
		if password is None:
			error = "La password no puede estar vacía"
		elif c.fetchone() is not None:
			error = "Usuario {} se encuentra registrado.".format(username)

		flash(error)

		if error is None:
			c.execute("INSERT INTO prueba.user (username, password) VALUES (%s, %s)", (username, generate_password_hash(password)))	
			db.commit()

			return redirect(url_for("auth.login"))

	return render_template("auth/register.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
	if g.user is not None:
		return redirect(url_for("market.home_page"))

	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		db,c = get_db()
		error = None
		c.execute("SELECT * FROM prueba.user WHERE username = %s", (username,))
		g.user = c.fetchone()

		if g.user is None:
			error = "Usuario y/o contraseña inválida"
		elif not check_password_hash(g.user["password"], password):
			error = "Usuario y/o contraseña inválida"

		flash(error)


		if error is None:
			session.clear()
			session["user_id"] = g.user["id"]
			return redirect(url_for("market.home_page"))

	return render_template("auth/login.html")

@bp.before_app_request
def load_logged_in_user():
	user_id = session.get("user_id")

	if user_id is None:
		g.user = None
	else:
		db, c = get_db()
		c.execute("SELECT * FROM prueba.user WHERE id = %s", (user_id,))
		g.user = c.fetchone

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("market.home_page"))
