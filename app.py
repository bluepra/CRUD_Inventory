from tempfile import TemporaryFile
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
inventory = None
warehouses = None


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


# Default (Inventory) page
@app.route("/", methods = ["POST", "GET"])
def inventory_page():
	global inventory, warehouses
	"""
    This function is used as the main page.
	Used to show the inventory.
	When users add an item using the form, the POST request is handled here as well
    """ 

	inventory = db.session.query(Item).all()
	warehouses = db.session.query(Warehouse).all()

	if request.method == "GET":
		return render_template("index.html", rows = inventory, warehouses = warehouses)
	
	# User submitted an entry
	elif request.method ==  "POST":
		new_item_name = request.form['item_input']
		new_item_quantity = request.form['quantity_input']
		new_item_price = request.form['price_input']
		new_item_warehouse = request.form['warehouse_select']

		# Create the new database row - new_item
		new_item = Item(name = new_item_name, quantity = new_item_quantity, price = new_item_price)

		# Add new entry to database
		try:
			db.session.add(new_item)
			db.session.commit()
		except:
			db.session.rollback()
			error_msg = ""
			if new_item_name == "":
				error_msg = "PLEASE PROVIDE A NAME"
			elif new_item_quantity == "":
				error_msg =  "PLEASE PROVIDE A QUANTITY"
			elif new_item_price == "":
				error_msg =  "PLEASE PROVIDE A PRICE"
			else:
				error_msg = "SOMETHING ELSE WENT WRONG WITH ADDING ITEM"

			return render_template("index.html", rows = inventory, 
		warehouses = warehouses, message = error_msg)
		
		return redirect("/")


def add_item_error_check():
	"""
    This function is used to check if user's inputs are valid.
	Returns True if all input is valid
	Returns False if there is any error in the input
    """ 
	pass

# Warehouse page
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


@app.route("/delete_item/<int:pid>")
def delete_item(pid):
	item_to_remove = db.session.query(Item).get_or_404(pid)

	try:
		db.session.delete(item_to_remove)
		db.session.commit()
	except:
		return f"Failed to delete item {pid}"
	
	return redirect("/")


@app.route("/delete_warehouse/<int:wid>")
def delete_warehouse(wid):
	warehouse_to_remove = db.session.query(Warehouse).get_or_404(wid)

	try:
		db.session.delete(warehouse_to_remove)
		db.session.commit()
	except:
		return f"Failed to delete warehouse {wid}"
	
	return redirect("/warehouses")


@app.route("/edit_item/<int:pid>", methods = ["POST", "GET"])
def edit_item(pid):
	item_to_edit = db.session.query(Item).get_or_404(pid)

	if request.method == "POST":
		item_to_edit.name = request.form["item_input"]
		item_to_edit.quantity = request.form["quantity_input"]
		item_to_edit.price = request.form["price_input"]
		# item_to_edit.warehouse_select = request.form["warehouse_select"]

		try:
			db.session.commit()
		except:
			return "ERROR UPDATING"
		
		return redirect("/")
	else: 
		# Get request
		return render_template("edit_item.html", pid = pid)
		

		



if __name__ == "__main__":  
	app.run(debug = True)