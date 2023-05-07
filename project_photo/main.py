from flask import Blueprint, render_template, request
from .helpers import print_red

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  return render_template('pages/main.html')

@main.route('/contacts', methods=['GET'])
def contacts():
  return render_template('pages/contacts.html')

@main.route('/upload_photo', methods=['POST'])
def upload_photo():
  image  = request.form.get('image')
  print_red(image)
  return render_template('pages/contacts.html')

@main.route('/admin', methods=['GET'])
def admin():
  return render_template('pages/admin.html')

