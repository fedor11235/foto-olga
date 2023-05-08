from flask import Blueprint, redirect, request, url_for
from flask_login import login_required, current_user
from .helpers import print_red
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

  db.session.commit()

  return redirect(url_for('main.admin'))

@admin.route('/add_like', methods=['GET'])
def add_lick():
  pass
