from flask import Blueprint, render_template
from .helpers import get_images, get_user, clients_object_to_dict
from .models import Clients

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  images = get_images()
  user = get_user()
  return render_template(
    'pages/main.html',
    images    = images,
    nick      = user.nick,
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
    full_name = user.full_name,
    likes     = user.likes,
    page      = 'CONTACTS'
  )

@main.route('/admin', methods=['GET'])
def admin():
  user = get_user()
  users_object = Clients.query.all()
  images       = get_images()
  clients      = clients_object_to_dict(users_object)
  return render_template(
    'pages/admin.html',
    images  = images,
    clients = clients,
    nick    = user.nick,
    page    = 'ADMIN'
  )

