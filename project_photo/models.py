from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  __tablename__ = 'admin'

  id             = db.Column(db.Integer, primary_key=True)

  login          = db.Column(db.String(100))
  password       = db.Column(db.String(100))
  # nick           = db.Column(db.String(100))
  # instagram      = db.Column(db.String(100))

class Photos(db.Model):
  __tablename__ = 'photo'

  id             = db.Column(db.Integer, primary_key=True)

  image          = db.Column(db.String(100))
