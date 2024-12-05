import os
import json

from flask import flash, redirect, render_template, url_for, session

from . import posts_blueprint
from .forms import PostForm
from .utils import write_data


post_id = 0


@posts_blueprint.route("/add_post", methods=["GET", "POST"])
def add_post():
    global post_id

    form = PostForm()
    if form.validate_on_submit():
        if "user" in session.keys():
            username = session["user"]
        else:
            username = "unauthorized"
        data = {
            "id": post_id,
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": form.publish_date.data.isoformat(),
            "author": username
        }
        write_data(data)
        post_id += 1
        flash("Post added successfully!", "success")
        return redirect(url_for("posts.add_post"))
    return render_template("add_post.html", form=form)


@posts_blueprint.route("/", methods=["GET"])
def show_posts():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'data', 'posts.json'), "r", encoding="utf-8") as file:
            posts = json.load(file)
    except FileNotFoundError:
        posts = []
    except json.JSONDecodeError:
        posts = []

    return render_template("posts.html", posts=posts)
