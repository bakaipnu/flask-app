from flask import Flask

from .config import config_by_name


def create_app(config_name="production"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    with app.app_context():
        from . import views
        from .posts import posts_blueprint
        from .users import users_blueprint
        app.register_blueprint(posts_blueprint)
        app.register_blueprint(users_blueprint)

    return app
