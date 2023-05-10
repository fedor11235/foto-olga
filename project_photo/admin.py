from flask import Blueprint, redirect, request, url_for
from flask_login import login_required, current_user
from .helpers import get_user
from .models import Clients
from . import db
import os

folder_with_avatar = './project_photo/static/img/admin'

admin = Blueprint('admin', __name__)

@admin.route('/upload_avatar', methods=['POST'])
def upload_avatar():
  image  = request.files['image']
  image.save(os.path.join(os.getcwd(), folder_with_avatar, 'avatar' + '.jpg'))
  return 'successfully'

@login_required
@admin.route('/edit', methods=['POST'])
def edit():
  instagram = request.form.get('instagram')
  nick      = request.form.get('nick')
  email     = request.form.get('email')
  login     = request.form.get('login')
  password  = request.form.get('password')
  full_name  = request.form.get('full_name')

  if instagram:
    current_user.instagram = instagram
  if nick:
    current_user.nick = nick
  if email:
    current_user.email = email
  if login:
    current_user.login = login
  if password:
    current_user.password = password
  if full_name:
    current_user.full_name = full_name

  db.session.commit()

  return redirect(url_for('main.admin'))

@admin.route('/add_like', methods=['GET'])
def add_lick():
  user = get_user()
  if user.likes and not user.likes == 0:
    user.likes += 1
  else:
    user.likes = 1
  db.session.commit()
  return 'successfully'

@admin.route('/enroll', methods=['POST'])
def enroll():
  name       = request.form.get('name')
  contacts    = request.form.get('contacts')
  consent    = request.form.get('consent')
  new_client = Clients(name=name, contacts=contacts, consent=consent)
  db.session.add(new_client)
  db.session.commit()
  return redirect(url_for('main.index'))

@admin.route('/deleted_customer', methods=['POST'])
def deleted_photo():
  customerId = request.form.get('customerId')
  client = Clients.query.filter_by(id=customerId).first()
  db.session.delete(client)
  db.session.commit()
  return 'successfully'
