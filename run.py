from app import app

from utils.config import get


if __name__ == "__main__":
    app.run(port=get("FLASK_PORT"))
