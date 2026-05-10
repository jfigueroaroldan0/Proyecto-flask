from flask import Flask, render_template, request, abort
import json
import os

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

@app.route("/motos")
def items():
    nombre_busqueda    = request.args.get("nombre", "").strip()
    marca_seleccionada = request.args.get("marca", "").strip()
    tipo_seleccionado  = request.args.get("tipo", "").strip()
    ordenar            = request.args.get("ordenar", "nombre_asc").strip()

    motos = MOTOS[:]

    if nombre_busqueda:
        motos = [m for m in motos if nombre_busqueda.lower() in m["nombre"].lower()]

    if marca_seleccionada:
        motos = [m for m in motos if m["marca"] == marca_seleccionada]

    if tipo_seleccionado:
        motos = [m for m in motos if m["tipo"] == tipo_seleccionado]

    order_map = {
        "nombre_asc":      ("nombre",        False),
        "nombre_desc":     ("nombre",        True),
        "precio_asc":      ("precio_euros",  False),
        "precio_desc":     ("precio_euros",  True),
        "cilindrada_asc":  ("cilindrada",    False),
        "cilindrada_desc": ("cilindrada",    True),
    }
    key, reverse = order_map.get(ordenar, ("nombre", False))
    motos.sort(key=lambda m: m[key], reverse=reverse)

    marcas = sorted({m["marca"] for m in MOTOS})

    if tipo_seleccionado:
        titulo = f"Motos de {tipo_seleccionado}"
    elif nombre_busqueda or marca_seleccionada:
        titulo = "Resultados de búsqueda"
    else:
        titulo = "Catálogo de Motos"

    return render_template("catalogo.html", motos=motos, marcas=marcas, titulo=titulo, total_resultados=len(motos), nombre_busqueda=nombre_busqueda, marca_seleccionada=marca_seleccionada, tipo_seleccionado=tipo_seleccionado, ordenar=ordenar)

@app.route("/motos/<int:id>")
def detalle(id):
    moto = next((m for m in MOTOS if m["id"] == id), None)
    if moto is None:
        abort(404)
    return render_template("detalle.html", moto=moto)

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

port=int(os.environ.get("PORT", 5000))
app.run("0.0.0.0", port=port ,debug=True)
