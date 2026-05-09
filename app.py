# Flask web application for ASHS Pizza
from flask import Flask, render_template

app = Flask(__name__)

# Sample pizza menu data
pizzas = [
            {
                'id': 1,
                'name': 'Chill Out Pizza',
                'price': '10',
                'image': 'images/ChillOut.png',
                'description': 'Margherita Pizza - All the basic flavours with fresh tomato slices, mozzarella, and basil leaves.'
            },
            {
                'id': 2,
                'name': 'Garden Break Pizza',
                'price': '12',
                'image': 'images/GardenBreak.png',
                'description': 'Veggie Pizza - A delightful blend of mushrooms, olives, bell peppers, onions, and tomatoes.'
            },
            {
                'id': 3,
                'name': 'Everything But Homework Pizza',
                'price': '20',
                'image': 'images/EverythingButHomework.png',
                'description': 'Supreme Pizza - A hearty pizza loaded with pepperoni, sausage, bell peppers, olives, and onions, perfect for those who want everything but the homework!'
            },
                        {
                'id': 4,
                'name': 'After School BBQ Pizza',
                'price': '14',
                'image': 'images/AfterSchoolBBQ.png',
                'description': 'Chicken BBQ Pizza - A delicious pizza with a tangy BBQ sauce, grilled chicken, red onions, and cilantro.'
            },
            {
                'id': 5,
                'name': 'Protien Power Pizza',
                'price': '14',
                'image': 'images/ProtienPower.png',
                'description': 'Meat Lovers Pizza - A delicious pizza packed with pepperoni, sausage, bacon, and ham.'
            },
            {
                'id': 6,
                'name': 'Hall Pass Pizza',
                'price': '12',
                'image': 'images/HallPass.png',
                'description': 'Pepperoni Pizza - A classic pizza loaded with pepperoni and melted mozzarella and tomato sauce.'
            }
        ]
cart = []

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Display pizzas with carousel
@app.route('/menu')
def pizzas_page():
    return render_template('menu.html', pizzas = pizzas)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Add to cart route
@app.route('/AddToCart/<int:pizza_id>')
def add_to_cart(pizza_id):
    pizza = next((p for p in pizzas if p['id'] == pizza_id), None)
    if pizza:
        cart.append({'id': len(cart), 'name': pizza['name'], 'price': pizza['price']})
    return render_template('menu.html', pizzas=pizzas)

# Remove from cart route
@app.route('/RemoveFromCart/<int:cart_item_id>')
def remove_from_cart(cart_item_id):
    global cart
    cart = [item for item in cart if item['id'] != cart_item_id]
    return render_template('cart.html', cart=cart)  

# View cart route
@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

# Checkout route
@app.route('/checkout')
def checkout():
    cart = []
    return render_template('checkout.html')

# Run Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
