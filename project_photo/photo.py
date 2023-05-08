import os
from flask import Blueprint, request, redirect, url_for

folder_with_pictures = './project_photo/static/img/photos'

photo = Blueprint('photo', __name__)

@photo.route('/upload_photo', methods=['POST'])
def upload_photo():
  image = request.files['image']

  number_photos = 0

  for _ in os.listdir(folder_with_pictures):
    number_photos += 1

  image.save(os.path.join(os.getcwd(), folder_with_pictures, str(number_photos) +".jpg"))
  return redirect(url_for('main.admin'))

@photo.route('/deleted_photo', methods=['GET'])
def deleted_photo():
  for f in os.listdir(folder_with_pictures):
      os.remove(os.path.join(folder_with_pictures, f))
  return redirect(url_for('main.admin'))
