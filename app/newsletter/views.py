from flask import request, redirect, url_for, flash
from .forms import NewsletterForm
from . import newsletter
from ..models import db, Newsletter

@newsletter.route('/subscribe', methods=['POST'])
def subscribe():
    form = NewsletterForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_user = Newsletter.query.filter_by(email=email).first()
        if existing_user:
            flash('You are already subscribed!', 'warning')
        else:
            new_subscriber = Newsletter(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('You have successfully subscribed!', 'success')
    return redirect(url_for('main.home_page'))

