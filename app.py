import os
from dotenv import load_dotenv
from project_photo import db, create_app

def main():
  load_dotenv()

  HOST = os.getenv('HOST')
  PORT = os.getenv('PORT')

  app  = create_app()
  with app.app_context():
    db.create_all()
  app.run(debug=True, host=HOST, port=PORT)

if __name__ == '__main__':
  main()