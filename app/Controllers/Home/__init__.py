__author__ = 'baboyx'
from flask import Blueprint

home = Blueprint('home', __name__)
from . import home
