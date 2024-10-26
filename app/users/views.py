from . import users_blueprint
from flask import render_template, request, url_for, redirect


@users_blueprint.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get("age", type=int)
    return render_template("hi.html", name=name, age=age)


@users_blueprint.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator", age=19, _external=True)
    print(to_url)
    return redirect(to_url)
