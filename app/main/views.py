from flask import render_template
from . import main

@main.route("/")
def home_page():
    return render_template('home.html')

@main.route("/")
def index_page():
    return render_template('index.html')

@main.route("/contact")
def contact_page():
    return render_template('contact.html')

@main.route("/about")
def about_page():
    return render_template('about.html')

@main.route("/services")
def services_page():
    return render_template('services.html')

@main.route("/faq")
def faq_page():
    return render_template('faq.html')
