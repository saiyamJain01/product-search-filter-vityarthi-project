from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET'])
def index():
    
    query = Product.query
  
    categoryFilter = request.args.get('category')
    colorFilter = request.args.get('color')
    maxPriceFilter = request.args.get('maxPrice')

    if categoryFilter and categoryFilter != 'all':
        query = query.filter_by(category=categoryFilter)

    if colorFilter and colorFilter != 'all':
        query = query.filter_by(color=colorFilter)

    if maxPriceFilter:
        try:
            query = query.filter(Product.price <= float(maxPriceFilter))
        except ValueError:
            pass 

    products = query.all()

    return render_template('index.html', 
                           products=products,
                           current_category=categoryFilter or 'all',
                           current_color=colorFilter or 'all',
                           currentPrice=maxPriceFilter or 10000)

def seed_database():
    with app.app_context():
        db.create_all()
        if Product.query.count() == 0:
            data = [
                Product(name="Classic White Tee", category="Clothing", price=2499.00, color="White", image="https://placehold.co/300x300/white/black?text=T-Shirt"),
                Product(name="Denim Jacket", category="Clothing", price=4999.00, color="Blue", image="https://placehold.co/300x300/1a4b8c/white?text=Jacket"),
                Product(name="Running Sneakers", category="Footwear", price=5500.00, color="Black", image="https://placehold.co/300x300/111/white?text=Sneakers"),
                Product(name="Leather Boots", category="Footwear", price=7800.00, color="Brown", image="https://placehold.co/300x300/8b4513/white?text=Boots"),
                Product(name="Smart Watch", category="Electronics", price=1999.00, color="Black", image="https://placehold.co/300x300/333/white?text=Watch"),
                Product(name="Wireless Earbuds", category="Electronics", price=799.00, color="White", image="https://placehold.co/300x300/eee/333?text=Earbuds"),
                Product(name="Blue Hoodie", category="Clothing", price=3500.00, color="Blue", image="https://placehold.co/300x300/0000ff/white?text=Hoodie"),
                Product(name="Red Cap", category="Accessories", price=150.00, color="Red", image="https://placehold.co/300x300/ff0000/white?text=Cap"),
            ]
            db.session.add_all(data)
            db.session.commit()
            print("Database seeded!")

if __name__ == '__main__':
    seed_database()
    app.run(debug=True)