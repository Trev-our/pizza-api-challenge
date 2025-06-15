from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Fixed typo
from flask_migrate import Migrate  # Fixed typo

db = SQLAlchemy()  # Corrected from "SQL4(chemy())"
migrate = Migrate()  # Corrected from "migrate()"

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints - FIXED IMPORTS
    from server.controllers.restaurant_controller import restaurant_bp  # Fixed comma->dot
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
    
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restaurant_pizza_bp)
    
    return app  # This was outside the function!