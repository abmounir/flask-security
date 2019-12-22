from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random,time
from models import app,db,ConnectClient
# @Author : Mehdi Yc

getToken = ConnectClient.query.all()


def getTokenUser(user):

	x = ''
	for b in getToken:

		if str(b.Email) == user:
			x = str(b.Token)

	return x

def setToken(email):
	token=random.randint(1000,9999)
	new_token=ConnectClient(Email=email,Token=token)
	if new_token:
		db.session.add(new_token)
		db.session.commit()
		time.sleep(1)
		for x in getToken:
			if str(x.Email)=='tst@aa.aa' :
				deleted=ConnectClient.query.filter_by(Email='tst@aa.aa').delete()
				if deleted:
					#db.session.delete(deleted)
					db.session.commit()
	return new_token


	#if new_token:
	 #   db.session.add(new_token)
	  #  db.session.commit()
	#return new_token
