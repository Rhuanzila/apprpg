from flask import Flask, render_template

app = Flask(__name__)

#first page
#route -> link: domain(route)
#function -> exbihit
#template -> code
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/players")
def contatos():
    return render_template("players.html")

@app.route("/users/<name_user>")
def users(name_user):
    return render_template("users.html", name_user = name_user)
#put in the air
if __name__ == "__main__":
    app.run(debug=True)