from app import create_app

from utils.config import get


if __name__ == "__main__":
    create_app().run(port=get("FLASK_PORT"))
