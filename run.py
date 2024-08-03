#runs the app
from app import create_app, db
from app.models import User, Product, Post

app = create_app()

with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

