from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages

from market.modelos import Item, User
from market.forms import Register_Form
from market.forms import Login_Form
from market import db
from flask_login import login_user

@app.route("/")
@app.route("/home")
def home_page():
	return render_template("market/home.html")

@app.route("/market")
def market_page():
	items = Item.query.all()
	return render_template("market/market.html", items=items)

@app.route("/register", methods=["GET","POST"])
def register_page():
	form = Register_Form()
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)

		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for("home_page"))

	if form.errors is not None:
		for err_msg in form.errors.values():
			flash (f"Hubo un error con la creacion del usuario: {err_msg}", category="danger")

	return render_template("auth/register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
	form = Login_Form()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f"Inicio exitoso! {attempted_user.username}", category="success")
			return redirect(url_for("market_page"))
		else:
			flash("Las credenciales son incorrectas", category="danger")

	return render_template("auth/login.html", form=form)
