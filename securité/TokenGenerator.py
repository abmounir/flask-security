from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
# @Author : Mehdi Yc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost:3306/BankToken"
db = SQLAlchemy(app)

class ConnectClient(db.Model):

    __tablename__ = 'token'

    Email = db.Column('Email', db.String, primary_key=True)
    Token = db.Column('Tokne', db.Integer)
    

       

getToken=ConnectClient.query.all()
for u in getToken:
     print(str(u.Token)+'\t'+'|\t'+str(u.Email))
    
db.session.commit()
   
     
def getTokenUser(user):
    x=''
    for b in getToken:
       if str(b.Email)==user:
          x=str(b.Token)
          print(x)
    return x
print(getTokenUser('test2@gmail.com'))


            
