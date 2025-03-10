from app import db, app
from db.models import User  # Ensure User model is imported

with app.app_context():
    db.create_all()