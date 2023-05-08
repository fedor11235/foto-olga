from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  __tablename__ = 'admin'

  id         = db.Column(db.Integer, primary_key=True)

  login      = db.Column(db.String(100))
  password   = db.Column(db.String(100))
  email      = db.Column(db.String(100))
  nick       = db.Column(db.String(100))
  instagram  = db.Column(db.String(100))
  likes      = db.Column(db.Integer)

class Clients(db.Model):
  __tablename__ = 'clients'

  id         = db.Column(db.Integer, primary_key=True)

  name       = db.Column(db.String(100))
  contacts   = db.Column(db.String(100))
  consent    = db.Column(db.String(100))
