from app import db
from datetime import datetime


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    number = db.Column(db.String(15), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)