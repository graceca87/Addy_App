from app import app
from flask import render_template
from app.forms import AddressBook


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/phone_book', methods=['GET', 'Post'])
def add_contacts():
    form = AddressBook()
    if form.validate_on_submit():
        print('Form has been validated! Hooray!!')
        print(form.name.data, form.number.data, form.address.data, form.email.data)
    return render_template('add_contact.html', form=form)