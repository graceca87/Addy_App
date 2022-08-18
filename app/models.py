from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(15), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # add foreign key (user_id REFERENCES User(id))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Address | {self.name}>'

    def __str__(self):
        return f"""
        Name: {self.name}
        Phone Number: {self.number}
        Address: {self.address}
        Email: {self.email}
        """

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='book_keeper', lazy='dynamic')
    

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

#LoginManager takes in id and stores it across requests. This callback is used to reload the user object
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

