from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        return render_template("saludo.html", nombre=nombre)
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
