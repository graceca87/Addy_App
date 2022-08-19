from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, AddyForm, LoginForm
from app.models import User, Contact


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)

@app.route('/phone_book', methods=['GET', 'Post'])
@login_required
def add_addy():
    form = AddyForm()
    states = ["Alabama", "Alaska", "Arizona"]
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.first_name.data
        phone_number = form.phone_number.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        email = form.email.data
        contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number, street_address=street_address, city=city, state=state, country=country, zip_code=zip_code, email=email, user_id=current_user.id)
        print('Form has been validated! Hooray!!')
        print(contact)
        return redirect(url_for('index'))
    return render_template('add_addy.html', form=form, states=states)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    # if the form is submitted and all the data is valid
    if form.validate_on_submit():
        print('Form has been validated! Hooray!!!!')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Before we add the user to the database, check to see if there is already a user with username or email
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('A user with that username or email already exists.', 'danger')
            return redirect(url_for('signup'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #get username and pw from form
        username = form.username.data
        password = form.password.data
        # Query user table for a user with the same username as the form
        user = User.query.filter_by(username=username).first()
        # if user exists and password is correct for that user
        if user is not None and user.check_password(password):
            # Log the user in with the login_user function from flask_login
            login_user(user)
            # Flash a success message
            flash(f'Welcome back {user.username}!', 'success')
            # Redirect back to the home pageUnboundLocalError: local variable 'user' referenced before assignment
            return redirect(url_for('index'))
        # If no user with username or password incorrect
        else:
            # flash a danger message
            flash('Incorrect username and/or password. Please try again', 'danger') 
            # Redirect back to login
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out.', 'primary')
    return redirect(url_for('index'))
