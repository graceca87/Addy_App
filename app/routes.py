from app import app
from flask import render_template
from app.forms import AddressBook



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/phone_book')
def add_contacts():
    form = AddressBook()
    return render_template('add_contact.html', form=form)