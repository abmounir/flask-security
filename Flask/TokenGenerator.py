from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
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
	db.session.add(new_token)
	db.session.commit()


#print(getTokenUser("mehdidouy@gmail.com"))
