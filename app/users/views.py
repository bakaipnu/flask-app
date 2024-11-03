from flask import render_template, request, url_for, redirect, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from . import users_blueprint


@users_blueprint.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get("age", type=int)
    return render_template("hi.html", name=name, age=age)


@users_blueprint.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator",
                     age=19, _external=True)
    print(to_url)
    return redirect(to_url)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    correct_username = "admin"
    correct_password = generate_password_hash("password123")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        is_username_correct = username == correct_username
        is_password_correct = check_password_hash(correct_password, password)

        if is_username_correct and is_password_correct:
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("users.profile", name=username))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")


@users_blueprint.route("/profile")
def profile():
    username = session.get("user")
    if not username:
        flash("You need to log in to view this page.", "warning")
        return redirect(url_for("users.login"))
    return render_template("profile.html", username=username)


@users_blueprint.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    flash("You have benn logged out.", "info")
    return redirect(url_for("users.login"))
