from flask import Blueprint, url_for, render_template, redirect


errors_scope = Blueprint("errors", __name__)   

@errors_scope.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404