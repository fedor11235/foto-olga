from flask import Blueprint, render_template
from .helpers import get_images, get_user, clients_object_to_dict, print_red
from .models import Clients

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  images = get_images()
  user = get_user()
  return render_template(
    'pages/main.html',
    images    = images,
    likes     = user.likes,
    instagram = user.instagram,
    page      = 'MAIN'
  )

@main.route('/contacts', methods=['GET'])
def contacts():
  user = get_user()
  return render_template(
    'pages/contacts.html',
    instagram = user.instagram,
    email     = user.email,
    nick      = user.nick,
    likes     = user.likes,
    page      = 'CONTACTS'
  )

@main.route('/admin', methods=['GET'])
def admin():
  users_object = Clients.query.all()
  images       = get_images()
  clients      = clients_object_to_dict(users_object)
  return render_template(
    'pages/admin.html',
    images  = images,
    clients = clients,
    page    = 'ADMIN'
  )

