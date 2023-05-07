import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app     = Flask(__name__)

app.debug                             = os.getenv('DEBUG')
# app.config['SECRET_KEY']              = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO']         = os.getenv('SQLALCHEMY_ECHO')

app.config['SQLALCHEMY_ECHO']         = os.getenv('SQLALCHEMY_ECHO')

db      = SQLAlchemy()
migrate = Migrate(app,  db)

def create_app():

  db.init_app(app)
  migrate.init_app(app, db)

  login_manager                = LoginManager()
  login_manager.login_view     = 'auth.login'
  login_manager.init_app(app)

  from .models import User
  @login_manager.user_loader
  def load_user(login):
    return User.query.get(login)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app