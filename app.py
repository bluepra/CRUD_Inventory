from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Link
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models for the Database
class Item(db.Model):
	pid = db.Column(db.Integer, primary_key = True) # Product/Item ID - primary key
	name = db.Column(db.String(100), nullable = False) # Item Name
	quantity = db.Column(db.Integer, nullable = False) # Quantity
	price = db.Column(db.Float, nullable = True) # Price of item

	def __repr__(self):
		return f"Item('{self.pid}', '{self.name}')"

class Warehouse(db.Model):
	wid = db.Column(db.Integer, primary_key = True) # Warehouse ID - primary key
	name = db.Column(db.String(100), nullable = False) # Warehouse Name
	city = db.Column(db.String(50)) # Quantity
	state = db.Column(db.String(50)) # Price of item

	def __repr__(self):
		return f"Warehouse('{self.wid}', '{self.name}')"

# Default page
@app.route('/', methods = ["POST", "GET"])
def inventory():
	if request.method == "GET":
		inventory = db.session.query(Item).all()
		return render_template("index.html", rows = inventory)
	
	# User submitted an entry
	elif request.method ==  "POST":
		new_item_name = request.form['item_input']
		new_item_quantity = request.form['quantity_input']
		new_item_price = request.form['price_input']

		# Create the new database row - new_item
		new_item = Item(name = new_item_name, quantity = new_item_quantity, price = new_item_price)

		# Add new entry to database
		try:
			db.session.add(new_item)
			db.session.commit()
		except:
			return "ERROR - COULD NOT ADD ITEM TO DATABASE"

		return redirect("/")
	

@app.route("/warehouses", methods = ["POST", "GET"])  
def warehouses_page():
	if request.method == "GET":
		warehouses = db.session.query(Warehouse).all()
		return render_template("warehouses.html", rows = warehouses)
	
	# User submitted an entry
	elif request.method ==  "POST":
		new_warehouse_name = request.form['w_name_input']
		new_warehouse_city = request.form['city_input']
		new_warehouse_state = request.form['state_input']

		# Create the new database row - new_warehouse
		new_warehouse = Warehouse(name = new_warehouse_name, city = new_warehouse_city, state = new_warehouse_state)

		# Add new warehouse to database
		try:
			db.session.add(new_warehouse)
			db.session.commit()
		except:
			return "ERROR - COULD NOT ADD WAREHOUSE TO DATABASE"

		return redirect("/warehouses")
	

if __name__ == "__main__":  
	app.run(debug = True)