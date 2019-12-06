from flask import Flask, redirect, url_for, render_template, request
from securité.captchacreater import create_image_captcha
from securité.sendmail_func import sendMail
from securité.TokenGenerator import getTokenUser


app = Flask(__name__)
@app.route("/home", methods=['POST'])
def home():
    name = request.form["name"]
    mail = request.form["email"]

    password = request.form["passw"]
    if(name != "mehdi"):
        return "<H1> the name is incorrect a khoya </H1>"
    elif(password != "mmeehhddii"):
        return "<H1> hna nba3tolo la page ta3 token XD </H1>"

    return render_template("signin.html")


@app.route("/")
def register():
    return render_template("register.html")


@app.route("/account", methods=['POST'])
def account():
    tkn = request.form["token"]
    user_tkn = getTokenUser('mehdidouy@gmail.com')
    print(tkn)
    print(user_tkn)
    if tkn == user_tkn:
        return "<h3> wlcm to your acc sir <h3>"
    else:
        return redirect("/token")


@app.route("/signin/")
def signin():
    return render_template("signin.html")


@app.route("/token", methods=['POST'])
def token():
    try:
        f = open("./securité/message.html", "r")
        ms = f.read()
        f.close()
        mail = request.form["email"]
        sendMail(mail, "Bank Token", ms)
        return render_template("token.html")
    except:
        return render_template("token.html")


if __name__ == "__main__":
    app.run(debug=True)
