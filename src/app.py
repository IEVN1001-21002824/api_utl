from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo:'IEVN-1001'
    list=['Jose', 'Juan', 'Miau', 'Cano']
    return render_template('uno.html')

@app.route("/user/<string:user>")
def user(user):
    return "El usuario es: {}".format(user)

@app.route("/numero/<int:n1>")
def user(n1):
    return "El numero es: {}".format(n1)

@app.route("/numero/<string:nom>/<int:id>")
def user(nom, id):
    return "<h1>ID: {} nombre {}".format(nom, id)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def nom2(nom:'kas'):
    return "<h1> el nombre es: {}</h1".format(nom)

if __name__ == "__main__":
    app.run(debug=True)