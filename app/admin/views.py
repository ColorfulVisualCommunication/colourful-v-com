from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import admin
from app.models import User
from app import db

@admin.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    return render_template('dashboard.html')

@admin.route('/users')
@login_required
def manage_users():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    users = User.query.all()
    return render_template('manage_users.html', users=users)


@admin.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('User updated successfully.', 'success')
        return redirect(url_for('admin.manage_users'))
    return render_template('edit_user.html', user=user)

@admin.route('/users/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin.manage_users'))
