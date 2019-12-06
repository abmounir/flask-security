from flask import Flask, redirect, url_for, render_template, request, session
from securité.captchacreater import create_image_captcha
from securité.sendmail_func import sendMail
from securité.TokenGenerator import getTokenUser
from flask import g
import os


app = Flask(__name__)
app.secret_key = os.urandom(21)


@app.route("/home", methods=['POST'])
def home():
    name = request.form["name"]
    mail = request.form["email"]
    session['userMail'] = mail
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

    user_tkn = getTokenUser(session['userMail'])
    if tkn == user_tkn:
        return "<h3> wlcm to your acc sir <h3>"
    else:
        return "wrong token sir"


@app.route("/signin/")
def signin():
    return render_template("signin.html")


@app.route("/token", methods=['POST'])
def token():

    f = open("./securité/message.html", "r")
    ms = f.read()
    f.close()
    mail = request.form["email"]
    session['userMail'] = mail
    print("user session is "+session['userMail'])
    sendMail(mail, "Bank Token", ms)
    return render_template("token.html")


@app.route("/resend")
def resendToken():
    f = open("./securité/message.html", "r")
    ms = f.read()
    f.close()
    sendMail(session['userMail'], "Bank Token", ms)
    return render_template("token.html")


if __name__ == "__main__":

    app.run(debug=True)
