__author__ = 'baboyx'

from . import controllers


@controllers.route('/')
def index():
    """
    Render the homepage template on the / route
    """
    return "Hi"
