from flask import Flask, render_template, request, url_for

# Global field that increments everytime new entry is added
entry_id = 1

# List of inventory entries (dictionaries)
inventory = []

app = Flask(__name__)

# Default page
@app.route('/', methods = ["POST", "GET"])  
def home():
	global entry_id
	# User submitted an entry
	if request.method ==  "POST":
		new_entry = {}
		new_entry['id'] = entry_id
		entry_id += 1

		new_entry["item"] = request.form['item_input']
		new_entry["quantity"] = request.form['quantity_input']
		new_entry["price"] = request.form['price_input']

		inventory.append(new_entry)

	return render_template("index.html", rows = inventory)


if __name__ == "__main__":  
	app.run(debug = True)