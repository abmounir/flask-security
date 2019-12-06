from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
@app.route("/home", methods=['POST'])
def home():
    name = request.form["name"]
    mail = request.form["email"]
    password = request.form["passw"]
    if(name != "mehdi"):
        return "<H1> the name is incorrect a khoya </H1>"
    elif(password != "mmeehhddii"):
        return "<H1> Le mot de passe est incorrect XD </H1>"

    return render_template("index2.html", val1="mehdi", val2="this is", val3="my name")


@app.route("/")
def register():
    return render_template("register.html", val1="mehdi", val2="this is", val3="my name")


@app.route("/signin/")
def signin():
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True)
