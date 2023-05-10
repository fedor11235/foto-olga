from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user
from flask import Blueprint, request, redirect, url_for, flash, render_template
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  login    = request.form.get('login')
  password = request.form.get('password')

  user = User.query.filter_by(login=login).first()

  if not user or not check_password_hash(user.password, password):
    flash('проверьте данные для входа и повторите попытку')
    return redirect(url_for('main.admin'))
  
  login_user(user)

  return redirect(url_for('main.admin'))

@auth.route('/logout', methods=['GET'])
def logout():
  logout_user()
  return redirect(url_for('main.admin'))

@auth.route('/signup', methods=['POST'])
def signup():
  login     = request.form.get('login')
  password = request.form.get('password')
  
  new_user    = User(login=login, password=generate_password_hash(password, method='sha256'))

  db.session.add(new_user)
  db.session.commit()

  return redirect(url_for('main.admin'))
