from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.app import db

# Define the restaurant_pizza Blueprint
restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
        # Create new RestaurantPizza
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(new_rp)
        db.session.commit()
        
        # Return the associated pizza data
        pizza = Pizza.query.get(data['pizza_id'])
        return jsonify(pizza.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Validation error"]}), 400
