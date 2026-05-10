import flask
import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

JSON_PATH = os.path.join(os.path.dirname(__file__), "data", "motos.json")

with open(JSON_PATH, encoding="utf-8") as f:
    MOTOS = json.load(f)

@app.template_filter("formato_precio")
def formato_precio(value):
    try:
        return f"{int(value):,} €".replace(",", ".")
    except (ValueError, TypeError):
        return value

@app.route("/")
def index():
    return render_template("index.html")

app.run("0.0.0.0",5000,debug=True)
