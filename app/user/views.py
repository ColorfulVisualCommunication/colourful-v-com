from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from . import user

@user.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title='Profile')

@user.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
