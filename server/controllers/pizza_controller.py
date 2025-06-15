from flask import Blueprint, jsonify
pizza_bp = Blueprint('pizza_bp', __name__)

# Sample data
pizzas = [
    {"id": 1, "name": "Margherita", "ingredients": ["tomato", "mozzarella", "basil"]},
    {"id": 2, "name": "Pepperoni", "ingredients": ["tomato", "mozzarella", "pepperoni"]}
]

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    return jsonify(pizzas)