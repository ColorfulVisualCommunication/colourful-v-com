from flask import render_template, jsonify, Blueprint
from .products.models import Product

main = Blueprint('main', __name__)

@main.route("/")
def home_page():
    return render_template('home.html')

@main.route("/products")
def product_page():
    products = Product.query.all()
    return render_template('products.html', products=products)

@main.route("/api/products")
def list_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])

@main.route("/products/<id>")
def show_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.as_dict())

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
