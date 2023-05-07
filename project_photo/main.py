from flask import Blueprint, render_template
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
  return render_template('pages/main.html')

@main.route('/admin')
def admin():
  return render_template('pages/admin.html')

