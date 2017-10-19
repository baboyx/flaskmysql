__author__ = 'baboyx'
__author__ = 'baboyx'
from flask import Blueprint

employees = Blueprint('employees', __name__)
from . import employee
