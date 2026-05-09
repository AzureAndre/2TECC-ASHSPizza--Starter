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
            }
        ]
# TODO 1: Add more pizzas to the menu as for all the pizza images are available


cart = []

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Display pizzas with carousel
# TODO 2: Add a route for menu to display pizzas in menu.html.  Remember to pass the pizzas data to the template so that it can be displayed in the carousel.


# About page route
# TODO 3: Add a route to /about and link the about page.


# Add to cart route
# TODO 4: This function adds items to the cart, make sure that it displays the menu again after adding the item to the cart.  Also, make sure to pass the pizzas data to the template so that it can be displayed in the menu again.
@app.route('/AddToCart/<int:pizza_id>')
def add_to_cart(pizza_id):
    pizza = next((p for p in pizzas if p['id'] == pizza_id), None)
    if pizza:
        cart.append({'id': len(cart), 'name': pizza['name'], 'price': pizza['price']})
    return "Item not added to the cart. Please try again." 

# Remove from cart route
# TODO 5: This function removes items from the cart, make sure that it displays the menu again after removing the item from the cart.  Also, make sure to pass the pizzas data to the template so that it can be displayed in the menu again.
@app.route('/RemoveFromCart/<int:cart_item_id>')
def remove_from_cart(cart_item_id):
    global cart
    cart = [item for item in cart if item['id'] != cart_item_id]
    return "Item not removed from the cart. Please try again."  

# View cart route
@app.route('/cart')
# TODO 6: This page displays the items in the cart, make sure that it displays the menu again after viewing the cart.  Also, make sure to pass the pizzas data to the template so that it can be displayed in the menu again.

# Checkout route
# TODO 7:  This function should display the checkout page. 
@app.route('/checkout')
def checkout():
    cart = []
    return "Not checked out. Please try again."

# Run Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)


# TODO 8: Change the website to your own preferences.  Change the colours, the images, the text, the fonts, and the pizzas.  Make it your own!