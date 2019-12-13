from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# @Author : Mehdi Yc

app = Flask(__name__)
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://Vpvv8swDIN:Lwj5xUAFl8@remotemysql.com:3306/Vpvv8swDIN"

db = SQLAlchemy(app)

#
# class <table name>(db.Model):
##   __tablename__ = "<table name>"
# <tablecolumn name> = db.Column('columnname', db.<columnType>, [prumary_key=True])
#
#


class User(db.Model):
    __tablename__ = "password"
    mail = db.Column('email', db.String, primary_key=True)
    password = db.Column('login', db.String)


getPassword = User.query.all()


def getUserPassword(user):

    x = ''
    for b in getPassword:

        if str(b.mail) == user:
            x = str(b.password)

    return x


print(getUserPassword("mehdidouy@gmail.com"))
# Insert  #add()
# RandomUser = User('examle@example.com','password')   #ecrypted par la suite
# db.session.add(RandomUser)
# db.session.commit()

# Delete  #delete()
# db.session.delete(RandomUser)
# db.session.commit()

# Select #query.filter().first()  #query.all() to get all users
#RandomUser = User.query.filter_by(usermail='examle@example.com').first()
#  RandomUser.password  # >output : 'password' RandomUser is None in case the mail doesn t exist in the database
