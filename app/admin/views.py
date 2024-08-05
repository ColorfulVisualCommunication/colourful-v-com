from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import admin
from app.models import User, BlogPost, Product, Chat
from app import db

@admin.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    return render_template('admin_dashboard.html')

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


@admin.route('/blog')
@login_required
def manage_blog():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    blog_posts = BlogPost.query.all()
    return render_template('manage_blog.html', blog_posts=blog_posts)

@admin.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        blog_post = BlogPost(title=title, content=content, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog post created successfully.', 'success')
        return redirect(url_for('admin.manage_blog'))
    return render_template('new_blog.html')

@admin.route('/blog/edit/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    blog_post = BlogPost.query.get_or_404(blog_id)
    if request.method == 'POST':
        blog_post.title = request.form['title']
        blog_post.content = request.form['content']
        db.session.commit()
        flash('Blog post updated successfully.', 'success')
        return redirect(url_for('admin.manage_blog'))
    return render_template('edit_blog.html', blog_post=blog_post)

@admin.route('/blog/delete/<int:blog_id>', methods=['POST'])
@login_required
def delete_blog(blog_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    blog_post = BlogPost.query.get_or_404(blog_id)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog post deleted successfully.', 'success')
    return redirect(url_for('admin.manage_blog'))

#products
@admin.route('/products')
@login_required
def manage_products():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    products = Product.query.all()
    return render_template('manage_products.html', products=products)

@admin.route('/products/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.form['image']
        new_product = Product(name=name, description=description, price=price, image=image)
        db.session.add(new_product)
        db.session.commit()
        flash('Product created successfully.', 'success')
        return redirect(url_for('admin.manage_products'))
    return render_template('new_product.html')

@admin.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']
        product.image = request.form['image']
        db.session.commit()
        flash('Product updated successfully.', 'success')
        return redirect(url_for('admin.manage_products'))
    return render_template('edit_product.html', product=product)

@admin.route('/products/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully.', 'success')
    return redirect(url_for('admin.manage_products'))

#chat routes
@admin.route('/chats')
@login_required
def manage_chats():
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    chats = Chat.query.all()
    return render_template('manage_chats.html', chats=chats)

@admin.route('/chats/delete/<int:chat_id>', methods=['POST'])
@login_required
def delete_chat(chat_id):
    if not current_user.is_admin:
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home_page'))
    chat = Chat.query.get_or_404(chat_id)
    db.session.delete(chat)
    db.session.commit()
    flash('Chat deleted successfully.', 'success')
    return redirect(url_for('admin.manage_chats'))