from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from array import array
# @Author : Mehdi Yc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://9EDsNxvuTb:Wz0VOBdaZx@remotemysql.com:3306/9EDsNxvuTb"


# email and password : "mysql://Vpvv8swDIN:Lwj5xUAFl8@remotemysql.com:3306/Vpvv8swDIN" table name : 'password'
# email and token    : "mysql://RE7esJnNWs:xsODaDhhpG@remotemysql.com:3306/RE7esJnNWs" table name : 'token'
# email and infos    : "mysql://9EDsNxvuTb:Wz0VOBdaZx@remotemysql.com:3306/9EDsNxvuTb" table name : 'utilisateur'


db = SQLAlchemy(app)


class Client(db.Model):

    __tablename__ = 'utilisateur'

    Email = db.Column('email', db.String, primary_key=True)
    Name = db.Column('nom', db.String)
    LastName = db.Column('prénom', db.String)
    CurrentBalance = db.Column('balance', db.String)
    Incomes = db.Column('incomes', db.String)
    Expenses = db.Column('expenses', db.String)


getData = Client.query.all()


def getClientData(user):

    x = []
    for b in getData:

        if str(b.Email) == user:
            x.append(str(b.Name))
            x.append(str(b.LastName))
            x.append(str(b.CurrentBalance))
            x.append(str(b.Incomes))
            x.append(str(b.Expenses))
            print(x)
        else:
            print('non')

    return x
