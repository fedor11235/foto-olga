from flask import Blueprint, render_template, request
from .helpers import print_red
import os

folder_with_avatar = './project_photo/static/img/admin'

admin = Blueprint('admin', __name__)

@admin.route('/upload_avatar', methods=['POST'])
def upload_avatar():
  image  = request.files['image']
  image.save(os.path.join(os.getcwd(), folder_with_avatar, 'avatar' + '.jpg'))
  return 'successfully'
