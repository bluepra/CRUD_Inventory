from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

# Global fields that increments everytime new entry is added
inventory_entry_id = 1
warehouse_entry_id = 1

# List of inventory entries (dictionaries)
inventory = []
# List of warehouse entries (dictionaries)
warehouses = []

# Default page
@app.route('/', methods = ["POST", "GET"])
@app.route('/inventory', methods = ["POST", "GET"])  
def home():
	global inventory_entry_id
	if request.method == "GET":
		return render_template("index.html", rows = inventory)
	# User submitted an entry
	elif request.method ==  "POST":
		new_entry = {}
		new_entry['id'] = inventory_entry_id
		inventory_entry_id += 1

		new_entry["item"] = request.form['item_input']
		new_entry["quantity"] = request.form['quantity_input']
		new_entry["price"] = request.form['price_input']

		inventory.append(new_entry)

		return redirect("/")


	

# Default page
@app.route("/warehouses", methods = ["POST", "GET"])  
def warehouses_page():
	global warehouse_entry_id

	if request.method == "GET":
		return render_template("warehouses.html", rows = warehouses)
	elif request.method ==  "POST":
		new_entry = {}
		new_entry["id"] = warehouse_entry_id
		warehouse_entry_id += 1

		new_entry["name"] = request.form['w_name_input']
		new_entry["city"] = request.form['city_input']
		new_entry["state"] = request.form['state_input']

		warehouses.append(new_entry)

		return redirect("/warehouses")

	

if __name__ == "__main__":  
	app.run(debug = True)