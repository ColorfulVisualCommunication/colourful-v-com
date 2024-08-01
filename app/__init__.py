from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()# init SQLAlchemy so we can use it later in our models
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    
    #Load all the configuration settings 
    #defined within the Config class found 
    #in the config.py file into the Flask application.
    app.config.from_object('config.Config')
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    
    from app.users.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Add other blueprints similarly...

    
    return app
    
# Define the user_loader function
@login_manager.user_loader
def load_user(user_id):
    from app.users.models import User  # Import here to avoid circular import
    # Query the User model to get the user by ID
    return User.query.get(int(user_id))
