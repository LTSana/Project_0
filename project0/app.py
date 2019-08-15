# Secret Mystery Python
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
	"""Render index page"""

	return render_template("index.html")


@app.route("/page_1")
def page_1():
	"""Render Page 1"""

	return render_template("/page_1.html")


@app.route("/page_2")
def page_2():
	"""Render Page 2"""

	return render_template("/page_2.html")


@app.route("/page_3")
def page_3():
	"""Render Page 3"""

	return render_template("/page_3.html")


@app.route("/page_4")
def page_4():
	"""Render Page 4"""

	return render_template("/page_4.html")


@app.route("/secret_page")
def secret_page():
	"""Render Secret Page that shows a image"""

	return render_template("/secret.html")


if __name__ == "__main__":
	app.run()