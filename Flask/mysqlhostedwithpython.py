from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import app,User,db
import time
# @Author : Mehdi Yc

getPassword = User.query.all()


def getUserPassword(user):

	x = ''
	for b in getPassword:

		if str(b.mail) == user:
			x = str(b.password)

	return x



def setUserData(email,login):
	new_user=User(mail=email,password=login)
	if new_user:
		db.session.add(new_user)
		db.session.commit()
		time.sleep(1)
		for x in getPassword:
			if str(x.mail)=='tst@aa.aa' :
				deleted=User.query.filter_by(mail='tst@aa.aa').delete()
				if deleted:
					#db.session.delete(deleted)
					db.session.commit()

	return new_user


#print(getUserPassword("mehdidouy@gmail.com"))
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
