from flask import Flask, g
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

db = SQLAlchemy()# init SQLAlchemy so we can use it later in our models
login_manager = LoginManager()
migrate = Migrate()
bcrypt = Bcrypt()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    
    #Load all the configuration settings 
    #defined within the Config class found 
    #in the config.py file into the Flask application.
    app.config.from_object('config.Config')
    
    db.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/')

    from .products import products as products_blueprint
    app.register_blueprint(products_blueprint, url_prefix='/')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .newsletter import newsletter as newsletter_blueprint
    app.register_blueprint(newsletter_blueprint, url_prefix='/newsletter')

    from app.newsletter.forms import NewsletterForm
    
    from app import views
    
    @app.before_request
    def inject_newsletter_form():
        g.newsletter_form = NewsletterForm()
        
    return app
    