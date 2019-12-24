from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
# @Author : Mehdi Yc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://RE7esJnNWs:xsODaDhhpG@remotemysql.com:3306/RE7esJnNWs"

db = SQLAlchemy(app)


class ConnectClient(db.Model):

    __tablename__ = 'token'

    Email = db.Column('email', db.String, primary_key=True)
    Token = db.Column('token', db.Integer)


getToken = ConnectClient.query.all()


def getTokenUser(user):

    x = ''
    for b in getToken:

        if str(b.Email) == user:
            x = str(b.Token)

    return x
