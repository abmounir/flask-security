from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random

# @Author : Mehdi Yc

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:toor@localhost:3306/db1"
app.config['SQLALCHEMY_BINDS'] = {'token_db': 'mysql://mounir:toor@169.254.131.199:3306/RE7esJnNWs',
                                  'clientInfo_db': 'mysql://root:toor@localhost:3306/db3'}


db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "password2"
    mail = db.Column('email', db.String, primary_key=True,
                     default='tst2@aa.aa')
    password = db.Column('login', db.String)


class ConnectClient(db.Model):
    __bind_key__ = 'token_db'
    __tablename__ = 'token'

    Email = db.Column('email', db.String, primary_key=True,
                      default='tst2@aa.aa')
    Token = db.Column('token', db.Integer)


class Client(db.Model):
    __bind_key__ = 'clientInfo_db'
    __tablename__ = 'utilisateur2'

    Email = db.Column('email', db.String, primary_key=True,
                      default='tst2@aa.aa')
    Name = db.Column('nom', db.String)
    Sex = db.Column('sexe', db.String)
    LastName = db.Column('prénom', db.String)
    CurrentBalance = db.Column('balance', db.String)
    Incomes = db.Column('incomes', db.String)
    Expenses = db.Column('expenses', db.String)
