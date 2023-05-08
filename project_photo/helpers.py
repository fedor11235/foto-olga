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

