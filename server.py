from flask import Flask, render_template, redirect, url_for
from cupcakes import get_cupcakes, add_cupcake_dict, find_cupcake, delete_cupcake

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes=get_cupcakes("cupcakes.csv"))


@app.route("/order")
def order():
    return render_template("order.html", order=get_cupcakes("order.csv"))


@app.route("/cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        add_cupcake_dict("order.csv", cupcake)
        return redirect(url_for("order"))
    else:
        return "Sorry, no cupcake found."


@app.route("/order/<name>")
def delete_cupcakes(name):
    cupcake = find_cupcake("order.csv", name)
    print(cupcake)
    if cupcake:
        delete_cupcake("order.csv", cupcake["name"])
        return redirect(url_for("order"))
    else:
        return "Sorry, no cupcake found."

@app.route("/cupcakes/<name>")
def view_cupcake(name):
    return render_template("cupcake.html", cupcake=find_cupcake("cupcakes.csv", name))


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True)
