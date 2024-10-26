from flask import render_template

from . import app


@app.route("/")
def main():
    return render_template("home.html", page_title="Головна")


@app.route("/resume")
def resume():
    return render_template("resume.html", page_title="Моє резюме")


@app.route('/contact')
def contact():
    return render_template('contacts.html', page_title="Контакти")