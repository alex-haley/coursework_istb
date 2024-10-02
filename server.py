from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Движение", "URL": "/essentials" },
    { "title": "Блоки", "URL": "/blocks" },
    { "title": "Эффекты", "URL": "/effects" },
    { "title": "Карты", "URL": "/maps" },
    { "title": "Глоссарий", "URL": "/glossary" },
    { "title": "О создателях", "URL": "/about" },
]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/")
def hello_world():
    return render_template("index.html", name="Главная")

@app.route("/about")
def about_view():
    return render_template("about.html", name="О создателях")

@app.route("/essentials")
def parkour_guide():
    return render_template("parkouressentials.html", name="Движение")

@app.route("/blocks")
def profparkour():
    return render_template("blocks.html", name="Блоки")

@app.route("/glossary")
def gloss():
    return render_template("glossary.html", name="Глоссарий")

@app.route("/maps")
def verdif():
    return render_template("maps.html", name="Карты")

@app.route("/effects")
def effecty():
    return render_template("effects.html", name="Эффекты")