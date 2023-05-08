from flask import Blueprint, render_template
from .helpers import get_images, get_user

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  images = get_images()
  user = get_user()
  return render_template(
    'pages/main.html',
    images    = images,
    likes     = user.likes,
    instagram = user.instagram
  )

@main.route('/contacts', methods=['GET'])
def contacts():
  user = get_user()
  return render_template(
    'pages/contacts.html',
    instagram = user.instagram,
    email = user.email,
    nick = user.nick
  )

@main.route('/admin', methods=['GET'])
def admin():
  images = get_images()
  return render_template('pages/admin.html', images=images)

