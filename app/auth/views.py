from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
import os
from . import auth
from .forms import LoginForm, RegistrationForm, UpdateProfileForm
from ..models import User
from .. import db, bcrypt

UPLOAD_FOLDER = 'app/static/img/profile_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if user.is_admin:
                return redirect(next_page) if next_page else redirect(url_for('admin.dashboard'))
            else:
                return redirect(next_page) if next_page else redirect(url_for('main.home_page'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_admin and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.dashboard'))
        else:
            flash('Admin Login Unsuccessful. Please check email and password', 'danger')
    return render_template('admin_login.html', title='Admin Login', form=form)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home_page'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Handle file upload
        profile_image = form.profile_image.data
        if profile_image and allowed_file(profile_image.filename):
            filename = secure_filename(profile_image.filename)
            profile_image.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
            filename = 'default.png'

        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password, profile_image=filename)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Register', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index_page'))

@auth.route("/profile")
@login_required
def profile():
    profile_image = url_for('static', filename='img/profile_pics/' + current_user.profile_image)
    return render_template('profile.html', title='Profile', profile_image=profile_image)

@auth.route("/profile/update", methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.profile_image.data:
            image_file = save_picture(form.profile_image.data)
            current_user.profile_image = image_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename='img/profile_pics/' + current_user.profile_image)
    return render_template('update_profile.html', title='Update Profile', profile_image=profile_image, form=form)

def save_picture(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = secure_filename(form_picture.filename)
    picture_path = os.path.join(current_app.root_path, 'static/img/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn
