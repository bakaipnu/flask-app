from flask import Flask, render_template


from utils.config import get


app = Flask(get("FLASK_APP"))


@app.route("/")
def main():
    return render_template("home.html", page_title="Головна")


@app.route("/resume")
def resume():
    return render_template("resume.html", page_title="Моє резюме")


@app.route('/contact')
def contact():
    return render_template('contacts.html', page_title="Контакти")


if __name__ == "__main__":
    debug_value = get("FLASK_DEBUG", int) or False
    app.run(debug=debug_value, port=get("FLASK_PORT"))
