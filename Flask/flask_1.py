from flask import Flask, redirect, url_for, render_template, request, session, url_for, flash
from captchacreater import create_image_captcha
from sendmail_func import sendMail, validMail
from TokenGenerator import getTokenUser, setToken,ChangeTokenUser
from mysqlhostedwithpython import getUserPassword, setUserData, init
from MainPage import getClientData, setClientData
from flask import g
import os
import time
from datetime import timedelta
from models import app, db


app.secret_key = os.urandom(21)
# session.permanent = True
app.permanent_session_lifetime = timedelta(
    minutes=1)  # will expire in 1 minute
########################################################################################


@app.route("/", methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('passw')
    prénom = request.form.get('prénom')
    print(email)
    if(email is not None):
        if(getUserPassword(email, init()) == ''):
            if(validMail(email)):
                tk = setToken(email=email)
                ud = setUserData(email=email, login=password, passwords=init())
                cd = setClientData(email=email, nom=name, prénom=prénom,
                                   sex='H', balance='0.0', incomes='0.0', expenses='0.0')
            else:
                return render_template("register.html", error="entrez un mail valide ! ")
        else:
            return render_template("register.html", error="votre mail existe deja")

    return render_template("register.html", error="")


@app.route("/account", methods=['POST'])
def account():
    tkn = request.form["token"]
    if not session.get('userMail') is None:
        z = getClientData(session['userMail'])
        user_tkn = getTokenUser(session['userMail'])
        if tkn == user_tkn:
            ChangeTokenUser(session['userMail'])
            return render_template("MainPage.html", balance=z[2], Incomes=z[3], Expenses=z[4])
        else:
            return "wrong token sir"
    else:
        return redirect('/signin')


@app.route("/signin/")
def signin():
    return render_template("signin.html", wrongpassword='')


@app.route("/signin", methods=['POST'])
def token():
    f = open("./securité/message.html", "r")
    ms = f.read()
    f.close()
    mail = request.form["email"]
    session['userMail'] = mail
    password = request.form["passw"]
    if(password == getUserPassword(mail, init())):
        sendMail(mail, "Bank Token", ms)
        return render_template("token.html")
    return render_template("signin.html", wrongpassword='Invalid Password Or Mail retry !')


@app.route("/resend")
def resendToken():
    f = open("./securité/message.html", "r")
    ms = f.read()
    f.close()
    sendMail(session['userMail'], "Bank Token", ms)
    return render_template("token.html")


if __name__ == "__main__":

    app.run(debug=True)
