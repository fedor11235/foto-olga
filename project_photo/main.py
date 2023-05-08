from flask import Blueprint, render_template
from .helpers import get_images

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  images = get_images()
  return render_template('pages/main.html', images=images)

@main.route('/contacts', methods=['GET'])
def contacts():
  return render_template('pages/contacts.html')

@main.route('/admin', methods=['GET'])
def admin():
  images = get_images()
  return render_template('pages/admin.html', images=images)



