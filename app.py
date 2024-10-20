from flask import Flask


from utils.config import get


app = Flask(get("FLASK_APP"))


@app.route("/")
def main():
    return "Hello, world!"


if __name__ == "__main__":
    debug_value = get("FLASK_DEBUG", int) or False
    app.run(debug=debug_value, port=get("FLASK_PORT"))
