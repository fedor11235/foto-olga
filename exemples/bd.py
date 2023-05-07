from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pprint import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:////tmp/users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    data = db.Column(db.PickleType())

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

# Create a user.
bob = User('Bob', {})
db.session.add(bob)
db.session.commit()

# Retrieve the row by its name.
bob = User.query.filter_by(name='Bob').first()
pprint(bob.data)  # {}

# Modifying data is ignored.
bob.data['foo'] = 123
db.session.commit()
bob = User.query.filter_by(name='Bob').first()
pprint(bob.data)  # {}

# Replacing data is respected.
bob.data = {'bar': 321}
db.session.commit()
bob = User.query.filter_by(name='Bob').first()
pprint(bob.data)  # {'bar': 321}

# Modifying data is ignored.
bob.data['moo'] = 789
db.session.commit()
bob = User.query.filter_by(name='Bob').first()
pprint(bob.data)  # {'bar': 321}