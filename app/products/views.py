from flask import render_template
from . import products

@products.route("/products")
def product_page():
    products = Product.query.all()
    return render_template('products.html', products=products)

@products.route("/api/products")
def list_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])

@products.route("/products/<id>")
def show_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.as_dict())