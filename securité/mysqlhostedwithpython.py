from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# @Author : Mehdi Yc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database hosted in remotemysql.com
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://888fSNfa8E:4s5p7JYHvD@remotemysql.com:3306/888fSNfa8E"
db = SQLAlchemy(app)


def getUserPassword(mail):
    pass


def getUserInfos():
    pass

# class <table name>(db.Model):
#   __tablename__ = "<table name>"
#   <tablecolumn name> = db.Column('columnname', db.<columnType>, [prumary_key=True])


class User(db.Model):
    __tablename__ = "user"

    mail = db.Column('usermail', db.String, primary_key=True)
    password = db.Column('password', db.String)


users = User.query.all()
print('|\tMail\t|\tPassword\t|')
for u in users:
    print('|\t'+str(u.mail)+'    |\t'+str(u.password)+'\t|')
print('________________________')


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
