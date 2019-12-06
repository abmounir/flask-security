from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, session
import os

from flask_sqlalchemy import SQLAlchemy
CurrentBalance="20000$"
app = Flask(__name__)
@app.route("/")
def Main_Page(): 

    return render_template("MainPage.html",balance=CurrentBalance)


if __name__ == "__main__":

    app.run(debug=True)
