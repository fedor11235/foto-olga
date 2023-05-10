from werkzeug.security import generate_password_hash
from .models import User
from . import db
import os

folder_with_pictures = './project_photo/static/img/photos'

def print_red(word):
  print('\033[31m !!!!!!!!!!!!!!!! \033[0m')
  print('\033[31m', word, '\033[0m')

def get_images():
  images = []
  for filename in os.listdir(folder_with_pictures):
    images.append(filename)
  return images

def get_user():
  return User.query.filter_by(id=1).first()

def add_admin():
  admin = get_user()
  if(not admin):
    new_user    = User(
      login     = 'admin',
      password  = generate_password_hash('admin', method='sha256'),
      email     = 'fedoravdeev3@gmail.com',
      nick      = 'olga',
      full_name = 'Ольга Иванова',
      instagram = 'https://www.instagram.com/fedoravdeev3/',
      likes     = 0
    )
    db.session.add(new_user)
    db.session.commit()

def clients_object_to_dict(clients_object):
  clients_dict = []
  for client_object in clients_object:
    user_dict = {
      'id' : client_object.id,
      'name' : client_object.name,
      'contacts': client_object.contacts,
      'consent': client_object.consent
    }
    clients_dict.append(user_dict)
  return clients_dict


