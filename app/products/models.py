from app import db
from datetime import datetime

class Product(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text, nullable=False)
  price = db.Column(db.Float, nullable=False)
  image = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)