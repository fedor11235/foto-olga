from flask import Blueprint, request, render_template
from .helpers import print_red
from .models import Photos
import os
from . import db

photo = Blueprint('photo', __name__)

@photo.route('/upload_photo', methods=['POST'])
def upload_photo():
  image = request.files['image']
  image.save(os.path.join(os.getcwd(), "project_photo/static", "current_image.jpg"))
  
  new_photo = Photos(image=image)
  print_red(new_photo)
  db.session.add(new_photo)
  db.session.commit()
  return render_template('pages/admin.html')

@photo.route('/deleted_photo', methods=['GET'])
def deleted_photo():
  db.session.query(Photos).delete()
  db.session.commit()
  return render_template('pages/admin.html')