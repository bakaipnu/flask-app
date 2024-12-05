from flask import Blueprint


posts_blueprint = Blueprint("posts", __name__, url_prefix="/posts", template_folder="templates")

from . import views
