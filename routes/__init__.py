from routes.auth import auth_bp
from routes.shopping import shopping_bp 

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(shopping_bp, url_prefix="/shop")