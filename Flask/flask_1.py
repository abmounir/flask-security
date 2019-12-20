from flask import Flask, redirect, url_for, render_template, request, session
from captchacreater import create_image_captcha
from sendmail_func import sendMail
from TokenGenerator import getTokenUser,setToken
from mysqlhostedwithpython import getUserPassword,setUserData
from MainPage import getClientData,setClientData
from flask import g
import os,time
from datetime import timedelta
from models import app,db




app.secret_key = os.urandom(21)
#session.permanent = True
app.permanent_session_lifetime = timedelta(minutes=1) #will expire in 1 minute
########################################################################################
@app.route("/home", methods=['POST'])
def home():
	name = request.form["name"]
	mail = request.form["email"]
	session['userMail'] = mail
	password = request.form["passw"]

	if(name != "mehdi"):
		return "<H1> the name is incorrect a khoya </H1>"
	elif(password != "123"):
		return "<H1> hna nba3tolo la page ta3 token XD </H1>"

	return render_template("signin.html")


@app.route("/", methods=['POST','GET'])
def register():
	email = request.form.get('email')
	name=request.form.get('name')
	password=request.form.get('passw')
	prénom=request.form.get('prénom')

	tk=setToken(email=email)
	ud=setUserData(email=email,login=password)
	cd=setClientData(email=email,nom=name,prénom=prénom,sex='H',balance='0.0',incomes='0.0',expenses='0.0')

	return render_template("register.html")


@app.route("/account", methods=['POST'])
def account():
	tkn = request.form["token"]
	if not session.get('userMail') is None:
		z = getClientData(session['userMail'])
		user_tkn = getTokenUser(session['userMail'])
		if tkn == user_tkn:
			return render_template("MainPage.html", balance=z[2], Incomes=z[3], Expenses=z[4])
		else:
			return "wrong token sir"
	else:
		return redirect('/signin')


@app.route("/signin/")
def signin():
	return render_template("signin.html", wrongpassword='')


@app.route("/token", methods=['POST'])
def token():

	f = open("./securité/message.html", "r")
	ms = f.read()
	f.close()
	mail = request.form["email"]
	session['userMail'] = mail
	password = request.form["passw"]
	if(password == getUserPassword(mail)):
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
