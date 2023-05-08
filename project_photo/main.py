from flask import Blueprint, render_template
from .models import Photos
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  return render_template('pages/main.html')

@main.route('/contacts', methods=['GET'])
def contacts():
  return render_template('pages/contacts.html')

@main.route('/admin', methods=['GET'])
def admin():
  images = db.session.query(Photos).all()
  return render_template('pages/admin.html', images=images[0].image)


