from app import app
from flask import render_template, redirect, url_for, request

#within app.route add the html page we are doing changes to
@app.route('/addy')
# def is normally how we define a function in python
def register():
 return render_template('register.html')
@app.route('/registerV')
def registerV():
 return render_template('registerV.html')