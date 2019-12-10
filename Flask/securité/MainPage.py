from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from array import array
# @Author : Mehdi Yc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost:3306/client"
db = SQLAlchemy(app)


class Client(db.Model):

    __tablename__ = 'client'

    Email = db.Column('Email', db.String, primary_key=True)
    Name = db.Column('Name', db.String)
    LastName = db.Column('LastName', db.String)
    CurrentBalance = db.Column('CurrentBalance', db.String)
    Incomes = db.Column('Incomes', db.String)
    Expenses = db.Column('Expenses', db.String)
    
getData = Client.query.all()
#for u in getData:
  #  print(str(u.Name)+'\t'+'|\t'+str(u.CurrentBalance))

db.session.commit()
def getClientData(user):
    x =[]
    for b in getData:

        if str(b.Email) == user:
            x.append(str(b.Name)) 
            x.append(str(b.LastName))
            x.append( str(b.CurrentBalance))
            x.append( str(b.Incomes))
            x.append(str(b.Expenses))
            print(x)
        else:
           print('non')   

            
    return x
getClientData('zaidasouhil@gmail.com')

