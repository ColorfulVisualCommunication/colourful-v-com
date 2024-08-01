from app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_image = db.Column(db.String(100))
    bio = db.Column(db.Text)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # Define additional methods as needed
