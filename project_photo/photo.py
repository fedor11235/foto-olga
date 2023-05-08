import os
from flask import Blueprint, request
from .helpers import print_red

folder_with_pictures = './project_photo/static/img/photos'

photo = Blueprint('photo', __name__)

@photo.route('/upload_photo', methods=['POST'])
def upload_photo():
  image         = request.files['image']
  number_photos = 0

  for _ in os.listdir(folder_with_pictures):
    number_photos += 1

  image.save(os.path.join(os.getcwd(), folder_with_pictures, str(number_photos) +".jpg"))
  return 'successfully'

@photo.route('/deleted_photo', methods=['POST'])
def deleted_photo():
  fileName    = request.form.get('fileName')
  print_red(fileName)
  os.remove(os.path.join(folder_with_pictures, fileName))
  return 'successfully'

@photo.route('/deleted_all_photo', methods=['GET'])
def deleted_all_photo():
  for f in os.listdir(folder_with_pictures):
      os.remove(os.path.join(folder_with_pictures, f))
  return 'successfully'
