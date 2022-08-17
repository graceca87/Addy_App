from app import app
from flask import render_template
from app.forms import AddressBook
from app.models import Contact


@app.route('/')
def index():
    addresses = []
    return render_template("index.html", addresses=addresses)

@app.route('/phone_book', methods=['GET', 'Post'])
def add_contacts():
    form = AddressBook()
    if form.validate_on_submit():
        print('Form has been validated! Hooray!!')
        print(form.name.data, form.number.data, form.address.data, form.email.data)
        name = form.name.data
        number = form.number.data
        address = form.address.data
        email = form.email.data
        contact = Contact(name=name, number=number, address=address, email=email)
    return render_template('add_contact.html', form=form)