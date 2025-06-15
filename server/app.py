from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
    from server.controllers.pizza_controller import pizza_bp  # NEW
    
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restaurant_pizza_bp)
    app.register_blueprint(pizza_bp)  # NEW
    
    return app