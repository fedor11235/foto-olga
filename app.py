import os
from dotenv import load_dotenv
from project_photo import db, create_app
from project_photo.helpers import add_admin

def main():
  load_dotenv()

  HOST = os.getenv('HOST')
  PORT = os.getenv('PORT')

  app  = create_app()
  with app.app_context():
    db.create_all()
    add_admin()
  app.run(debug=True, host=HOST, port=PORT)

if __name__ == '__main__':
  main()