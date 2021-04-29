from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint("market", __name__)


@bp.route("/")
@bp.route("/home")
def home_page():
    return render_template("market/home.html")

@bp.route("/market")
def market_page():
	items = [
    {'id': 1, 'name': 'Producto 1', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Producto 2', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Producto 3', 'barcode': '231985128446', 'price': 500}
]
	return render_template("market/market.html", items=items)



