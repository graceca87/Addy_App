from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='book_owner', lazy='dynamic')
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Save the password as the hashed version of the password
        self.set_password(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id} | {self.username}>"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit

#LoginManager takes in id and stores it across requests. This callback is used to reload the user object
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    street_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(25), nullable=False)
    zip_code = db.Column(db.String(15), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Address | {self.street_address}>'

    def __str__(self):
        return f"""
        Name: {self.first_name}{self.last_name}
        Phone Number: {self.phone_number}
        Address: {self.street_address}
        Email: {self.email}
        """