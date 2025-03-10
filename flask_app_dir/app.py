from flask import Flask
from db import db, init_db
from routes import register_blueprints
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
init_db(app)

# Register Blueprints
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)