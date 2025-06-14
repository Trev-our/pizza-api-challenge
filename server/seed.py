from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding database...")

    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Flavor Ave")
    r2 = Restaurant(name="Pizza Palace", address="456 Crust Rd")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Cheese, Pepperoni")

    # Join data
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=8, restaurant=r2, pizza=p1)

    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    
