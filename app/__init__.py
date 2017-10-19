__author__ = 'baboyx'
# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



# local imports
from config import app_config
# after the db variable initialization
login_manager = LoginManager()

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from .Controllers.Home import home as controllers_blueprint
    app.register_blueprint(controllers_blueprint)

    from .Controllers.Employee import employees as employees_blueprint
    app.register_blueprint(employees_blueprint)

    return app