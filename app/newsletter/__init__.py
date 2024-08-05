from flask import Blueprint

newsletter = Blueprint('newsletter', __name__, template_folder='templates')

from . import views
